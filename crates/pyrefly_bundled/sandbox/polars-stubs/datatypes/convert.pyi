from __future__ import annotations
import contextlib
import functools
import re
from collections.abc import Collection
from datetime import date, datetime, time, timedelta
from decimal import Decimal as PyDecimal
from typing import TYPE_CHECKING, Any
from polars._dependencies import numpy as np
from polars._dependencies import pyarrow as pa
from polars.datatypes.classes import (
    Array,
    Binary,
    Boolean,
    Categorical,
    DataType,
    DataTypeClass,
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
    Unknown,
)
from typing import Final, TypeGuard
from polars._typing import PolarsDataType, PythonDataType, TimeUnit


def is_polars_dtype(dtype: Any, *, include_unknown: bool = False, require_instantiated: bool = False) -> TypeGuard[PolarsDataType]: ...


def unpack_dtypes(*dtypes: PolarsDataType | None, include_compound: bool = False) -> set[PolarsDataType]: ...


DataTypeMappings: Final[_DataTypeMappings]


def dtype_to_ffiname(dtype: PolarsDataType) -> str: ...


def dtype_to_py_type(dtype: PolarsDataType) -> PythonDataType: ...


def py_type_to_arrow_type(dtype: PythonDataType) -> pa.DataType: ...


def dtype_short_repr_to_dtype(dtype_string: str | None) -> PolarsDataType | None: ...


def supported_numpy_char_code(dtype_char: str) -> bool: ...


def numpy_char_code_to_dtype(dtype_char: str) -> PolarsDataType: ...


def maybe_cast(el: Any, dtype: PolarsDataType) -> Any: ...
