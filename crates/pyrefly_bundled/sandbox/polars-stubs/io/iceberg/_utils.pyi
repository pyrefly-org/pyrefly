from _typeshed import Incomplete

from __future__ import annotations
import abc
import ast
import contextlib
import math
import re
import uuid
from _ast import GtE, Lt, LtE
from ast import (
    Attribute,
    BinOp,
    BitAnd,
    BitOr,
    Call,
    Compare,
    Constant,
    Eq,
    Gt,
    Invert,
    List,
    Name,
    NotEq,
    UnaryOp,
    USub,
)
from dataclasses import dataclass
from functools import cache, singledispatch
from typing import TYPE_CHECKING, Any
import polars._reexport as pl
from polars._utils.convert import to_py_date, to_py_datetime
from polars._utils.logging import eprint
from polars._utils.wrap import wrap_s
from polars.datatypes import Boolean
from polars.exceptions import ComputeError, InvalidOperationError, SchemaError
from polars.io._utils import null_count_dtype
from collections.abc import Callable, Iterable, Sequence
from datetime import date, datetime
import pyarrow as pa
import pyiceberg
import pyiceberg.schema
from pyiceberg.manifest import DataFile
from pyiceberg.table import Table
from pyiceberg.types import IcebergType, NestedField
from polars import DataFrame

ICEBERG_TIME_TO_NS: int = 1000


def try_convert_pyarrow_predicate(pyarrow_predicate: str, schema: pyiceberg.schema.Schema | None = None) -> Any | None: ...


def extract_field_initial_default(field: NestedField) -> pl.Series | None: ...


def pl_dtype_from_iceberg_field(field: NestedField) -> pl.DataType: ...


def name_mapping_by_field_id(tbl: Table) -> dict[int, list[str]] | None: ...


def load_puffin_deletion_file(puffin_bytes: bytes) -> list[tuple[int, str, pl.Series]]: ...


def filter_for_pyiceberg_reader(expr: pyiceberg.expressions.BooleanExpression, schema: pyiceberg.schema.Schema) -> pyiceberg.expressions.BooleanExpression | None: ...


def filter_for_scan_schema(expr: pyiceberg.expressions.BooleanExpression, scan_schema: pyiceberg.schema.Schema, current_schema: pyiceberg.schema.Schema) -> pyiceberg.expressions.BooleanExpression | None: ...


def filter_for_truncate_overflow(expr: pyiceberg.expressions.BooleanExpression, table: Table) -> pyiceberg.expressions.BooleanExpression | None: ...


def filter_for_required_is_null(expr: pyiceberg.expressions.BooleanExpression, schema: pyiceberg.schema.Schema) -> pyiceberg.expressions.BooleanExpression | None: ...


def filter_with_nan_ordering(expr: pyiceberg.expressions.BooleanExpression, schema: pyiceberg.schema.Schema) -> pyiceberg.expressions.BooleanExpression: ...


class IdentityTransformedPartitionValuesBuilder:
    partition_spec_id_to_identity_transforms: dict[int, list[tuple[int, int]]]
    partition_values: dict[int, list[Any] | str]
    partition_values_dtypes: dict[int, DataType]
    present_indices: dict[int, list[int]]

    def __init__(self, table: Table, projected_schema: pyiceberg.schema.Schema) -> None: ...

    def push_partition_values(self, *, current_index: int, partition_spec_id: int, partition_values: pyiceberg.typedef.Record) -> None: ...

    def finish(self) -> dict[int, pl.Series | str]: ...

    @staticmethod
    def present_masks(present_indices: dict[int, list[int]], values: dict[int, pl.Series | str], num_sources: int) -> dict[int, pl.Series]: ...

    @staticmethod
    def fill_absent_with_initial_defaults(values: dict[int, pl.Series | str], present_indices: dict[int, list[int]], initial_defaults: dict[int, pl.Series], num_sources: int) -> dict[int, pl.Series | str]: ...


class IcebergStatisticsLoader:
    best_effort_columns: set[str]
    file_column_statistics: dict[int, IcebergColumnStatisticsLoader]
    file_lengths: list[int]
    load_as_empty_statistics: list[str]
    statistics_schema: Incomplete

    def __init__(self, table: Table, statistics_schema: pyiceberg.schema.Schema, *, best_effort_columns: Sequence[str] = ()) -> None: ...

    def push_file_statistics(self, file: DataFile) -> None: ...

    def finish(self, expected_height: int, identity_transformed_values: dict[int, pl.Series | str]) -> pl.DataFrame: ...


@dataclass
class IcebergColumnStatisticsLoader:
    column_name: str
    column_dtype: pl.DataType
    field_id: int
    load_from_bytes_impl: LoadFromBytesImpl | None
    null_count: list[int | None]
    min_values: list[bytes | None]
    max_values: list[bytes | None]

    def push_file_statistics(self, file: DataFile) -> None: ...

    def null_statistics(self, height: int) -> pl.DataFrame: ...

    def finish(self, expected_height: int, identity_transformed_values: pl.Series | str | None) -> pl.DataFrame: ...

    def __init__(self, column_name: str, column_dtype: DataType, field_id: int, load_from_bytes_impl: LoadFromBytesImpl | None, null_count: list[int | None], min_values: list[bytes | None], max_values: list[bytes | None]) -> None: ...


class LoadFromBytesImpl(abc.ABC):
    polars_dtype: DataType

    def __init__(self, polars_dtype: pl.DataType) -> None: ...

    @staticmethod
    def init_for_field_type(current_field_type: IcebergType, all_field_types: set[IcebergType], field_polars_dtype: pl.DataType) -> LoadFromBytesImpl | None: ...

    @abc.abstractmethod
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadBinaryFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadDateFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadTimeFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadTimestampFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadTimestamptzFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadBooleanFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadDecimalFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadFixedFromBytes(LoadBinaryFromBytes):
    ...


class LoadInt32FromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadInt64FromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


class LoadStringFromBytes(LoadFromBytesImpl):
    def load_from_bytes(self, byte_values: list[bytes | None]) -> pl.Series: ...


def predicate_to_pyiceberg_delete_filter(predicate: pl.Expr, table: Table) -> pyiceberg.expressions.BooleanExpression: ...


def with_table_nullability(data: pa.Table, table_schema: pyiceberg.schema.Schema) -> pa.Table: ...
