from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
from polars._utils.deprecation import deprecated
from types import TracebackType
from typing import Self

__all__ = ([
    "StringCache",
    "disable_string_cache",
    "enable_string_cache",
    "using_string_cache",
])


@deprecated("the string cache has been replaced by pl.Categories")
class StringCache(contextlib.ContextDecorator):
    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...


@deprecated("the string cache has been replaced by pl.Categories")
def enable_string_cache() -> None: ...


@deprecated("the string cache has been replaced by pl.Categories")
def disable_string_cache() -> None: ...


@deprecated("the string cache has been replaced by pl.Categories")
def using_string_cache() -> bool: ...
