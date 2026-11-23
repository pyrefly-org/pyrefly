import os
import sys
from collections.abc import Callable
from typing import Any


def verbose() -> bool: ...


def eprint(*a: Any, **kw: Any) -> None: ...


def verbose_print_sensitive(create_log_message: Callable[[], str]) -> None: ...
