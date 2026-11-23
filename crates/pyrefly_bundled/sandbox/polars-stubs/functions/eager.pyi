from __future__ import annotations
import contextlib
from collections.abc import Generator, Iterator, Sequence
from functools import reduce
from itertools import chain
from typing import TYPE_CHECKING, get_args
import polars._reexport as pl
from polars import functions as F
from polars._typing import ConcatMethod
from polars._utils.deprecation import issue_deprecation_warning
from polars._utils.reduce_balanced import reduce_balanced
from polars._utils.unstable import unstable
from polars._utils.various import (
    is_non_empty_sequence_of,
    ordered_unique,
    qualified_type_name,
)
from polars._utils.wrap import wrap_df, wrap_expr, wrap_ldf, wrap_s
from polars.exceptions import InvalidOperationError
from collections.abc import Iterable
from polars import DataFrame, Expr, LazyFrame, Series
from polars._typing import FrameType, JoinStrategy, PolarsType


def concat(items: Iterable[PolarsType], *, how: ConcatMethod = "vertical", rechunk: bool = False, parallel: bool = True, strict: bool | None = None) -> PolarsType: ...


def union(items: Iterable[PolarsType], *, how: ConcatMethod = "vertical", strict: bool | None = None) -> PolarsType: ...


@unstable()
def merge_sorted(items: Iterable[PolarsType], key: str | Sequence[str], *, maintain_order: bool = False) -> PolarsType: ...


def align_frames(*frames: FrameType | Iterable[FrameType], on: str | Expr | Sequence[str] | Sequence[Expr] | Sequence[str | Expr], how: JoinStrategy = "full", select: str | Expr | Sequence[str | Expr] | None = None, descending: bool | Sequence[bool] = False) -> list[FrameType]: ...
