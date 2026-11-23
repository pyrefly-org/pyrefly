from __future__ import annotations
import ast
import inspect
import sys
from collections import defaultdict
from collections.abc import Sequence
from functools import wraps
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeVar, get_args
from polars._typing import DeprecationType
from collections.abc import Callable
from polars._utils.various import IdentityFunction
from polars._warnings import issue_warning
from collections.abc import Mapping
from typing import ParamSpec
from polars._typing import Ambiguous


def deprecate_renamed_parameter(old_name: str, new_name: str, *, version: str) -> IdentityFunction: ...


def deprecate_nonkeyword_arguments(allowed_args: list[str] | None = None, message: str | None = None, *, version: str) -> IdentityFunction: ...


def deprecate_parameter_as_multi_positional(old_name: str) -> IdentityFunction: ...


def identify_deprecations(*types: DeprecationType) -> dict[str, list[str]]: ...


__all__ = ([
    "deprecate_nonkeyword_arguments",
    "deprecate_parameter_as_multi_positional",
    "deprecate_renamed_parameter",
    "deprecated",
    "identify_deprecations",
])
