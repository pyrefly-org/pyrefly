from __future__ import annotations
import functools
import re
from contextlib import suppress
from inspect import isclass
from typing import TYPE_CHECKING, Any
from polars.datatypes import (
    Binary,
    Boolean,
    Date,
    Datetime,
    Decimal,
    Duration,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    Int128,
    List,
    Null,
    String,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
)
from polars.datatypes._parse import parse_py_type_into_dtype
from polars.datatypes.group import (
    INTEGER_DTYPES,
    UNSIGNED_INTEGER_DTYPES,
)
from polars._typing import PolarsDataType


def dtype_from_database_typename(value: str, *, raise_unmatched: bool = True) -> PolarsDataType | None: ...


def dtype_from_cursor_description(description: tuple[Any, ...]) -> PolarsDataType | None: ...


@functools.lru_cache(8)
def integer_dtype_from_nbits(bits: int, *, unsigned: bool, default: PolarsDataType | None = None) -> PolarsDataType | None: ...


def timeunit_from_precision(precision: int | str | None) -> str | None: ...
