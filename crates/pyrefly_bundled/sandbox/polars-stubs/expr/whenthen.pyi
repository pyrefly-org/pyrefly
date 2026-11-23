from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Any
import polars.functions as F
from polars._utils.parse import (
    parse_into_expression,
    parse_predicates_constraints_into_expression,
)
from polars._utils.wrap import wrap_expr
from polars.expr.expr import Expr
from collections.abc import Iterable
from polars._plr import PyExpr
from polars._typing import IntoExpr


class When:
    def __init__(self, when: Any) -> None: ...

    def then(self, statement: IntoExpr) -> Then: ...


class Then(Expr):
    def __init__(self, then: Any) -> None: ...

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, state: bytes) -> None: ...

    def when(self, *predicates: IntoExpr | Iterable[IntoExpr], **constraints: Any) -> ChainedWhen: ...

    def otherwise(self, statement: IntoExpr) -> Expr: ...


class ChainedWhen:
    def __init__(self, chained_when: Any) -> None: ...

    def then(self, statement: IntoExpr) -> ChainedThen: ...


class ChainedThen(Expr):
    def __init__(self, chained_then: Any) -> None: ...

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, state: bytes) -> None: ...

    def when(self, *predicates: IntoExpr | Iterable[IntoExpr], **constraints: Any) -> ChainedWhen: ...

    def otherwise(self, statement: IntoExpr) -> Expr: ...
