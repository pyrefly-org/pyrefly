from __future__ import annotations
from pathlib import Path
from typing import Any, Final, Generic, TypeVar
from polars._utils.various import is_path_or_str_sequence
from polars.io.partition import PartitionBy

POLARS_STORAGE_CONFIG_KEYS: Final[frozenset[str]]

T = TypeVar("T")


class NoPickleOption(Generic[T]):
    def __init__(self, opt_value: T | None = None) -> None: ...

    def get(self) -> T | None: ...

    def set(self, value: T | None) -> None: ...

    def __getstate__(self) -> tuple[()]: ...

    def __setstate__(self, _state: tuple[()]) -> None: ...
