from __future__ import annotations
from typing import TYPE_CHECKING, Any
from polars._utils.expired import getattr_fallback, raise_for_removed_attributes
from polars._utils.unstable import unstable
from polars._utils.various import qualified_type_name
from polars._utils.wrap import wrap_expr
from polars.datatypes import parse_into_datatype_expr
import polars._reexport as pl
from polars import Expr
from polars._typing import (
        PolarsDataType,
    )


class ExprCatNameSpace:
    def __init__(self, expr: Expr) -> None: ...

    def len_bytes(self) -> Expr: ...

    def len_chars(self) -> Expr: ...

    def starts_with(self, prefix: str) -> Expr: ...

    def ends_with(self, suffix: str) -> Expr: ...

    def slice(self, offset: int, length: int | None = None) -> Expr: ...

    @unstable()
    def to(self, dtype: PolarsDataType | pl.DataTypeExpr, *, strict: bool = True) -> Expr: ...

    @unstable()
    def physical(self) -> Expr: ...
