from __future__ import annotations
import warnings
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any
from polars._dependencies import _DELTALAKE_AVAILABLE, deltalake
from polars._utils.logging import eprint
from polars.datatypes import Null, Time
from polars.datatypes.convert import unpack_dtypes
from polars.io._utils import null_count_dtype
from polars.io.cloud._utils import POLARS_STORAGE_CONFIG_KEYS, _get_path_scheme
from collections.abc import Sequence
from deltalake import DeltaTable
from polars import DataFrame, DataType, Series
from polars._typing import PolarsDataType, SchemaDict, StorageOptionsDict
