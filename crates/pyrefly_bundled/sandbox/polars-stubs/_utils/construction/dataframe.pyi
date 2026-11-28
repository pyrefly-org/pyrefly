from __future__ import annotations
import contextlib
from collections.abc import Generator, Mapping, Sequence
from datetime import date, datetime, time, timedelta
from functools import singledispatch
from itertools import islice, zip_longest
from operator import attrgetter, itemgetter
from typing import (
    TYPE_CHECKING,
    Any,
    cast,
)
import polars._reexport as pl
import polars._utils.construction as plc
from polars import functions as F
from polars._dependencies import (
    _NUMPY_AVAILABLE,
    _PYARROW_AVAILABLE,
    _check_for_numpy,
    _check_for_pandas,
)
from polars._dependencies import numpy as np
from polars._dependencies import pandas as pd
from polars._dependencies import pyarrow as pa
from polars._utils.construction.utils import (
    contains_nested,
    get_first_non_none,
    is_dataclass_instance,
    is_namedtuple,
    is_pydantic_model,
    is_simple_numpy_backed_pandas_series,
    is_sqlalchemy_row,
    nt_unpack,
    try_get_type_hints,
)
from polars._utils.various import (
    _is_generator,
    arrlen,
    parse_version,
)
from polars._warnings import issue_warning
from polars.datatypes import (
    N_INFER_DEFAULT,
    Categorical,
    Duration,
    Enum,
    Object,
    String,
    Struct,
    Unknown,
    is_polars_dtype,
    parse_into_dtype,
    try_parse_into_dtype,
)
from polars.exceptions import DataOrientationWarning, ShapeError
from polars.meta import thread_pool_size
from collections.abc import Callable, Iterable, MutableMapping
from polars import DataFrame, Series
from polars._plr import PySeries
from polars._typing import (
        ArrayLike,
        NonNestedLiteral,
        Orientation,
        PolarsDataType,
        SchemaDefinition,
        SchemaDict,
    )


def dict_to_pydf(data: Mapping[str, ArrayLike | NonNestedLiteral | None], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, nan_to_null: bool = False, allow_multithreaded: bool = True) -> PyDataFrame: ...


def sequence_to_pydf(data: Sequence[Any], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, orient: Orientation | None = None, infer_schema_length: int | None = ..., nan_to_null: bool = False) -> PyDataFrame: ...


def iterable_to_pydf(data: Iterable[Any], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, orient: Orientation | None = None, chunk_size: int | None = None, infer_schema_length: int | None = ..., rechunk: bool = True) -> PyDataFrame: ...


def pandas_to_pydf(data: pd.DataFrame, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, rechunk: bool = True, nan_to_null: bool = True, include_index: bool = False) -> PyDataFrame: ...


def arrow_to_pydf(data: pa.Table | pa.RecordBatch, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, rechunk: bool = True) -> PyDataFrame: ...


def numpy_to_pydf(data: np.ndarray[Any, Any], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, orient: Orientation | None = None, strict: bool = True, nan_to_null: bool = False) -> PyDataFrame: ...


def series_to_pydf(data: Series, schema: SchemaDefinition | None = None, schema_overrides: SchemaDict | None = None, *, strict: bool = True) -> PyDataFrame: ...


def dataframe_to_pydf(data: DataFrame, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True) -> PyDataFrame: ...
