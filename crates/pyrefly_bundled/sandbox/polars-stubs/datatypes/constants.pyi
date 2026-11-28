from __future__ import annotations
from typing import TYPE_CHECKING, Final
from polars._typing import TimeUnit

N_INFER_DEFAULT: Final = 100
DTYPE_TEMPORAL_UNITS: Final[frozenset[TimeUnit]]
