from __future__ import annotations
import datetime
import dis
import inspect
import re
import sys
import types
import warnings
from bisect import bisect_left
from collections import defaultdict
from collections.abc import Collection
from dis import get_instructions
from enum import Enum, auto
from inspect import signature
from itertools import count, zip_longest
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Final,
    Literal,
    NamedTuple,
    TypedDict,
)
from polars._dependencies import _check_for_pandas
from polars._utils.cache import LRUCache
from polars._utils.various import NO_DEFAULT, re_escape
from polars.dataframe.frame import DataFrame
from polars.datatypes import List, String
from collections.abc import Callable, Iterable, Iterator, MutableMapping
from collections.abc import Set as AbstractSet
from dis import Instruction
from typing import TypeAlias
from polars._typing import PolarsDataType
from polars._utils.various import NoDefault


class BytecodeParser:
    def __init__(self, function: Callable[[Any], Any], map_target: MapTarget) -> None: ...

    @property
    def map_target(self) -> MapTarget: ...

    def can_attempt_rewrite(self) -> bool: ...

    def dis(self) -> None: ...

    @property
    def function(self) -> Callable[[Any], Any]: ...

    @property
    def original_instructions(self) -> list[Instruction]: ...

    @property
    def param_name(self) -> str | None: ...

    @property
    def rewritten_instructions(self) -> list[Instruction]: ...

    def to_expression(self, col: str, dtype: PolarsDataType | None = None) -> str | None: ...

    def warn(self, col: str, *, dtype: PolarsDataType | None = None, suggestion_override: str | None = None, udf_override: str | None = None) -> None: ...


def warn_on_inefficient_map(function: Callable[[Any], Any], columns: list[str], map_target: MapTarget, dtype: PolarsDataType | None = None) -> None: ...


__all__ = ["BytecodeParser", "warn_on_inefficient_map"]
