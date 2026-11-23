from __future__ import annotations
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast
from collections.abc import Iterator


@contextmanager
def PortableTemporaryFile(mode: str = "w+b", *, buffering: int = -1, encoding: str | None = None, newline: str | None = None, suffix: str | None = None, prefix: str | None = None, dir: str | Path | None = None, delete: bool = True, errors: str | None = None) -> Iterator[Any]: ...
