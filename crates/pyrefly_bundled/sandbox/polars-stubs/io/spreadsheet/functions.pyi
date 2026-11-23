from __future__ import annotations
import os
import re
import warnings
from collections import defaultdict
from collections.abc import Sequence
from datetime import time
from glob import glob
from io import BufferedReader, BytesIO, StringIO, TextIOWrapper
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, NoReturn, cast, overload
import polars._reexport as pl
from polars import functions as F
from polars._dependencies import _PYARROW_AVAILABLE, import_optional
from polars._utils.expired import RenamedParameter, removed_parameters
from polars._utils.various import (
    deduplicate_names,
    is_non_empty_sequence_of,
    normalize_filepath,
    parse_version,
)
from polars.datatypes import (
    N_INFER_DEFAULT,
    Boolean,
    Date,
    Datetime,
    Duration,
    Int64,
    Null,
    String,
    Time,
    UInt8,
)
from polars.datatypes.group import FLOAT_DTYPES, INTEGER_DTYPES, NUMERIC_DTYPES
from polars.exceptions import (
    ModuleUpgradeRequiredError,
    NoDataError,
    ParameterCollisionError,
)
from polars.functions import concat
from polars.io._utils import looks_like_url, process_file_url
from polars.io.csv.functions import read_csv
from collections.abc import Callable
from typing import Literal
from polars._typing import ExcelSpreadsheetEngine, FileSource, SchemaDict


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: None = ..., sheet_name: str, table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., read_options: dict[str, Any] | None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: None = ..., sheet_name: None = ..., table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., has_header: bool = ..., read_options: dict[str, Any] | None = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: int, sheet_name: str, table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., read_options: dict[str, Any] | None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> NoReturn: ...


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: Literal[0] | Sequence[int], sheet_name: None = ..., table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., read_options: dict[str, Any] | None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> dict[str, pl.DataFrame]: ...


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: int, sheet_name: None = ..., table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., read_options: dict[str, Any] | None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_excel(source: FileSource | memoryview[int], *, sheet_id: None = ..., sheet_name: list[str] | tuple[str, ...], table_name: str | None = ..., engine: ExcelSpreadsheetEngine = ..., engine_options: dict[str, Any] | None = ..., read_options: dict[str, Any] | None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | str | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> dict[str, pl.DataFrame]: ...


@overload
def read_ods(source: FileSource, *, sheet_id: None = ..., sheet_name: str, has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_ods(source: FileSource, *, sheet_id: None = ..., sheet_name: None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_ods(source: FileSource, *, sheet_id: int, sheet_name: str, has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> NoReturn: ...


@overload
def read_ods(source: FileSource, *, sheet_id: Literal[0] | Sequence[int], sheet_name: None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> dict[str, pl.DataFrame]: ...


@overload
def read_ods(source: FileSource, *, sheet_id: int, sheet_name: None = ..., has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> pl.DataFrame: ...


@overload
def read_ods(source: FileSource, *, sheet_id: None = ..., sheet_name: list[str] | tuple[str, ...], has_header: bool = ..., columns: Sequence[int] | Sequence[str] | None = ..., schema_overrides: SchemaDict | None = ..., infer_schema_length: int | None = ..., include_file_paths: str | None = ..., drop_empty_rows: bool = ..., drop_empty_cols: bool = ..., raise_if_empty: bool = ...) -> dict[str, pl.DataFrame]: ...
