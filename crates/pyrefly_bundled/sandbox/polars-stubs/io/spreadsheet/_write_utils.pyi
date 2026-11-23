from __future__ import annotations
from collections.abc import Mapping, Sequence
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, overload
from polars import functions as F
from polars._dependencies import json
from polars._utils.various import qualified_type_name
from polars.datatypes import (
    Date,
    Datetime,
    Float64,
    Int64,
    Time,
)
from polars.datatypes.group import FLOAT_DTYPES, INTEGER_DTYPES
from polars.exceptions import DuplicateError
from polars.selectors import (
    _expand_selector_dicts,
    _expand_selector_dicts_tuple_keys,
    _expand_selectors,
    numeric,
)
from collections.abc import Iterable
from typing import Literal
from xlsxwriter import Workbook
from xlsxwriter.format import Format
from xlsxwriter.worksheet import Worksheet
from polars import DataFrame, Schema, Series
from polars._typing import (
        ColumnFormatDict,
        ColumnTotalsDefinition,
        ConditionalFormatDict,
        OneOrMoreDataTypes,
        PolarsDataType,
        RowTotalsDefinition,
    )
from polars.expr import Expr
