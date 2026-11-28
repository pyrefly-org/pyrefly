from __future__ import annotations
import inspect
import warnings
from pathlib import Path
from typing import Any
import polars as pl


def find_stacklevel() -> int: ...


def issue_warning(message: str, category: type[Warning], **kwargs: Any) -> None: ...
