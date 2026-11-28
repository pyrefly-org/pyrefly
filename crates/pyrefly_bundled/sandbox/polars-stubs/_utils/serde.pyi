from __future__ import annotations
from io import BytesIO, StringIO
from pathlib import Path
from typing import TYPE_CHECKING, Literal, overload
from polars._utils.various import normalize_filepath
from collections.abc import Callable
from io import IOBase
from polars._typing import SerializationFormat


@overload
def serialize_polars_object(serializer: Callable[[IOBase | str], None], file: None, format: Literal["binary"]) -> bytes: ...


@overload
def serialize_polars_object(serializer: Callable[[IOBase | str], None], file: None, format: Literal["json"]) -> str: ...


@overload
def serialize_polars_object(serializer: Callable[[IOBase | str], None], file: IOBase | str | Path, format: SerializationFormat) -> None: ...
