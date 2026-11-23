from __future__ import annotations
import contextlib
from datetime import time
from typing import TYPE_CHECKING, overload
from polars import functions as F
from polars._utils.parse import parse_into_expression
from polars._utils.wrap import wrap_expr
from polars.functions.range._utils import parse_interval_argument
from datetime import timedelta
from typing import Literal
from polars import Expr, Series
from polars._typing import ClosedInterval, IntoExprColumn


@overload
def time_range(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def time_range(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[True]) -> Series: ...


@overload
def time_range(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: bool) -> Series | Expr: ...


@overload
def time_ranges(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def time_ranges(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: Literal[True]) -> Series: ...


@overload
def time_ranges(start: time | IntoExprColumn | None = ..., end: time | IntoExprColumn | None = ..., interval: str | timedelta = ..., *, closed: ClosedInterval = ..., eager: bool) -> Series | Expr: ...
