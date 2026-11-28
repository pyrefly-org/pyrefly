from __future__ import annotations
import contextlib
import io
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any
import polars.functions as F
from polars import concat as plconcat
from polars._dependencies import import_optional
from polars._utils.expired import RemovedParameter, RenamedParameter, removed_parameters
from polars._utils.unstable import issue_unstable_warning
from polars._utils.various import (
    is_int_sequence,
    normalize_filepath,
    qualified_type_name,
)
from polars._utils.wrap import wrap_ldf
from polars.convert import from_arrow
from polars.io._utils import (
    get_sources,
    parse_row_index_args,
    prepare_file_arg,
)
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.scan_options._options import ScanOptions
from collections.abc import Sequence
from typing import Literal
from polars import DataFrame, DataType, LazyFrame
from polars._typing import (
        ColumnMapping,
        DefaultFieldValues,
        DeletionFiles,
        FileSource,
        ParallelStrategy,
        SchemaDict,
        StorageOptionsDict,
    )
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.decryption import ParquetDecryptionProperties
from polars.io.scan_options import ScanCastOptions


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
    RenamedParameter(
        name="allow_missing_columns",
        new_name="missing_columns",
        deprecated_in="1.30.0",
        removed_in="2.0",
        hint="Pass one of `('insert', 'raise')`; `allow_missing_columns=True` corresponds to `missing_columns='insert'`.",
    ),
)
@removed_parameters(
    RemovedParameter(
        name="retries",
        deprecated_in="1.37.1",
        removed_in="2.0",
        hint='Pass {"max_retries": n} via `storage_options` instead.',
    ),
)
def read_parquet(source: FileSource, *, columns: list[int] | list[str] | None = None, n_rows: int | None = None, row_index_name: str | None = None, row_index_offset: int = 0, parallel: ParallelStrategy = "auto", use_statistics: bool = True, hive_partitioning: bool | None = None, glob: bool = True, schema: SchemaDict | None = None, hive_schema: SchemaDict | None = None, try_parse_hive_dates: bool = True, low_memory: bool = False, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", use_pyarrow: bool = False, pyarrow_options: dict[str, Any] | None = None, memory_map: bool = True, include_file_paths: str | None = None, missing_columns: Literal["insert", "raise"] = "raise", decryption: ParquetDecryptionProperties | None = None, _expand_paths: bool = True) -> DataFrame: ...


def read_parquet_schema(source: str | Path | IO[bytes] | bytes) -> dict[str, DataType]: ...


@removed_parameters(
    RemovedParameter(
        name="retries",
        deprecated_in="1.37.1",
        removed_in="2.0",
        hint='Pass {"max_retries": n} via `storage_options` instead.',
    ),
)
def read_parquet_metadata(source: str | Path | IO[bytes] | bytes, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto") -> dict[str, str]: ...


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
    RenamedParameter(
        name="allow_missing_columns",
        new_name="missing_columns",
        deprecated_in="1.30.0",
        removed_in="2.0",
        hint="Pass one of `('insert', 'raise')`; `allow_missing_columns=True` corresponds to `missing_columns='insert'`.",
    ),
)
@removed_parameters(
    RemovedParameter(
        name="retries",
        deprecated_in="1.37.1",
        removed_in="2.0",
        hint='Pass {"max_retries": n} via `storage_options` instead.',
    ),
)
def scan_parquet(source: FileSource, *, n_rows: int | None = None, row_index_name: str | None = None, row_index_offset: int = 0, parallel: ParallelStrategy = "auto", use_statistics: bool = True, hive_partitioning: bool | None = None, glob: bool = True, hidden_file_prefix: str | Sequence[str] | None = None, schema: SchemaDict | None = None, hive_schema: SchemaDict | None = None, try_parse_hive_dates: bool = True, low_memory: bool = False, cache: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None, missing_columns: Literal["insert", "raise"] = "raise", extra_columns: Literal["ignore", "raise"] = "raise", cast_options: ScanCastOptions | None = None, decryption: ParquetDecryptionProperties | None = None, _expand_paths: bool = True, _column_mapping: ColumnMapping | None = None, _default_values: DefaultFieldValues | None = None, _deletion_files: DeletionFiles | None = None, _table_statistics: DataFrame | None = None, _row_count: tuple[int, int] | None = None, _source_sizes: Sequence[int] | None = None, _resolve_heavy_sources: int | None = None) -> LazyFrame: ...
