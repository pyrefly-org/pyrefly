from __future__ import annotations
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, NoReturn, overload
import polars._reexport as pl
import polars.functions as F
from polars._dependencies import _check_for_numpy
from polars._dependencies import numpy as np
from polars._utils.constants import U32_MAX
from polars._utils.slice import PolarsSlice
from polars._utils.various import qualified_type_name, range_to_slice
from polars.datatypes.classes import (
    Boolean,
    Int8,
    Int16,
    Int32,
    Int64,
    String,
    UInt32,
    UInt64,
)
from polars.meta.index_type import get_index_type
from collections.abc import Iterable
from polars import DataFrame, Series
from polars._typing import (
        MultiColSelector,
        MultiIndexSelector,
        SingleColSelector,
        SingleIndexSelector,
    )

__all__ = ([
    "get_df_item_by_key",
    "get_series_item_by_key",
])


@overload
def get_series_item_by_key(s: Series, key: SingleIndexSelector) -> Any: ...


@overload
def get_series_item_by_key(s: Series, key: MultiIndexSelector) -> Series: ...


@overload
def get_df_item_by_key(df: DataFrame, key: tuple[SingleIndexSelector, SingleColSelector]) -> Any: ...


@overload
def get_df_item_by_key(df: DataFrame, key: str | tuple[MultiIndexSelector, SingleColSelector]) -> Series: ...


@overload
def get_df_item_by_key(df: DataFrame, key: (SingleIndexSelector
        | MultiIndexSelector
        | MultiColSelector
        | tuple[SingleIndexSelector, MultiColSelector]
        | tuple[MultiIndexSelector, MultiColSelector])) -> DataFrame: ...
