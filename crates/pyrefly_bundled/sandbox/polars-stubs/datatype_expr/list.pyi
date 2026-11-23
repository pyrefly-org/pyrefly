from __future__ import annotations
import polars._reexport as pl


class DataTypeExprListNameSpace:
    def __init__(self, expr: pl.DataTypeExpr) -> None: ...

    def inner_dtype(self) -> pl.DataTypeExpr: ...
