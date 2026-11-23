from __future__ import annotations
import inspect
import sys
from functools import wraps
from typing import TYPE_CHECKING, Any, TypeVar, cast
import polars._reexport as pl
from polars import functions as F
from polars._utils.expired import removed_parameters
from polars._utils.wrap import wrap_s
from polars.datatypes import dtype_to_ffiname
from polars.exceptions import AttributeRemovedError
from collections.abc import Callable
from typing import ParamSpec
from polars import Series
from polars._plr import PySeries
from polars._typing import PolarsDataType

T = TypeVar("T")

P = ParamSpec("P")

SeriesMethod = Callable[..., Series]


def expr_dispatch(cls: type[T]) -> type[T]: ...


def call_expr(func: SeriesMethod) -> SeriesMethod: ...


def get_ffi_func(name: str, dtype: PolarsDataType, obj: PySeries) -> Callable[..., Any] | None: ...
