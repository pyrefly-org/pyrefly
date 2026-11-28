from __future__ import annotations
from typing import TYPE_CHECKING, Protocol, runtime_checkable
from polars.dataframe import DataFrame
from polars.lazyframe import LazyFrame


@runtime_checkable
class QueryResult(Protocol):
    @property
    def head(self) -> DataFrame | None: ...

    @property
    def n_rows_total(self) -> int | None: ...

    def lazy(self) -> LazyFrame: ...


class SingleNodeQueryResult:
    def __init__(self, df: DataFrame) -> None: ...

    @property
    def head(self) -> DataFrame | None: ...

    @property
    def n_rows_total(self) -> int | None: ...

    def lazy(self) -> LazyFrame: ...

    def __repr__(self) -> str: ...
