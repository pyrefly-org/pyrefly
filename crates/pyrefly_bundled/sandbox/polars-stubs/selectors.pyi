from __future__ import annotations
import builtins
import contextlib
import datetime as pydatetime
from collections.abc import Collection, Mapping, Sequence
from decimal import Decimal as PyDecimal
from functools import reduce
from operator import or_
from typing import (
    TYPE_CHECKING,
    Any,
    NoReturn,
    overload,
)
import polars.datatypes.classes as pldt
from polars import functions as F
from polars._utils.parse.expr import _parse_inputs_as_iterable
from polars._utils.unstable import unstable
from polars._utils.various import is_column, re_escape
from polars.datatypes import (
    Binary,
    Boolean,
    Categorical,
    Date,
    String,
    Time,
    is_polars_dtype,
)
from polars.expr import Expr
from types import NoneType
import sys
from collections.abc import Iterable
from polars import DataFrame, LazyFrame
from polars._typing import PolarsDataType, PythonDataType, TimeUnit

__all__ = ([
    # class
    "Selector",
    # functions
    "all",
    "alpha",
    "alphanumeric",
    "array",
    "binary",
    "boolean",
    "by_dtype",
    "by_index",
    "by_name",
    "categorical",
    "contains",
    "date",
    "datetime",
    "decimal",
    "digit",
    "duration",
    "ends_with",
    "enum",
    "exclude",
    "expand_selector",
    "first",
    "float",
    "integer",
    "is_selector",
    "last",
    "list",
    "map",
    "matches",
    "nested",
    "numeric",
    "signed_integer",
    "starts_with",
    "string",
    "struct",
    "temporal",
    "time",
    "unsigned_integer",
])


def is_selector(obj: Any) -> TypeIs[Selector]: ...


def expand_selector(target: DataFrame | LazyFrame | Mapping[str, PolarsDataType], selector: Selector | Expr, *, strict: bool = True) -> tuple[str, ...]: ...


class Selector(Expr):
    def __getstate__(self) -> bytes: ...

    def __setstate__(self, state: bytes) -> None: ...

    def __repr__(self) -> str: ...

    def __hash__(self) -> int: ...

    def __invert__(cls) -> Selector: ...

    def __add__(self, other: Any) -> Expr: ...

    def __radd__(self, other: Any) -> Expr: ...

    @overload
    def __and__(self, other: Selector) -> Selector: ...

    @overload
    def __and__(self, other: Any) -> Expr: ...

    def __rand__(self, other: Any) -> Expr: ...

    @overload
    def __or__(self, other: Selector) -> Selector: ...

    @overload
    def __or__(self, other: Any) -> Expr: ...

    def __ror__(self, other: Any) -> Expr: ...

    @overload
    def __sub__(self, other: Selector) -> Selector: ...

    @overload
    def __sub__(self, other: Any) -> Expr: ...

    def __rsub__(self, other: Any) -> NoReturn: ...

    @overload
    def __xor__(self, other: Selector) -> Selector: ...

    @overload
    def __xor__(self, other: Any) -> Expr: ...

    def __rxor__(self, other: Any) -> Expr: ...

    def exclude(self, columns: str | PolarsDataType | Collection[str | PolarsDataType], *more_columns: str | PolarsDataType) -> Selector: ...

    def as_expr(self) -> Expr: ...


def all() -> Selector: ...


def alpha(ascii_only: bool = False, *, ignore_spaces: bool = False) -> Selector: ...


def alphanumeric(ascii_only: bool = False, *, ignore_spaces: bool = False) -> Selector: ...


def binary() -> Selector: ...


def boolean() -> Selector: ...


def by_dtype(*dtypes: (PolarsDataType
        | PythonDataType
        | Iterable[PolarsDataType]
        | Iterable[PythonDataType])) -> Selector: ...


def by_index(*indices: int | range | Sequence[int | range], require_all: bool = True) -> Selector: ...


def by_name(*names: str | Collection[str], require_all: bool = True) -> Selector: ...


@unstable()
def enum() -> Selector: ...


@unstable()
def list(inner: None | Selector = None) -> Selector: ...


@unstable()
def array(inner: Selector | None = None, *, width: int | None = None) -> Selector: ...


@unstable()
def struct() -> Selector: ...


@unstable()
def map() -> Selector: ...


@unstable()
def nested() -> Selector: ...


def categorical() -> Selector: ...


def contains(*substring: str) -> Selector: ...


def date() -> Selector: ...


def datetime(time_unit: TimeUnit | Collection[TimeUnit] | None = None, time_zone: str | pydatetime.timezone | Collection[str | pydatetime.timezone | None] | None = ...) -> Selector: ...


def decimal() -> Selector: ...


def digit(ascii_only: bool = False) -> Selector: ...


def duration(time_unit: TimeUnit | Collection[TimeUnit] | None = None) -> Selector: ...


def ends_with(*suffix: str) -> Selector: ...


def exclude(columns: (str
        | PolarsDataType
        | Selector
        | Expr
        | Collection[str | PolarsDataType | Selector | Expr]), *more_columns: str | PolarsDataType | Selector | Expr) -> Selector: ...


def first(*, strict: bool = True) -> Selector: ...


def float() -> Selector: ...


def integer() -> Selector: ...


def signed_integer() -> Selector: ...


def unsigned_integer() -> Selector: ...


def last(*, strict: bool = True) -> Selector: ...


def matches(pattern: str) -> Selector: ...


def numeric() -> Selector: ...


def starts_with(*prefix: str) -> Selector: ...


def string(*, include_categorical: bool = False) -> Selector: ...


def temporal() -> Selector: ...


def time() -> Selector: ...
