from __future__ import annotations
import enum
import functools
import re
from datetime import date, datetime, time, timedelta
from decimal import Decimal as PyDecimal
from types import NoneType, UnionType
from typing import (
    TYPE_CHECKING,
    Any,
    Final,
    ForwardRef,
    NoReturn,
    Union,
    get_args,
    get_origin,
)
import polars._reexport as pl
from polars.datatypes.classes import (
    Binary,
    Boolean,
    Date,
    Datetime,
    Decimal,
    Duration,
    Enum,
    Float64,
    Int64,
    List,
    Null,
    Object,
    String,
    Time,
    Unknown,
)
from polars.datatypes.convert import is_polars_dtype
from polars._typing import PolarsDataType, PythonDataType, SchemaDict


def parse_into_datatype_expr(input: Any) -> pl.DataTypeExpr: ...


def parse_into_dtype(input: Any) -> PolarsDataType: ...


def try_parse_into_dtype(input: Any) -> PolarsDataType | None: ...


@functools.lru_cache(16)
def parse_py_type_into_dtype(input: PythonDataType | type[object]) -> PolarsDataType: ...


PY_TYPE_STR_TO_DTYPE: Final[SchemaDict]
