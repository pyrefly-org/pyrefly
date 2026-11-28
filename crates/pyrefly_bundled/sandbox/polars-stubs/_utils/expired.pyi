from __future__ import annotations
import inspect
from dataclasses import dataclass
from functools import wraps
from typing import TYPE_CHECKING, NoReturn, TypeVar
from polars.exceptions import ArgumentRemovedError, AttributeRemovedError
from collections.abc import Callable
from typing import Any, ParamSpec
from polars._utils.various import IdentityFunction

P = ParamSpec("P")

T = TypeVar("T")


@dataclass(frozen=True, kw_only=True)
class RemovedParameter:
    name: str
    deprecated_in: str | None = None
    removed_in: str
    hint: str | None = None

    def __init__(self, *, name: str, deprecated_in: str | None = ..., removed_in: str, hint: str | None = ...) -> None: ...


@dataclass(frozen=True, kw_only=True)
class RenamedParameter:
    name: str
    new_name: str
    deprecated_in: str | None = None
    removed_in: str
    hint: str | None = None

    def __init__(self, *, name: str, new_name: str, deprecated_in: str | None = ..., removed_in: str, hint: str | None = ...) -> None: ...


def raise_for_removed_attributes(obj: object, name: str, attributes: dict[str, str | None], *, version: str) -> None: ...


def getattr_fallback(obj: object, superclass: object, name: str, *, meta: bool = False) -> Any: ...


def removed_parameters(*params: RemovedParameter | RenamedParameter) -> IdentityFunction: ...
