from __future__ import annotations
from collections.abc import Awaitable
from typing import TYPE_CHECKING, Any, Generic, TypeVar
from polars._dependencies import _GEVENT_AVAILABLE
from polars._utils.wrap import wrap_df
from asyncio.futures import Future
from collections.abc import Generator
from polars import DataFrame
from polars._plr import PyDataFrame

T = TypeVar("T")
