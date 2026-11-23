from __future__ import annotations
import contextlib
from decimal import Decimal as D
from functools import lru_cache
from typing import TYPE_CHECKING, Any, overload
from polars import functions as F
from polars._utils.parse import parse_into_expression
from polars._utils.various import qualified_type_name
from polars._utils.wrap import wrap_expr
from polars.datatypes import (
    Array,
    Boolean,
    Decimal,
    Float64,
    List,
    Utf8,
)
from polars.datatypes.group import FLOAT_DTYPES, INTEGER_DTYPES
from typing import Literal
from polars import Expr, Series
from polars._typing import IntoExpr, PolarsDataType


@overload
def repeat(value: IntoExpr | None, n: int | Expr, *, dtype: PolarsDataType | None = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def repeat(value: IntoExpr | None, n: int | Expr, *, dtype: PolarsDataType | None = ..., eager: Literal[True]) -> Series: ...


@overload
def repeat(value: IntoExpr | None, n: int | Expr, *, dtype: PolarsDataType | None = ..., eager: bool) -> Expr | Series: ...


@overload
def ones(n: int | Expr, dtype: PolarsDataType = ..., *, eager: Literal[False] = ...) -> Expr: ...


@overload
def ones(n: int | Expr, dtype: PolarsDataType = ..., *, eager: Literal[True]) -> Series: ...


@overload
def ones(n: int | Expr, dtype: PolarsDataType = ..., *, eager: bool) -> Expr | Series: ...


@overload
def zeros(n: int | Expr, dtype: PolarsDataType = ..., *, eager: Literal[False] = ...) -> Expr: ...


@overload
def zeros(n: int | Expr, dtype: PolarsDataType = ..., *, eager: Literal[True]) -> Series: ...


@overload
def zeros(n: int | Expr, dtype: PolarsDataType = ..., *, eager: bool) -> Expr | Series: ...
