from __future__ import annotations
from typing import TYPE_CHECKING
import polars._reexport as pl
from polars import DataFrame, Expr, LazyFrame, Series
from polars._plr import PyDataFrame, PyExpr, PyLazyFrame, PySeries


def wrap_df(df: PyDataFrame) -> DataFrame: ...


def wrap_ldf(ldf: PyLazyFrame) -> LazyFrame: ...


def wrap_s(s: PySeries) -> Series: ...


def wrap_expr(pyexpr: PyExpr) -> Expr: ...
