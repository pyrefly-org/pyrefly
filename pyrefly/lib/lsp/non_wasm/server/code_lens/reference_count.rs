/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

//! Lazy reference-count CodeLens creation and resolution.

use std::collections::HashSet;

use lsp_types::CodeLens;
use lsp_types::Command;
use lsp_types::DocumentSymbol;
use lsp_types::Location;
use lsp_types::Range;
use lsp_types::SymbolKind;
use lsp_types::Uri;
use pyrefly_build::handle::Handle;
use pyrefly_util::telemetry::EmptyResponseReason;
use ruff_text_size::Ranged;
use serde::Deserialize;
use serde::Serialize;

use super::CodeLensError;
use crate::binding::binding::KeyUndecoratedFunction;
use crate::state::state::Transaction;

#[derive(Debug, Deserialize, Serialize)]
pub(super) struct ReferenceCodeLensData {
    pub(super) uri: Uri,
    pub(super) version: Option<i32>,
}

/// Collect unresolved lenses without performing definition lookup or global reference searches.
pub(super) fn unresolved_code_lenses(
    transaction: &Transaction<'_>,
    handle: &Handle,
    uri: &Uri,
    version: Option<i32>,
) -> Result<Vec<CodeLens>, EmptyResponseReason> {
    let symbols = transaction
        .symbols(handle, None)
        .ok_or(EmptyResponseReason::ModuleInfoNotFound)?;
    let module_info = transaction
        .get_module_info(handle)
        .ok_or(EmptyResponseReason::ModuleInfoNotFound)?;
    let answers = transaction
        .get_answers(handle)
        .ok_or(EmptyResponseReason::ModuleInfoNotFound)?;
    let bindings = answers.bindings();
    // Cached decorator metadata recognizes overload aliases without looking up each definition.
    let overloads: HashSet<_> = bindings
        .keys::<KeyUndecoratedFunction>()
        .filter(|idx| {
            answers
                .get_idx(*idx)
                .is_some_and(|function| function.metadata.flags.is_overload)
        })
        .map(|idx| {
            let start = module_info
                .to_lsp_range(bindings.idx_to_key(idx).range())
                .start;
            (start.line, start.character)
        })
        .collect();
    let mut lenses = Vec::new();
    collect_symbol_lenses(&symbols, uri, version, &overloads, &mut lenses);
    Ok(lenses)
}

/// Decode the opaque data attached to an unresolved reference-count lens.
pub(super) fn resolve_data(lens: &CodeLens) -> Result<ReferenceCodeLensData, CodeLensError> {
    let data = lens.data.clone().ok_or(CodeLensError::MissingData)?;
    serde_json::from_value(data).map_err(CodeLensError::InvalidData)
}

/// Attach the reference command, excluding every location backed by a notebook cell.
pub(super) fn resolve_code_lens(
    mut lens: CodeLens,
    source_uri: &Uri,
    results: Vec<(Uri, Vec<Range>)>,
    notebook_cells: &HashSet<Uri>,
) -> CodeLens {
    let mut locations = Vec::new();
    for (uri, ranges) in results {
        if notebook_cells.contains(&uri) || uri.path().ends_with(".ipynb") {
            continue;
        }
        for range in ranges {
            locations.push(Location {
                uri: uri.clone(),
                range,
            });
        }
    }

    let reference_count = locations.len();
    let title = if reference_count == 1 {
        "1 reference".to_owned()
    } else {
        format!("{reference_count} references")
    };
    lens.command = Some(Command {
        title,
        command: "pyrefly.showReferences".to_owned(),
        arguments: Some(vec![
            serde_json::to_value(source_uri).expect("URI should serialize for code lens"),
            serde_json::to_value(lens.range.start)
                .expect("Position should serialize for code lens"),
            serde_json::to_value(&locations).expect("Locations should serialize for code lens"),
        ]),
        tooltip: None,
    });
    lens.data = None;
    lens
}

/// Traverse document symbols and create one unresolved lens per reference-countable definition.
fn collect_symbol_lenses(
    symbols: &[DocumentSymbol],
    uri: &Uri,
    version: Option<i32>,
    overloads: &HashSet<(u32, u32)>,
    lenses: &mut Vec<CodeLens>,
) {
    for symbol in symbols {
        if matches!(
            symbol.kind,
            SymbolKind::Class | SymbolKind::Function | SymbolKind::Method
        ) && !overloads.contains(&(
            symbol.selection_range.start.line,
            symbol.selection_range.start.character,
        )) {
            lenses.push(CodeLens {
                range: symbol.selection_range,
                command: None,
                data: Some(
                    serde_json::to_value(ReferenceCodeLensData {
                        uri: uri.clone(),
                        version,
                    })
                    .expect("Reference CodeLens data should serialize"),
                ),
            });
        }
        if let Some(children) = symbol.children.as_deref() {
            collect_symbol_lenses(children, uri, version, overloads, lenses);
        }
    }
}

#[cfg(test)]
mod tests {
    use lsp_types::Uri;

    use super::unresolved_code_lenses;
    use crate::state::require::Require;
    use crate::test::util::TestEnv;

    #[test]
    fn overload_signatures_have_no_reference_lenses() {
        let source = r#"from typing import overload as signature
import typing
@signature
def f(x: int) -> int: ...
@typing.overload
def f(x: str) -> str: ...
def f(x):
    def inner():
        pass
    inner()
    return x
f(1)
f("a")
class C:
    @property
    def p(self) -> int:
        return 1
    @p.setter
    def p(self, value: int) -> None: pass
C().p
"#;
        let mut env = TestEnv::new().with_default_require_level(Require::Everything);
        env.add("main", source);
        let (state, handle) = env.to_state();
        let transaction = state.transaction();
        let lenses = unresolved_code_lenses(
            &transaction,
            &handle("main"),
            &Uri::parse("file:///main.py").unwrap(),
            Some(1),
        )
        .unwrap();
        let lines: Vec<_> = lenses.iter().map(|lens| lens.range.start.line).collect();
        assert_eq!(lines, vec![6, 7, 13, 15, 18]);
    }
}
