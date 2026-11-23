from typing import Literal
from _typeshed import Incomplete

from __future__ import annotations
import copy
import hashlib
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING, Any, Final, Literal, TypeAlias
import polars._reexport as pl
from polars._utils.logging import eprint, verbose, verbose_print_sensitive
from polars._utils.various import qualified_type_name
from polars.exceptions import ComputeError
from polars.io.iceberg._cache import (
    describe_metadata_file_cache,
    get_metadata_file_cache,
    load_static_table,
)
from polars.io.iceberg._plugin import (
    plugin_planner_required,
    plugin_scan,
    use_plugin_planner,
)
from polars.io.iceberg._utils import (
    IcebergStatisticsLoader,
    IdentityTransformedPartitionValuesBuilder,
    _new_pyiceberg_scan,
    _normalize_windows_iceberg_file_uri,
    extract_field_initial_default,
    filter_for_pyiceberg_reader,
    filter_for_required_is_null,
    filter_for_scan_schema,
    filter_for_truncate_overflow,
    filter_with_nan_ordering,
    name_mapping_by_field_id,
    try_convert_pyarrow_predicate,
)
from polars.io.scan_options.cast_options import ScanCastOptions
import pyarrow as pa
import pyiceberg.catalog
import pyiceberg.schema
import pyiceberg.table
import pyiceberg.typedef
from polars._typing import StorageOptionsDict
from polars.io.cloud._utils import NoPickleOption
from polars.lazyframe.frame import LazyFrame


class IcebergTableSerializer(ABC):
    @staticmethod
    @abstractmethod
    def serialize_table(table: pyiceberg.table.Table) -> SerializedTableState: ...


class IcebergScanTableSerializer(IcebergTableSerializer):
    @staticmethod
    def serialize_table(table: pyiceberg.table.Table) -> SerializedTableState: ...


@dataclass(kw_only=True)
class IcebergCatalogTableDescriptor:
    table_identifier: str | pyiceberg.typedef.Identifier
    catalog_config: IcebergCatalogConfig
    catalog_: NoPickleOption[pyiceberg.catalog.Catalog] | None = None
    display_name: str | None = None

    def __init__(self, *, table_identifier: Incomplete, catalog_config: IcebergCatalogConfig, catalog_: Incomplete = ..., display_name: str | None = ...) -> None: ...


SerializedTableState: TypeAlias = str | IcebergCatalogTableDescriptor


@dataclass(kw_only=True)
class IcebergTableWrap:
    table_: NoPickleOption[pyiceberg.table.Table]
    table_descriptor_: SerializedTableState | None
    serializer: IcebergTableSerializer
    iceberg_storage_properties: StorageOptionsDict | None

    def get(self) -> pyiceberg.table.Table: ...

    def arrow_schema(self) -> pa.schema: ...

    def __getstate__(self) -> dict[str, Any]: ...

    def __setstate__(self, state: dict[str, Any]) -> None: ...

    __dict__: dict[str, Any]

    def __init__(self, *, table_: Incomplete, table_descriptor_: IcebergCatalogTableDescriptor | str | None, serializer: IcebergTableSerializer, iceberg_storage_properties: dict[str, Any] | None) -> None: ...


@dataclass(kw_only=True)
class IcebergCatalogConfig:
    class_: type[pyiceberg.catalog.Catalog]
    name: str
    properties: dict[str, str]

    @staticmethod
    def from_catalog(catalog: pyiceberg.catalog.Catalog) -> IcebergCatalogConfig: ...

    def __init__(self, *, class_: type[Any], name: str, properties: dict[str, str]) -> None: ...


@dataclass(kw_only=True)
class IcebergScanResolver:
    table: IcebergTableWrap
    snapshot_id: int | None
    from_snapshot_id_exclusive: int | None
    to_snapshot_id_inclusive: int | None
    reader_override: Literal["native", "pyiceberg"] | None
    use_metadata_statistics: bool
    fast_deletion_count: bool
    use_pyiceberg_filter: bool
    schema_at_creation: pyiceberg.schema.Schema | None

    def schema(self) -> pa.schema: ...

    def to_dataset_scan(self, *, existing_resolved_version_key: str | None = None, limit: int | None = None, projection: list[str] | None = None, filter_columns: list[str] | None = None, statistics_columns: list[str] | None = None, pyarrow_predicate: str | None = None) -> tuple[LazyFrame, str] | None: ...

    def __init__(self, *, table: IcebergTableWrap, snapshot_id: int | None, from_snapshot_id_exclusive: int | None, to_snapshot_id_inclusive: int | None, reader_override: Literal['native', 'pyiceberg'] | None, use_metadata_statistics: bool, fast_deletion_count: bool, use_pyiceberg_filter: bool) -> None: ...


ICEBERG_TO_OBJECT_STORE_CONFIG_KEY_MAP: Final[dict[str, str]]
