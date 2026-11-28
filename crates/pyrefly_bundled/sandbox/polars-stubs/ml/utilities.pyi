from typing import Any
from polars import DataFrame
from polars._dependencies import numpy as np
from polars._typing import IndexOrder
from polars.datatypes import Array, List


def frame_to_numpy(df: DataFrame, *, writable: bool, target: str, order: IndexOrder = "fortran") -> np.ndarray[Any, Any]: ...
