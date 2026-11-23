from __future__ import annotations
from inspect import isfunction
from typing import TYPE_CHECKING, Generic, TypeVar
from warnings import warn
import polars._reexport as pl
from polars._warnings import find_stacklevel
from collections.abc import Callable
from polars import DataFrame, Expr, LazyFrame, Series

__all__ = ([
    "register_dataframe_namespace",
    "register_expr_namespace",
    "register_lazyframe_namespace",
    "register_series_namespace",
])


def register_expr_namespace(name: str) -> Callable[[type[NS]], type[NS]]: ...


def register_dataframe_namespace(name: str) -> Callable[[type[NS]], type[NS]]: ...


def register_lazyframe_namespace(name: str) -> Callable[[type[NS]], type[NS]]: ...


def register_series_namespace(name: str) -> Callable[[type[NS]], type[NS]]: ...
