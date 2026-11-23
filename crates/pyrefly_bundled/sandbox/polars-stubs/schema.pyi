from __future__ import annotations
import contextlib
from collections import OrderedDict
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, overload
from polars._typing import PythonDataType
from polars._utils.unstable import unstable
from polars.datatypes import DataType, DataTypeClass, is_polars_dtype
from polars.datatypes._parse import parse_into_dtype
from polars.datatypes.convert import unpack_dtypes
from polars.exceptions import DuplicateError
from polars.interchange.protocol import CompatLevel
import sys
from collections.abc import Iterable
from typing import TypeAlias
import pyarrow as pa
from polars import DataFrame, LazyFrame
from polars._typing import ArrowSchemaExportable

__all__ = ["Schema"]


class Schema(BaseSchema):
    def __init__(self, schema: (Mapping[str, SchemaInitDataType]
            | Iterable[tuple[str, SchemaInitDataType] | ArrowSchemaExportable]
            | ArrowSchemaExportable
            | None) = None, *, check_dtypes: bool = True) -> None: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    def __setitem__(self, name: str, dtype: DataType | DataTypeClass | PythonDataType) -> None: ...

    @unstable()
    def __arrow_c_schema__(self) -> object: ...

    def names(self) -> list[str]: ...

    def dtypes(self) -> list[DataType]: ...

    @unstable()
    def to_arrow(self, *, compat_level: CompatLevel | None = None) -> pa.Schema: ...

    @overload
    def to_frame(self, *, eager: Literal[False]) -> LazyFrame: ...

    @overload
    def to_frame(self, *, eager: Literal[True] = ...) -> DataFrame: ...

    def len(self) -> int: ...

    def to_python(self) -> dict[str, type]: ...

    def contains_dtype(self, dtype: DataType, *, recursive: bool) -> bool: ...
