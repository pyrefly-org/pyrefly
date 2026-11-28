from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.wrap import wrap_df
from polars import DataFrame
from polars._plr import PyInProcessQuery


class InProcessQuery:
    def __init__(self, ipq: PyInProcessQuery) -> None: ...

    def cancel(self) -> None: ...

    def fetch(self) -> DataFrame | None: ...

    def fetch_blocking(self) -> DataFrame: ...
