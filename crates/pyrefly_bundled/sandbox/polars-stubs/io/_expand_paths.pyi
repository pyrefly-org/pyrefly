from __future__ import annotations
import contextlib
from typing import IO, TYPE_CHECKING, Literal
from polars._utils.wrap import wrap_ldf
from polars.io._utils import get_sources
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.scan_options._options import ScanOptions
from collections.abc import Sequence
from pathlib import Path
from polars._typing import StorageOptionsDict
from polars.io.cloud import CredentialProviderFunction
from polars.lazyframe.frame import LazyFrame
