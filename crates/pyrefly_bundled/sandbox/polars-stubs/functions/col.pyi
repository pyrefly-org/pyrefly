from __future__ import annotations
import contextlib
import re
from collections.abc import Iterable
from datetime import datetime, timedelta
from typing import TYPE_CHECKING
import polars._reexport as pl
from polars._utils.wrap import wrap_expr
from polars.datatypes import (
    Datetime,
    Duration,
    is_polars_dtype,
    parse_into_dtype,
)
from polars.datatypes.group import (
    DATETIME_DTYPES,
    DURATION_DTYPES,
    FLOAT_DTYPES,
    INTEGER_DTYPES,
)
from types import FrameType
from polars._typing import PolarsDataType, PythonDataType
from polars.expr.expr import Expr

__all__ = ["col"]
col: Col
