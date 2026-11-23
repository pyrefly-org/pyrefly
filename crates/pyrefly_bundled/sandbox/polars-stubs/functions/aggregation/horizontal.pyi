from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
import polars.functions as F
from polars._utils.parse import parse_into_list_of_expressions
from polars._utils.wrap import wrap_expr
from collections.abc import Iterable
from polars import Expr
from polars._typing import IntoExpr


def all_horizontal(*exprs: IntoExpr | Iterable[IntoExpr]) -> Expr: ...


def any_horizontal(*exprs: IntoExpr | Iterable[IntoExpr]) -> Expr: ...


def max_horizontal(*exprs: IntoExpr | Iterable[IntoExpr]) -> Expr: ...


def min_horizontal(*exprs: IntoExpr | Iterable[IntoExpr]) -> Expr: ...


def sum_horizontal(*exprs: IntoExpr | Iterable[IntoExpr], ignore_nulls: bool = True) -> Expr: ...


def mean_horizontal(*exprs: IntoExpr | Iterable[IntoExpr], ignore_nulls: bool = True) -> Expr: ...


def cum_sum_horizontal(*exprs: IntoExpr | Iterable[IntoExpr]) -> Expr: ...
