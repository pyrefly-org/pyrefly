from __future__ import annotations
import contextlib
from io import BytesIO, StringIO
from pathlib import Path
from typing import TYPE_CHECKING
from polars._utils.various import normalize_filepath
from polars._utils.wrap import wrap_df
from polars.datatypes import N_INFER_DEFAULT
from io import IOBase
from polars import DataFrame
from polars._typing import SchemaDefinition


def read_json(source: str | Path | IOBase | bytes, *, schema: SchemaDefinition | None = None, schema_overrides: SchemaDefinition | None = None, infer_schema_length: int | None = ...) -> DataFrame: ...
