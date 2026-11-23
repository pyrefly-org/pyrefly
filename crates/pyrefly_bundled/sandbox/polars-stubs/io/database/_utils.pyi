from __future__ import annotations
import re
from importlib import import_module
from typing import TYPE_CHECKING, Any
from polars._dependencies import _PYARROW_AVAILABLE, import_optional
from polars._utils.various import parse_version
from polars.exceptions import ModuleUpgradeRequiredError
from collections.abc import Coroutine
from polars import DataFrame
from polars._typing import SchemaDict
