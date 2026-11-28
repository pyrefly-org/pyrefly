from __future__ import annotations
import glob
import re
from collections.abc import Sequence
from contextlib import contextmanager
from io import BytesIO, StringIO
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, cast, overload
from polars._dependencies import _FSSPEC_AVAILABLE, fsspec
from polars._utils.various import (
    is_int_sequence,
    is_path_or_str_sequence,
    is_str_sequence,
    normalize_filepath,
)
from polars.exceptions import NoDataError
from collections.abc import Iterator
from contextlib import AbstractContextManager as ContextManager
from polars._typing import PolarsDataType, StorageOptionsDict


def null_count_dtype(dtype: PolarsDataType) -> PolarsDataType: ...


def parse_columns_arg(columns: Sequence[str] | Sequence[int] | str | int | None) -> tuple[Sequence[int] | None, Sequence[str] | None]: ...


def parse_row_index_args(row_index_name: str | None = None, row_index_offset: int = 0) -> tuple[str, int] | None: ...


@overload
def prepare_file_arg(file: str | Path | list[str] | IO[bytes] | bytes, encoding: str | None = ..., *, use_pyarrow: bool = ..., raise_if_empty: bool = ..., storage_options: StorageOptionsDict | None = ...) -> ContextManager[str | BytesIO]: ...


@overload
def prepare_file_arg(file: str | Path | IO[str] | IO[bytes] | bytes, encoding: str | None = ..., *, use_pyarrow: bool = ..., raise_if_empty: bool = ..., storage_options: StorageOptionsDict | None = ...) -> ContextManager[str | BytesIO]: ...


@overload
def prepare_file_arg(file: str | Path | list[str] | IO[str] | IO[bytes] | bytes, encoding: str | None = ..., *, use_pyarrow: bool = ..., raise_if_empty: bool = ..., storage_options: StorageOptionsDict | None = ...) -> ContextManager[str | list[str] | BytesIO | list[BytesIO]]: ...


def looks_like_url(path: str) -> bool: ...


def process_file_url(path: str, encoding: str | None = None) -> BytesIO: ...


def is_glob_pattern(file: str) -> bool: ...


def is_local_file(file: str) -> bool: ...


def get_sources(source: (str
    | Path
    | IO[bytes]
    | IO[str]
    | bytes
    | list[str]
    | list[Path]
    | list[IO[bytes]]
    | list[IO[str]]
    | list[bytes])) -> list[str] | list[Path] | list[IO[str]] | list[IO[bytes]] | list[bytes]: ...
