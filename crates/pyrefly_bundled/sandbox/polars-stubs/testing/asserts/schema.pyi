from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
from polars._utils.unstable import unstable
from polars._typing import SchemaDict


@unstable()
def assert_schema_equal(left_schema: SchemaDict, right_schema: SchemaDict, *, check_column_order: bool = True, check_dtypes: bool = True) -> None: ...
