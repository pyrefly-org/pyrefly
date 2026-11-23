from __future__ import annotations
from collections.abc import Callable, Collection, Iterable, Mapping, Sequence
from pathlib import Path
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Literal,
    Protocol,
    TypeVar,
    Union,
)
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from typing import TypeAlias
from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine as AlchemyEngine
from sqlalchemy.ext.asyncio import (
        AsyncConnection,
        AsyncEngine,
        AsyncSession,
        async_sessionmaker,
    )
from sqlalchemy.orm import Session
from xlsxwriter.format import Format
from polars import DataFrame, Expr, LazyFrame, Series
from polars._dependencies import numpy as np
from polars._utils.async_ import _AioDataFrameResult, _GeventDataFrameResult
from polars.datatypes import DataType, DataTypeClass, IntegerType, TemporalType
from polars.lazyframe.engine import Engine
from polars.selectors import Selector


class ArrowArrayExportable(Protocol):
    def __arrow_c_array__(self, requested_schema: object | None = None) -> tuple[object, object]: ...


class ArrowStreamExportable(Protocol):
    def __arrow_c_stream__(self, requested_schema: object | None = None) -> object: ...


PolarsDataType: TypeAlias = Union["DataTypeClass", "DataType"]
PolarsTemporalType: TypeAlias = Union[type["TemporalType"], "TemporalType"]
PolarsIntegerType: TypeAlias = Union[type["IntegerType"], "IntegerType"]
OneOrMoreDataTypes: TypeAlias = PolarsDataType | Iterable[PolarsDataType]
PythonDataType: TypeAlias = (type[int]
    | type[float]
    | type[bool]
    | type[str]
    | type["date"]
    | type["time"]
    | type["datetime"]
    | type["timedelta"]
    | type[list[Any]]
    | type[tuple[Any, ...]]
    | type[bytes]
    | type[object]
    | type["Decimal"]
    | type[None])
SchemaDefinition: TypeAlias = (Mapping[str, PolarsDataType | PythonDataType | None]
    | Sequence[str | tuple[str, PolarsDataType | PythonDataType | None]])
SchemaDict: TypeAlias = Mapping[str, PolarsDataType]
NumericLiteral: TypeAlias = Union[int, float, "Decimal"]
TemporalLiteral: TypeAlias = Union["date", "time", "datetime", "timedelta"]
NonNestedLiteral: TypeAlias = NumericLiteral | TemporalLiteral | str | bool | bytes
PythonLiteral: TypeAlias = Union[NonNestedLiteral, "np.ndarray[Any, Any]", list[Any]]
IntoExprColumn: TypeAlias = Union["Expr", "Series", str]
IntoExpr: TypeAlias = PythonLiteral | IntoExprColumn | None
ComparisonOperator: TypeAlias = Literal["eq", "neq", "gt", "lt", "gt_eq", "lt_eq"]
Alignment: TypeAlias = Literal["left", "center", "right", "LEFT", "CENTER", "RIGHT"]
SelectorType: TypeAlias = "Selector"
ColumnNameOrSelector: TypeAlias = Union["str", SelectorType]
Ambiguous: TypeAlias = Literal["earliest", "latest", "raise", "null"]
AvroCompression: TypeAlias = Literal["uncompressed", "snappy", "deflate"]
CsvQuoteStyle: TypeAlias = Literal["necessary", "always", "non_numeric", "never"]
CategoricalOrdering: TypeAlias = Literal["physical", "lexical"]
CsvEncoding: TypeAlias = Literal["utf8", "utf8-lossy"]
FillNullStrategy: TypeAlias = (Literal[
    "forward", "backward", "min", "max", "mean", "zero", "one"
])
FloatFmt: TypeAlias = Literal["full", "mixed"]
IndexOrder: TypeAlias = Literal["c", "fortran"]
IpcCompression: TypeAlias = Literal["uncompressed", "lz4", "zstd"]
JoinValidation: TypeAlias = Literal["m:m", "m:1", "1:m", "1:1"]
Label: TypeAlias = Literal["left", "right", "datapoint"]
MaintainOrderJoin: TypeAlias = (Literal[
    "none", "left", "right", "left_right", "right_left"
])
NdjsonCompression: TypeAlias = Literal["uncompressed", "gzip", "zstd"]
NonExistent: TypeAlias = Literal["raise", "null"]
NullBehavior: TypeAlias = Literal["ignore", "drop"]
ParallelStrategy: TypeAlias = (Literal[
    "auto", "columns", "row_groups", "prefiltered", "none"
])
ParquetCompression: TypeAlias = (Literal[
    "lz4", "uncompressed", "snappy", "gzip", "brotli", "zstd"
])
PivotAgg: TypeAlias = (Literal[
    "min", "max", "first", "last", "sum", "mean", "median", "len", "item"
])
QuantileMethod: TypeAlias = (Literal[
    "nearest", "higher", "lower", "midpoint", "linear", "equiprobable"
])
ApproxQuantileMethod: TypeAlias = Literal["auto", "kll", "req_lo", "req_hi", "req_both"]
ApproxQuantileErrorBound: TypeAlias = Literal["empirical", "formal"]
RankMethod: TypeAlias = Literal["average", "min", "max", "dense", "ordinal", "random"]
Roll: TypeAlias = Literal["raise", "forward", "backward"]
SerializationFormat: TypeAlias = Literal["binary", "json"]
Endianness: TypeAlias = Literal["little", "big"]
SizeUnit: TypeAlias = (Literal[
    "b",
    "kb",
    "mb",
    "gb",
    "tb",
    "bytes",
    "kilobytes",
    "megabytes",
    "gigabytes",
    "terabytes",
])
StartBy: TypeAlias = (Literal[
    "window",
    "datapoint",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
])
SyncOnCloseMethod: TypeAlias = Literal["data", "all"]
TimeUnit: TypeAlias = Literal["ns", "us", "ms"]
UnicodeForm: TypeAlias = Literal["NFC", "NFKC", "NFD", "NFKD"]
UniqueKeepStrategy: TypeAlias = Literal["first", "last", "any", "none"]
UnstackDirection: TypeAlias = Literal["vertical", "horizontal"]
MapElementsStrategy: TypeAlias = Literal["thread_local", "threading"]
AsofJoinStrategy: TypeAlias = Literal["backward", "forward", "nearest"]
ClosedInterval: TypeAlias = Literal["left", "right", "both", "none"]
InterpolationMethod: TypeAlias = Literal["linear", "nearest"]
JoinStrategy: TypeAlias = (Literal[
    "inner", "left", "right", "full", "semi", "anti", "cross"
])
JoinWhereStrategy: TypeAlias = Literal["inner", "left", "right", "full"]

ConcatMethod = Literal[
    "vertical",
    "vertical_relaxed",
    "diagonal",
    "diagonal_relaxed",
    "horizontal",
    "horizontal_extend",
    "align",
    "align_full",
    "align_inner",
    "align_left",
    "align_right",
]

CorrelationMethod: TypeAlias = Literal["pearson", "spearman"]
DbReadEngine: TypeAlias = Literal["adbc", "connectorx"]
DbWriteEngine: TypeAlias = Literal["sqlalchemy", "adbc"]
DbWriteMode: TypeAlias = Literal["replace", "append", "fail"]

EpochTimeUnit = Literal["ns", "us", "ms", "s", "d"]

JaxExportType: TypeAlias = Literal["array", "dict"]
Orientation: TypeAlias = Literal["col", "row"]
SearchSortedSide: TypeAlias = Literal["any", "left", "right"]
TorchExportType: TypeAlias = Literal["tensor", "dataset", "dict"]
TransferEncoding: TypeAlias = Literal["hex", "base64"]
WindowMappingStrategy: TypeAlias = Literal["group_to_rows", "join", "explode"]
ExplainFormat: TypeAlias = Literal["plain", "tree"]
FrameInitTypes: TypeAlias = (Union[
    Mapping[str, ArrayLike | NonNestedLiteral | None],
    Iterable[Any],
    NumpyArray,
    PyArrowTable,
    PandasDataFrame,
    "ArrowArrayExportable",
    "ArrowStreamExportable",
    TorchTensor,
    "DataFrame",
])
ColumnFormatDict: TypeAlias = (Mapping[
    # dict of colname(s) or selector(s) to format string or dict
    ColumnNameOrSelector | tuple[ColumnNameOrSelector, ...],
    Union[str, Mapping[str, str], "Format"],
])
ConditionalFormatDict: TypeAlias = (Mapping[
    # dict of colname(s) to str, dict, or sequence of str/dict
    ColumnNameOrSelector | Collection[str],
    str | Mapping[str, Any] | Sequence[str | Mapping[str, Any]],
])
ColumnTotalsDefinition: TypeAlias = (Mapping[ColumnNameOrSelector | tuple[ColumnNameOrSelector], str]
    | Sequence[str]
    | bool)
ColumnWidthsDefinition: TypeAlias = Mapping[ColumnNameOrSelector, tuple[str, ...] | int] | int
RowTotalsDefinition: TypeAlias = Mapping[str, str | Collection[str]] | Collection[str] | bool
ParametricProfileNames: TypeAlias = Literal["fast", "balanced", "expensive"]

PolarsType = TypeVar("PolarsType", "DataFrame", "LazyFrame", "Series", "Expr")

FrameType = TypeVar("FrameType", "DataFrame", "LazyFrame")

ExcelSpreadsheetEngine: TypeAlias = Literal["calamine", "openpyxl", "xlsx2csv"]


class Cursor(BasicCursor):
    def fetchall(self, *args: Any, **kwargs: Any) -> Any: ...

    def fetchmany(self, *args: Any, **kwargs: Any) -> Any: ...


ConnectionOrCursor: TypeAlias = BasicConnection | BasicCursor | Cursor | AlchemyConnection | AlchemyAsyncConnection
SingleIndexSelector: TypeAlias = int
MultiIndexSelector: TypeAlias = (Union[
    slice,
    range,
    Sequence[int],
    "Series",
    "np.ndarray[Any, Any]",
])
SingleNameSelector: TypeAlias = str
MultiNameSelector: TypeAlias = (Union[
    slice,
    Sequence[str],
    "Series",
    "np.ndarray[Any, Any]",
])
BooleanMask: TypeAlias = (Union[
    Sequence[bool],
    "Series",
    "np.ndarray[Any, Any]",
])
SingleColSelector: TypeAlias = SingleIndexSelector | SingleNameSelector
MultiColSelector: TypeAlias = MultiIndexSelector | MultiNameSelector | BooleanMask
EngineTypeName: TypeAlias = Literal["auto", "in-memory", "streaming", "gpu"]
EngineType: TypeAlias = Union[EngineTypeName, "Engine"]
ScalingMode: TypeAlias = Literal["auto", "single-node", "distributed"]
PlanTypePreference: TypeAlias = Literal["dot", "plain"]
FileSource: TypeAlias = (str
    | Path
    | IO[bytes]
    | bytes
    | list[str]
    | list[Path]
    | list[IO[bytes]]
    | list[bytes])

JSONEncoder = Callable[[Any], bytes] | Callable[[Any], str]

DeprecationType: TypeAlias = (Literal[
    "function",
    "renamed_parameter",
    "nonkeyword_arguments",
    "parameter_as_multi_positional",
])
__all__ = ([
    "Alignment",
    "Ambiguous",
    "ApproxQuantileErrorBound",
    "ApproxQuantileMethod",
    "ArrowArrayExportable",
    "ArrowStreamExportable",
    "AsofJoinStrategy",
    "AvroCompression",
    "BooleanMask",
    "CategoricalOrdering",
    "ClosedInterval",
    "ColumnFormatDict",
    "ColumnNameOrSelector",
    "ColumnTotalsDefinition",
    "ColumnWidthsDefinition",
    "ComparisonOperator",
    "ConcatMethod",
    "ConditionalFormatDict",
    "ConnectionOrCursor",
    "CorrelationMethod",
    "CsvEncoding",
    "CsvQuoteStyle",
    "Cursor",
    "DbReadEngine",
    "DbWriteEngine",
    "DbWriteMode",
    "DeprecationType",
    "Endianness",
    "EngineType",
    "EngineTypeName",
    "EpochTimeUnit",
    "ExcelSpreadsheetEngine",
    "ExplainFormat",
    "FileSource",
    "FillNullStrategy",
    "FloatFmt",
    "FrameInitTypes",
    "FrameType",
    "IndexOrder",
    "InterpolationMethod",
    "IntoExpr",
    "IntoExprColumn",
    "IpcCompression",
    "JSONEncoder",
    "JaxExportType",
    "JoinStrategy",
    "JoinValidation",
    "JoinWhereStrategy",
    "Label",
    "MaintainOrderJoin",
    "MapElementsStrategy",
    "MultiColSelector",
    "MultiIndexSelector",
    "MultiNameSelector",
    "NdjsonCompression",
    "NonExistent",
    "NonNestedLiteral",
    "NullBehavior",
    "NumericLiteral",
    "OneOrMoreDataTypes",
    "Orientation",
    "ParallelStrategy",
    "ParametricProfileNames",
    "ParquetCompression",
    "PivotAgg",
    "PlanTypePreference",
    "PolarsDataType",
    "PolarsIntegerType",
    "PolarsTemporalType",
    "PolarsType",
    "PythonDataType",
    "PythonLiteral",
    "QuantileMethod",
    "RankMethod",
    "Roll",
    "RowTotalsDefinition",
    "ScalingMode",
    "SchemaDefinition",
    "SchemaDict",
    "SearchSortedSide",
    "SelectorType",
    "SerializationFormat",
    "SingleColSelector",
    "SingleIndexSelector",
    "SingleNameSelector",
    "SizeUnit",
    "StartBy",
    "SyncOnCloseMethod",
    "TemporalLiteral",
    "TimeUnit",
    "TorchExportType",
    "TransferEncoding",
    "UnicodeForm",
    "UniqueKeepStrategy",
    "UnstackDirection",
    "WindowMappingStrategy",
])
