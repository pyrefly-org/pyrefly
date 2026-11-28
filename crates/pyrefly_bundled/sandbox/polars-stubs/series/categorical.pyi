from __future__ import annotations
from typing import TYPE_CHECKING, Any
from polars._utils.expired import getattr_fallback, raise_for_removed_attributes
from polars._utils.unstable import unstable
from polars.series.utils import expr_dispatch
from polars import Series
from polars._plr import PySeries
from polars._typing import (
        PolarsDataType,
    )


@expr_dispatch
class CatNameSpace:
    def __init__(self, series: Series) -> None: ...

    def len_bytes(self) -> Series: ...

    def len_chars(self) -> Series: ...

    def starts_with(self, prefix: str) -> Series: ...

    def ends_with(self, suffix: str) -> Series: ...

    def slice(self, offset: int, length: int | None = None) -> Series: ...

    @unstable()
    def to(self, dtype: PolarsDataType, *, strict: bool = True) -> Series: ...

    @unstable()
    def physical(self) -> Series: ...
