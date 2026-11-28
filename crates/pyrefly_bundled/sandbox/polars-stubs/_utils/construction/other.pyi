from __future__ import annotations
from typing import TYPE_CHECKING, Any
from polars._dependencies import pyarrow as pa
from polars._utils.construction.utils import get_first_non_none
from polars._dependencies import pandas as pd


def pandas_series_to_arrow(values: pd.Series[Any] | pd.Index[Any], *, length: int | None = None, nan_to_null: bool = True) -> pa.Array: ...


def coerce_arrow(array: pa.Array) -> pa.Array: ...
