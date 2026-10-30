/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

use lsp_types::CompletionItem;
use lsp_types::CompletionItemTextEdit;
use lsp_types::Range;
use lsp_types::TextEdit;
use pretty_assertions::assert_eq;
use pyrefly_python::ast::Ast;
use pyrefly_python::sys_info::PythonVersion;
use ruff_python_ast::PySourceType;
use ruff_text_size::TextSize;

use crate::state::lsp::ImportFormat;
use crate::state::require::Require;
use crate::test::util::TestEnv;
use crate::test::util::mk_multi_file_state;
use crate::test::util::mk_multi_file_state_with_env;

/// Applies the completion and all additional edits to the original buffer.
fn complete(code: &str, dependencies: &[(&'static str, &str)]) -> (CompletionItem, String) {
    complete_in_module("main", code, dependencies, ImportFormat::Absolute)
}

fn complete_in_module(
    module_name: &'static str,
    code: &str,
    dependencies: &[(&'static str, &str)],
    import_format: ImportFormat,
) -> (CompletionItem, String) {
    let mut files = dependencies.to_vec();
    files.push((module_name, code));
    let (handles, state) = mk_multi_file_state(&files, Require::Everything, false);
    let handle = &handles[module_name];
    let txn = state.transaction();
    let module = txn.get_module_info(handle).unwrap();
    let name_start = code.rfind("def met").unwrap() + "def ".len();
    let position = TextSize::try_from(name_start + "met".len()).unwrap();
    let item = txn
        .completion(handle, position, import_format, true, None)
        .into_iter()
        .find(|item| item.label == "method")
        .expect("expected a method-name completion");
    let main_edit = match &item.text_edit {
        Some(CompletionItemTextEdit::TextEdit(edit)) => edit.clone(),
        Some(CompletionItemTextEdit::InsertReplaceEdit(_)) => {
            panic!("unexpected insert/replace edit")
        }
        None => TextEdit {
            range: Range::new(
                module.to_lsp_position(TextSize::try_from(name_start).unwrap()),
                module.to_lsp_position(position),
            ),
            new_text: item
                .insert_text
                .clone()
                .unwrap_or_else(|| item.label.clone()),
        },
    };
    let mut edits = item.additional_text_edits.clone().unwrap_or_default();
    edits.push(main_edit);
    let mut edits = edits
        .into_iter()
        .map(|edit| {
            let start = module.from_lsp_position(edit.range.start, None).to_usize();
            let end = module.from_lsp_position(edit.range.end, None).to_usize();
            (start..end, edit.new_text)
        })
        .collect::<Vec<_>>();
    edits.sort_by_key(|(range, _)| range.start);
    for pair in edits.windows(2) {
        assert!(pair[0].0.end <= pair[1].0.start, "completion edits overlap");
    }
    let mut result = code.to_owned();
    for (range, text) in edits.into_iter().rev() {
        result.replace_range(range, &text);
    }
    (item, result)
}

/// Checks Python syntax and type errors after all completion edits apply.
fn check_result(code: &str, dependencies: &[(&'static str, &str)]) {
    let (_, errors, unsupported) = Ast::parse(code, PySourceType::Python);
    assert!(
        errors.is_empty(),
        "invalid completed source:\n{code}\n{errors:?}"
    );
    assert!(unsupported.is_empty(), "{unsupported:?}");
    let mut files = dependencies.to_vec();
    files.push(("main", code));
    mk_multi_file_state(&files, Require::Everything, true);
}

#[test]
fn instance_method() {
    let code = r#"class Base:
    def method(this, value: str, /, *args: int, flag: bool = False, **kwargs: str) -> int:
        return 0

class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    assert_eq!(
        result,
        r#"from typing import override
class Base:
    def method(this, value: str, /, *args: int, flag: bool = False, **kwargs: str) -> int:
        return 0

class Child(Base):
    @override
    def method(this, value: 'str', /, *args: 'int', flag: 'bool' = False, **kwargs: 'str') -> 'int':
        return super().method(value, *args, flag=flag, **kwargs)
"#
    );
    check_result(&result, &[]);
}

#[test]
fn imported_annotations_and_future_import() {
    let deps = [(
        "base",
        r#"class Payload: pass
class Base:
    def method(self, value: Payload) -> Payload:
        return value
"#,
    )];
    let code = r#""""Module documentation."""
from __future__ import annotations
from base import Base

class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &deps);
    assert!(item.text_edit.is_some());
    assert!(
        result.starts_with(
            r#""""Module documentation."""
from __future__ import annotations
from typing import override
from base import Base, Payload
"#
        ),
        "{result}"
    );
    check_result(&result, &deps);
}

#[test]
fn existing_import_aliases() {
    let deps = [(
        "base",
        r#"class Payload: pass
class Base:
    def method(self, value: Payload) -> Payload:
        return value
"#,
    )];
    let code = r#"from base import Base, Payload as Data
from typing import override as overrides
class Child(Base):
    def met
"#;
    let (_, result) = complete(code, &deps);
    assert!(
        result.contains(
            r#"@overrides
    def method(self, value: 'Data') -> 'Data':"#
        ),
        "{result}"
    );
    assert_eq!(result.matches("from typing").count(), 1);
    check_result(&result, &deps);
}

#[test]
fn crlf_and_tabs() {
    let code = "class Base:\r\n\tdef method(this, value: int = 7) -> int:\r\n\t\treturn value\r\nclass Child(Base):\r\n\tdef met\r\n";
    let (_, result) = complete(code, &[]);
    assert!(!result.replace("\r\n", "").contains('\n'));
    assert!(result.contains("\t@override\r\n\tdef method(this, value: 'int' = 7) -> 'int':\r\n\t\treturn super().method(value)"), "{result}");
    check_result(&result, &[]);
}

#[test]
fn existing_declaration_stays_name_only() {
    let code = r#"class Base:
    def method(this, value: int) -> int:
        return value
class Child(Base):
    def met(this, value: int) -> int:
        return value + 1
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_none());
    assert!(item.additional_text_edits.is_none());
    assert_eq!(result, code.replace("def met(", "def method("));
    check_result(&result, &[]);
}

#[test]
fn unsupported_methods_stay_name_only() {
    for (base, child) in [
        (
            r#"    @staticmethod
    def method(self: int) -> int: return self
"#,
            r#"    def met
"#,
        ),
        (
            r#"    @staticmethod
    def method(cls: int) -> int: return cls
"#,
            r#"    @staticmethod
    def met
"#,
        ),
        (
            r#"    @classmethod
    def method(cls, value: int) -> int: return value
"#,
            r#"    @classmethod
    def met
"#,
        ),
        (
            r#"    @classmethod
    def method(cls, value: int) -> int: return value
"#,
            r#"    def met
"#,
        ),
        (
            r#"    @property
    def method(self) -> int: return 0
"#,
            r#"    @property
    def met
"#,
        ),
        (
            r#"    async def method(self) -> int: return 0
"#,
            r#"    async def met
"#,
        ),
        (
            r#"    async def method(self):
        yield 1
"#,
            r#"    async def met
"#,
        ),
        (
            r#"    def method[T](self, value: T) -> T: return value
"#,
            r#"    def met
"#,
        ),
        (
            r#"    def method(self, callback: Callable[[int], str]) -> str: return callback(0)
"#,
            r#"    def met
"#,
        ),
        (
            r#"    def method(self, values: tuple[int, ...] = ()) -> tuple[int, ...]: return values
"#,
            r#"    def met
"#,
        ),
        (
            r#"    @overload
    def method(self, value: int) -> int: ...
    @overload
    def method(self, value: str) -> str: ...
    def method(self, value: int | str) -> int | str: return value
"#,
            r#"    def met
"#,
        ),
        (
            r#"    def method(self) -> None: pass
"#,
            r#"    @override
    def met
"#,
        ),
        (
            r#"    def method(super, value: int) -> int: return value
"#,
            r#"    def met
"#,
        ),
        (
            r#"    def method(self) -> None: pass
"#,
            r#"    override = 0
    def met
"#,
        ),
    ] {
        let code = format!(
            r#"from typing import Callable, overload, override
class Base:
{base}
class Child(Base):
{child}"#
        );
        let (item, _) = complete(&code, &[]);
        assert!(item.text_edit.is_none(), "unexpected stub for:\n{code}");
        assert!(
            item.additional_text_edits.is_none(),
            "unexpected edits for:\n{code}"
        );
    }
}

#[test]
fn current_class_method_stays_name_only() {
    let code = r#"class Child:
    def method(this, value: int) -> int:
        return value
    def met
"#;
    let (item, _) = complete(code, &[]);
    assert!(item.text_edit.is_none());
    assert!(item.additional_text_edits.is_none());
}

#[test]
fn unresolved_override_binding_stays_name_only() {
    let code = r#"override = 0
typing = 0
class Base:
    def method(self) -> None: pass
class Child(Base):
    def met
"#;
    let (item, _) = complete(code, &[]);
    assert!(item.text_edit.is_none());
    assert!(item.additional_text_edits.is_none());
}

#[test]
fn shadowed_override_uses_module_import() {
    let code = r#"override = 0
class Base:
    def method(self) -> None: pass
class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    assert!(result.starts_with("import typing\n"), "{result}");
    assert!(result.contains("@typing.override\n"), "{result}");
    check_result(&result, &[]);
}

#[test]
fn missing_override_export_stays_name_only() {
    let code = r#"class Base:
    def method(self) -> None: pass
class Child(Base):
    def met
"#;
    let env = TestEnv::new().with_version(PythonVersion {
        major: 3,
        minor: 11,
        micro: 0,
    });
    let (handles, state) =
        mk_multi_file_state_with_env(env, &[("main", code)], Require::Everything, false);
    let position = TextSize::try_from(code.rfind("met").unwrap() + "met".len()).unwrap();
    let item = state
        .transaction()
        .completion(
            &handles["main"],
            position,
            ImportFormat::Absolute,
            true,
            None,
        )
        .into_iter()
        .find(|item| item.label == "method")
        .expect("expected inherited method completion");
    assert!(item.text_edit.is_none());
    assert!(item.additional_text_edits.is_none());
}

#[test]
fn merges_typing_import() {
    let code = r#"from typing import Any
class Base:
    def method(self, value: Any) -> int:
        return 0
class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    assert!(
        result.contains("from typing import Any, override\n"),
        "{result}"
    );
    assert_eq!(result.matches("from typing import").count(), 1);
    check_result(&result, &[]);
}

#[test]
fn relative_annotation_import() {
    let deps = [
        ("pkg", ""),
        (
            "pkg.base",
            r#"class Payload: pass
class Base:
    def method(self, value: Payload) -> Payload:
        return value
"#,
        ),
    ];
    let code = r#"from .base import Base
class Child(Base):
    def met
"#;
    let (item, result) = complete_in_module("pkg.main", code, &deps, ImportFormat::Relative);
    assert!(item.text_edit.is_some());
    assert!(
        result.contains("from .base import Base, Payload\n"),
        "{result}"
    );
    let mut files = deps.to_vec();
    files.push(("pkg.main", &result));
    mk_multi_file_state(&files, Require::Everything, true);
}

#[test]
fn forward_annotations_are_quoted() {
    let code = r#"class Base:
    def method(self, value: "Later") -> "Later":
        return value
class Child(Base):
    def met
class Later: pass
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    assert_eq!(
        result,
        r#"from typing import override
class Base:
    def method(self, value: "Later") -> "Later":
        return value
class Child(Base):
    @override
    def method(self, value: 'Later') -> 'Later':
        return super().method(value)
class Later: pass
"#
    );
    check_result(&result, &[]);
}

#[test]
fn dunder_override_has_one_completion() {
    let code = r#"class Child:
    def __re
"#;
    let (handles, state) = mk_multi_file_state(&[("main", code)], Require::Everything, false);
    let position = TextSize::try_from(code.rfind("__re").unwrap() + "__re".len()).unwrap();
    let items = state.transaction().completion(
        &handles["main"],
        position,
        ImportFormat::Absolute,
        true,
        None,
    );
    let items = items
        .iter()
        .filter(|item| item.label == "__repr__")
        .collect::<Vec<_>>();
    assert_eq!(items.len(), 1);
    assert!(items[0].text_edit.is_some());
}

#[test]
fn existing_typing_extensions_override() {
    let code = r#"from typing_extensions import override
class Base:
    def method(self) -> None: pass
class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    assert!(!result.contains("from typing import"), "{result}");
    check_result(&result, &[]);
}

#[test]
fn literal_annotations_and_defaults() {
    let code = r#"from typing import Literal
class Base:
    def method(self, value: Literal["a'b\\c"] = "a'b\\c", *, flag: bool = False) -> Literal["a'b\\c"]:
        return value
class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &[]);
    assert!(item.text_edit.is_some());
    check_result(&result, &[]);
}

#[test]
fn conflicting_annotation_names_use_module_imports() {
    let deps = [
        ("left", "class Payload: pass"),
        ("right", "class Payload: pass"),
        (
            "base",
            r#"from left import Payload as Left
from right import Payload as Right
class Base:
    def method(self, left: Left, right: Right) -> tuple[Left, Right]:
        return left, right
"#,
        ),
    ];
    let code = r#"from base import Base
class Child(Base):
    def met
"#;
    let (item, result) = complete(code, &deps);
    assert!(item.text_edit.is_some());
    assert!(result.contains("import left\n"), "{result}");
    assert!(result.contains("import right\n"), "{result}");
    assert!(result.contains("'left.Payload'"), "{result}");
    assert!(result.contains("'right.Payload'"), "{result}");
    check_result(&result, &deps);

    let code = code.replace("    def met", "    left = 0\n    def met");
    let (item, _) = complete(&code, &deps);
    assert!(item.text_edit.is_none());
    assert!(item.additional_text_edits.is_none());
}
