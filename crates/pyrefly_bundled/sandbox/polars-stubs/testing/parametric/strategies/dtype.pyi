from __future__ import annotations
from typing import TYPE_CHECKING
import hypothesis.strategies as st
from hypothesis.errors import InvalidArgument
from polars import register_extension_type
from polars.datatypes import (
    Array,
    Binary,
    Boolean,
    Categorical,
    DataType,
    Date,
    Datetime,
    Decimal,
    Duration,
    Enum,
    Extension,
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
    String,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt128,
)
from collections.abc import Collection, Sequence
from typing import Final
from hypothesis.strategies import DrawFn, SearchStrategy
from polars._typing import PolarsDataType, TimeUnit
from polars.datatypes import DataTypeClass

TestExtension: Final[Extension]


def dtypes(*, allowed_dtypes: Collection[PolarsDataType] | None = None, excluded_dtypes: Sequence[PolarsDataType] | None = None, allow_time_zones: bool = True, nesting_level: int = 3) -> SearchStrategy[DataType]: ...
