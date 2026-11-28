from __future__ import annotations
import contextlib
from collections.abc import Collection, Iterable, Mapping
from typing import TYPE_CHECKING, Any, Literal, overload
import polars._reexport as pl
from polars import functions as F
from polars._utils.various import qualified_type_name
from polars.exceptions import ComputeError
from polars import Expr
from polars._plr import PyExpr
from polars._typing import ColumnNameOrSelector, IntoExpr, PolarsDataType


def parse_into_expression(input: IntoExpr, *, str_as_lit: bool = False, list_as_series: bool = False, structify: bool = False, dtype: PolarsDataType | None = None, require_selector: bool = False) -> PyExpr: ...


def parse_into_list_of_expressions(*inputs: IntoExpr | Iterable[IntoExpr], **named_inputs: IntoExpr) -> list[PyExpr]: ...


def parse_into_list_of_expressions_require_selectors(*inputs: IntoExpr | Iterable[IntoExpr], **named_inputs: IntoExpr) -> list[PyExpr]: ...


@overload
def parse_into_selector(i: ColumnNameOrSelector, *, strict: bool = ..., raise_if_not_selector: Literal[False] = False) -> pl.Selector: ...


@overload
def parse_into_selector(i: ColumnNameOrSelector, *, strict: bool = ..., raise_if_not_selector: Literal[True]) -> pl.Selector | None: ...


def parse_list_into_selector(inputs: ColumnNameOrSelector | Collection[ColumnNameOrSelector], *, strict: bool = True) -> pl.Selector: ...


def parse_predicates_constraints_into_expression(*predicates: IntoExpr | Iterable[IntoExpr], **constraints: Any) -> PyExpr: ...
