from __future__ import annotations
import contextlib
from polars import datatypes as dt
from polars._utils.unstable import unstable


@unstable()
def register_extension_type(ext_name: str, ext_class: type[dt.BaseExtension] | None = None, *, as_storage: bool = False) -> None: ...


@unstable()
def unregister_extension_type(ext_name: str) -> None: ...


@unstable()
def get_extension_type(ext_name: str) -> type[dt.BaseExtension] | str | None: ...
