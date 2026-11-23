from typing import Literal

from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal
from polars._utils.unstable import issue_unstable_warning
from polars.exceptions import DuplicateError
from polars.schema import Schema
from datetime import datetime
from polars.datatypes.classes import DataType


@dataclass
class CatalogInfo:
    name: str
    comment: str | None
    properties: dict[str, str]
    options: dict[str, str]
    storage_location: str | None
    created_at: datetime | None
    created_by: str | None
    updated_at: datetime | None
    updated_by: str | None

    def __init__(self, name: str, comment: str | None, properties: dict[str, str], options: dict[str, str], storage_location: str | None, created_at: datetime | None, created_by: str | None, updated_at: datetime | None, updated_by: str | None) -> None: ...


@dataclass
class NamespaceInfo:
    name: str
    comment: str | None
    properties: dict[str, str]
    storage_location: str | None
    created_at: datetime | None
    created_by: str | None
    updated_at: datetime | None
    updated_by: str | None

    def __init__(self, name: str, comment: str | None, properties: dict[str, str], storage_location: str | None, created_at: datetime | None, created_by: str | None, updated_at: datetime | None, updated_by: str | None) -> None: ...


@dataclass
class TableInfo:
    name: str
    comment: str | None
    table_id: str
    table_type: TableType
    storage_location: str | None
    data_source_format: DataSourceFormat | None
    columns: list[ColumnInfo] | None
    properties: dict[str, str]
    created_at: datetime | None
    created_by: str | None
    updated_at: datetime | None
    updated_by: str | None

    def get_polars_schema(self) -> Schema | None: ...

    def __init__(self, name: str, comment: str | None, table_id: str, table_type: Literal['EXTERNAL', 'EXTERNAL_SHALLOW_CLONE', 'FOREIGN', 'MANAGED', 'MANAGED_SHALLOW_CLONE', 'MATERIALIZED_VIEW', 'STREAMING_TABLE', 'VIEW'], storage_location: str | None, data_source_format: Literal['AVRO', 'BIGQUERY_FORMAT', 'CSV', 'DATABRICKS_FORMAT', 'DELTA', 'DELTASHARING', 'HIVE_CUSTOM', 'HIVE_SERDE', 'JSON', 'NETSUITE_FORMAT', 'ORC', 'PARQUET', 'REDSHIFT_FORMAT', 'SALESFORCE_FORMAT', 'SNOWFLAKE_FORMAT', 'SQLDW_FORMAT', 'TEXT', 'UNITY_CATALOG', 'VECTOR_INDEX_FORMAT', 'WORKDAY_RAAS_FORMAT'] | None, columns: list[ColumnInfo] | None, properties: dict[str, str], created_at: datetime | None, created_by: str | None, updated_at: datetime | None, updated_by: str | None) -> None: ...


@dataclass
class ColumnInfo:
    name: str
    type_name: str
    type_text: str
    type_json: str
    position: int | None
    comment: str | None
    partition_index: int | None

    def get_polars_dtype(self) -> DataType: ...

    def __init__(self, name: str, type_name: str, type_text: str, type_json: str, position: int | None, comment: str | None, partition_index: int | None) -> None: ...


TableType = Literal[
    "MANAGED",
    "EXTERNAL",
    "VIEW",
    "MATERIALIZED_VIEW",
    "STREAMING_TABLE",
    "MANAGED_SHALLOW_CLONE",
    "FOREIGN",
    "EXTERNAL_SHALLOW_CLONE",
]

DataSourceFormat = Literal[
    "DELTA",
    "CSV",
    "JSON",
    "AVRO",
    "PARQUET",
    "ORC",
    "TEXT",
    "UNITY_CATALOG",
    "DELTASHARING",
    "DATABRICKS_FORMAT",
    "REDSHIFT_FORMAT",
    "SNOWFLAKE_FORMAT",
    "SQLDW_FORMAT",
    "SALESFORCE_FORMAT",
    "BIGQUERY_FORMAT",
    "NETSUITE_FORMAT",
    "WORKDAY_RAAS_FORMAT",
    "HIVE_SERDE",
    "HIVE_CUSTOM",
    "VECTOR_INDEX_FORMAT",
]
