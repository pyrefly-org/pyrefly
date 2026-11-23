from __future__ import annotations
from typing import Any
from polars._utils.polars_version import get_polars_version

__build__: dict[str, Any]

from polars._plr import __build__


def build_info() -> dict[str, Any]: ...
