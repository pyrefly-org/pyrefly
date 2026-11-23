from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
import polars as pl
from polars._utils.deprecation import deprecate_nonkeyword_arguments
from polars._utils.parse import parse_into_expression
from polars._utils.unstable import unstable
from polars._utils.wrap import wrap_expr
from collections.abc import Iterable
from datetime import date
from polars import Expr, Series
from polars._typing import IntoExprColumn


@unstable()
@deprecate_nonkeyword_arguments(allowed_args=["start", "end"], version="1.27.0")
def business_day_count(start: date | IntoExprColumn, end: date | IntoExprColumn, week_mask: Iterable[bool] = ..., holidays: Iterable[date] | Expr | Series = ()) -> Expr: ...
