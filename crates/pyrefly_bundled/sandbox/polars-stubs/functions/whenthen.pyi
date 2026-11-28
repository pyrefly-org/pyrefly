from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Any
import polars._reexport as pl
from polars._utils.parse import parse_predicates_constraints_into_expression
from collections.abc import Iterable
from polars._typing import IntoExprColumn


def when(*predicates: IntoExprColumn | Iterable[IntoExprColumn] | bool, **constraints: Any) -> pl.When: ...
