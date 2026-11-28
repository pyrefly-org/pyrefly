from __future__ import annotations
from datetime import timedelta
from polars._utils.convert import parse_as_duration_string


def parse_interval_argument(interval: str | timedelta) -> str: ...
