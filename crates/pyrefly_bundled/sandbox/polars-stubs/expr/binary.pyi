from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.parse import parse_into_expression
from polars._utils.various import scale_bytes
from polars._utils.wrap import wrap_expr
from polars.datatypes import parse_into_datatype_expr
from polars import DataTypeExpr, Expr
from polars._typing import (
        Endianness,
        IntoExpr,
        PolarsDataType,
        SizeUnit,
        TransferEncoding,
    )


class ExprBinaryNameSpace:
    def __init__(self, expr: Expr) -> None: ...

    def contains(self, literal: IntoExpr) -> Expr: ...

    def ends_with(self, suffix: IntoExpr) -> Expr: ...

    def starts_with(self, prefix: IntoExpr) -> Expr: ...

    def decode(self, encoding: TransferEncoding, *, strict: bool = True) -> Expr: ...

    def encode(self, encoding: TransferEncoding) -> Expr: ...

    def size(self, unit: SizeUnit = "b") -> Expr: ...

    def reinterpret(self, *, dtype: PolarsDataType | DataTypeExpr, endianness: Endianness = "little") -> Expr: ...

    def slice(self, offset: int | IntoExpr, length: int | IntoExpr | None = None) -> Expr: ...

    def head(self, n: int | IntoExpr = 5) -> Expr: ...

    def tail(self, n: int | IntoExpr = 5) -> Expr: ...

    def get(self, index: int | IntoExpr, *, null_on_oob: bool = False) -> Expr: ...
