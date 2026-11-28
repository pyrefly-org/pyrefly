from __future__ import annotations
import contextlib
import enum
from datetime import UTC, date, datetime, time, timedelta
from typing import TYPE_CHECKING, Any, cast
from zoneinfo import ZoneInfo
import polars._reexport as pl
from polars._dependencies import (
    _check_for_numpy,
    _check_for_pytz,
    _check_for_torch,
    pytz,
    torch,
)
from polars._dependencies import numpy as np
from polars._utils.wrap import wrap_expr
from polars.datatype_expr import DataTypeExpr
from polars.datatypes import (
    BaseExtension,
    Date,
    Datetime,
    Duration,
    Map,
    Object,
    Unknown,
)
from polars.datatypes.convert import DataTypeMappings
from polars import Expr
from polars._typing import PolarsDataType, TimeUnit


def lit(value: Any, dtype: PolarsDataType | DataTypeExpr | None = None, *, allow_object: bool = False) -> Expr: ...
