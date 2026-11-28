from _typeshed import Incomplete

from __future__ import annotations
from collections.abc import Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, overload
import hypothesis.strategies as st
from polars import select, when
from polars._utils.expired import RemovedParameter, removed_parameters
from polars.dataframe import DataFrame
from polars.datatypes import Array, Boolean, DataType, DataTypeClass, List, Null, Struct
from polars.series import Series
from polars.testing.parametric.strategies._utils import flexhash
from polars.testing.parametric.strategies.data import data
from polars.testing.parametric.strategies.dtype import _instantiate_dtype, dtypes
from collections.abc import Collection, Sequence
from typing import Literal
from hypothesis.strategies import DrawFn, SearchStrategy
from polars import LazyFrame
from polars._typing import PolarsDataType


@removed_parameters(
    RemovedParameter(
        name="null_probability",
        deprecated_in="0.20.26",
        removed_in="1.0.0",
        hint="Use `allow_null` instead.",
    ),
    RemovedParameter(
        name="allow_infinities",
        deprecated_in="0.20.26",
        removed_in="1.0.0",
        hint="Use `allow_infinity` instead.",
    ),
    RemovedParameter(
        name="size",
        deprecated_in="1.0.0",
        removed_in="2.0.0",
        hint="Use `min_size` and `max_size` instead.",
    ),
)
@st.composite
def series(draw: DrawFn, /, *, name: str | SearchStrategy[str] | None = None, dtype: PolarsDataType | None = None, min_size: int = 0, max_size: int = ..., strategy: SearchStrategy[Any] | None = None, allow_null: bool = True, allow_chunks: bool = True, allow_masked_out: bool = True, unique: bool = False, allowed_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, excluded_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, allow_time_zones: bool = True, **kwargs: Any) -> Series: ...


@overload
def dataframes(cols: int | column | Sequence[column] | None = None, *, lazy: Literal[False] = ..., min_cols: int = 0, max_cols: int = ..., min_size: int = 0, max_size: int = ..., include_cols: Sequence[column] | column | None = None, allow_null: bool | Mapping[str, bool] = True, allow_chunks: bool = True, allow_masked_out: bool = True, allowed_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, excluded_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, allow_time_zones: bool = True, **kwargs: Any) -> SearchStrategy[DataFrame]: ...


@overload
def dataframes(cols: int | column | Sequence[column] | None = None, *, lazy: Literal[True], min_cols: int = 0, max_cols: int = ..., min_size: int = 0, max_size: int = ..., include_cols: Sequence[column] | column | None = None, allow_null: bool | Mapping[str, bool] = True, allow_chunks: bool = True, allow_masked_out: bool = True, allowed_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, excluded_dtypes: Collection[PolarsDataType] | PolarsDataType | None = None, allow_time_zones: bool = True, **kwargs: Any) -> SearchStrategy[LazyFrame]: ...


@dataclass
class column:
    name: str | None = None
    dtype: PolarsDataType | None = None
    strategy: SearchStrategy[Any] | None = None
    allow_null: bool | None = None
    unique: bool = False

    def __init__(self, name: str | None = ..., dtype: DataType | DataTypeClass | None = ..., strategy: Incomplete = ..., allow_null: bool | None = ..., unique: bool = ...) -> None: ...
