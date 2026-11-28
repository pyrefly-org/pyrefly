from __future__ import annotations
from datetime import UTC, datetime, time, timedelta
from decimal import Context
from functools import lru_cache
from typing import (
    TYPE_CHECKING,
    Any,
    NoReturn,
    overload,
)
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from polars._utils.constants import (
    EPOCH,
    EPOCH_DATE,
    EPOCH_UTC,
    MS_PER_SECOND,
    NS_PER_SECOND,
    SECONDS_PER_DAY,
    SECONDS_PER_HOUR,
    US_PER_SECOND,
)
from collections.abc import Callable
from datetime import date, tzinfo
from decimal import Decimal
from polars._typing import TimeUnit


@overload
def parse_as_duration_string(td: None) -> None: ...


@overload
def parse_as_duration_string(td: timedelta | str) -> str: ...


def negate_duration_string(duration: str) -> str: ...


def date_to_int(d: date) -> int: ...


def time_to_int(t: time) -> int: ...


def datetime_to_int(dt: datetime, time_unit: TimeUnit) -> int: ...


def timedelta_to_int(td: timedelta, time_unit: TimeUnit) -> int: ...


@lru_cache(256)
def to_py_date(value: int | float) -> date: ...


def to_py_time(value: int) -> time: ...


def to_py_datetime(value: int | float, time_unit: TimeUnit, time_zone: str | None = None) -> datetime: ...


def to_py_timedelta(value: int | float, time_unit: TimeUnit) -> timedelta: ...


def to_py_decimal(prec: int, value: str) -> Decimal: ...
