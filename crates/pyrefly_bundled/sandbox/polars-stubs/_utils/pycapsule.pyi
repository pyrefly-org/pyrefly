from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Any
from polars._utils.construction.dataframe import dataframe_to_pydf
from polars._utils.wrap import wrap_df
from polars import DataFrame
from polars._typing import SchemaDefinition, SchemaDict


def is_pycapsule(obj: Any) -> bool: ...


def pycapsule_to_frame(obj: Any, *, schema: SchemaDefinition | None = None, schema_overrides: SchemaDict | None = None, rechunk: bool = False) -> DataFrame: ...
