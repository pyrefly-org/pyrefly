from __future__ import annotations
import json
from collections.abc import Iterable, Mapping, Sequence
from typing import TYPE_CHECKING, Any
from polars._utils.unstable import unstable
from polars.dataframe import DataFrame
from polars.datatypes.constants import N_INFER_DEFAULT
from polars._typing import JSONEncoder
from polars.schema import Schema


@unstable()
def json_normalize(data: dict[Any, Any] | Sequence[dict[Any, Any] | Any], *, separator: str = ".", max_level: int | None = None, schema: Schema | None = None, strict: bool = True, infer_schema_length: int | None = ..., encoder: JSONEncoder | None = None) -> DataFrame: ...
