from typing import Literal
from _typeshed import Incomplete

from __future__ import annotations
import contextlib
import importlib
import importlib.util
import sys
from dataclasses import dataclass
from time import perf_counter
from typing import TYPE_CHECKING, Any, ClassVar, Literal
from polars._utils.logging import eprint
from polars._utils.wrap import wrap_ldf
from polars.exceptions import ComputeError
from polars.io.cloud._utils import NoPickleOption
from polars.io.iceberg._dataset import (
    IcebergCatalogConfig,
    _convert_iceberg_to_object_store_storage_options,
)
from polars.io.iceberg._utils import (
    _is_null_pushdown_safe,
    _normalize_windows_iceberg_file_uri,
    predicate_to_pyiceberg_delete_filter,
)
from polars.io.partition import _InternalPlPathProviderConfig
from collections.abc import Collection, Iterable
import pyarrow as pa
import pyiceberg.catalog
import pyiceberg.table
from pyiceberg.expressions import BooleanExpression
from pyiceberg.io.pyarrow import StatisticsCollector
from pyiceberg.manifest import DataFile
from pyiceberg.partitioning import PartitionSpec
from pyiceberg.schema import Schema
from pyiceberg.table import CommitTableResponse, Transaction
from pyiceberg.table.metadata import TableMetadata
from pyiceberg.table.sorting import SortOrder
from pyiceberg.table.update import TableRequirement, TableUpdate
from pyiceberg.transforms import Transform
from pyiceberg.typedef import Record
from pyiceberg.types import IcebergType
import polars as pl
from polars._plr import PyLazyFrame
from polars._typing import (
        ParquetCompression,
        PolarsDataType,
        StorageOptionsDict,
    )


@dataclass(kw_only=True)
class IcebergSinkState:
    py_catalog_class_module: str
    py_catalog_class_qualname: str
    catalog_name: str
    catalog_properties: dict[str, str]
    table_name: str
    mode: Literal["append", "overwrite"]
    schema_mode: Literal["merge", "overwrite"] | None
    overwrite_filter: BooleanExpression | pl.Expr | None
    dynamic_partition_overwrite: bool
    create_if_not_exists: bool
    create_namespace_if_not_exists: bool
    snapshot_properties: dict[str, str]
    iceberg_storage_properties: StorageOptionsDict
    compression: ParquetCompression
    compression_level: int | None
    row_group_size: int | None
    maintain_order: bool
    sink_uuid_str: str
    table_: NoPickleOption[pyiceberg.table.Table]
    source_schema: pa.Schema | None
    sort_order_id: int | None
    partition_spec_id: int | None
    commit_result_df: NoPickleOption[pl.DataFrame]

    @staticmethod
    def new(target: str | pyiceberg.table.Table, *, mode: Literal["append", "overwrite"] = "append", schema_mode: Literal["merge", "overwrite"] | None = None, overwrite_filter: pl.Expr | BooleanExpression | str | None = None, partition_overwrite: Literal["dynamic"] | None = None, create_if_not_exists: bool = False, create_namespace_if_not_exists: bool = False, snapshot_properties: dict[str, str] | None = None, catalog: pyiceberg.catalog.Catalog | IcebergCatalogConfig | None = None, storage_options: StorageOptionsDict | None = None, compression: ParquetCompression = "zstd", compression_level: int | None = None, row_group_size: int | None = None, maintain_order: bool = True) -> IcebergSinkState: ...

    def table(self) -> pyiceberg.table.Table: ...

    def attach_sink(self, lf: pl.LazyFrame) -> pl.LazyFrame: ...

    def commit(self, sinked_files: list[_IcebergSinkedFile]) -> pl.DataFrame: ...

    def sink_base_path(self, *, object_storage_enabled: bool) -> str: ...

    def __init__(self, *, py_catalog_class_module: str, py_catalog_class_qualname: str, catalog_name: str, catalog_properties: dict[str, str], table_name: str, mode: Literal['append', 'overwrite'], schema_mode: Literal['merge', 'overwrite'] | None, overwrite_filter: Incomplete, dynamic_partition_overwrite: bool, create_if_not_exists: bool, create_namespace_if_not_exists: bool, snapshot_properties: dict[str, str], iceberg_storage_properties: dict[str, Any], compression: Literal['brotli', 'gzip', 'lz4', 'snappy', 'uncompressed', 'zstd'], compression_level: int | None, row_group_size: int | None, maintain_order: bool, sink_uuid_str: str, table_: Incomplete, source_schema: Incomplete, sort_order_id: int | None, partition_spec_id: int | None, commit_result_df: NoPickleOption[DataFrame]) -> None: ...


@dataclass(frozen=True, kw_only=True)
class PlIcebergPathProviderConfig(_InternalPlPathProviderConfig):
    pl_path_provider_id: ClassVar[str] = "iceberg"
    extension: ClassVar[Literal["parquet"]] = "parquet"
    object_storage_partitioned_paths: bool | None = None

    def __init__(self, *, object_storage_partitioned_paths: bool | None = ...) -> None: ...
