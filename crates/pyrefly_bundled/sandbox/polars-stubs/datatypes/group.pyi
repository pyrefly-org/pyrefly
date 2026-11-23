from __future__ import annotations
from typing import TYPE_CHECKING, Any, Final
from polars.datatypes.classes import (
    Array,
    DataType,
    DataTypeClass,
    Date,
    Datetime,
    Decimal,
    Duration,
    Float16,
    Float32,
    Float64,
    Int8,
    Int16,
    Int32,
    Int64,
    Int128,
    List,
    Map,
    Struct,
    Time,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt128,
)
from collections.abc import Iterable
from typing import Self
from polars._typing import (
        PolarsDataType,
        PolarsIntegerType,
        PolarsTemporalType,
    )


class DataTypeGroup(frozenset):
    def __new__(cls, items: Iterable[DataType | DataTypeClass], *, match_base_type: bool = True) -> Self: ...

    def __contains__(self, item: Any) -> bool: ...


SIGNED_INTEGER_DTYPES: Final[frozenset[PolarsIntegerType]]
UNSIGNED_INTEGER_DTYPES: Final[frozenset[PolarsIntegerType]]
INTEGER_DTYPES: Final[frozenset[PolarsIntegerType]]
FLOAT_DTYPES: Final[frozenset[PolarsDataType]]
NUMERIC_DTYPES: Final[frozenset[PolarsDataType]]
DATETIME_DTYPES: Final[frozenset[PolarsDataType]]
DURATION_DTYPES: Final[frozenset[PolarsDataType]]
TEMPORAL_DTYPES: Final[frozenset[PolarsTemporalType]]
NESTED_DTYPES: Final[frozenset[PolarsDataType]]
