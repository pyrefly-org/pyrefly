from typing import Literal

from __future__ import annotations
import re
import sys
from functools import cache
from importlib import import_module
from importlib.util import find_spec
from types import ModuleType
from typing import TYPE_CHECKING, Any, ClassVar, cast
from collections.abc import Hashable

_ALTAIR_AVAILABLE: Literal[True] = True
_DELTALAKE_AVAILABLE: Literal[True] = True
_FSSPEC_AVAILABLE: Literal[True] = True
_GEVENT_AVAILABLE: Literal[True] = True
_GREAT_TABLES_AVAILABLE: Literal[True] = True
_HYPOTHESIS_AVAILABLE: Literal[True] = True
_NUMPY_AVAILABLE: Literal[True] = True
_PANDAS_AVAILABLE: Literal[True] = True
_POLARS_CLOUD_AVAILABLE: Literal[True] = True
_PYARROW_AVAILABLE: Literal[True] = True
_PYDANTIC_AVAILABLE: Literal[True] = True
_PYICEBERG_AVAILABLE: Literal[True] = True
_TORCH_AVAILABLE: Literal[True] = True

import dataclasses
import html
import json
import pickle
import subprocess
import altair
import boto3
import deltalake
import fsspec
import gevent
import great_tables
import hypothesis
import numpy
import pandas
import polars_cloud
import pyarrow
import pydantic
import pyiceberg
import pyiceberg.schema
import pytz
import torch


def _check_for_numpy(obj: Any, *, check_type: bool = True) -> bool: ...


def _check_for_pandas(obj: Any, *, check_type: bool = True) -> bool: ...


def _check_for_pyarrow(obj: Any, *, check_type: bool = True) -> bool: ...


def _check_for_pydantic(obj: Any, *, check_type: bool = True) -> bool: ...


def _check_for_torch(obj: Any, *, check_type: bool = True) -> bool: ...


def _check_for_pytz(obj: Any, *, check_type: bool = True) -> bool: ...


__all__ = ([
    # lazy-load rarely-used/heavy builtins (for fast startup)
    "dataclasses",
    "html",
    "json",
    "pickle",
    "subprocess",
    # lazy-load third party libs
    "altair",
    "boto3",
    "deltalake",
    "fsspec",
    "gevent",
    "great_tables",
    "numpy",
    "pandas",
    "polars_cloud",
    "pydantic",
    "pyiceberg",
    "pyarrow",
    "torch",
    "pytz",
    # lazy utilities
    "_check_for_numpy",
    "_check_for_pandas",
    "_check_for_pyarrow",
    "_check_for_pydantic",
    "_check_for_torch",
    "_check_for_pytz",
    # exported flags/guards
    "_ALTAIR_AVAILABLE",
    "_DELTALAKE_AVAILABLE",
    "_FSSPEC_AVAILABLE",
    "_GEVENT_AVAILABLE",
    "_GREAT_TABLES_AVAILABLE",
    "_HYPOTHESIS_AVAILABLE",
    "_NUMPY_AVAILABLE",
    "_PANDAS_AVAILABLE",
    "_POLARS_CLOUD_AVAILABLE",
    "_PYARROW_AVAILABLE",
    "_PYDANTIC_AVAILABLE",
    "_PYICEBERG_AVAILABLE",
    "_TORCH_AVAILABLE",
])
