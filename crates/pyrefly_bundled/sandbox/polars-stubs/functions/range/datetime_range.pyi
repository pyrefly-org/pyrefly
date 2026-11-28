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
from polars._typing import ClosedInterval, IntoExprColumn, TimeUnit


@overload
def datetime_range(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def datetime_range(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: Literal[True]) -> Series: ...


@overload
def datetime_range(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: bool) -> Series | Expr: ...


@overload
def datetime_ranges(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def datetime_ranges(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: Literal[True]) -> Series: ...


@overload
def datetime_ranges(start: datetime | date | IntoExprColumn, end: datetime | date | IntoExprColumn, interval: str | timedelta = ..., *, closed: ClosedInterval = ..., time_unit: TimeUnit | None = ..., time_zone: str | None = ..., eager: bool) -> Series | Expr: ...
