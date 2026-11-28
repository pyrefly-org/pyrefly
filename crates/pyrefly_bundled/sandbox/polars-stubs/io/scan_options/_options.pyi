from typing import Literal
from _typeshed import Incomplete

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
from collections.abc import Sequence
from polars._typing import (
        ColumnMapping,
        DefaultFieldValues,
        DeletionFiles,
        SchemaDict,
        StorageOptionsDict,
    )
from polars.dataframe.frame import DataFrame
from polars.io.cloud.credential_provider._builder import CredentialProviderBuilder
from polars.io.scan_options.cast_options import ScanCastOptions
from dataclasses import dataclass


@dataclass(kw_only=True)
class ScanOptions:
    row_index: tuple[str, int] | None = None
    pre_slice: tuple[int, int] | None = None
    cast_options: ScanCastOptions | None = None
    extra_columns: Literal["ignore", "raise"] = "raise"
    missing_columns: Literal["insert", "raise"] = "raise"
    include_file_paths: str | None = None
    glob: bool = True
    expand_paths: bool = True
    hidden_file_prefix: Sequence[str] | None = None
    hive_partitioning: bool | None = None
    hive_schema: SchemaDict | None = None
    try_parse_hive_dates: bool = True
    rechunk: bool = False
    cache: bool = True
    storage_options: StorageOptionsDict | None = None
    credential_provider: CredentialProviderBuilder | None = None
    column_mapping: ColumnMapping | None = None
    default_values: DefaultFieldValues | None = None
    deletion_files: DeletionFiles | None = None
    table_statistics: DataFrame | None = None
    row_count: tuple[int, int] | None = None
    source_sizes: Sequence[int] | None = None
    resolve_heavy_sources: int | None = None

    def __init__(self, *, row_index: tuple[str, int] | None = ..., pre_slice: tuple[int, int] | None = ..., cast_options: ScanCastOptions | None = ..., extra_columns: Literal['ignore', 'raise'] = ..., missing_columns: Literal['insert', 'raise'] = ..., include_file_paths: str | None = ..., glob: bool = ..., expand_paths: bool = ..., hidden_file_prefix: Sequence[str] | None = ..., hive_partitioning: bool | None = ..., hive_schema: Mapping[str, DataType | DataTypeClass] | None = ..., try_parse_hive_dates: bool = ..., rechunk: bool = ..., cache: bool = ..., storage_options: dict[str, Any] | None = ..., credential_provider: CredentialProviderBuilder | None = ..., column_mapping: tuple[Literal['iceberg-column-mapping'], Any] | tuple[Literal['iceberg-column-mapping'], Any, dict[int, list[str]] | None] | None = ..., default_values: tuple[Literal['iceberg'], tuple[dict[int, Series | str], dict[int, Series]] | tuple[dict[int, Series | str], dict[int, Series], dict[int, Series]]] | None = ..., deletion_files: Incomplete = ..., table_statistics: DataFrame | None = ..., row_count: tuple[int, int] | None = ..., source_sizes: Sequence[int] | None = ..., resolve_heavy_sources: int | None = ...) -> None: ...
