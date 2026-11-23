from __future__ import annotations
import contextlib
from typing import Any
from polars._utils.deprecation import deprecate_renamed_parameter
from polars._utils.expired import RenamedParameter, removed_parameters
from polars.series import Series
from polars.testing.asserts.utils import raise_assertion_error


@removed_parameters(
    RenamedParameter(
        name="check_dtype",
        new_name="check_dtypes",
        deprecated_in="0.20.31",
        removed_in="2.0",
    ),
)
@deprecate_renamed_parameter("rtol", "rel_tol", version="1.32.3")
@deprecate_renamed_parameter("atol", "abs_tol", version="1.32.3")
def assert_series_equal(left: Series, right: Series, *, check_dtypes: bool = True, check_names: bool = True, check_order: bool = True, check_exact: bool = False, rel_tol: float = 1e-5, abs_tol: float = 1e-8, categorical_as_str: bool = False) -> None: ...


@removed_parameters(
    RenamedParameter(
        name="check_dtype",
        new_name="check_dtypes",
        deprecated_in="0.20.31",
        removed_in="2.0",
    ),
)
@deprecate_renamed_parameter("rtol", "rel_tol", version="1.32.3")
@deprecate_renamed_parameter("atol", "abs_tol", version="1.32.3")
def assert_series_not_equal(left: Series, right: Series, *, check_dtypes: bool = True, check_names: bool = True, check_order: bool = True, check_exact: bool = False, rel_tol: float = 1e-5, abs_tol: float = 1e-8, categorical_as_str: bool = False) -> None: ...
