from __future__ import annotations
import re
import sys
from polars._cpu_check import get_runtime_repr
from polars._utils.polars_version import get_polars_build_commit, get_polars_version
from polars.meta.index_type import get_index_type


def show_versions() -> None: ...
