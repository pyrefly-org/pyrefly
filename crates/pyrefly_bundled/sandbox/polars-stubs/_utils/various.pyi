from typing import Literal

from __future__ import annotations
import inspect
import os
import re
import sys
import warnings
from collections import Counter
from collections.abc import (
    Collection,
    Generator,
    Iterable,
    MappingView,
    Sequence,
    Sized,
)
from enum import Enum
from io import BytesIO
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    NoReturn,
    TypeVar,
    overload,
)
import polars as pl
from polars import functions as F
from polars._dependencies import _check_for_numpy, import_optional, subprocess
from polars._dependencies import numpy as np
from polars._warnings import find_stacklevel
from polars.datatypes import (
    Boolean,
    Date,
    Datetime,
    Decimal,
    Duration,
    Int64,
    String,
    Time,
)
from polars.datatypes.group import FLOAT_DTYPES, INTEGER_DTYPES
from collections.abc import (
        Callable,
        Iterator,
        MutableMapping,
        Reversible,
    )
from typing import ParamSpec, Protocol, TypeGuard
from polars import DataFrame, Expr
from polars._typing import PolarsDataType, SizeUnit

P = ParamSpec("P")

T = TypeVar("T")


class IdentityFunction(Protocol):
    def __call__(self, fn: Callable[P, T], /) -> Callable[P, T]: ...


def is_path_or_str_sequence(val: object, *, allow_str: bool = False, include_series: bool = False) -> TypeGuard[Sequence[str | Path]]: ...


def is_bool_sequence(val: object, *, include_series: bool = False) -> TypeGuard[Sequence[bool]]: ...


def is_int_sequence(val: object, *, include_series: bool = False) -> TypeGuard[Sequence[int]]: ...


def is_sequence(val: object, *, include_series: bool = False) -> TypeGuard[Sequence[Any]]: ...


def is_non_empty_sequence_of(obj: Sequence[Any], tp: type[T]) -> TypeIs[Sequence[T]]: ...


def is_str_sequence(val: object, *, allow_str: bool = False, include_series: bool = False) -> TypeGuard[Sequence[str]]: ...


def is_column(obj: Any) -> bool: ...


def warn_null_comparison(obj: Any) -> None: ...


def range_to_series(name: str, rng: range, dtype: PolarsDataType | None = None) -> pl.Series: ...


def range_to_slice(rng: range) -> slice: ...


def arrlen(obj: Any) -> int | None: ...


def normalize_filepath(path: str | Path, *, check_not_directory: bool = True) -> str: ...


def parse_version(version: Sequence[str | int]) -> tuple[int, ...]: ...


def ordered_unique(values: Sequence[Any]) -> list[Any]: ...


def deduplicate_names(names: Iterable[str]) -> list[str]: ...


@overload
def scale_bytes(sz: int, unit: SizeUnit) -> int | float: ...


@overload
def scale_bytes(sz: Expr, unit: SizeUnit) -> Expr: ...


NS = TypeVar("NS")


class sphinx_accessor(property):
    def __get__(self, instance: Any, cls: type[NS]) -> NS: ...


BUILDING_SPHINX_DOCS: str | None
NO_DEFAULT: Literal[_NoDefault.no_default]

NoDefault = Literal[_NoDefault.no_default]


def extend_bool(value: bool | Sequence[bool], n_match: int, value_name: str, match_name: str) -> Sequence[bool]: ...


def in_terminal_that_supports_colour() -> bool: ...


def parse_percentiles(percentiles: Sequence[float] | float | None, *, inject_median: bool = False) -> Sequence[float]: ...


def re_escape(s: str) -> str: ...


def display_dot_graph(*, dot: str, show: bool = True, output_path: str | Path | None = None, raw_output: bool = False, figsize: tuple[float, float] = ...) -> str | None: ...


def qualified_type_name(obj: Any, *, qualify_polars: bool = False) -> str: ...


def require_same_type(current: Any, other: Any) -> None: ...
