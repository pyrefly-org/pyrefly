from polars._typing import PolarsDataType
from polars.datatypes.classes import Array, List, Struct


def dtype_to_init_repr(dtype: PolarsDataType, prefix: str = "pl.") -> str: ...
