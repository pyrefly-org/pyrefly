from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.parse import (
    parse_into_list_of_expressions,
)
from polars._utils.various import _NamespaceSuggestMixin, qualified_type_name
from polars._utils.wrap import wrap_expr
from collections.abc import Iterable, Sequence
from polars import Expr
from polars._typing import IntoExpr


class ExprStructNameSpace(_NamespaceSuggestMixin):
    def __init__(self, expr: Expr) -> None: ...

    def __getitem__(self, item: str | int) -> Expr: ...

    def field(self, name: str | list[str], *more_names: str) -> Expr: ...

    def unnest(self) -> Expr: ...

    def rename_fields(self, names: Sequence[str]) -> Expr: ...

    def drop(self, names: Sequence[str], *, strict: bool = True) -> Expr: ...

    def json_encode(self) -> Expr: ...

    def with_fields(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> Expr: ...

    def eval(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> Expr: ...
