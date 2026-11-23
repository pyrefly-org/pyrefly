from __future__ import annotations
from itertools import chain
from typing import TYPE_CHECKING, Any
from polars import functions as F
from polars._utils.convert import parse_as_duration_string
from polars._utils.expired import getattr_fallback, raise_for_removed_attributes
from polars._utils.parse.expr import _parse_inputs_as_iterable
from collections.abc import Callable, Iterable, Iterator
from datetime import timedelta
from polars import DataFrame, Series
from polars._typing import (
        ClosedInterval,
        IntoExpr,
        Label,
        QuantileMethod,
        SchemaDict,
        StartBy,
    )
from polars.lazyframe.group_by import LazyGroupBy


class GroupByIter:
    def __init__(self, df: DataFrame, group_names: Iterator[tuple[Any, ...]], group_indices: Series) -> None: ...

    def __iter__(self) -> GroupByIter: ...

    def __next__(self) -> tuple[tuple[Any, ...], DataFrame]: ...


class RollingGroupByIter:
    def __init__(self, df: DataFrame, group_names: Iterator[tuple[Any, ...]], group_indices: Series) -> None: ...

    def __iter__(self) -> RollingGroupByIter: ...

    def __next__(self) -> tuple[tuple[object, ...], DataFrame]: ...


class DynamicGroupByIter:
    def __init__(self, df: DataFrame, group_names: Iterator[tuple[Any, ...]], group_indices: Series) -> None: ...

    def __iter__(self) -> DynamicGroupByIter: ...

    def __next__(self) -> tuple[tuple[object, ...], DataFrame]: ...


class GroupBy:
    df: DataFrame
    by: tuple[IntoExpr | Iterable[IntoExpr], ...]
    named_by: dict[str, IntoExpr]
    maintain_order: bool
    predicates: Iterable[Any] | None

    def __init__(self, df: DataFrame, *by: IntoExpr | Iterable[IntoExpr], maintain_order: bool, predicates: Iterable[Any] | None, **named_by: IntoExpr) -> None: ...

    def __iter__(self) -> GroupByIter: ...

    def having(self, *predicates: IntoExpr | Iterable[IntoExpr]) -> GroupBy: ...

    def agg(self, *aggs: IntoExpr | Iterable[IntoExpr], **named_aggs: IntoExpr) -> DataFrame: ...

    def map_groups(self, function: Callable[[DataFrame], DataFrame]) -> DataFrame: ...

    def head(self, n: int = 5) -> DataFrame: ...

    def tail(self, n: int = 5) -> DataFrame: ...

    def all(self) -> DataFrame: ...

    def len(self, name: str | None = None) -> DataFrame: ...

    def first(self, *, ignore_nulls: bool = False) -> DataFrame: ...

    def last(self, *, ignore_nulls: bool = False) -> DataFrame: ...

    def max(self) -> DataFrame: ...

    def mean(self) -> DataFrame: ...

    def median(self) -> DataFrame: ...

    def min(self) -> DataFrame: ...

    def n_unique(self) -> DataFrame: ...

    def quantile(self, quantile: float, interpolation: QuantileMethod = "nearest") -> DataFrame: ...

    def sum(self) -> DataFrame: ...


class RollingGroupBy:
    df: DataFrame
    time_column: IntoExpr
    period: str
    offset: str | None
    closed: ClosedInterval
    group_by: IntoExpr | Iterable[IntoExpr] | None
    predicates: Iterable[Any] | None

    def __init__(self, df: DataFrame, index_column: IntoExpr, *, period: str | timedelta, offset: str | timedelta | None, closed: ClosedInterval, group_by: IntoExpr | Iterable[IntoExpr] | None, predicates: Iterable[Any] | None) -> None: ...

    def __iter__(self) -> RollingGroupByIter: ...

    def having(self, *predicates: IntoExpr | Iterable[IntoExpr]) -> RollingGroupBy: ...

    def agg(self, *aggs: IntoExpr | Iterable[IntoExpr], **named_aggs: IntoExpr) -> DataFrame: ...

    def map_groups(self, function: Callable[[DataFrame], DataFrame], schema: SchemaDict | None) -> DataFrame: ...


class DynamicGroupBy:
    df: DataFrame
    time_column: IntoExpr
    every: str
    period: str | None
    offset: str | None
    label: Label
    include_boundaries: bool
    closed: ClosedInterval
    group_by: IntoExpr | Iterable[IntoExpr] | None
    start_by: StartBy
    predicates: Iterable[Any] | None

    def __init__(self, df: DataFrame, index_column: IntoExpr, *, every: str | timedelta, period: str | timedelta | None, offset: str | timedelta | None, include_boundaries: bool, closed: ClosedInterval, label: Label, group_by: IntoExpr | Iterable[IntoExpr] | None, start_by: StartBy, predicates: Iterable[Any] | None) -> None: ...

    def __iter__(self) -> DynamicGroupByIter: ...

    def having(self, *predicates: IntoExpr | Iterable[IntoExpr]) -> DynamicGroupBy: ...

    def agg(self, *aggs: IntoExpr | Iterable[IntoExpr], **named_aggs: IntoExpr) -> DataFrame: ...

    def map_groups(self, function: Callable[[DataFrame], DataFrame], schema: SchemaDict | None) -> DataFrame: ...
