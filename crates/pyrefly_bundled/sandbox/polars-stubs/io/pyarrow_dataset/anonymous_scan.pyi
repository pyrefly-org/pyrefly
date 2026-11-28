from __future__ import annotations
from functools import partial
from typing import TYPE_CHECKING, Any
import polars as pl
from collections.abc import Iterator
from polars import DataFrame, LazyFrame
from polars._dependencies import pyarrow as pa
