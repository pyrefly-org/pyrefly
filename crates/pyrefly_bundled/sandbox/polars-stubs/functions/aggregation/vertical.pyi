from __future__ import annotations
from typing import TYPE_CHECKING
import polars.functions as F
from polars import Expr


def all(*names: str, ignore_nulls: bool = True) -> Expr: ...


def any(*names: str, ignore_nulls: bool = True) -> Expr | bool | None: ...


def max(*names: str) -> Expr: ...


def min(*names: str) -> Expr: ...


def sum(*names: str) -> Expr: ...


def cum_sum(*names: str) -> Expr: ...
