from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.unstable import unstable
from polars.io.pyarrow_dataset.anonymous_scan import _scan_pyarrow_dataset
from polars import LazyFrame
from polars._dependencies import pyarrow as pa


@unstable()
def scan_pyarrow_dataset(source: pa.dataset.Dataset, *, allow_pyarrow_filter: bool = True, batch_size: int | None = None) -> LazyFrame: ...
