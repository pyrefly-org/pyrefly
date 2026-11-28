from _typeshed import Incomplete

from __future__ import annotations
import re
from collections.abc import Coroutine, Iterable, Sequence
from contextlib import suppress
from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any, Final, cast
from polars import functions as F
from polars._utils.various import parse_version, qualified_type_name
from polars.datatypes import N_INFER_DEFAULT
from polars.exceptions import (
    DuplicateError,
    ModuleUpgradeRequiredError,
    UnsuitableSQLError,
)
from polars.io.database._arrow_registry import ARROW_DRIVER_REGISTRY
from polars.io.database._cursor_proxies import (
    ODBCCursorProxy,
    OracleCursorProxy,
    SurrealDBCursorProxy,
)
from polars.io.database._inference import dtype_from_cursor_description
from polars.io.database._utils import _run_async
from collections.abc import Iterator
from types import TracebackType
from typing import Self
import pyarrow as pa
from sqlalchemy.sql.elements import TextClause
from sqlalchemy.sql.expression import Selectable
from polars import DataFrame
from polars._typing import ConnectionOrCursor, Cursor, SchemaDict
from polars.io.database._arrow_registry import ArrowDriverProperties


class CloseAfterFrameIter:
    def __init__(self, frames: Any, *, cursor: Cursor) -> None: ...

    def __iter__(self) -> Iterator[DataFrame]: ...


class ConnectionExecutor:
    can_close_cursor: bool = False
    cursor: Cursor
    driver_name: str
    result: Incomplete

    def __init__(self, connection: ConnectionOrCursor) -> None: ...

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

    def __repr__(self) -> str: ...

    def execute(self, query: str | TextClause | Selectable, *, options: dict[str, Any] | None = None, select_queries_only: bool = True) -> Self: ...

    def to_polars(self, *, iter_batches: bool = False, batch_size: int | None = None, schema_overrides: SchemaDict | None = None, infer_schema_length: int | None = ...) -> DataFrame | Iterator[DataFrame]: ...
