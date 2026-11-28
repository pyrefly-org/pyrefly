from __future__ import annotations
import contextlib
import importlib
import importlib.util
import os
import sys
from typing import TYPE_CHECKING, Any, Literal
from polars._utils.expired import RemovedParameter, removed_parameters
from polars._utils.unstable import issue_unstable_warning
from polars._utils.wrap import wrap_ldf
from polars.catalog.unity.models import (
    CatalogInfo,
    ColumnInfo,
    NamespaceInfo,
    TableInfo,
)
from collections.abc import Generator
from datetime import datetime
import deltalake
from polars._typing import SchemaDict, StorageOptionsDict
from polars.catalog.unity.models import DataSourceFormat, TableType
from polars.dataframe.frame import DataFrame
from polars.io.cloud import (
        CredentialProviderFunction,
        CredentialProviderFunctionReturn,
    )
from polars.io.cloud.credential_provider._builder import CredentialProviderBuilder
from polars.lazyframe import LazyFrame


class Catalog:
    def __init__(self, workspace_url: str, *, bearer_token: str | None = "auto", require_https: bool = True) -> None: ...

    def list_catalogs(self) -> list[CatalogInfo]: ...

    def list_namespaces(self, catalog_name: str) -> list[NamespaceInfo]: ...

    def list_tables(self, catalog_name: str, namespace: str) -> list[TableInfo]: ...

    def get_table_info(self, catalog_name: str, namespace: str, table_name: str) -> TableInfo: ...

    @removed_parameters(
        RemovedParameter(
            name="retries",
            deprecated_in="1.37.1",
            removed_in="2.0",
            hint='Pass {"max_retries": n} via `storage_options` instead.',
        ),
    )
    def scan_table(self, catalog_name: str, namespace: str, table_name: str, *, delta_table_version: int | str | datetime | None = None, delta_table_options: dict[str, Any] | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto") -> LazyFrame: ...

    def write_table(self, df: DataFrame, catalog_name: str, namespace: str, table_name: str, *, delta_mode: (Literal[
            "error", "append", "overwrite", "ignore", "merge"
        ]) = "error", delta_write_options: dict[str, Any] | None = None, delta_merge_options: dict[str, Any] | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto") -> None | deltalake.table.TableMerger: ...

    def create_catalog(self, catalog_name: str, *, comment: str | None = None, storage_root: str | None = None) -> CatalogInfo: ...

    def delete_catalog(self, catalog_name: str, *, force: bool = False) -> None: ...

    def create_namespace(self, catalog_name: str, namespace: str, *, comment: str | None = None, storage_root: str | None = None) -> NamespaceInfo: ...

    def delete_namespace(self, catalog_name: str, namespace: str, *, force: bool = False) -> None: ...

    def create_table(self, catalog_name: str, namespace: str, table_name: str, *, schema: SchemaDict | None, table_type: TableType, data_source_format: DataSourceFormat | None = None, comment: str | None = None, storage_root: str | None = None, properties: dict[str, str] | None = None) -> TableInfo: ...

    def delete_table(self, catalog_name: str, namespace: str, table_name: str) -> None: ...


class CatalogCredentialProvider:
    catalog: Catalog
    table_id: str
    write: bool

    def __init__(self, catalog: Catalog, table_id: str, *, write: bool) -> None: ...

    def __call__(self) -> CredentialProviderFunctionReturn: ...
