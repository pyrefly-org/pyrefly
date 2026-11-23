from __future__ import annotations
import importlib
import importlib.util
from typing import TYPE_CHECKING, Literal
from polars._utils.unstable import issue_unstable_warning
from polars._utils.wrap import wrap_ldf
from polars.io.cloud._utils import NoPickleOption
from polars.io.iceberg._dataset import (
    IcebergCatalogConfig,
    IcebergCatalogTableDescriptor,
    IcebergScanResolver,
    IcebergScanTableSerializer,
    IcebergTableWrap,
    _reusable_catalog,
)
import pyiceberg.catalog
import pyiceberg.table
import polars.io.iceberg
from polars._typing import StorageOptionsDict
from polars.expr.expr import Expr
from polars.lazyframe.frame import LazyFrame


def scan_iceberg(source: str | pyiceberg.table.Table, *, snapshot_id: int | None = None, from_snapshot_id_exclusive: int | None = None, to_snapshot_id_inclusive: int | None = None, storage_options: StorageOptionsDict | None = None, catalog: (pyiceberg.catalog.Catalog
    | polars.io.iceberg.IcebergCatalogConfig
    | None) = None, reader_override: Literal["native", "pyiceberg"] | None = None, use_metadata_statistics: bool = True, fast_deletion_count: bool | None = None, use_pyiceberg_filter: bool = True) -> LazyFrame: ...


def delete_iceberg(target: str | pyiceberg.table.Table, predicate: Expr) -> None: ...
