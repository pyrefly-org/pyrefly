from __future__ import annotations
from typing import TYPE_CHECKING, Literal, overload
from polars.dataframe import DataFrame
from polars.lazyframe import LazyFrame

__all__ = ["sql"]


@overload
def sql(query: str, *, eager: Literal[False] = False) -> LazyFrame: ...


@overload
def sql(query: str, *, eager: Literal[True]) -> DataFrame: ...
