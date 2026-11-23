from typing import TYPE_CHECKING
from polars._plr import (
        CategoricalRemappingWarning,
        ColumnNotFoundError,
        ComputeError,
        DuplicateError,
        InvalidOperationError,
        MapWithoutReturnDtypeWarning,
        NoDataError,
        OutOfBoundsError,
        PanicException,
        PerformanceWarning,
        PolarsError,
        PolarsWarning,
        SchemaError,
        SchemaFieldNotFoundError,
        ShapeError,
        SQLInterfaceError,
        SQLSyntaxError,
        StringCacheMismatchError,
        StructFieldNotFoundError,
    )


class RowsError(PolarsError):
    ...


class NoRowsReturnedError(RowsError):
    ...


class TooManyRowsReturnedError(RowsError):
    ...


class ModuleUpgradeRequiredError(ModuleNotFoundError):
    ...


class ParameterCollisionError(PolarsError):
    ...


class UnsuitableSQLError(PolarsError):
    ...


class ChronoFormatWarning(PolarsWarning):
    ...


class CustomUFuncWarning(PolarsWarning):
    ...


class DataOrientationWarning(PolarsWarning):
    ...


class PolarsInefficientMapWarning(PerformanceWarning):
    ...


class UnstableWarning(PolarsWarning):
    ...


class ArgumentRemovedError(TypeError):
    ...


class AttributeRemovedError(AttributeError):
    ...


__all__ = ([
    # Errors
    "PolarsError",
    "ArgumentRemovedError",
    "AttributeRemovedError",
    "ColumnNotFoundError",
    "ComputeError",
    "DuplicateError",
    "InvalidOperationError",
    "ModuleUpgradeRequiredError",
    "NoDataError",
    "NoRowsReturnedError",
    "OutOfBoundsError",
    "ParameterCollisionError",
    "RowsError",
    "SQLInterfaceError",
    "SQLSyntaxError",
    "SchemaError",
    "SchemaFieldNotFoundError",
    "ShapeError",
    "StringCacheMismatchError",
    "StructFieldNotFoundError",
    "TooManyRowsReturnedError",
    "UnsuitableSQLError",
    # Warnings
    "PolarsWarning",
    "CategoricalRemappingWarning",
    "ChronoFormatWarning",
    "CustomUFuncWarning",
    "DataOrientationWarning",
    "MapWithoutReturnDtypeWarning",
    "PerformanceWarning",
    "PolarsInefficientMapWarning",
    "UnstableWarning",
    # Panic
    "PanicException",
])
