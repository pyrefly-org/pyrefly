/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

use pyrefly_types::function::Deprecation;
use ruff_python_ast::Expr;
use ruff_python_ast::ExprCall;
use ruff_python_ast::ExprStringLiteral;

fn extract_message(call: &ExprCall) -> Option<String> {
    if let Some(arg) = call.arguments.args.first()
        && let Expr::StringLiteral(ExprStringLiteral { value, .. }) = arg
    {
        Some(value.to_string())
    } else {
        None
    }
}

/// Parse a decorator using a custom resolver for SpecialExport::Deprecated.
pub fn parse_deprecation(e: &Expr, is_deprecated: impl Fn(&Expr) -> bool) -> Option<Deprecation> {
    let call = e.as_call_expr()?;
    if !is_deprecated(&call.func) {
        return None;
    }
    Some(Deprecation::new(extract_message(call)))
}
