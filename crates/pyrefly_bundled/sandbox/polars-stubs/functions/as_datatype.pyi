from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, overload
from polars import functions as F
from polars._utils.parse import (
    parse_into_expression,
    parse_into_list_of_expressions,
)
from polars._utils.unstable import issue_unstable_warning
from polars._utils.wrap import wrap_expr
from polars.datatypes import Date, Struct, Time
from collections.abc import Iterable
from typing import Literal
from polars import Expr, Series
from polars._typing import Ambiguous, IntoExpr, SchemaDict, TimeUnit


def datetime_(year: int | IntoExpr, month: int | IntoExpr, day: int | IntoExpr, hour: int | IntoExpr | None = None, minute: int | IntoExpr | None = None, second: int | IntoExpr | None = None, microsecond: int | IntoExpr | None = None, *, time_unit: TimeUnit = "us", time_zone: str | None = None, ambiguous: Ambiguous | Expr = "raise") -> Expr: ...


def date_(year: Expr | str | int, month: Expr | str | int, day: Expr | str | int) -> Expr: ...


def time_(hour: Expr | str | int | None = None, minute: Expr | str | int | None = None, second: Expr | str | int | None = None, microsecond: Expr | str | int | None = None) -> Expr: ...


def duration(*, weeks: Expr | str | int | float | None = None, days: Expr | str | int | float | None = None, hours: Expr | str | int | float | None = None, minutes: Expr | str | int | float | None = None, seconds: Expr | str | int | float | None = None, milliseconds: Expr | str | int | float | None = None, microseconds: Expr | str | int | float | None = None, nanoseconds: Expr | str | int | float | None = None, time_unit: TimeUnit | None = None) -> Expr: ...


def concat_list(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr) -> Expr: ...


def list(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr) -> Expr: ...


def concat_arr(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr) -> Expr: ...


@overload
def struct(*exprs: IntoExpr | Iterable[IntoExpr], schema: SchemaDict | None = ..., eager: Literal[False] = ..., **named_exprs: IntoExpr) -> Expr: ...


@overload
def struct(*exprs: IntoExpr | Iterable[IntoExpr], schema: SchemaDict | None = ..., eager: Literal[True], **named_exprs: IntoExpr) -> Series: ...


@overload
def struct(*exprs: IntoExpr | Iterable[IntoExpr], schema: SchemaDict | None = ..., eager: bool, **named_exprs: IntoExpr) -> Expr | Series: ...


def concat_str(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr, separator: str = "", ignore_nulls: bool = False) -> Expr: ...


def format(f_string: str, *args: IntoExpr) -> Expr: ...
