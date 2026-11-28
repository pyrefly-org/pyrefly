from __future__ import annotations
import contextlib
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Literal
import polars._reexport as pl
import polars.functions as F
from polars._dependencies import import_optional
from polars._utils.expired import RemovedParameter, RenamedParameter, removed_parameters
from polars._utils.various import (
    normalize_filepath,
)
from polars._utils.wrap import wrap_df, wrap_ldf
from polars.io._utils import (
    get_sources,
    parse_columns_arg,
    parse_row_index_args,
    prepare_file_arg,
)
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.scan_options._options import ScanOptions
from collections.abc import Sequence
from polars import DataFrame, DataType, LazyFrame
from polars._typing import SchemaDict, StorageOptionsDict
from polars.io.cloud import CredentialProviderFunction


@removed_parameters(
    RenamedParameter(
        name="row_count_name",
        new_name="row_index_name",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RenamedParameter(
        name="row_count_offset",
        new_name="row_index_offset",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
def read_ipc(source: str | Path | IO[bytes] | bytes, *, columns: list[int] | list[str] | None = None, n_rows: int | None = None, use_pyarrow: bool = False, storage_options: StorageOptionsDict | None = None, row_index_name: str | None = None, row_index_offset: int = 0) -> DataFrame: ...


@removed_parameters(
    RenamedParameter(
        name="row_count_name",
        new_name="row_index_name",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RenamedParameter(
        name="row_count_offset",
        new_name="row_index_offset",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
def read_ipc_stream(source: str | Path | IO[bytes] | bytes, *, columns: list[int] | list[str] | None = None, n_rows: int | None = None, use_pyarrow: bool = False, storage_options: StorageOptionsDict | None = None, row_index_name: str | None = None, row_index_offset: int = 0) -> DataFrame: ...


def read_ipc_schema(source: str | Path | IO[bytes] | bytes) -> dict[str, DataType]: ...


@removed_parameters(
    RenamedParameter(
        name="row_count_name",
        new_name="row_index_name",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RenamedParameter(
        name="row_count_offset",
        new_name="row_index_offset",
        deprecated_in="0.20.4",
        removed_in="2.0",
    ),
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
@removed_parameters(
    RemovedParameter(
        name="retries",
        deprecated_in="1.37.1",
        removed_in="2.0",
        hint='Pass {"max_retries": n} via `storage_options` instead.',
    ),
    RemovedParameter(
        name="file_cache_ttl",
        deprecated_in="1.40.0",
        removed_in="2.0",
        hint="The file cache is no longer supported.",
    ),
    RemovedParameter(
        name="cache",
        deprecated_in="1.40.0",
        removed_in="2.0",
        hint="The file cache is no longer supported.",
    ),
)
def scan_ipc(source: (str
        | Path
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[bytes]]
        | list[bytes]), *, n_rows: int | None = None, row_index_name: str | None = None, row_index_offset: int = 0, glob: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", hive_partitioning: bool | None = None, hive_schema: SchemaDict | None = None, try_parse_hive_dates: bool = True, include_file_paths: str | None = None, _record_batch_statistics: bool = False) -> LazyFrame: ...
