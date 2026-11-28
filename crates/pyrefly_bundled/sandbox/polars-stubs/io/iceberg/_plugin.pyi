from typing import Literal

from __future__ import annotations
import importlib.metadata
import os
from typing import TYPE_CHECKING, Any
from polars._utils.logging import verbose
from polars._utils.wrap import wrap_ldf
from polars._warnings import issue_warning
from polars.exceptions import ComputeError, PerformanceWarning
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.iceberg._cache import (
    _BUILTIN_FILE_IO_CLASSES,
    get_metadata_file_cache,
    plugin_storage_scope,
)
from polars.io.scan_options.cast_options import ScanCastOptions
from collections.abc import Mapping
import pyiceberg.expressions
import pyiceberg.table
from polars import LazyFrame
from polars._typing import StorageOptionsDict

PLUGIN_PACKAGE_NAME: Literal['polars_iceberg'] = "polars_iceberg"
PLANNER_ENV_VAR: Literal['POLARS_ICEBERG_PLANNER'] = "POLARS_ICEBERG_PLANNER"


def use_plugin_planner() -> bool: ...


def plugin_planner_required() -> bool: ...


def plugin_scan(tbl: pyiceberg.table.Table, *, snapshot_id: int | None, from_snapshot_id_exclusive: int | None, to_snapshot_id_inclusive: int | None, projection: list[str] | None, filter_columns: list[str] | None, statistics_columns: list[str] | None, iceberg_table_filter: pyiceberg.expressions.BooleanExpression | None, limit: int | None, use_metadata_statistics: bool, fast_deletion_count: bool, user_storage_options: StorageOptionsDict | None) -> LazyFrame: ...
