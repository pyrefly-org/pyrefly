from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, overload
from polars import functions as F
from polars._utils.parse import parse_into_expression
from polars._utils.unstable import unstable
from polars._utils.wrap import wrap_expr
from typing import Literal
from polars import Expr, Series
from polars._typing import (
        ClosedInterval,
        IntoExpr,
        IntoExprColumn,
        NumericLiteral,
        TemporalLiteral,
    )


@overload
def linear_space(start: NumericLiteral | TemporalLiteral | IntoExpr, end: NumericLiteral | TemporalLiteral | IntoExpr, num_samples: int | IntoExpr, *, closed: ClosedInterval = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def linear_space(start: NumericLiteral | TemporalLiteral | IntoExpr, end: NumericLiteral | TemporalLiteral | IntoExpr, num_samples: int | IntoExpr, *, closed: ClosedInterval = ..., eager: Literal[True]) -> Series: ...


@overload
def linear_space(start: NumericLiteral | TemporalLiteral | IntoExpr, end: NumericLiteral | TemporalLiteral | IntoExpr, num_samples: int | IntoExpr, *, closed: ClosedInterval = ..., eager: bool) -> Expr | Series: ...


@overload
def linear_spaces(start: NumericLiteral | TemporalLiteral | IntoExprColumn, end: NumericLiteral | TemporalLiteral | IntoExprColumn, num_samples: int | IntoExprColumn, *, closed: ClosedInterval = ..., as_array: bool = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def linear_spaces(start: NumericLiteral | TemporalLiteral | IntoExprColumn, end: NumericLiteral | TemporalLiteral | IntoExprColumn, num_samples: int | IntoExprColumn, *, closed: ClosedInterval = ..., as_array: bool = ..., eager: Literal[True]) -> Series: ...


@overload
def linear_spaces(start: NumericLiteral | TemporalLiteral | IntoExprColumn, end: NumericLiteral | TemporalLiteral | IntoExprColumn, num_samples: int | IntoExprColumn, *, closed: ClosedInterval = ..., as_array: bool = ..., eager: bool) -> Expr | Series: ...
