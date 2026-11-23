from __future__ import annotations
import os
import sys
from collections.abc import Callable, Iterator
from typing import TYPE_CHECKING, Protocol, cast, runtime_checkable
import polars._reexport as pl
from polars._utils.unstable import unstable
from collections.abc import Callable, Iterator
from polars import DataFrame, Expr, LazyFrame
from polars._typing import SchemaDict


@runtime_checkable
class IOSourceScanFunction(Protocol):
    io_source: (Callable[
        [list[str] | None, Expr | None, int | None, int | None], Iterator[DataFrame]
    ])

    def __call__(self, with_columns: list[str] | None, predicate: bytes | None, n_rows: int | None, batch_size: int | None) -> tuple[Iterator[DataFrame], bool]: ...


@unstable()
def register_io_source(io_source: (Callable[
        [list[str] | None, Expr | None, int | None, int | None], Iterator[DataFrame]
    ]), *, schema: Callable[[], SchemaDict] | SchemaDict, validate_schema: bool = False, is_pure: bool = False, explain_name: str | None = None, explain_detail: str | None = None) -> LazyFrame: ...
