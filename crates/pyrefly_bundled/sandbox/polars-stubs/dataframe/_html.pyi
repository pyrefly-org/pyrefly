from __future__ import annotations
import os
import re
from textwrap import dedent
from typing import TYPE_CHECKING
from polars._dependencies import html
from collections.abc import Iterable
from types import TracebackType
from polars import DataFrame


def replace_consecutive_spaces(s: str) -> str: ...


class Tag:
    attributes: dict[str, str] | None
    elements: list[str]
    tag: str

    def __init__(self, elements: list[str], tag: str, attributes: dict[str, str] | None = None) -> None: ...

    def __enter__(self) -> None: ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...


class HTMLFormatter:
    col_idx: Iterable[int]
    df: DataFrame
    elements: list[str]
    from_series: bool
    max_cols: int
    max_rows: int
    row_idx: Iterable[int]

    def __init__(self, df: DataFrame, *, max_cols: int = 75, max_rows: int = 40, from_series: bool = False) -> None: ...

    def write_header(self) -> None: ...

    def write_body(self) -> None: ...

    def write(self, inner: str) -> None: ...

    def render(self) -> list[str]: ...


class NotebookFormatter(HTMLFormatter):
    def write_style(self) -> None: ...

    def render(self) -> list[str]: ...
