from __future__ import annotations
import contextlib
import enum
from collections import OrderedDict
from collections.abc import Mapping
from datetime import tzinfo
from inspect import isclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar, overload
import polars._reexport as pl
import polars.datatypes
from polars._utils.expired import (
    RemovedParameter,
    getattr_fallback,
    raise_for_removed_attributes,
    removed_parameters,
)
import polars.datatypes.classes as pldt
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Self
from polars import Series
from polars._typing import (
        PolarsDataType,
        PythonDataType,
        SchemaDict,
        TimeUnit,
    )

R_co = TypeVar("R_co", covariant=True)


class classinstmethod(Generic[R_co]):
    func: Callable[..., R_co]

    def __init__(self, func: Callable[..., R_co]) -> None: ...

    def __get__(self, instance: Any, type_: Any) -> Callable[..., R_co]: ...


class DataTypeClass(type):
    def __repr__(cls) -> str: ...

    @classmethod
    def base_type(cls) -> DataTypeClass: ...

    @classmethod
    def is_(cls, other: PolarsDataType) -> bool: ...

    @classmethod
    def is_numeric(cls) -> bool: ...

    @classmethod
    def is_decimal(cls) -> bool: ...

    @classmethod
    def is_integer(cls) -> bool: ...

    @classmethod
    def is_object(cls) -> bool: ...

    @classmethod
    def is_signed_integer(cls) -> bool: ...

    @classmethod
    def is_unsigned_integer(cls) -> bool: ...

    @classmethod
    def is_float(cls) -> bool: ...

    @classmethod
    def is_temporal(cls) -> bool: ...

    @classmethod
    def is_nested(cls) -> bool: ...

    @classmethod
    def is_extension(cls) -> bool: ...

    @classmethod
    def from_python(cls, py_type: PythonDataType) -> PolarsDataType: ...

    @classmethod
    def to_python(cls) -> PythonDataType: ...

    @classmethod
    def to_dtype_expr(cls) -> pl.DataTypeExpr: ...


class DataType(metaclass=DataTypeClass):
    @overload
    def __eq__(self, other: pl.DataTypeExpr) -> pl.Expr: ...

    @overload
    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...

    @classmethod
    def base_type(cls) -> type[Self]: ...

    @classinstmethod
    def is_(self, other: PolarsDataType) -> bool: ...

    @classmethod
    def is_numeric(cls) -> bool: ...

    @classmethod
    def is_decimal(cls) -> bool: ...

    @classmethod
    def is_integer(cls) -> bool: ...

    @classmethod
    def is_object(cls) -> bool: ...

    @classmethod
    def is_signed_integer(cls) -> bool: ...

    @classmethod
    def is_unsigned_integer(cls) -> bool: ...

    @classmethod
    def is_float(cls) -> bool: ...

    @classmethod
    def is_temporal(cls) -> bool: ...

    @classmethod
    def is_nested(cls) -> bool: ...

    @classmethod
    def is_extension(cls) -> bool: ...

    @classmethod
    def from_python(cls, py_type: PythonDataType) -> PolarsDataType: ...

    @classinstmethod
    def to_python(self) -> PythonDataType: ...

    @classinstmethod
    def to_dtype_expr(self) -> pl.DataTypeExpr: ...


class NumericType(DataType):
    @classmethod
    def max(cls) -> pl.Expr: ...

    @classmethod
    def min(cls) -> pl.Expr: ...


class IntegerType(NumericType):
    ...


class SignedIntegerType(IntegerType):
    ...


class UnsignedIntegerType(IntegerType):
    ...


class FloatType(NumericType):
    ...


class TemporalType(DataType):
    ...


class NestedType(DataType):
    ...


class ObjectType(DataType):
    ...


class Int8(SignedIntegerType):
    ...


class Int16(SignedIntegerType):
    ...


class Int32(SignedIntegerType):
    ...


class Int64(SignedIntegerType):
    ...


class Int128(SignedIntegerType):
    ...


class UInt8(UnsignedIntegerType):
    ...


class UInt16(UnsignedIntegerType):
    ...


class UInt32(UnsignedIntegerType):
    ...


class UInt64(UnsignedIntegerType):
    ...


class UInt128(UnsignedIntegerType):
    ...


class Float16(FloatType):
    ...


class Float32(FloatType):
    ...


class Float64(FloatType):
    ...


class Decimal(NumericType):
    precision: int
    scale: int

    def __init__(self, precision: int | None = None, scale: int = 0) -> None: ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...


class Boolean(DataType):
    ...


class String(DataType):
    ...


Utf8: type[String]


class Binary(DataType):
    ...


class Date(TemporalType):
    ...


class Time(TemporalType):
    @classmethod
    def max(cls) -> pl.Expr: ...

    @classmethod
    def min(cls) -> pl.Expr: ...


class Datetime(TemporalType):
    time_unit: TimeUnit
    time_zone: str | None

    def __init__(self, time_unit: TimeUnit = "us", time_zone: str | tzinfo | None = None) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Duration(TemporalType):
    time_unit: TimeUnit

    def __init__(self, time_unit: TimeUnit = "us") -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Categories:
    __dict__: dict[str, Any]

    def __init__(self, name: str | None = None, namespace: str = "", physical: PolarsDataType = ...) -> None: ...

    @staticmethod
    def random(namespace: str = "", physical: PolarsDataType = ...) -> Categories: ...

    def name(self) -> str: ...

    def namespace(self) -> str: ...

    def physical(self) -> PolarsDataType: ...

    def is_global(self) -> bool: ...

    def __getitem__(self, key: str | int) -> str | int: ...

    def __contains__(self, item: str | int) -> bool: ...

    def __iter__(self) -> Iterator[str | None]: ...

    def to_series(self) -> Series: ...

    def to_dict(self) -> dict[str, int]: ...

    def __repr__(self) -> str: ...

    def __hash__(self) -> int: ...

    def __eq__(self, other: object) -> bool: ...

    def __getstate__(self) -> tuple[str, str, PolarsDataType]: ...

    def __setstate__(self, state: tuple[str, str, PolarsDataType]) -> None: ...


class Categorical(DataType):
    categories: Categories

    def __init__(self, categories: Categories | str | None = None) -> None: ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...


class Enum(DataType):
    categories: Series

    def __init__(self, categories: Series | Iterable[str] | type[enum.Enum]) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Object(ObjectType):
    ...


class Null(DataType):
    ...


class Unknown(DataType):
    ...


class List(NestedType):
    inner: PolarsDataType

    def __init__(self, inner: PolarsDataType | PythonDataType) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Map(NestedType):
    key: PolarsDataType
    value: PolarsDataType

    def __init__(self, key: PolarsDataType | PythonDataType, value: PolarsDataType | PythonDataType) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Array(NestedType):
    inner: PolarsDataType
    size: int
    shape: tuple[int, ...]

    @removed_parameters(
        RemovedParameter(
            name="width",
            deprecated_in="0.20.31",
            removed_in="2.0",
            hint="use `shape` instead.",
        )
    )
    def __init__(self, inner: PolarsDataType | PythonDataType, shape: int | tuple[int, ...] | None = None) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Field:
    name: str
    dtype: PolarsDataType

    def __init__(self, name: str, dtype: PolarsDataType) -> None: ...

    def __eq__(self, other: Field) -> bool: ...

    def __hash__(self) -> int: ...

    def __repr__(self) -> str: ...


class Struct(NestedType):
    fields: list[Field]

    def __init__(self, fields: Sequence[Field] | SchemaDict) -> None: ...

    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __hash__(self) -> int: ...

    def __iter__(self) -> Iterator[tuple[str, PolarsDataType]]: ...

    def __reversed__(self) -> Iterator[tuple[str, PolarsDataType]]: ...

    def __repr__(self) -> str: ...

    def to_schema(self) -> OrderedDict[str, PolarsDataType]: ...


class BaseExtension(DataType):
    __dict__: dict[str, Any]

    def __init__(self, name: str, storage: PolarsDataType, metadata: str | None = None) -> None: ...

    @classmethod
    def ext_from_params(cls, name: str, storage: PolarsDataType, metadata: str | None) -> Any: ...

    def ext_name(self) -> str: ...

    def ext_storage(self) -> PolarsDataType: ...

    def ext_metadata(self) -> str | None: ...

    def __repr__(self) -> str: ...

    def __hash__(self) -> int: ...

    @overload
    def __eq__(self, other: pl.DataTypeExpr) -> pl.Expr: ...

    @overload
    def __eq__(self, other: PolarsDataType) -> bool: ...

    def __getstate__(self) -> tuple[str, PolarsDataType, str | None]: ...

    def __setstate__(self, state: tuple[str, PolarsDataType, str | None]) -> None: ...


class Extension(BaseExtension):
    ...
