from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
from polars._utils.wrap import wrap_expr
from polars import Expr


def len() -> Expr: ...
