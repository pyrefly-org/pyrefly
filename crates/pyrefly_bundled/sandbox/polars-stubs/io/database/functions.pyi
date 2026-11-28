from __future__ import annotations
import re
from typing import TYPE_CHECKING, Any, Literal, overload
from polars._dependencies import _PYARROW_AVAILABLE, import_optional
from polars._utils.unstable import issue_unstable_warning
from polars._utils.various import parse_version, qualified_type_name
from polars.datatypes import N_INFER_DEFAULT
from polars.exceptions import ModuleUpgradeRequiredError
from polars.io.database._cursor_proxies import ODBCCursorProxy
from polars.io.database._executor import ConnectionExecutor
from collections.abc import Iterator
from sqlalchemy.sql.elements import TextClause
from sqlalchemy.sql.expression import Selectable
from polars import DataFrame
from polars._typing import ConnectionOrCursor, DbReadEngine, SchemaDict


@overload
def read_database(query: str | TextClause | Selectable, connection: ConnectionOrCursor | str, *, iter_batches: Literal[False] = ..., batch_size: int | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., execute_options: dict[str, Any] | None = ...) -> DataFrame: ...


@overload
def read_database(query: str | TextClause | Selectable, connection: ConnectionOrCursor | str, *, iter_batches: Literal[True], batch_size: int | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., execute_options: dict[str, Any] | None = ...) -> Iterator[DataFrame]: ...


@overload
def read_database(query: str | TextClause | Selectable, connection: ConnectionOrCursor | str, *, iter_batches: bool, batch_size: int | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., execute_options: dict[str, Any] | None = ...) -> DataFrame | Iterator[DataFrame]: ...


@overload
def read_database_uri(query: str, uri: str, *, partition_on: str | None = None, partition_range: tuple[int, int] | None = None, partition_num: int | None = None, protocol: str | None = None, engine: Literal["adbc"], schema_overrides: SchemaDict | None = None, execute_options: dict[str, Any] | None = None, pre_execution_query: str | list[str] | None = None) -> DataFrame: ...


@overload
def read_database_uri(query: list[str] | str, uri: str, *, partition_on: str | None = None, partition_range: tuple[int, int] | None = None, partition_num: int | None = None, protocol: str | None = None, engine: Literal["connectorx"] | None = None, schema_overrides: SchemaDict | None = None, execute_options: None = None, pre_execution_query: str | list[str] | None = None) -> DataFrame: ...


@overload
def read_database_uri(query: str, uri: str, *, partition_on: str | None = None, partition_range: tuple[int, int] | None = None, partition_num: int | None = None, protocol: str | None = None, engine: DbReadEngine | None = None, schema_overrides: None = None, execute_options: dict[str, Any] | None = None, pre_execution_query: str | list[str] | None = None) -> DataFrame: ...
