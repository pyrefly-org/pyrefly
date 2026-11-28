from __future__ import annotations
import contextlib
from io import StringIO
from typing import TYPE_CHECKING, Any
from polars.io.csv.functions import read_csv
from polars import DataFrame


def read_clipboard(separator: str = "\t", **kwargs: Any) -> DataFrame: ...
