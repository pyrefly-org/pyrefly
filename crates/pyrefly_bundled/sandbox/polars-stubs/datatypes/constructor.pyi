from __future__ import annotations
import functools
from decimal import Decimal as PyDecimal
from typing import TYPE_CHECKING, Any
from polars import datatypes as dt
from polars._dependencies import numpy as np
from collections.abc import Callable, Sequence
from polars._typing import PolarsDataType
from polars._plr import PySeries


def polars_type_to_constructor(dtype: PolarsDataType) -> Callable[[str, Sequence[Any], bool], PySeries]: ...


def numpy_values_and_dtype(values: np.ndarray[Any, Any]) -> tuple[np.ndarray[Any, Any], type]: ...


def numpy_type_to_constructor(values: np.ndarray[Any, Any], dtype: type[np.dtype[Any]]) -> Callable[..., PySeries]: ...


def py_type_to_constructor(py_type: type[Any]) -> Callable[..., PySeries]: ...
