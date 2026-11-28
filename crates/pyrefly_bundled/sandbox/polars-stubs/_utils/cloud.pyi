from __future__ import annotations
from typing import TYPE_CHECKING
import polars._plr as plr
from polars.lazyframe.opt_flags import DEFAULT_QUERY_OPT_FLAGS
from polars import LazyFrame, QueryOptFlags


def prepare_cloud_plan(lf: LazyFrame, *, optimizations: QueryOptFlags = ...) -> bytes: ...
