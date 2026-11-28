from __future__ import annotations
import contextlib
import io
import warnings
from collections.abc import Collection, Iterable, Mapping, Sequence
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, time, timedelta
from functools import lru_cache, reduce
from io import BytesIO, StringIO
from operator import and_
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    NoReturn,
    TypeVar,
    overload,
)
import polars._reexport as pl
import polars.selectors as cs
from polars import functions as F
from polars._dependencies import (
    _PYARROW_AVAILABLE,
    _check_for_numpy,
    subprocess,
)
from polars._dependencies import numpy as np
from polars._dependencies import polars_cloud as pc
from polars._dependencies import pyarrow as pa
from polars._typing import (
    ParquetMetadata,
)
from polars._utils.convert import negate_duration_string, parse_as_duration_string
from polars._utils.expired import (
    RemovedParameter,
    RenamedParameter,
    getattr_fallback,
    raise_for_removed_attributes,
    removed_parameters,
)
from polars._utils.parse import (
    parse_into_expression,
    parse_into_list_of_expressions,
    parse_into_list_of_expressions_require_selectors,
)
from polars._utils.parse.expr import parse_list_into_selector
from polars._utils.serde import serialize_polars_object
from polars._utils.slice import LazyPolarsSlice
from polars._utils.unstable import issue_unstable_warning, unstable
from polars._utils.various import (
    _is_generator,
    display_dot_graph,
    extend_bool,
    is_bool_sequence,
    is_sequence,
    normalize_filepath,
    parse_percentiles,
    qualified_type_name,
    require_same_type,
)
from polars._utils.wrap import wrap_expr, wrap_ldf
from polars._warnings import find_stacklevel, issue_warning
from polars.datatypes import (
    DTYPE_TEMPORAL_UNITS,
    N_INFER_DEFAULT,
    Boolean,
    Categorical,
    Date,
    Datetime,
    Duration,
    Enum,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    Int128,
    Null,
    Object,
    String,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Unknown,
    is_polars_dtype,
    parse_into_datatype_expr,
    parse_into_dtype,
)
from polars.datatypes.classes import Struct
from polars.datatypes.group import DataTypeGroup
from polars.exceptions import InvalidOperationError, PerformanceWarning
from polars.lazyframe.engine_config import (
    _eager_engine,
    _select_engine,
    _validate_engine,
)
from polars.lazyframe.group_by import LazyGroupBy
from polars.lazyframe.opt_flags import DEFAULT_QUERY_OPT_FLAGS, REMOVED_OLD_OPT_FLAGS
from polars.lazyframe.resolver._resolver import LazyFrameResolver
from polars.lazyframe.sink_plan import (
    _sink_batches_plan,
    _sink_csv_plan,
    _sink_ipc_plan,
    _sink_ndjson_plan,
    _sink_parquet_plan,
)
from polars.schema import Schema
from polars.selectors import by_dtype, expand_selector
from builtins import slice as slice_
from collections.abc import Awaitable, Callable
from io import IOBase
from typing import IO, Concatenate, Literal, ParamSpec
import deltalake
import pyiceberg.catalog
import pyiceberg.expressions
import pyiceberg.table
import polars.io.iceberg
from polars.io.partition import PartitionBy, SinkedPathsCallback
from polars.lazyframe.engine import _CollectBatches
from polars.lazyframe.opt_flags import QueryOptFlags
from polars import DataFrame, DataType, Expr
from polars._typing import (
        Alignment,
        ArrowSchemaExportable,
        AsofJoinStrategy,
        AsyncResult,
        ClosedInterval,
        ColumnNameOrSelector,
        CsvQuoteStyle,
        EngineType,
        ExplainFormat,
        FillNullStrategy,
        FloatFmt,
        FrameInitTypes,
        IntoExpr,
        IntoExprColumn,
        IpcCompression,
        JoinBuildSide,
        JoinStrategy,
        JoinValidation,
        JoinWhereStrategy,
        Label,
        MaintainOrderJoin,
        Orientation,
        ParquetCompression,
        ParquetMetadata,
        PivotAgg,
        PlanStage,
        PolarsDataType,
        PythonDataType,
        QuantileMethod,
        SchemaDefinition,
        SchemaDict,
        SerializationFormat,
        StartBy,
        StorageOptionsDict,
        SyncOnCloseMethod,
        UniqueKeepStrategy,
    )
from polars._utils.async_ import _GeventDataFrameResult
from polars.config import TableFormatNames
from polars.interchange.protocol import CompatLevel
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.encryption import ParquetEncryptionProperties
from polars.lazyframe.in_process import InProcessQuery
from polars.lazyframe.query_result import QueryResult

T = TypeVar("T")

P = ParamSpec("P")


class LazyFrame:
    def __init__(self, data: FrameInitTypes | None = None, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, orient: Orientation | None = None, infer_schema_length: int | None = ..., nan_to_null: bool = False, height: int | None = None) -> None: ...

    @staticmethod
    def from_lazyframe_resolver(resolver: LazyFrameResolver) -> LazyFrame: ...

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, state: bytes) -> None: ...

    @classmethod
    def deserialize(cls, source: str | bytes | Path | IOBase, *, format: SerializationFormat = "binary") -> LazyFrame: ...

    @property
    def columns(self) -> list[str]: ...

    @property
    def dtypes(self) -> list[DataType]: ...

    @property
    def schema(self) -> Schema: ...

    @property
    def width(self) -> int: ...

    def __bool__(self) -> NoReturn: ...

    def __eq__(self, other: object) -> NoReturn: ...

    def __ne__(self, other: object) -> NoReturn: ...

    def __gt__(self, other: Any) -> NoReturn: ...

    def __lt__(self, other: Any) -> NoReturn: ...

    def __ge__(self, other: Any) -> NoReturn: ...

    def __le__(self, other: Any) -> NoReturn: ...

    def __contains__(self, key: str) -> bool: ...

    def __copy__(self) -> LazyFrame: ...

    def __deepcopy__(self, memo: None = None) -> LazyFrame: ...

    def __getitem__(self, item: slice_) -> LazyFrame: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    @overload
    def serialize(self, file: None = ..., *, format: Literal["binary"] = ...) -> bytes: ...

    @overload
    def serialize(self, file: None = ..., *, format: Literal["json"]) -> str: ...

    @overload
    def serialize(self, file: IOBase | str | Path, *, format: SerializationFormat = ...) -> None: ...

    def pipe(self, function: Callable[Concatenate[LazyFrame, P], T], *args: P.args, **kwargs: P.kwargs) -> T: ...

    @unstable()
    def pipe_with_schema(self, function: Callable[[LazyFrame, Schema], LazyFrame]) -> LazyFrame: ...

    def describe(self, percentiles: Sequence[float] | float | None = ..., *, interpolation: QuantileMethod = "nearest") -> DataFrame: ...

    @removed_parameters(
        RemovedParameter(
            name="streaming",
            deprecated_in="1.25.0",
            removed_in="2.0",
            hint='Use `engine="streaming"` instead.',
        ),
        RemovedParameter(
            name="tree_format",
            deprecated_in="0.20.30",
            removed_in="2.0",
            hint='Use `format="tree"` instead.',
        ),
        *REMOVED_OLD_OPT_FLAGS,
    )
    def explain(self, *, format: ExplainFormat = "plain", optimized: bool = True, engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> str: ...

    @overload
    def show_graph(self, *, optimized: bool = ..., show: bool = ..., output_path: str | Path | None = ..., raw_output: Literal[True], figsize: tuple[float, float] = ..., engine: EngineType = ..., plan_stage: PlanStage = ..., optimizations: QueryOptFlags = ...) -> str: ...

    @overload
    def show_graph(self, *, optimized: bool = ..., show: bool = ..., output_path: str | Path | None = ..., raw_output: Literal[False] = ..., figsize: tuple[float, float] = ..., engine: EngineType = ..., plan_stage: PlanStage = ..., optimizations: QueryOptFlags = ...) -> None: ...

    @overload
    def show_graph(self, *, optimized: bool = ..., show: bool = ..., output_path: str | Path | None = ..., raw_output: bool = ..., figsize: tuple[float, float] = ..., engine: EngineType = ..., plan_stage: PlanStage = ..., optimizations: QueryOptFlags = ...) -> str | None: ...

    def inspect(self, fmt: str = "{}") -> LazyFrame: ...

    def sort(self, by: IntoExpr | Iterable[IntoExpr], *more_by: IntoExpr, descending: bool | Sequence[bool] = False, nulls_last: bool | Sequence[bool] = False, maintain_order: bool = False, multithreaded: bool = True) -> LazyFrame: ...

    def sql(self, query: str, *, table_name: str = "self") -> LazyFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="descending",
            new_name="reverse",
            deprecated_in="1.0.0",
            removed_in="2.0",
        )
    )
    def top_k(self, k: int, *, by: IntoExpr | Iterable[IntoExpr], reverse: bool | Sequence[bool] = False) -> LazyFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="descending",
            new_name="reverse",
            deprecated_in="1.0.0",
            removed_in="2.0",
        )
    )
    def bottom_k(self, k: int, *, by: IntoExpr | Iterable[IntoExpr], reverse: bool | Sequence[bool] = False) -> LazyFrame: ...

    @unstable()
    def execute(self, *, optimizations: QueryOptFlags = ..., engine: EngineType = "auto", **_kwargs: Any) -> QueryResult: ...

    @overload
    def collect(self, *, engine: EngineType = "auto", background: Literal[True], optimizations: QueryOptFlags = ...) -> InProcessQuery: ...

    @overload
    def collect(self, *, engine: EngineType = "auto", background: Literal[False] = False, optimizations: QueryOptFlags = ...) -> DataFrame: ...

    @overload
    def collect_async(self, *, gevent: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> _GeventDataFrameResult[DataFrame]: ...

    @overload
    def collect_async(self, *, gevent: Literal[False] = False, engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> Awaitable[DataFrame]: ...

    def collect_schema(self) -> Schema: ...

    @overload
    def sink_parquet(self, path: str | Path | IO[bytes] | PartitionBy, *, compression: ParquetCompression = "zstd", compression_level: int | None = None, statistics: bool | str | dict[str, bool] = True, row_group_size: int | None = None, data_page_size: int | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[False] = ..., engine: EngineType = "auto", metadata: ParquetMetadata | None = None, arrow_schema: ArrowSchemaExportable | None = None, encryption: ParquetEncryptionProperties | None = None, optimizations: QueryOptFlags = ..., sinked_paths_callback: SinkedPathsCallback | None = None) -> None: ...

    @overload
    def sink_parquet(self, path: str | Path | IO[bytes] | PartitionBy, *, compression: ParquetCompression = "zstd", compression_level: int | None = None, statistics: bool | str | dict[str, bool] = True, row_group_size: int | None = None, data_page_size: int | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[True], engine: EngineType = "auto", metadata: ParquetMetadata | None = None, arrow_schema: ArrowSchemaExportable | None = None, encryption: ParquetEncryptionProperties | None = None, optimizations: QueryOptFlags = ..., sinked_paths_callback: SinkedPathsCallback | None = None) -> LazyFrame: ...

    @overload
    def sink_delta(self, target: str | Path | deltalake.DeltaTable, *, mode: Literal["error", "append", "overwrite", "ignore"] = ..., storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ..., delta_write_options: dict[str, Any] | None = ..., engine: EngineType = ..., optimizations: QueryOptFlags = ...) -> None: ...

    @overload
    def sink_delta(self, target: str | Path | deltalake.DeltaTable, *, mode: Literal["merge"], storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ..., delta_merge_options: dict[str, Any], engine: EngineType = ..., optimizations: QueryOptFlags = ...) -> deltalake.table.TableMerger: ...

    @unstable()
    def sink_iceberg(self, target: str | pyiceberg.table.Table, *, mode: Literal["append", "overwrite"], schema_mode: Literal["merge", "overwrite"] | None = None, overwrite_filter: (Expr
        | pyiceberg.expressions.BooleanExpression
        | str
        | None) = None, partition_overwrite: Literal["dynamic"] | None = None, create_if_not_exists: bool = False, create_namespace_if_not_exists: bool = False, snapshot_properties: dict[str, str] | None = None, catalog: (pyiceberg.catalog.Catalog
        | polars.io.iceberg.IcebergCatalogConfig
        | None) = None, storage_options: StorageOptionsDict | None = None, compression: ParquetCompression = "zstd", compression_level: int | None = None, row_group_size: int | None = None, maintain_order: bool = True, engine: EngineType = "auto") -> pl.DataFrame: ...

    @overload
    def sink_ipc(self, path: str | Path | IO[bytes] | PartitionBy, *, compression: IpcCompression | None = "uncompressed", compat_level: CompatLevel | None = None, record_batch_size: int | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[False] = ..., engine: EngineType = "auto", optimizations: QueryOptFlags = ..., _record_batch_statistics: bool = False, sinked_paths_callback: SinkedPathsCallback | None = None) -> None: ...

    @overload
    def sink_ipc(self, path: str | Path | IO[bytes] | PartitionBy, *, compression: IpcCompression | None = "uncompressed", compat_level: CompatLevel | None = None, record_batch_size: int | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ..., _record_batch_statistics: bool = False, sinked_paths_callback: SinkedPathsCallback | None = None) -> LazyFrame: ...

    @overload
    def sink_csv(self, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, include_bom: bool = False, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True, include_header: bool = True, separator: str = ",", line_terminator: str = "\n", quote_char: str = '"', batch_size: int = 1024, datetime_format: str | None = None, date_format: str | None = None, time_format: str | None = None, float_scientific: bool | None = None, float_precision: int | None = None, decimal_comma: bool = False, null_value: str | None = None, quote_style: CsvQuoteStyle | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[False] = ..., engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> None: ...

    @overload
    def sink_csv(self, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, include_bom: bool = False, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True, include_header: bool = True, separator: str = ",", line_terminator: str = "\n", quote_char: str = '"', batch_size: int = 1024, datetime_format: str | None = None, date_format: str | None = None, time_format: str | None = None, float_scientific: bool | None = None, float_precision: int | None = None, decimal_comma: bool = False, null_value: str | None = None, quote_style: CsvQuoteStyle | None = None, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> LazyFrame: ...

    @overload
    def sink_ndjson(self, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[False] = ..., engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> None: ...

    @overload
    def sink_ndjson(self, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True, maintain_order: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: (CredentialProviderFunction
        | Literal["auto"]
        | None) = "auto", sync_on_close: SyncOnCloseMethod | None = None, mkdir: bool = False, lazy: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> LazyFrame: ...

    @overload
    def sink_batches(self, function: Callable[[DataFrame], bool | None], *, chunk_size: int | None = None, maintain_order: bool = True, lazy: Literal[False] = ..., engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> None: ...

    @overload
    def sink_batches(self, function: Callable[[DataFrame], bool | None], *, chunk_size: int | None = None, maintain_order: bool = True, lazy: Literal[True], engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> pl.LazyFrame: ...

    @unstable()
    def collect_batches(self, *, chunk_size: int | None = None, maintain_order: bool = True, lazy: bool = False, engine: EngineType = "auto", optimizations: QueryOptFlags = ...) -> _CollectBatches: ...

    def lazy(self) -> LazyFrame: ...

    def cache(self) -> LazyFrame: ...

    def cast(self, dtypes: (Mapping[
                ColumnNameOrSelector | PolarsDataType, PolarsDataType | PythonDataType
            ]
            | PolarsDataType
            | pl.DataTypeExpr
            | Schema), *, strict: bool = True) -> LazyFrame: ...

    def clear(self, n: int = 0) -> LazyFrame: ...

    def clone(self) -> LazyFrame: ...

    def filter(self, *predicates: (IntoExprColumn
            | Iterable[IntoExprColumn]
            | bool
            | list[bool]
            | np.ndarray[Any, Any]), **constraints: Any) -> LazyFrame: ...

    def remove(self, *predicates: (IntoExprColumn
            | Iterable[IntoExprColumn]
            | bool
            | list[bool]
            | np.ndarray[Any, Any]), **constraints: Any) -> LazyFrame: ...

    def select(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> LazyFrame: ...

    def select_seq(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> LazyFrame: ...

    def group_by(self, *by: IntoExpr | Iterable[IntoExpr], maintain_order: bool = False, **named_by: IntoExpr) -> LazyGroupBy: ...

    @removed_parameters(
        RenamedParameter(
            name="by",
            new_name="group_by",
            deprecated_in="0.20.14",
            removed_in="2.0",
        )
    )
    def rolling(self, index_column: IntoExpr, *, period: str | timedelta, offset: str | timedelta | None = None, closed: ClosedInterval = "right", group_by: IntoExpr | Iterable[IntoExpr] | None = None) -> LazyGroupBy: ...

    @removed_parameters(
        RenamedParameter(
            name="by",
            new_name="group_by",
            deprecated_in="0.20.14",
            removed_in="2.0",
        )
    )
    def group_by_dynamic(self, index_column: IntoExpr, *, every: str | timedelta, period: str | timedelta | None = None, offset: str | timedelta | None = None, include_boundaries: bool = False, closed: ClosedInterval = "left", label: Label = "left", group_by: IntoExpr | Iterable[IntoExpr] | None = None, start_by: StartBy = "window") -> LazyGroupBy: ...

    def join_asof(self, other: LazyFrame, *, left_on: str | None | Expr = None, right_on: str | None | Expr = None, on: str | None | Expr = None, by_left: str | Sequence[str] | None = None, by_right: str | Sequence[str] | None = None, by: str | Sequence[str] | None = None, strategy: AsofJoinStrategy = "backward", suffix: str = "_right", tolerance: str | int | float | timedelta | None = None, allow_parallel: bool = True, force_parallel: bool = False, coalesce: bool = True, allow_exact_matches: bool = True, check_sortedness: bool = True) -> LazyFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="join_nulls",
            new_name="nulls_equal",
            deprecated_in="1.24",
            removed_in="2.0",
        )
    )
    def join(self, other: LazyFrame, on: str | Expr | Sequence[str | Expr] | None = None, how: JoinStrategy = "inner", *, left_on: str | Expr | Sequence[str | Expr] | None = None, right_on: str | Expr | Sequence[str | Expr] | None = None, suffix: str = "_right", validate: JoinValidation = "m:m", nulls_equal: bool = False, coalesce: bool | None = None, maintain_order: MaintainOrderJoin | None = None, build_side: JoinBuildSide = "auto", allow_parallel: bool = True, force_parallel: bool = False) -> LazyFrame: ...

    @unstable()
    def join_where(self, other: LazyFrame, *predicates: Expr | Iterable[Expr], how: JoinWhereStrategy = "inner", suffix: str = "_right") -> LazyFrame: ...

    @unstable()
    def gather(self, indices: (int
        | Sequence[int]
        | IntoExpr
        | pl.Series
        | np.ndarray[Any, Any]
        | pl.LazyFrame), *, null_on_oob: bool = False) -> LazyFrame: ...

    def with_columns(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> LazyFrame: ...

    def with_columns_seq(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> LazyFrame: ...

    def drop(self, *columns: ColumnNameOrSelector | Iterable[ColumnNameOrSelector], strict: bool = True) -> LazyFrame: ...

    def rename(self, mapping: Mapping[str, str] | Callable[[str], str], *, strict: bool = True) -> LazyFrame: ...

    def reverse(self) -> LazyFrame: ...

    def shift(self, n: int | IntoExprColumn = 1, *, fill_value: IntoExpr | None = None) -> LazyFrame: ...

    def slice(self, offset: int, length: int | None = None) -> LazyFrame: ...

    def limit(self, n: int = 5) -> LazyFrame: ...

    def head(self, n: int = 5) -> LazyFrame: ...

    def tail(self, n: int = 5) -> LazyFrame: ...

    def last(self) -> LazyFrame: ...

    def first(self) -> LazyFrame: ...

    def with_row_index(self, name: str = "index", offset: int = 0) -> LazyFrame: ...

    def gather_every(self, n: int, offset: int = 0) -> LazyFrame: ...

    def fill_null(self, value: Any | Expr | None = None, strategy: FillNullStrategy | None = None, limit: int | None = None, *, matches_supertype: bool = True) -> LazyFrame: ...

    def fill_nan(self, value: int | float | Expr | None) -> LazyFrame: ...

    def std(self, ddof: int = 1) -> LazyFrame: ...

    def var(self, ddof: int = 1) -> LazyFrame: ...

    def max(self) -> LazyFrame: ...

    def min(self) -> LazyFrame: ...

    def sum(self) -> LazyFrame: ...

    def mean(self) -> LazyFrame: ...

    def median(self) -> LazyFrame: ...

    def null_count(self) -> LazyFrame: ...

    def quantile(self, quantile: float | Expr, interpolation: QuantileMethod = "nearest") -> LazyFrame: ...

    def explode(self, columns: ColumnNameOrSelector | Iterable[ColumnNameOrSelector], *more_columns: ColumnNameOrSelector, empty_as_null: bool = False, keep_nulls: bool = True) -> LazyFrame: ...

    def unique(self, subset: IntoExpr | Collection[IntoExpr] | None = None, *, keep: UniqueKeepStrategy = "any", maintain_order: bool = False) -> LazyFrame: ...

    def drop_nans(self, subset: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None) -> LazyFrame: ...

    def drop_nulls(self, subset: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None) -> LazyFrame: ...

    def pivot(self, on: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], on_columns: Sequence[Any] | pl.Series | pl.DataFrame, *, index: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, values: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, aggregate_function: PivotAgg | Expr | None = None, maintain_order: bool = False, separator: str = "_", column_naming: Literal["auto", "combine"] = "auto") -> LazyFrame: ...

    @removed_parameters(
        RemovedParameter(name="streamable", deprecated_in="1.5.0", removed_in="2.0")
    )
    def unpivot(self, on: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, *, index: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, variable_name: str | None = None, value_name: str | None = None) -> LazyFrame: ...

    @removed_parameters(
        RemovedParameter(
            name="no_optimizations",
            deprecated_in="1.39.3",
            removed_in="2.0",
            hint="Use the `predicate_pushdown`, `projection_pushdown`, and `slice_pushdown` flags instead.",
        ),
    )
    def map_batches(self, function: Callable[[DataFrame], DataFrame], *, predicate_pushdown: bool = False, projection_pushdown: bool = False, slice_pushdown: bool = False, schema: None | SchemaDict = None, validate_output_schema: bool = True, streamable: bool = False) -> LazyFrame: ...

    def interpolate(self) -> LazyFrame: ...

    def unnest(self, columns: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None, *more_columns: ColumnNameOrSelector, separator: str | None = None) -> LazyFrame: ...

    def merge_sorted(self, other: LazyFrame, key: str | Sequence[str], *, maintain_order: bool = False) -> LazyFrame: ...

    def set_sorted(self, column: str | list[str], *more_columns: str, descending: bool | list[bool] = False, nulls_last: bool | list[bool] = False) -> LazyFrame: ...

    @unstable()
    def update(self, other: LazyFrame, on: str | Sequence[str] | None = None, how: Literal["left", "inner", "full"] = "left", *, left_on: str | Sequence[str] | None = None, right_on: str | Sequence[str] | None = None, include_nulls: bool = False, maintain_order: MaintainOrderJoin | None = "left") -> LazyFrame: ...

    def count(self) -> LazyFrame: ...

    @unstable()
    def remote(self, context: pc.ClientContext | None = None, *, plan_type: pc._typing.PlanTypePreference = "dot", n_retries: int = 0, engine: pc._typing.Engine = "auto", scaling_mode: pc._typing.ScalingMode = "auto") -> pc.LazyFrameRemote: ...

    @unstable()
    def match_to_schema(self, schema: SchemaDict | Schema, *, missing_columns: (Literal["insert", "raise"]
        | Mapping[str, Literal["insert", "raise"] | Expr]
        | Expr) = "raise", missing_struct_fields: (Literal["insert", "raise"]
        | Mapping[str, Literal["insert", "raise"]]) = "raise", extra_columns: Literal["ignore", "raise"] = "raise", extra_struct_fields: (Literal["ignore", "raise"]
        | Mapping[str, Literal["ignore", "raise"]]) = "raise", integer_cast: (Literal["upcast", "forbid"]
        | Mapping[str, Literal["upcast", "forbid"]]) = "forbid", float_cast: (Literal["upcast", "forbid"]
        | Mapping[str, Literal["upcast", "forbid"]]) = "forbid") -> LazyFrame: ...

    def show(self, limit: int | None = 5, *, ascii_tables: bool | None = None, decimal_separator: str | None = None, thousands_separator: str | bool | None = None, float_precision: int | None = None, fmt_float: FloatFmt | None = None, fmt_str_lengths: int | None = None, fmt_table_cell_list_len: int | None = None, tbl_cell_alignment: Alignment | None = None, tbl_cell_numeric_alignment: Alignment | None = None, tbl_cols: int | None = None, tbl_column_data_type_inline: bool | None = None, tbl_dataframe_shape_below: bool | None = None, tbl_formatting: TableFormatNames | None = None, tbl_hide_column_data_types: bool | None = None, tbl_hide_column_names: bool | None = None, tbl_hide_dtype_separator: bool | None = None, tbl_hide_dataframe_shape: bool | None = None, tbl_width_chars: int | None = None, trim_decimal_zeros: bool | None = True) -> None: ...
