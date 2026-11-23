from __future__ import annotations
import contextlib
import importlib.util
from typing import (
    TYPE_CHECKING,
    Generic,
    overload,
)
from polars._dependencies import _check_for_pandas, _check_for_pyarrow
from polars._dependencies import pandas as pd
from polars._dependencies import pyarrow as pa
from polars._typing import FrameType
from polars._utils.expired import RenamedParameter, removed_parameters
from polars._utils.pycapsule import is_pycapsule
from polars._utils.unstable import issue_unstable_warning
from polars._utils.various import _get_stack_locals, qualified_type_name
from polars._utils.wrap import wrap_ldf
from polars.convert import from_pandas
from polars.dataframe import DataFrame
from polars.lazyframe import LazyFrame
from polars.series import Series
from collections.abc import Callable, Collection, Mapping, Sequence
from types import TracebackType
from typing import Any, Final, Literal, Self, TypeAlias
import pyiceberg.catalog
from polars._plr import PyLazyFrame
from polars._typing import StorageOptionsDict
from polars.io.iceberg import IcebergCatalogConfig

__all__ = ["SQLContext"]


class SQLContext(Generic[FrameType]):
    @overload
    def __init__(self: SQLContext[LazyFrame], frames: Mapping[str, CompatibleFrameType | None] | None = ..., *, register_globals: bool | int = ..., eager: Literal[False] = False, **named_frames: CompatibleFrameType | None) -> None: ...

    @overload
    def __init__(self: SQLContext[DataFrame], frames: Mapping[str, CompatibleFrameType | None] | None = ..., *, register_globals: bool | int = ..., eager: Literal[True], **named_frames: CompatibleFrameType | None) -> None: ...

    @overload
    def __init__(self: SQLContext[DataFrame], frames: Mapping[str, CompatibleFrameType | None] | None = ..., *, register_globals: bool | int = ..., eager: bool, **named_frames: CompatibleFrameType | None) -> None: ...

    @overload
    @classmethod
    def execute_global(cls, query: str, *, eager: Literal[False] = False) -> LazyFrame: ...

    @overload
    @classmethod
    def execute_global(cls, query: str, *, eager: Literal[True]) -> DataFrame: ...

    @overload
    @classmethod
    def execute_global(cls, query: str, *, eager: bool) -> DataFrame | LazyFrame: ...

    def __enter__(self) -> SQLContext[FrameType]: ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

    def __repr__(self) -> str: ...

    @overload
    def execute(self: SQLContext[DataFrame], query: str, *, eager: None = ...) -> DataFrame: ...

    @overload
    def execute(self: SQLContext[DataFrame], query: str, *, eager: Literal[False]) -> LazyFrame: ...

    @overload
    def execute(self: SQLContext[DataFrame], query: str, *, eager: Literal[True]) -> DataFrame: ...

    @overload
    def execute(self: SQLContext[LazyFrame], query: str, *, eager: None = ...) -> LazyFrame: ...

    @overload
    def execute(self: SQLContext[LazyFrame], query: str, *, eager: Literal[False]) -> LazyFrame: ...

    @overload
    def execute(self: SQLContext[LazyFrame], query: str, *, eager: Literal[True]) -> DataFrame: ...

    @overload
    def execute(self, query: str, *, eager: bool | None = ...) -> LazyFrame | DataFrame: ...

    def register_catalog(self, name: str, catalog: pyiceberg.catalog.Catalog | IcebergCatalogConfig, *, default_namespace: str | Sequence[str] | None = None, default: bool = False, storage_options: StorageOptionsDict | None = None) -> Self: ...

    def unregister_catalog(self, name: str) -> Self: ...

    def register(self, name: str, frame: CompatibleFrameType | None) -> Self: ...

    def register_globals(self, n: int | None = None, *, all_compatible: bool = True) -> Self: ...

    def register_many(self, frames: Mapping[str, CompatibleFrameType | None] | None = None, **named_frames: CompatibleFrameType | None) -> Self: ...

    def unregister(self, names: str | Collection[str]) -> Self: ...

    def tables(self) -> list[str]: ...
