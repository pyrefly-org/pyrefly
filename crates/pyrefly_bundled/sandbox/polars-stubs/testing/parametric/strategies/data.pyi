from __future__ import annotations
import decimal
from collections.abc import Mapping
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any, Literal, cast
from zoneinfo import ZoneInfo
import hypothesis.strategies as st
from hypothesis.errors import InvalidArgument
from polars._utils.constants import (
    EPOCH,
    I8_MAX,
    I8_MIN,
    I16_MAX,
    I16_MIN,
    I32_MAX,
    I32_MIN,
    I64_MAX,
    I64_MIN,
    I128_MAX,
    I128_MIN,
    U8_MAX,
    U16_MAX,
    U32_MAX,
    U64_MAX,
    U128_MAX,
)
from polars.datatypes import (
    Array,
    BaseExtension,
    Binary,
    Boolean,
    Categorical,
    Date,
    Datetime,
    Decimal,
    Duration,
    Enum,
    Field,
    Float16,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    Int128,
    List,
    Map,
    Null,
    Object,
    String,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt128,
)
from polars.testing.parametric.strategies._utils import flexhash
from polars.testing.parametric.strategies.dtype import (
    _DEFAULT_ARRAY_WIDTH_LIMIT,
    _DEFAULT_ENUM_CATEGORIES_LIMIT,
    _DEFAULT_MAP_SIZE_LIMIT,
)
from collections.abc import Sequence
from datetime import date, time
from hypothesis.strategies import SearchStrategy
from polars._typing import PolarsDataType, SchemaDict, TimeUnit
from polars.datatypes import DataType, DataTypeClass, FloatType


def integers(bit_width: Literal[8, 16, 32, 64, 128] = 64, *, signed: bool = True) -> SearchStrategy[int]: ...


def floats(bit_width: Literal[16, 32, 64] = 64, *, allow_nan: bool = True, allow_infinity: bool = True) -> SearchStrategy[float]: ...


def booleans() -> SearchStrategy[bool]: ...


def strings() -> SearchStrategy[str]: ...


def binary() -> SearchStrategy[bytes]: ...


def categories(n_categories: int = ...) -> SearchStrategy[str]: ...


def times() -> SearchStrategy[time]: ...


def dates() -> SearchStrategy[date]: ...


def datetimes(time_unit: TimeUnit = "us", time_zone: str | None = None) -> SearchStrategy[datetime]: ...


def durations(time_unit: TimeUnit = "us") -> SearchStrategy[timedelta]: ...


def decimals(precision: int | None = 38, scale: int = 0) -> SearchStrategy[decimal.Decimal]: ...


def lists(inner_dtype: DataType, *, select_from: Sequence[Any] | None = None, min_size: int = 0, max_size: int | None = None, unique: bool = False, **kwargs: Any) -> SearchStrategy[list[Any]]: ...


def structs(fields: Sequence[Field] | SchemaDict, *, allow_null: bool = True, **kwargs: Any) -> SearchStrategy[dict[str, Any]]: ...


def maps(key: PolarsDataType, value: PolarsDataType, *, min_size: int = 0, max_size: int | None = None, allow_null: bool = True, **kwargs: Any) -> SearchStrategy[dict[Any, Any]]: ...


def nulls() -> SearchStrategy[None]: ...


def objects() -> SearchStrategy[object]: ...


def data(dtype: PolarsDataType, *, allow_null: bool = False, **kwargs: Any) -> SearchStrategy[Any]: ...
