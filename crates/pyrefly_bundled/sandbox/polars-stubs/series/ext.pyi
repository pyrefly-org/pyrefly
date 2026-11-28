from __future__ import annotations
from typing import TYPE_CHECKING
from polars import datatypes as dt
from polars._utils.unstable import unstable
from polars._utils.wrap import wrap_s
from polars.series.utils import expr_dispatch
from polars import Series
from polars._plr import PySeries
from polars._typing import (
        PolarsDataType,
    )


@expr_dispatch
class ExtensionNameSpace:
    def __init__(self, series: Series) -> None: ...

    @unstable()
    def to(self, dtype: PolarsDataType) -> Series: ...

    @unstable()
    def storage(self) -> Series: ...
