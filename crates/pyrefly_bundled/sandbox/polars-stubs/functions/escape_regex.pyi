from __future__ import annotations
import contextlib
from polars._utils.various import qualified_type_name
import polars._reexport as pl


def escape_regex(s: str) -> str: ...
