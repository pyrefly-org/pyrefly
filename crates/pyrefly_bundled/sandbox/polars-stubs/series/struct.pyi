from __future__ import annotations
import sys
from typing import TYPE_CHECKING
from polars._utils.various import (
    BUILDING_SPHINX_DOCS,
    _NamespaceSuggestMixin,
    qualified_type_name,
    sphinx_accessor,
)
from polars._utils.wrap import wrap_df
from polars.schema import Schema
from polars.series.utils import expr_dispatch
from collections.abc import Iterable, Sequence
from polars import DataFrame, Series
from polars._plr import PySeries
from polars._typing import IntoExpr


@expr_dispatch
class StructNameSpace(_NamespaceSuggestMixin):
    def __init__(self, series: Series) -> None: ...

    def __getitem__(self, item: int | str) -> Series: ...

    @property
    def fields(self) -> list[str]: ...

    def field(self, name: str) -> Series: ...

    def rename_fields(self, names: Sequence[str]) -> Series: ...

    def drop(self, names: Sequence[str], *, strict: bool = True) -> Series: ...

    @property
    def schema(self) -> Schema: ...

    def unnest(self) -> DataFrame: ...

    def eval(self, *exprs: IntoExpr | Iterable[IntoExpr], **named_exprs: IntoExpr) -> Series: ...

    def json_encode(self) -> Series: ...
