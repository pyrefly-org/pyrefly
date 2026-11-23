from __future__ import annotations
from typing import Any, NoReturn


def raise_assertion_error(objects: str, detail: str, left: Any, right: Any, *, cause: Exception | None = None) -> NoReturn: ...
