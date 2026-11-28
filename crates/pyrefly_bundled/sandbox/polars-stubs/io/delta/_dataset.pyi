from _typeshed import Incomplete

from __future__ import annotations
import sys
from dataclasses import dataclass
from functools import partial
from time import perf_counter
from typing import TYPE_CHECKING, Any
import polars as pl
from polars._utils.logging import eprint
from polars._utils.various import parse_version
from polars.io.cloud.credential_provider._providers import (
    _get_credentials_from_provider_expiry_aware,
)
from polars.io.delta._utils import _extract_table_statistics_from_delta_add_actions
from polars.io.parquet.functions import scan_parquet
from polars.io.scan_options.cast_options import ScanCastOptions
from polars.schema import Schema
from datetime import datetime
from deltalake import DeltaTable
from polars._typing import DeletionFiles, StorageOptionsDict
from polars.io.cloud._utils import NoPickleOption
from polars.io.cloud.credential_provider._builder import CredentialProviderBuilder
from polars.lazyframe.frame import LazyFrame


@dataclass(kw_only=True)
class DeltaDataset:
    table_: NoPickleOption[DeltaTable]
    table_uri_: str | None
    version: int | str | datetime | None
    storage_options: StorageOptionsDict | None
    credential_provider_builder: CredentialProviderBuilder | None
    delta_table_options: dict[str, Any] | None
    use_pyarrow: bool
    pyarrow_options: dict[str, Any] | None

    def schema(self) -> Schema: ...

    def to_dataset_scan(self, *, existing_resolved_version_key: str | None = None, limit: int | None = None, projection: list[str] | None = None, filter_columns: list[str] | None = None, statistics_columns: list[str] | None = None, pyarrow_predicate: str | None = None) -> tuple[LazyFrame, str] | None: ...

    def table_uri(self) -> str: ...

    def table(self) -> DeltaTable: ...

    def __getstate__(self) -> dict[str, Any]: ...

    def __setstate__(self, state: dict[str, Any]) -> None: ...

    __dict__: dict[str, Any]

    def __init__(self, *, table_: Incomplete, table_uri_: str | None, version: datetime | int | str | None, storage_options: dict[str, Any] | None, credential_provider_builder: CredentialProviderBuilder | None, delta_table_options: dict[str, Any] | None, use_pyarrow: bool, pyarrow_options: dict[str, Any] | None) -> None: ...
