from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Any, overload
import polars._reexport as pl
import polars.functions as F
import polars.selectors as cs
from polars._dependencies import _check_for_numpy
from polars._dependencies import numpy as np
from polars._utils.expired import (
    RemovedParameter,
    RenamedParameter,
    removed_parameters,
)
from polars._utils.parse import (
    parse_into_expression,
    parse_into_list_of_expressions,
)
from polars._utils.unstable import issue_unstable_warning, unstable
from polars._utils.various import extend_bool, qualified_type_name
from polars._utils.wrap import wrap_expr, wrap_s
from polars.datatypes import DTYPE_TEMPORAL_UNITS, Date, Datetime, Int64
from polars.datatypes._parse import parse_into_datatype_expr
from polars.lazyframe.engine_config import _eager_engine, _select_engine
from polars.lazyframe.opt_flags import (
    DEFAULT_QUERY_OPT_FLAGS,
    REMOVED_OLD_OPT_FLAGS,
)
from polars.meta.index_type import get_index_type
from collections.abc import Awaitable, Callable, Collection, Iterable, Sequence
from typing import Literal
from polars import DataFrame, Expr, LazyFrame, Series
from polars._plr import PyExpr
from polars._typing import (
        AsyncResult,
        CorrelationMethod,
        EngineType,
        EpochTimeUnit,
        IntoExpr,
        PolarsDataType,
        QuantileMethod,
    )
from polars._utils.async_ import _GeventDataFrameResult
from polars.datatypes import DataType
from polars.lazyframe.opt_flags import (
        QueryOptFlags,
    )


def field(name: str | list[str]) -> Expr: ...


def element() -> Expr: ...


def count(*columns: str) -> Expr: ...


def cum_count(*columns: str, reverse: bool = False) -> Expr: ...


def implode(*columns: str, maintain_order: bool = True) -> Expr: ...


def std(column: str, ddof: int = 1) -> Expr: ...


def var(column: str, ddof: int = 1) -> Expr: ...


def mean(*columns: str) -> Expr: ...


def median(*columns: str) -> Expr: ...


def n_unique(*columns: str) -> Expr: ...


def approx_n_unique(*columns: str) -> Expr: ...


def first(*columns: str) -> Expr: ...


def last(*columns: str) -> Expr: ...


def nth(*indices: int | Sequence[int], strict: bool = True) -> Expr: ...


def head(column: str, n: int = 10) -> Expr: ...


def tail(column: str, n: int = 10) -> Expr: ...


@overload
def corr(a: IntoExpr, b: IntoExpr, *, method: CorrelationMethod = ..., propagate_nans: bool = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def corr(a: IntoExpr, b: IntoExpr, *, method: CorrelationMethod = ..., propagate_nans: bool = ..., eager: Literal[True]) -> Series: ...


@overload
def cov(a: IntoExpr, b: IntoExpr, *, ddof: int = ..., eager: Literal[False] = ...) -> Expr: ...


@overload
def cov(a: IntoExpr, b: IntoExpr, *, ddof: int = ..., eager: Literal[True]) -> Series: ...


def map_batches(exprs: Sequence[str | Expr], function: Callable[[Sequence[Series]], Series | Any], return_dtype: PolarsDataType | pl.DataTypeExpr | None = None, *, is_elementwise: bool = False, returns_scalar: bool = False) -> Expr: ...


def map_groups(exprs: Sequence[str | Expr], function: Callable[[Sequence[Series]], Series | Any], return_dtype: PolarsDataType | pl.DataTypeExpr | None = None, *, is_elementwise: bool = False, returns_scalar: bool = False) -> Expr: ...


@unstable()
def pipe_with_dtype(exprs: Sequence[str | Expr], function: Callable[[list[tuple[Expr, DataType]]], IntoExpr]) -> Expr: ...


def fold(acc: IntoExpr, function: Callable[[Series, Series], Series], exprs: Sequence[Expr | str] | Expr, *, returns_scalar: bool = False, return_dtype: pl.DataTypeExpr | PolarsDataType | None = None) -> Expr: ...


def reduce(function: Callable[[Series, Series], Series], exprs: Sequence[Expr | str] | Expr, *, returns_scalar: bool = False, return_dtype: pl.DataTypeExpr | PolarsDataType | None = None) -> Expr: ...


def cum_fold(acc: IntoExpr, function: Callable[[Series, Series], Series], exprs: Sequence[Expr | str] | Expr, *, returns_scalar: bool = False, return_dtype: pl.DataTypeExpr | PolarsDataType | None = None, include_init: bool = False) -> Expr: ...


def cum_reduce(function: Callable[[Series, Series], Series], exprs: Sequence[Expr | str] | Expr, *, returns_scalar: bool = False, return_dtype: pl.DataTypeExpr | PolarsDataType | None = None) -> Expr: ...


def arctan2(y: str | Expr, x: str | Expr) -> Expr: ...


def exclude(columns: str | PolarsDataType | Collection[str] | Collection[PolarsDataType], *more_columns: str | PolarsDataType) -> Expr: ...


def quantile(column: str, quantile: float | Expr, interpolation: QuantileMethod = "nearest") -> Expr: ...


def arg_sort_by(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr, descending: bool | Sequence[bool] = False, nulls_last: bool | Sequence[bool] = False, multithreaded: bool = True, maintain_order: bool = False) -> Expr: ...


@overload
def collect_all(lazy_frames: Iterable[LazyFrame], *, optimizations: QueryOptFlags = ..., engine: EngineType = "auto", lazy: Literal[False] = False) -> list[DataFrame]: ...


@overload
def collect_all(lazy_frames: Iterable[LazyFrame], *, optimizations: QueryOptFlags = ..., engine: EngineType = "auto", lazy: Literal[True]) -> LazyFrame: ...


@overload
def collect_all_async(lazy_frames: Iterable[LazyFrame], *, gevent: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> _GeventDataFrameResult[list[DataFrame]]: ...


@overload
def collect_all_async(lazy_frames: Iterable[LazyFrame], *, gevent: Literal[False] = False, engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> Awaitable[list[DataFrame]]: ...


@unstable()
def explain_all(lazy_frames: Iterable[LazyFrame], *, optimizations: QueryOptFlags = ...) -> str: ...


@overload
def select(*exprs: IntoExpr | Iterable[IntoExpr], eager: Literal[True] = ..., **named_exprs: IntoExpr) -> DataFrame: ...


@overload
def select(*exprs: IntoExpr | Iterable[IntoExpr], eager: Literal[False], **named_exprs: IntoExpr) -> LazyFrame: ...


@overload
def arg_where(condition: Expr | Series, *, eager: Literal[False] = ...) -> Expr: ...


@overload
def arg_where(condition: Expr | Series, *, eager: Literal[True]) -> Series: ...


@overload
def coalesce(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr, eager: Literal[False] = ...) -> Expr: ...


@overload
def coalesce(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr, eager: Literal[True]) -> Series: ...


@overload
def coalesce(exprs: IntoExpr | Iterable[IntoExpr], *more_exprs: IntoExpr, eager: bool) -> Expr | Series: ...


@overload
def from_epoch(column: str | Expr, time_unit: EpochTimeUnit = ...) -> Expr: ...


@overload
def from_epoch(column: Series | Sequence[int | float], time_unit: EpochTimeUnit = ...) -> Series: ...


@removed_parameters(
    RenamedParameter(
        name="min_periods",
        new_name="min_samples",
        deprecated_in="1.21.0",
        removed_in="2.0",
    ),
)
def rolling_cov(a: str | Expr, b: str | Expr, *, window_size: int, min_samples: int | None = None, ddof: int = 1) -> Expr: ...


@removed_parameters(
    RenamedParameter(
        name="min_periods",
        new_name="min_samples",
        deprecated_in="1.21.0",
        removed_in="2.0",
    ),
)
def rolling_corr(a: str | Expr, b: str | Expr, *, window_size: int, min_samples: int | None = None) -> Expr: ...


@overload
def sql_expr(sql: str) -> Expr: ...


@overload
def sql_expr(sql: Sequence[str]) -> list[Expr]: ...


@unstable()
def row_index(name: str = "index") -> pl.Expr: ...
