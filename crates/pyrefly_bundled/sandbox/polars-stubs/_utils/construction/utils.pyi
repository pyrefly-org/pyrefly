from __future__ import annotations
from collections.abc import Sequence
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Final, get_type_hints
import polars as pl
from polars._dependencies import _check_for_pydantic, dataclasses, pydantic
from collections.abc import Callable
import pandas as pd

PANDAS_SIMPLE_NUMPY_DTYPES: Final[set[str]]


def try_get_type_hints(obj: type) -> dict[str, Any]: ...


@lru_cache(64)
def is_namedtuple(cls: Any, *, annotated: bool = False) -> bool: ...


def is_dataclass_instance(value: Any) -> bool: ...


def is_pydantic_model(value: Any) -> bool: ...


def is_sqlalchemy_row(value: Any) -> bool: ...


def get_first_non_none(values: Sequence[Any | None] | pl.Series) -> Any: ...


def nt_unpack(obj: Any) -> Any: ...


def contains_nested(value: Any, is_nested: Callable[[Any], bool]) -> bool: ...


def is_simple_numpy_backed_pandas_series(series: pd.Series[Any] | pd.Index[Any] | pd.DatetimeIndex) -> bool: ...
