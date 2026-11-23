from __future__ import annotations
from collections.abc import Collection
from typing import TYPE_CHECKING, Literal, TypeVar
from polars._utils.unstable import issue_unstable_warning
from typing import TypeAlias

FloatCastOption: TypeAlias = Literal["upcast", "downcast", "forbid"]
IntegerCastOption: TypeAlias = Literal["upcast", "allow-float", "forbid"]
DatetimeCastOption: TypeAlias = (Literal[
    "convert-timezone",
    "nanosecond-downcast",
    "microsecond-downcast",
    "microsecond-upcast",
    "millisecond-upcast",
    "downcast",
    "upcast",
    "forbid",
])


class ScanCastOptions:
    integer_cast: _CastConfig[IntegerCastOption]
    float_cast: _CastConfig[FloatCastOption]
    datetime_cast: _CastConfig[DatetimeCastOption]
    missing_struct_fields: Literal["insert", "raise"]
    extra_struct_fields: Literal["ignore", "raise"]
    categorical_to_string: Literal["allow", "forbid"]

    def __init__(self, *, integer_cast: _CastConfig[IntegerCastOption] = "forbid", float_cast: _CastConfig[FloatCastOption] = "forbid", datetime_cast: _CastConfig[DatetimeCastOption] = "forbid", missing_struct_fields: Literal["insert", "raise"] = "raise", extra_struct_fields: Literal["ignore", "raise"] = "raise", categorical_to_string: Literal["allow", "forbid"] = "forbid", _internal_call: bool = False) -> None: ...
