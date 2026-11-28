from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, overload
from polars import functions as F
from polars._utils.parse import parse_into_expression
from polars._utils.wrap import wrap_expr
from polars.functions.range._utils import parse_interval_argument
from datetime import date, datetime, timedelta
from typing import Literal
from polars import Expr, Series
from polars._typing import ClosedInterval, IntoExprColumn


@overload
def date_range(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def date_range(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[True]) -> Series: ...


@overload
def date_range(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: bool) -> Series | Expr: ...


@overload
def date_ranges(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def date_ranges(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[True]) -> Series: ...


@overload
def date_ranges(start: date | datetime | IntoExprColumn, end: date | datetime | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: bool) -> Series | Expr: ...
