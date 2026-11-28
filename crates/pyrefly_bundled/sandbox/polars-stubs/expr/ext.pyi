from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.unstable import unstable
from polars._utils.wrap import wrap_expr
from polars.datatypes import parse_into_datatype_expr
import polars._reexport as pl
from polars import Expr
from polars._typing import (
        PolarsDataType,
    )


class ExprExtensionNameSpace:
    def __init__(self, expr: Expr) -> None: ...

    @unstable()
    def to(self, dtype: PolarsDataType | pl.DataTypeExpr) -> Expr: ...

    @unstable()
    def storage(self) -> Expr: ...
