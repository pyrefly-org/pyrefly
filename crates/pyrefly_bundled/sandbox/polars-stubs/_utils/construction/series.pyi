from __future__ import annotations
import contextlib
from collections.abc import Generator, Iterator, Mapping
from datetime import date, datetime, time, timedelta
from enum import Enum as PyEnum
from itertools import islice
from typing import (
    TYPE_CHECKING,
    Any,
)
import polars._reexport as pl
import polars._utils.construction as plc
from polars._dependencies import _PYARROW_AVAILABLE, _check_for_numpy
from polars._dependencies import numpy as np
from polars._dependencies import pyarrow as pa
from polars._utils.construction.dataframe import _sequence_of_dict_to_pydf
from polars._utils.construction.utils import (
    get_first_non_none,
    is_dataclass_instance,
    is_namedtuple,
    is_pydantic_model,
    is_simple_numpy_backed_pandas_series,
    is_sqlalchemy_row,
)
from polars._utils.various import (
    range_to_series,
)
from polars._utils.wrap import wrap_s
from polars.datatypes import (
    Array,
    BaseExtension,
    Boolean,
    Categorical,
    Date,
    Datetime,
    Decimal,
    Duration,
    Enum,
    List,
    Map,
    Null,
    Object,
    String,
    Struct,
    Time,
    Unknown,
    dtype_to_py_type,
    is_polars_dtype,
    numpy_char_code_to_dtype,
    parse_into_dtype,
    try_parse_into_dtype,
)
from polars.datatypes.constructor import (
    numpy_type_to_constructor,
    numpy_values_and_dtype,
    polars_type_to_constructor,
    py_type_to_constructor,
)
from collections.abc import Callable, Iterable, Sequence
from polars import DataFrame, Series
from polars._dependencies import pandas as pd
from polars._typing import PolarsDataType


def sequence_to_pyseries(name: str, values: Sequence[Any], dtype: PolarsDataType | None = None, *, strict: bool = True, nan_to_null: bool = False) -> PySeries: ...


def iterable_to_pyseries(name: str, values: Iterable[Any], dtype: PolarsDataType | None = None, *, chunk_size: int = 1_000_000, strict: bool = True) -> PySeries: ...


def pandas_to_pyseries(name: str, values: pd.Series[Any] | pd.Index[Any] | pd.DatetimeIndex, dtype: PolarsDataType | None = None, *, strict: bool = True, nan_to_null: bool = True) -> PySeries: ...


def arrow_to_pyseries(name: str, values: pa.Array, dtype: PolarsDataType | None = None, *, strict: bool = True, rechunk: bool = True) -> PySeries: ...


def numpy_to_pyseries(name: str, values: np.ndarray[Any, Any], *, strict: bool = True, nan_to_null: bool = False) -> PySeries: ...


def series_to_pyseries(name: str | None, values: Series, *, dtype: PolarsDataType | None = None, strict: bool = True) -> PySeries: ...


def dataframe_to_pyseries(name: str | None, values: DataFrame, *, dtype: PolarsDataType | None = None, strict: bool = True) -> PySeries: ...
