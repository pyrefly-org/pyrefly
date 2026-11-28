from __future__ import annotations
from typing import TYPE_CHECKING, Any
import polars._reexport as pl
from polars._utils.unstable import unstable
from polars.io.plugins import register_io_source
from collections.abc import Iterator
from polars import DataFrame, Expr
from polars.lazyframe import LazyFrame

__all__ = ["scan_arrow_c_stream"]


@unstable()
def scan_arrow_c_stream(source: Any) -> LazyFrame: ...
