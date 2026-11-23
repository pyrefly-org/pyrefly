from __future__ import annotations
import contextlib
from pathlib import Path
from typing import IO, TYPE_CHECKING, Literal
from polars._utils.expired import RemovedParameter, RenamedParameter, removed_parameters
from polars._utils.various import is_path_or_str_sequence, normalize_filepath
from polars._utils.wrap import wrap_ldf
from polars.datatypes import N_INFER_DEFAULT
from polars.io._utils import parse_row_index_args
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars import DataFrame, LazyFrame
from polars._typing import SchemaDefinition, StorageOptionsDict
from polars.io.cloud import CredentialProviderFunction


@removed_parameters(
    RemovedParameter(
        name="retries",
        deprecated_in="1.37.1",
        removed_in="2.0",
        hint='Pass {"max_retries": n} via `storage_options` instead.',
    ),
    RemovedParameter(
        name="file_cache_ttl",
        deprecated_in="1.39.0",
        removed_in="2.0",
        hint="The file cache is no longer supported.",
    ),
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
def read_ndjson(source: (str
    | Path
    | IO[str]
    | IO[bytes]
    | bytes
    | list[str]
    | list[Path]
    | list[IO[str]]
    | list[IO[bytes]]), *, schema: SchemaDefinition | None = None, schema_overrides: SchemaDefinition | None = None, infer_schema_length: int | None = ..., batch_size: int | None = 1024, n_rows: int | None = None, low_memory: bool = False, row_index_name: str | None = None, row_index_offset: int = 0, ignore_errors: bool = False, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None) -> DataFrame: ...


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
        deprecated_in="1.39.0",
        removed_in="2.0",
        hint="The file cache is no longer supported.",
    ),
)
def scan_ndjson(source: (str
        | Path
        | IO[str]
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[str]]
        | list[IO[bytes]]), *, schema: SchemaDefinition | None = None, schema_overrides: SchemaDefinition | None = None, infer_schema_length: int | None = ..., batch_size: int | None = 1024, n_rows: int | None = None, low_memory: bool = False, row_index_name: str | None = None, row_index_offset: int = 0, ignore_errors: bool = False, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None) -> LazyFrame: ...
