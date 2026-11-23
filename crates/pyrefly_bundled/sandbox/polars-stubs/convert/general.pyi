from __future__ import annotations
import io
import itertools
import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING, Any, Literal, overload
import polars._reexport as pl
from polars import functions as F
from polars._dependencies import _check_for_pyarrow
from polars._dependencies import pandas as pd
from polars._dependencies import pyarrow as pa
from polars._utils.construction.dataframe import (
    arrow_to_pydf,
    dict_to_pydf,
    numpy_to_pydf,
    pandas_to_pydf,
    sequence_to_pydf,
)
from polars._utils.construction.series import arrow_to_pyseries, pandas_to_pyseries
from polars._utils.expired import (
    RemovedParameter,
    RenamedParameter,
    removed_parameters,
)
from polars._utils.pycapsule import is_pycapsule, pycapsule_to_frame
from polars._utils.various import (
    _cast_repr_strings_with_schema,
    qualified_type_name,
)
from polars._utils.wrap import wrap_df, wrap_s
from polars.datatypes import N_INFER_DEFAULT, Categorical, String
from polars.exceptions import NoDataError
from collections.abc import Mapping
from polars import DataFrame, Series
from polars._dependencies import numpy as np
from polars._dependencies import torch
from polars._typing import (
        ArrowArrayExportable,
        ArrowStreamExportable,
        Orientation,
        PolarsDataType,
        SchemaDefinition,
        SchemaDict,
    )


def from_dict(data: Mapping[str, Sequence[object] | Mapping[str, Sequence[object]] | Series], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True) -> DataFrame: ...


def from_dicts(data: Iterable[Mapping[str, Any]], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, infer_schema_length: int | None = ...) -> DataFrame: ...


def from_records(data: Sequence[Any], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, strict: bool = True, orient: Orientation | None = None, infer_schema_length: int | None = ...) -> DataFrame: ...


def from_numpy(data: np.ndarray[Any, Any], schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, orient: Orientation | None = None) -> DataFrame: ...


def from_torch(tensor: torch.Tensor, schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, orient: Orientation | None = None, force: bool = False) -> DataFrame: ...


def from_arrow(data: (pa.Table
        | pa.Array
        | pa.ChunkedArray
        | pa.RecordBatch
        | Iterable[pa.RecordBatch | pa.Table]
        | ArrowArrayExportable
        | ArrowStreamExportable), schema: SchemaDefinition | None = None, *, schema_overrides: SchemaDict | None = None, rechunk: bool = False) -> DataFrame | Series: ...


@overload
def from_pandas(data: pd.DataFrame, *, schema_overrides: SchemaDict | None = ..., rechunk: bool = ..., nan_to_null: bool = ..., include_index: bool = ...) -> DataFrame: ...


@overload
def from_pandas(data: pd.Series[Any] | pd.Index[Any] | pd.DatetimeIndex, *, schema_overrides: SchemaDict | None = ..., rechunk: bool = ..., nan_to_null: bool = ..., include_index: Literal[False] = ...) -> Series: ...


@overload
def from_pandas(data: pd.Series[Any], *, schema_overrides: SchemaDict | None = ..., rechunk: bool = ..., nan_to_null: bool = ..., include_index: Literal[True]) -> DataFrame: ...


class TableRepr(Enum):
    UTF8 = ...
    ASCII = ...

    @property
    def patterns(self) -> _TablePatterns: ...


@removed_parameters(
    RenamedParameter(
        name="tbl",
        new_name="data",
        deprecated_in="0.20.17",
        removed_in="2.0",
    ),
)
def from_repr(data: str) -> DataFrame | Series: ...


@removed_parameters(
    RemovedParameter(name="allow_copy", deprecated_in="1.23.0", removed_in="2.0.0")
)
def from_dataframe(df: ArrowArrayExportable | ArrowStreamExportable, *, rechunk: bool = True) -> DataFrame: ...
