from _typeshed import Incomplete

from __future__ import annotations
import abc
from dataclasses import dataclass
from typing import TYPE_CHECKING
from collections.abc import Collection
import pyarrow.compute
import polars as pl
from polars._typing import SchemaDict


class LazyFrameResolver(abc.ABC):
    def lazy(self) -> pl.LazyFrame: ...

    @abc.abstractmethod
    def schema(self) -> SchemaDict: ...

    @abc.abstractmethod
    def resolve_lazyframe(self, *, projection: list[str] | None, limit: int | None, filters: list[FilterExpr], filter_columns: list[str], filter_drop_columns_idx: int | None, existing_resolved_version_key: str | None) -> pl.LazyFrame | tuple[pl.LazyFrame | None, ResolvedLazyFrameProps]: ...

    def cse_eq(self, other: object) -> bool: ...


@dataclass(kw_only=True)
class FilterExpr:
    expr: pl.Expr
    pyarrow_str: str | None

    @property
    def pyarrow_expr(self) -> pyarrow.compute.Expression | None: ...

    def __init__(self, *, expr: Expr, pyarrow_str: str | None, _pyarrow_expr: Incomplete) -> None: ...


@dataclass(kw_only=True)
class ResolvedLazyFrameProps:
    version_key: str | None = None
    applied_filters: Collection[int]

    def __init__(self, *, version_key: str | None = ..., applied_filters: Collection[int] = ...) -> None: ...
