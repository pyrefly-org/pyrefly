from typing import Callable, ClassVar
from _typeshed import Incomplete

from __future__ import annotations
from inspect import iscoroutinefunction
from typing import TYPE_CHECKING, Any, ClassVar
from polars._dependencies import import_optional
from polars._utils.various import parse_version
from polars.io.database._utils import _run_async
from collections.abc import Coroutine, Iterable, Iterator
from typing import Self
import pyarrow as pa


class ODBCCursorProxy:
    connection_string: str
    execute_options: dict[str, Any]
    query: str | None

    def __init__(self, connection_string: str) -> None: ...

    def close(self) -> None: ...

    def execute(self, query: str, **execute_options: Any) -> None: ...

    def fetch_arrow_table(self, batch_size: int = 10_000, *, fetch_all: bool = False) -> pa.Table: ...

    def fetch_record_batches(self, batch_size: int = 10_000, *, fetch_all: bool = False) -> Iterable[pa.RecordBatch]: ...

    fetchall: ClassVar[Callable[..., Incomplete]]
    fetchmany: ClassVar[Callable[..., Incomplete]]


class SurrealDBCursorProxy:
    client: Incomplete
    execute_options: dict[str, Any]
    is_async: bool
    query: str

    def __init__(self, client: Any) -> None: ...

    def close(self) -> None: ...

    def execute(self, query: str, **execute_options: Any) -> Self: ...

    def fetchall(self) -> list[dict[str, Any]]: ...

    def fetchmany(self, size: int) -> list[dict[str, Any]]: ...


class OracleCursorProxy:
    minimum_version: ClassVar[str] = "3.4.0"
    connection: Incomplete
    execute_options: dict[str, Any]
    query: str | None

    def __init__(self, connection: Any) -> None: ...

    @classmethod
    def supports_arrow(cls, connection: Any) -> bool: ...

    def close(self) -> None: ...

    def execute(self, query: str, **execute_options: Any) -> Self: ...

    def fetch_df_all(self) -> Any: ...

    def fetch_df_batches(self, size: int) -> Iterator[Any]: ...
