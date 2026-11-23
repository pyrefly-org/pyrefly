from __future__ import annotations
import contextlib
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Literal
import polars._reexport as pl
import polars.functions as F
from polars._utils.expired import RemovedParameter, RenamedParameter, removed_parameters
from polars._utils.unstable import issue_unstable_warning
from polars._utils.various import (
    _process_null_values,
    is_path_or_str_sequence,
    normalize_filepath,
    qualified_type_name,
)
from polars._utils.wrap import wrap_ldf
from polars.datatypes import N_INFER_DEFAULT, parse_into_dtype
from polars.io._utils import (
    parse_columns_arg,
    parse_row_index_args,
    prepare_file_arg,
)
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.csv._utils import _check_arg_is_1byte, _update_columns
from collections.abc import Callable
from polars import DataFrame, LazyFrame
from polars._typing import (
        CsvEncoding,
        PolarsDataType,
        SchemaDict,
        StorageOptionsDict,
    )
from polars.io.cloud import CredentialProviderFunction


@removed_parameters(
    RenamedParameter(
        name="dtypes",
        new_name="schema_overrides",
        deprecated_in="0.20.31",
        removed_in="2.0",
    ),
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
def read_csv(source: (str
        | Path
        | IO[str]
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[str]]
        | list[IO[bytes]]
        | list[bytes]), *, columns: Sequence[int] | Sequence[str] | None = None, has_header: bool = True, separator: str = ",", comment_prefix: str | None = None, quote_char: str | None = '"', skip_rows: int = 0, skip_lines: int = 0, schema: SchemaDict | None = None, schema_overrides: SchemaDict | Sequence[PolarsDataType] | None = None, null_values: str | Sequence[str] | dict[str, str] | None = None, empty_string_is_null: bool = True, ignore_errors: bool = False, with_column_names: Callable[[list[str]], list[str]] | None = None, infer_schema: bool = True, infer_schema_length: int | None = ..., infer_schema_files: int = ..., n_rows: int | None = None, encoding: CsvEncoding | str = "utf8", low_memory: bool = False, skip_rows_after_header: int = 0, row_index_name: str | None = None, row_index_offset: int = 0, try_parse_dates: bool = False, eol_char: str = "\n", new_columns: Sequence[str] | None = None, truncate_ragged_lines: bool | None = None, raise_if_empty: bool | None = None, decimal_comma: bool = False, glob: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None, extra_columns: Literal["ignore", "raise"] | None = None, missing_columns: Literal["insert", "raise"] | None = None, use_pyarrow: bool = False) -> DataFrame: ...


@removed_parameters(
    RenamedParameter(
        name="dtypes",
        new_name="schema_overrides",
        deprecated_in="0.20.31",
        removed_in="2.0",
    ),
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
def scan_csv(source: (str
        | Path
        | IO[str]
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[str]]
        | list[IO[bytes]]
        | list[bytes]), *, has_header: bool = True, separator: str = ",", comment_prefix: str | None = None, quote_char: str | None = '"', skip_rows: int = 0, skip_lines: int = 0, schema: SchemaDict | None = None, schema_overrides: SchemaDict | Sequence[PolarsDataType] | None = None, null_values: str | Sequence[str] | dict[str, str] | None = None, empty_string_is_null: bool = True, ignore_errors: bool = False, with_column_names: Callable[[list[str]], list[str]] | None = None, infer_schema: bool = True, infer_schema_length: int | None = ..., infer_schema_files: int = ..., n_rows: int | None = None, encoding: CsvEncoding = "utf8", low_memory: bool = False, skip_rows_after_header: int = 0, row_index_name: str | None = None, row_index_offset: int = 0, try_parse_dates: bool = False, eol_char: str = "\n", new_columns: Sequence[str] | None = None, truncate_ragged_lines: bool | None = None, raise_if_empty: bool | None = None, decimal_comma: bool = False, glob: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None, extra_columns: Literal["ignore", "raise"] | None = None, missing_columns: Literal["insert", "raise"] | None = None) -> LazyFrame: ...
