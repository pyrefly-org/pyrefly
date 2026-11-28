from __future__ import annotations
import inspect
import os
from functools import wraps
from typing import TYPE_CHECKING, TypeVar
from polars._warnings import issue_warning
from polars.exceptions import UnstableWarning
from collections.abc import Callable
from typing import ParamSpec
from polars._utils.various import IdentityFunction

P = ParamSpec("P")

T = TypeVar("T")


def issue_unstable_warning(message: str | None = None) -> None: ...


def unstable() -> IdentityFunction: ...
