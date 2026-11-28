from __future__ import annotations
import contextlib
import sys
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any
from polars._utils.parse import parse_into_list_of_expressions
from polars._utils.wrap import wrap_expr
from collections.abc import Iterable
from polars import Expr
from polars._typing import IntoExpr

__all__ = ["register_plugin_function"]


def register_plugin_function(*, plugin_path: Path | str, function_name: str, args: IntoExpr | Iterable[IntoExpr], kwargs: dict[str, Any] | None = None, is_elementwise: bool = False, changes_length: bool = False, returns_scalar: bool = False, cast_to_supertype: bool = False, input_wildcard_expansion: bool = False, pass_name_to_apply: bool = False, use_abs_path: bool = False, is_deterministic: bool = True) -> Expr: ...
