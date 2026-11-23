from __future__ import annotations
import contextlib
import io
import operator
import os
from collections import defaultdict
from collections.abc import (
    Generator,
    Iterable,
    Mapping,
    Sequence,
    Sized,
)
from io import BytesIO, StringIO
from pathlib import Path
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    ClassVar,
    NoReturn,
    TypeVar,
    cast,
    get_args,
    overload,
)
import polars._reexport as pl
from polars import functions as F
from polars._dependencies import (
    _ALTAIR_AVAILABLE,
    _GREAT_TABLES_AVAILABLE,
    _PANDAS_AVAILABLE,
    _PYARROW_AVAILABLE,
    _check_for_numpy,
    _check_for_pandas,
    _check_for_pyarrow,
    _check_for_torch,
    altair,
    great_tables,
    import_optional,
    torch,
)
from polars._dependencies import numpy as np
from polars._dependencies import pandas as pd
from polars._dependencies import pyarrow as pa
from polars._typing import DbWriteMode, JaxExportType, TorchExportType
from polars._utils.construction import (
    arrow_to_pydf,
    dataframe_to_pydf,
    dict_to_pydf,
    iterable_to_pydf,
    numpy_to_pydf,
    pandas_to_pydf,
    sequence_to_pydf,
    series_to_pydf,
)
from polars._utils.convert import parse_as_duration_string
from polars._utils.expired import (
    RemovedParameter,
    RenamedParameter,
    getattr_fallback,
    raise_for_removed_attributes,
    removed_parameters,
)
from polars._utils.getitem import get_df_item_by_key
from polars._utils.parse import parse_into_list_of_expressions_require_selectors
from polars._utils.pycapsule import is_pycapsule, pycapsule_to_frame
from polars._utils.serde import serialize_polars_object
from polars._utils.unstable import issue_unstable_warning, unstable
from polars._utils.various import (
    NO_DEFAULT,
    _in_notebook,
    is_bool_sequence,
    normalize_filepath,
    parse_version,
    qualified_type_name,
    require_same_type,
    scale_bytes,
    warn_null_comparison,
)
from polars._utils.wrap import wrap_ldf, wrap_s
from polars.config import Config
from polars.dataframe._html import NotebookFormatter
from polars.dataframe.group_by import DynamicGroupBy, GroupBy, RollingGroupBy
from polars.dataframe.plotting import DataFramePlot
from polars.datatypes import (
    N_INFER_DEFAULT,
    Boolean,
    Float32,
    Float64,
    Int32,
    Int64,
    List,
    Null,
    Object,
    String,
    Struct,
    UInt16,
    UInt32,
    UInt64,
)
from polars.datatypes.group import INTEGER_DTYPES
from polars.exceptions import (
    ColumnNotFoundError,
    InvalidOperationError,
    ModuleUpgradeRequiredError,
    NoRowsReturnedError,
    TooManyRowsReturnedError,
    UnstableWarning,
)
from polars.functions import col, lit
from polars.interchange.protocol import CompatLevel
from polars.schema import Schema
from polars.selectors import _expand_selector_dicts, _expand_selectors
from collections.abc import (
        Callable,
        Collection,
        Iterator,
    )
from datetime import timedelta
from io import IOBase
from typing import Concatenate, Literal, ParamSpec
import deltalake
import jax
import pyiceberg
from great_tables import GT
from sqlalchemy.engine import Engine
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet
from polars import DataType, Expr, LazyFrame, Series
from polars._typing import (
        Alignment,
        ArrowSchemaExportable,
        AsofJoinStrategy,
        AvroCompression,
        ClosedInterval,
        ColumnFormatDict,
        ColumnNameOrSelector,
        ColumnTotalsDefinition,
        ColumnWidthsDefinition,
        ComparisonOperator,
        ConditionalFormatDict,
        ConnectionOrCursor,
        CsvQuoteStyle,
        DbWriteEngine,
        EngineType,
        FillNullStrategy,
        FloatFmt,
        FrameInitTypes,
        IndexOrder,
        IntoExpr,
        IntoExprColumn,
        IpcCompression,
        JoinBuildSide,
        JoinStrategy,
        JoinValidation,
        JoinWhereStrategy,
        Label,
        MaintainOrderJoin,
        MultiColSelector,
        MultiIndexSelector,
        OneOrMoreDataTypes,
        Orientation,
        ParquetCompression,
        ParquetMetadata,
        PivotAgg,
        PolarsDataType,
        PythonDataType,
        QuantileMethod,
        RowTotalsDefinition,
        SchemaDefinition,
        SchemaDict,
        SelectorType,
        SerializationFormat,
        SingleColSelector,
        SingleIndexSelector,
        SizeUnit,
        StartBy,
        StorageOptionsDict,
        UniqueKeepStrategy,
        UnstackDirection,
    )
from polars._utils.various import NoDefault
from polars.config import TableFormatNames
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.encryption import ParquetEncryptionProperties
from polars.io.partition import PartitionBy
from polars.ml.torch import PolarsDataset

T = TypeVar("T")

P = ParamSpec("P")


class DataFrame:
    def __init__(self, data: FrameInitTypes | None = None, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, orient: Orientation | None = None, infer_schema_length: int | None = ..., nan_to_null: bool = False, height: int | None = None) -> None: ...

    @classmethod
    def deserialize(cls, source: str | bytes | Path | IOBase, *, format: SerializationFormat = "binary") -> DataFrame: ...

    @property
    @unstable()
    def plot(self) -> DataFramePlot: ...

    @property
    @unstable()
    def style(self) -> GT: ...

    @property
    def shape(self) -> tuple[int, int]: ...

    @property
    def height(self) -> int: ...

    @property
    def width(self) -> int: ...

    @property
    def columns(self) -> list[str]: ...

    @columns.setter
    def columns(self, names: Sequence[str]) -> None: ...

    @property
    def dtypes(self) -> list[DataType]: ...

    @property
    def flags(self) -> dict[str, dict[str, bool]]: ...

    @property
    def schema(self) -> Schema: ...

    def __array__(self, dtype: np.dtype[Any] | None = None, copy: bool | None = None) -> np.ndarray[Any, Any]: ...

    def __floordiv__(self, other: DataFrame | Series | int | float) -> DataFrame: ...

    def __truediv__(self, other: DataFrame | Series | int | float) -> DataFrame: ...

    def __bool__(self) -> NoReturn: ...

    def __eq__(self, other: object) -> DataFrame: ...

    def __ne__(self, other: object) -> DataFrame: ...

    def __gt__(self, other: Any) -> DataFrame: ...

    def __lt__(self, other: Any) -> DataFrame: ...

    def __ge__(self, other: Any) -> DataFrame: ...

    def __le__(self, other: Any) -> DataFrame: ...

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, state: bytes) -> None: ...

    def __mul__(self, other: DataFrame | Series | int | float) -> DataFrame: ...

    def __rmul__(self, other: int | float) -> DataFrame: ...

    def __add__(self, other: DataFrame | Series | int | float | bool | str) -> DataFrame: ...

    def __radd__(self, other: DataFrame | Series | int | float | bool | str) -> DataFrame: ...

    def __sub__(self, other: DataFrame | Series | int | float) -> DataFrame: ...

    def __mod__(self, other: DataFrame | Series | int | float) -> DataFrame: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    def __contains__(self, key: str) -> bool: ...

    def __iter__(self) -> Iterator[Series]: ...

    def __reversed__(self) -> Iterator[Series]: ...

    @overload
    def __getitem__(self, key: tuple[SingleIndexSelector, SingleColSelector]) -> Any: ...

    @overload
    def __getitem__(self, key: str | tuple[MultiIndexSelector, SingleColSelector]) -> Series: ...

    @overload
    def __getitem__(self, key: (SingleIndexSelector
            | MultiIndexSelector
            | MultiColSelector
            | tuple[SingleIndexSelector, MultiColSelector]
            | tuple[MultiIndexSelector, MultiColSelector])) -> DataFrame: ...

    def __setitem__(self, key: str | Sequence[str] | tuple[Any, str | int], value: Any) -> None: ...

    def __len__(self) -> int: ...

    def __copy__(self) -> DataFrame: ...

    def __deepcopy__(self, memo: None = None) -> DataFrame: ...

    def __arrow_c_stream__(self, requested_schema: object | None = None) -> object: ...

    def collect_schema(self) -> Schema: ...

    def item(self, row: int | None = None, column: int | str | None = None) -> Any: ...

    @removed_parameters(
        RenamedParameter(
            name="future",
            new_name="compat_level",
            deprecated_in="1.1",
            removed_in="2.0",
        )
    )
    def to_arrow(self, *, compat_level: CompatLevel | None = None) -> pa.Table: ...

    @overload
    def to_dict(self, *, as_series: Literal[True] = ...) -> dict[str, Series]: ...

    @overload
    def to_dict(self, *, as_series: Literal[False]) -> dict[str, list[Any]]: ...

    @overload
    def to_dict(self, *, as_series: bool) -> dict[str, Series] | dict[str, list[Any]]: ...

    def to_dicts(self) -> list[dict[str, Any]]: ...

    @overload
    def to_numpy(self, *, order: IndexOrder = ..., writable: bool = ..., allow_copy: bool = ..., structured: bool = ..., masked: Literal[False] = ...) -> np.ndarray[Any, Any]: ...

    @overload
    def to_numpy(self, *, order: IndexOrder = ..., writable: bool = ..., allow_copy: bool = ..., structured: bool = ..., masked: Literal[True]) -> np.ma.MaskedArray[Any, Any]: ...

    @overload
    def to_numpy(self, *, order: IndexOrder = ..., writable: bool = ..., allow_copy: bool = ..., structured: bool = ..., masked: bool) -> np.ndarray[Any, Any]: ...

    @overload
    def to_jax(self, return_type: Literal["array"] = ..., *, device: jax.Device | str | None = ..., label: str | Expr | Sequence[str | Expr] | None = ..., features: str | Expr | Sequence[str | Expr] | None = ..., dtype: PolarsDataType | None = ..., order: IndexOrder = ...) -> jax.Array: ...

    @overload
    def to_jax(self, return_type: Literal["dict"], *, device: jax.Device | str | None = ..., label: str | Expr | Sequence[str | Expr] | None = ..., features: str | Expr | Sequence[str | Expr] | None = ..., dtype: PolarsDataType | None = ..., order: IndexOrder = ...) -> dict[str, jax.Array]: ...

    @overload
    def to_torch(self, return_type: Literal["tensor"] = ..., *, label: str | Expr | Sequence[str | Expr] | None = ..., features: str | Expr | Sequence[str | Expr] | None = ..., dtype: PolarsDataType | None = ...) -> torch.Tensor: ...

    @overload
    def to_torch(self, return_type: Literal["dataset"], *, label: str | Expr | Sequence[str | Expr] | None = ..., features: str | Expr | Sequence[str | Expr] | None = ..., dtype: PolarsDataType | None = ...) -> PolarsDataset: ...

    @overload
    def to_torch(self, return_type: Literal["dict"], *, label: str | Expr | Sequence[str | Expr] | None = ..., features: str | Expr | Sequence[str | Expr] | None = ..., dtype: PolarsDataType | None = ...) -> dict[str, torch.Tensor]: ...

    def to_pandas(self, *, use_pyarrow_extension_array: bool = False, **kwargs: Any) -> pd.DataFrame: ...

    def to_series(self, index: int = 0) -> Series: ...

    def to_init_repr(self, n: int = 1000) -> str: ...

    @overload
    def serialize(self, file: None = ..., *, format: Literal["binary"] = ...) -> bytes: ...

    @overload
    def serialize(self, file: None = ..., *, format: Literal["json"]) -> str: ...

    @overload
    def serialize(self, file: IOBase | str | Path, *, format: SerializationFormat = ...) -> None: ...

    @overload
    def write_json(self, file: None = ...) -> str: ...

    @overload
    def write_json(self, file: IOBase | str | Path) -> None: ...

    @overload
    def write_ndjson(self, file: None = None, *, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True) -> str: ...

    @overload
    def write_ndjson(self, file: str | Path | IO[bytes] | IO[str], *, compression: Literal["uncompressed", "gzip", "zstd"] = "uncompressed", compression_level: int | None = None, check_extension: bool = True) -> None: ...

    @overload
    def write_csv(self, file: None = None, *, include_bom: bool = ..., compression: Literal["uncompressed", "gzip", "zstd"] = ..., compression_level: int | None = None, check_extension: bool = ..., include_header: bool = ..., separator: str = ..., line_terminator: str = ..., quote_char: str = ..., batch_size: int = ..., datetime_format: str | None = ..., date_format: str | None = ..., time_format: str | None = ..., float_scientific: bool | None = ..., float_precision: int | None = ..., decimal_comma: bool = ..., null_value: str | None = ..., quote_style: CsvQuoteStyle | None = ..., storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ...) -> str: ...

    @overload
    def write_csv(self, file: str | Path | IO[str] | IO[bytes], *, include_bom: bool = ..., compression: Literal["uncompressed", "gzip", "zstd"] = ..., compression_level: int | None = None, check_extension: bool = ..., include_header: bool = ..., separator: str = ..., line_terminator: str = ..., quote_char: str = ..., batch_size: int = ..., datetime_format: str | None = ..., date_format: str | None = ..., time_format: str | None = ..., float_scientific: bool | None = ..., float_precision: int | None = ..., decimal_comma: bool = ..., null_value: str | None = ..., quote_style: CsvQuoteStyle | None = ..., storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ...) -> None: ...

    def write_clipboard(self, *, separator: str = "\t", **kwargs: Any) -> None: ...

    @unstable()
    def write_avro(self, file: str | Path | IO[bytes], compression: AvroCompression = "uncompressed", name: str = "") -> None: ...

    def write_excel(self, workbook: str | Workbook | IO[bytes] | Path | None = None, worksheet: str | Worksheet | None = None, *, position: tuple[int, int] | str = "A1", table_style: str | dict[str, Any] | None = None, table_name: str | None = None, column_formats: ColumnFormatDict | None = None, dtype_formats: dict[OneOrMoreDataTypes, str] | None = None, conditional_formats: ConditionalFormatDict | None = None, header_format: dict[str, Any] | None = None, column_totals: ColumnTotalsDefinition | None = None, column_widths: ColumnWidthsDefinition | None = None, row_totals: RowTotalsDefinition | None = None, row_heights: dict[int | tuple[int, ...], int] | int | None = None, sparklines: dict[str, Sequence[str] | dict[str, Any]] | None = None, formulas: dict[str, str | dict[str, str]] | None = None, float_precision: int = 3, include_header: bool = True, autofilter: bool = True, autofit: bool = False, hidden_columns: Sequence[str] | SelectorType | None = None, hide_gridlines: bool = False, sheet_zoom: int | None = None, freeze_panes: (str
            | tuple[int, int]
            | tuple[str, int, int]
            | tuple[int, int, int, int]
            | None) = None, use_zip64: bool = False) -> Workbook: ...

    @overload
    def write_ipc(self, file: None, *, compression: IpcCompression = "uncompressed", compat_level: CompatLevel | None = None, record_batch_size: int | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto") -> BytesIO: ...

    @overload
    def write_ipc(self, file: str | Path | IO[bytes], *, compression: IpcCompression = "uncompressed", compat_level: CompatLevel | None = None, record_batch_size: int | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto") -> None: ...

    @overload
    def write_ipc_stream(self, file: None, *, compression: IpcCompression = "uncompressed", compat_level: CompatLevel | None = None) -> BytesIO: ...

    @overload
    def write_ipc_stream(self, file: str | Path | IO[bytes], *, compression: IpcCompression = "uncompressed", compat_level: CompatLevel | None = None) -> None: ...

    @removed_parameters(
        RemovedParameter(
            name="retries",
            deprecated_in="1.37.1",
            removed_in="2.0",
            hint="Specify `max_retries` in `storage_options` instead.",
        )
    )
    def write_parquet(self, file: str | Path | IO[bytes], *, compression: ParquetCompression = "zstd", compression_level: int | None = None, statistics: bool | str | dict[str, bool] = True, row_group_size: int | None = None, data_page_size: int | None = None, use_pyarrow: bool = False, pyarrow_options: dict[str, Any] | None = None, partition_by: str | Sequence[str] | None = None, partition_chunk_size_bytes: int = 4_294_967_296, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", metadata: ParquetMetadata | None = None, arrow_schema: ArrowSchemaExportable | None = None, encryption: ParquetEncryptionProperties | None = None, mkdir: bool = False) -> None: ...

    def write_database(self, table_name: str, connection: ConnectionOrCursor | str, *, if_table_exists: DbWriteMode = "fail", engine: DbWriteEngine | None = None, engine_options: dict[str, Any] | None = None) -> int: ...

    @unstable()
    def write_iceberg(self, target: str | pyiceberg.table.Table, mode: Literal["append", "overwrite"]) -> None: ...

    @overload
    def write_delta(self, target: str | Path | deltalake.DeltaTable, *, mode: Literal["error", "append", "overwrite", "ignore"] = ..., storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ..., delta_write_options: dict[str, Any] | None = ...) -> None: ...

    @overload
    def write_delta(self, target: str | Path | deltalake.DeltaTable, *, mode: Literal["merge"], storage_options: StorageOptionsDict | None = ..., credential_provider: CredentialProviderFunction | Literal["auto"] | None = ..., delta_merge_options: dict[str, Any]) -> deltalake.table.TableMerger: ...

    def estimated_size(self, unit: SizeUnit = "b") -> int | float: ...

    def transpose(self, *, include_header: bool = False, header_name: str = "column", column_names: str | Iterable[str] | None = None) -> DataFrame: ...

    def reverse(self) -> DataFrame: ...

    def rename(self, mapping: Mapping[str, str] | Callable[[str], str], *, strict: bool = True) -> DataFrame: ...

    def insert_column(self, index: int, column: IntoExprColumn) -> DataFrame: ...

    def filter(self, *predicates: (IntoExprColumn
            | Iterable[IntoExprColumn]
            | bool
            | list[bool]
            | np.ndarray[Any, Any]), **constraints: Any) -> DataFrame: ...

    def remove(self, *predicates: (IntoExprColumn
            | Iterable[IntoExprColumn]
            | bool
            | list[bool]
            | np.ndarray[Any, Any]), **constraints: Any) -> DataFrame: ...

    @overload
    def glimpse(self, *, max_items_per_column: int = ..., max_colname_length: int = ..., return_type: None = ...) -> None: ...

    @overload
    def glimpse(self, *, max_items_per_column: int = ..., max_colname_length: int = ..., return_type: Literal["string"]) -> str: ...

    @overload
    def glimpse(self, *, max_items_per_column: int = ..., max_colname_length: int = ..., return_type: Literal["frame", "self"]) -> DataFrame: ...

    def describe(self, percentiles: Sequence[float] | float | None = ..., *, interpolation: QuantileMethod = "nearest") -> DataFrame: ...

    def get_column_index(self, name: str) -> int: ...

    def replace_column(self, index: int, column: Series) -> DataFrame: ...

    def sort(self, by: IntoExpr | Iterable[IntoExpr], *more_by: IntoExpr, descending: bool | Sequence[bool] = False, nulls_last: bool | Sequence[bool] = False, multithreaded: bool = True, maintain_order: bool = False) -> DataFrame: ...

    def sql(self, query: str, *, table_name: str = "self") -> DataFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="descending",
            new_name="reverse",
            deprecated_in="1.0.0",
            removed_in="2.0",
        )
    )
    def top_k(self, k: int, *, by: IntoExpr | Iterable[IntoExpr], reverse: bool | Sequence[bool] = False) -> DataFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="descending",
            new_name="reverse",
            deprecated_in="1.0.0",
            removed_in="2.0",
        )
    )
    def bottom_k(self, k: int, *, by: IntoExpr | Iterable[IntoExpr], reverse: bool | Sequence[bool] = False) -> DataFrame: ...

    def equals(self, other: DataFrame, *, null_equal: bool = True) -> bool: ...

    def slice(self, offset: int, length: int | None = None) -> DataFrame: ...

    def head(self, n: int = 5) -> DataFrame: ...

    def tail(self, n: int = 5) -> DataFrame: ...

    def limit(self, n: int = 5) -> DataFrame: ...

    def drop_nans(self, subset: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None) -> DataFrame: ...

    def drop_nulls(self, subset: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None) -> DataFrame: ...

    def pipe(self, function: Callable[Concatenate[DataFrame, P], T], *args: P.args, **kwargs: P.kwargs) -> T: ...

    def map_columns(self, column_names: str | Sequence[str] | pl.Selector, function: Callable[Concatenate[Series, P], Series], *args: P.args, **kwargs: P.kwargs) -> DataFrame: ...

    def with_row_index(self, name: str = "index", offset: int = 0) -> DataFrame: ...

    def group_by(self, *by: IntoExpr | Iterable[IntoExpr], maintain_order: bool = False, **named_by: IntoExpr) -> GroupBy: ...

    @removed_parameters(
        RenamedParameter(
            name="by", new_name="group_by", deprecated_in="0.20.14", removed_in="2.0"
        )
    )
    def rolling(self, index_column: IntoExpr, *, period: str | timedelta, offset: str | timedelta | None = None, closed: ClosedInterval = "right", group_by: IntoExpr | Iterable[IntoExpr] | None = None) -> RollingGroupBy: ...

    @removed_parameters(
        RenamedParameter(
            name="by", new_name="group_by", deprecated_in="0.20.14", removed_in="2.0"
        )
    )
    def group_by_dynamic(self, index_column: IntoExpr, *, every: str | timedelta, period: str | timedelta | None = None, offset: str | timedelta | None = None, include_boundaries: bool = False, closed: ClosedInterval = "left", label: Label = "left", group_by: IntoExpr | Iterable[IntoExpr] | None = None, start_by: StartBy = "window") -> DynamicGroupBy: ...

    @removed_parameters(
        RenamedParameter(
            name="by", new_name="group_by", deprecated_in="0.20.14", removed_in="2.0"
        )
    )
    def upsample(self, time_column: str, *, every: str | timedelta, group_by: str | Sequence[str] | None = None, maintain_order: bool = False) -> DataFrame: ...

    def join_asof(self, other: DataFrame, *, left_on: str | None | Expr = None, right_on: str | None | Expr = None, on: str | None | Expr = None, by_left: str | Sequence[str] | None = None, by_right: str | Sequence[str] | None = None, by: str | Sequence[str] | None = None, strategy: AsofJoinStrategy = "backward", suffix: str = "_right", tolerance: str | int | float | timedelta | None = None, allow_parallel: bool = True, force_parallel: bool = False, coalesce: bool = True, allow_exact_matches: bool = True, check_sortedness: bool = True) -> DataFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="join_nulls",
            new_name="nulls_equal",
            deprecated_in="1.24",
            removed_in="2.0",
        )
    )
    def join(self, other: DataFrame, on: str | Expr | Sequence[str | Expr] | None = None, how: JoinStrategy = "inner", *, left_on: str | Expr | Sequence[str | Expr] | None = None, right_on: str | Expr | Sequence[str | Expr] | None = None, suffix: str = "_right", validate: JoinValidation = "m:m", nulls_equal: bool = False, coalesce: bool | None = None, maintain_order: MaintainOrderJoin | None = None, build_side: JoinBuildSide = "auto") -> DataFrame: ...

    @unstable()
    def join_where(self, other: DataFrame, *predicates: Expr | Iterable[Expr], how: JoinWhereStrategy = "inner", suffix: str = "_right") -> DataFrame: ...

    @unstable()
    def gather(self, indices: int | Sequence[int] | IntoExpr | Series | np.ndarray[Any, Any], *, null_on_oob: bool = False) -> DataFrame: ...

    def map_rows(self, function: Callable[[tuple[Any, ...]], Any], return_dtype: PolarsDataType | None = None, *, inference_size: int = 256) -> DataFrame: ...

    def hstack(self, columns: list[Series] | DataFrame, *, in_place: bool = False) -> DataFrame: ...

    def vstack(self, other: DataFrame, *, in_place: bool = False) -> DataFrame: ...

    def extend(self, other: DataFrame) -> DataFrame: ...

    def drop(self, *columns: ColumnNameOrSelector | Iterable[ColumnNameOrSelector], strict: bool = True) -> DataFrame: ...

    def drop_in_place(self, name: str) -> Series: ...

    def cast(self, dtypes: (Mapping[
                ColumnNameOrSelector | PolarsDataType, PolarsDataType | PythonDataType
            ]
            | PolarsDataType
            | Schema), *, strict: bool = True) -> DataFrame: ...

    def clear(self, n: int = 0) -> DataFrame: ...

    def clone(self) -> DataFrame: ...

    def get_columns(self) -> list[Series]: ...

    @overload
    def get_column(self, name: str, *, default: Series | NoDefault = ...) -> Series: ...

    @overload
    def get_column(self, name: str, *, default: Any) -> Any: ...

    def fill_null(self, value: Any | Expr | None = None, strategy: FillNullStrategy | None = None, limit: int | None = None, *, matches_supertype: bool = True) -> DataFrame: ...

    def fill_nan(self, value: Expr | int | float | None) -> DataFrame: ...

    def explode(self, columns: ColumnNameOrSelector | Iterable[ColumnNameOrSelector], *more_columns: ColumnNameOrSelector, empty_as_null: bool = False, keep_nulls: bool = True) -> DataFrame: ...

    @removed_parameters(
        RenamedParameter(
            name="columns", new_name="on", deprecated_in="1.0.0", removed_in="2.0"
        )
    )
    def pivot(self, on: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], on_columns: Sequence[Any] | pl.Series | pl.DataFrame | None = None, *, index: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, values: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, aggregate_function: PivotAgg | Expr | None = None, maintain_order: bool = True, sort_columns: bool = False, separator: str = "_", column_naming: Literal["auto", "combine"] = "auto") -> DataFrame: ...

    def unpivot(self, on: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, *, index: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, variable_name: str | None = None, value_name: str | None = None) -> DataFrame: ...

    def unstack(self, *, step: int, how: UnstackDirection = "vertical", columns: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, fill_values: list[Any] | None = None) -> DataFrame: ...

    @overload
    def partition_by(self, by: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *more_by: ColumnNameOrSelector, maintain_order: bool = ..., include_key: bool = ..., as_dict: Literal[False] = ...) -> list[DataFrame]: ...

    @overload
    def partition_by(self, by: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *more_by: ColumnNameOrSelector, maintain_order: bool = ..., include_key: bool = ..., as_dict: Literal[True]) -> dict[tuple[Any, ...], DataFrame]: ...

    @overload
    def partition_by(self, by: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *more_by: ColumnNameOrSelector, maintain_order: bool = ..., include_key: bool = ..., as_dict: bool) -> list[DataFrame] | dict[tuple[Any, ...], DataFrame]: ...

    def shift(self, n: int = 1, *, fill_value: IntoExpr | None = None) -> DataFrame: ...

    @unstable()
    def is_sorted(self, by: str | Iterable[str], *more_by: str, descending: bool | Sequence[bool] = False, nulls_last: bool | Sequence[bool] = False) -> bool: ...

    def is_duplicated(self) -> Series: ...

    def is_unique(self) -> Series: ...

    def lazy(self) -> LazyFrame: ...

    def select(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> DataFrame: ...

    def select_seq(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> DataFrame: ...

    def with_columns(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> DataFrame: ...

    def with_columns_seq(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> DataFrame: ...

    @overload
    def n_chunks(self, strategy: Literal["first"] = ...) -> int: ...

    @overload
    def n_chunks(self, strategy: Literal["all"]) -> list[int]: ...

    def max(self) -> DataFrame: ...

    def max_horizontal(self) -> Series: ...

    def min(self) -> DataFrame: ...

    def min_horizontal(self) -> Series: ...

    def sum(self) -> DataFrame: ...

    def sum_horizontal(self, *, ignore_nulls: bool = True) -> Series: ...

    def mean(self) -> DataFrame: ...

    def mean_horizontal(self, *, ignore_nulls: bool = True) -> Series: ...

    def std(self, ddof: int = 1) -> DataFrame: ...

    def var(self, ddof: int = 1) -> DataFrame: ...

    def median(self) -> DataFrame: ...

    def product(self) -> DataFrame: ...

    def quantile(self, quantile: float, interpolation: QuantileMethod = "nearest") -> DataFrame: ...

    def to_dummies(self, columns: ColumnNameOrSelector | Sequence[ColumnNameOrSelector] | None = None, *, separator: str = "_", drop_first: bool = False, drop_nulls: bool = False) -> DataFrame: ...

    def unique(self, subset: IntoExpr | Collection[IntoExpr] | None = None, *, keep: UniqueKeepStrategy = "any", maintain_order: bool = False) -> DataFrame: ...

    def n_unique(self, subset: IntoExpr | Collection[IntoExpr] | None = None) -> int: ...

    def rechunk(self) -> DataFrame: ...

    def null_count(self) -> DataFrame: ...

    def sample(self, n: int | Series | None = None, *, fraction: float | Series | None = None, with_replacement: bool = False, shuffle: bool | None = None, seed: int | None = None) -> DataFrame: ...

    def fold(self, operation: Callable[[Series, Series], Series]) -> Series: ...

    @overload
    def row(self, index: int | None = ..., *, by_predicate: Expr | None = ..., named: Literal[False] = ...) -> tuple[Any, ...]: ...

    @overload
    def row(self, index: int | None = ..., *, by_predicate: Expr | None = ..., named: Literal[True]) -> dict[str, Any]: ...

    @overload
    def rows(self, *, named: Literal[False] = ...) -> list[tuple[Any, ...]]: ...

    @overload
    def rows(self, *, named: Literal[True]) -> list[dict[str, Any]]: ...

    @overload
    def rows_by_key(self, key: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *, named: Literal[False] = ..., include_key: bool = ..., unique: Literal[False] = ...) -> dict[Any, list[Any]]: ...

    @overload
    def rows_by_key(self, key: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *, named: Literal[False] = ..., include_key: bool = ..., unique: Literal[True]) -> dict[Any, Any]: ...

    @overload
    def rows_by_key(self, key: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *, named: Literal[True], include_key: bool = ..., unique: Literal[False] = ...) -> dict[Any, list[dict[str, Any]]]: ...

    @overload
    def rows_by_key(self, key: ColumnNameOrSelector | Sequence[ColumnNameOrSelector], *, named: Literal[True], include_key: bool = ..., unique: Literal[True]) -> dict[Any, dict[str, Any]]: ...

    @overload
    def iter_rows(self, *, named: Literal[False] = ..., buffer_size: int = ...) -> Iterator[tuple[Any, ...]]: ...

    @overload
    def iter_rows(self, *, named: Literal[True], buffer_size: int = ...) -> Iterator[dict[str, Any]]: ...

    def iter_columns(self) -> Iterator[Series]: ...

    def iter_slices(self, n_rows: int = 10_000) -> Iterator[DataFrame]: ...

    def shrink_to_fit(self, *, in_place: bool = False) -> DataFrame: ...

    def gather_every(self, n: int, offset: int = 0) -> DataFrame: ...

    def hash_rows(self, seed: int = 0) -> Series: ...

    def interpolate(self) -> DataFrame: ...

    def is_empty(self) -> bool: ...

    def to_struct(self, name: str = "") -> Series: ...

    def unnest(self, columns: ColumnNameOrSelector | Collection[ColumnNameOrSelector] | None = None, *more_columns: ColumnNameOrSelector, separator: str | None = None) -> DataFrame: ...

    def corr(self, *, label: str | None = None, **kwargs: Any) -> DataFrame: ...

    def merge_sorted(self, other: DataFrame, key: str | Sequence[str], *, maintain_order: bool = False) -> DataFrame: ...

    def set_sorted(self, column: str, *, descending: bool = False, nulls_last: bool = False) -> DataFrame: ...

    @unstable()
    def update(self, other: DataFrame, on: str | Sequence[str] | None = None, how: Literal["left", "inner", "full"] = "left", *, left_on: str | Sequence[str] | None = None, right_on: str | Sequence[str] | None = None, include_nulls: bool = False, maintain_order: MaintainOrderJoin | None = "left") -> DataFrame: ...

    def count(self) -> DataFrame: ...

    def show(self, limit: int | None = 5, *, ascii_tables: bool | None = None, decimal_separator: str | None = None, thousands_separator: str | bool | None = None, float_precision: int | None = None, fmt_float: FloatFmt | None = None, fmt_str_lengths: int | None = None, fmt_table_cell_list_len: int | None = None, tbl_cell_alignment: Alignment | None = None, tbl_cell_numeric_alignment: Alignment | None = None, tbl_cols: int | None = None, tbl_column_data_type_inline: bool | None = None, tbl_dataframe_shape_below: bool | None = None, tbl_formatting: TableFormatNames | None = None, tbl_hide_column_data_types: bool | None = None, tbl_hide_column_names: bool | None = None, tbl_hide_dtype_separator: bool | None = None, tbl_hide_dataframe_shape: bool | None = None, tbl_width_chars: int | None = None, trim_decimal_zeros: bool | None = True) -> None: ...

    @unstable()
    def match_to_schema(self, schema: SchemaDict | Schema, *, missing_columns: (Literal["insert", "raise"]
        | Mapping[str, Literal["insert", "raise"] | Expr]) = "raise", missing_struct_fields: (Literal["insert", "raise"]
        | Mapping[str, Literal["insert", "raise"]]) = "raise", extra_columns: Literal["ignore", "raise"] = "raise", extra_struct_fields: (Literal["ignore", "raise"]
        | Mapping[str, Literal["ignore", "raise"]]) = "raise", integer_cast: (Literal["upcast", "forbid"]
        | Mapping[str, Literal["upcast", "forbid"]]) = "forbid", float_cast: (Literal["upcast", "forbid"]
        | Mapping[str, Literal["upcast", "forbid"]]) = "forbid") -> DataFrame: ...
