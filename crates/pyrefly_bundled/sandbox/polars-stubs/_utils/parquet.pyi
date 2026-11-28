from collections.abc import Callable
from typing import Any
from polars._typing import ParquetMetadataContext, ParquetMetadataFn


def wrap_parquet_metadata_callback(fn: ParquetMetadataFn) -> Callable[[Any], list[tuple[str, str]]]: ...
