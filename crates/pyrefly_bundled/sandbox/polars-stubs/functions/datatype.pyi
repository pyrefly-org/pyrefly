from __future__ import annotations
from typing import TYPE_CHECKING
import polars._reexport as pl
from polars import functions as F
from polars._utils.unstable import unstable
from polars._utils.various import qualified_type_name
from collections.abc import Mapping
from polars import Expr
from polars._typing import PolarsDataType


@unstable()
def dtype_of(col_or_expr: str | Expr) -> pl.DataTypeExpr: ...


@unstable()
def self_dtype() -> pl.DataTypeExpr: ...


@unstable()
def struct_with_fields(mapping: Mapping[str, PolarsDataType | pl.DataTypeExpr]) -> pl.DataTypeExpr: ...
