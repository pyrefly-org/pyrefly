from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, overload
from polars import functions as F
from polars._utils.parse import parse_into_expression
from polars._utils.wrap import wrap_expr, wrap_s
from polars.datatypes import Int64
from polars.datatypes._parse import parse_into_datatype_expr
from typing import Literal
from polars import DataTypeExpr, Expr, Series
from polars._typing import IntoExprColumn, PolarsIntegerType


@overload
def arange(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def arange(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[True]) -> Series: ...


@overload
def arange(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: bool) -> Expr | Series: ...


@overload
def int_range(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def int_range(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[True]) -> Series: ...


@overload
def int_range(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: bool) -> Expr | Series: ...


@overload
def int_ranges(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int | IntoExprColumn = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def int_ranges(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int | IntoExprColumn = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: Literal[True]) -> Series: ...


@overload
def int_ranges(start: int | IntoExprColumn = ..., end: int | IntoExprColumn | None = ..., step: int | IntoExprColumn = ..., *, dtype: PolarsIntegerType | DataTypeExpr = ..., eager: bool) -> Expr | Series: ...
