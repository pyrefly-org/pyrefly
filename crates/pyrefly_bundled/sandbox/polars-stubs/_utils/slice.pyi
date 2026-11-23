from __future__ import annotations
from typing import TYPE_CHECKING
import polars._reexport as pl
from typing import TypeAlias
from polars import DataFrame, LazyFrame, Series

FrameOrSeries: TypeAlias = DataFrame | Series


class PolarsSlice:
    stop: int
    start: int
    stride: int
    slice_length: int
    is_unbounded: bool
    obj: FrameOrSeries

    def __init__(self, obj: FrameOrSeries) -> None: ...

    def apply(self, s: slice) -> FrameOrSeries: ...


class LazyPolarsSlice:
    obj: LazyFrame

    def __init__(self, obj: LazyFrame) -> None: ...

    def apply(self, s: slice) -> LazyFrame: ...
