from __future__ import annotations
import contextlib
from pathlib import Path
from typing import IO, TYPE_CHECKING
from polars._utils.unstable import unstable
from polars._utils.various import normalize_filepath
from polars._utils.wrap import wrap_df
from polars.io._utils import parse_columns_arg
from polars import DataFrame


@unstable()
def read_avro(source: str | Path | IO[bytes] | bytes, *, columns: list[int] | list[str] | None = None, n_rows: int | None = None) -> DataFrame: ...
