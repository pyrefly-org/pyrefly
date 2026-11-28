from typing import Literal

import builtins
import os
import sys
from polars._cpu_check import check_cpu_flags

PKG_VERSION: Literal['2.1.0'] = "2.1.0"


def rt_compat() -> None: ...


def rt_64() -> None: ...


def rt_32() -> None: ...
