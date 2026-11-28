from __future__ import annotations
import io
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal
from polars._utils.unstable import issue_unstable_warning
from polars._utils.various import normalize_filepath, qualified_type_name
from polars._utils.wrap import wrap_df, wrap_ldf
from collections.abc import Callable
from typing import IO
from polars._typing import (
        ArrowSchemaExportable,
        CsvQuoteStyle,
        IpcCompression,
        ParquetCompression,
        ParquetMetadata,
        StorageOptionsDict,
        SyncOnCloseMethod,
    )
from polars.dataframe import DataFrame
from polars.interchange.protocol import CompatLevel
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.encryption import ParquetEncryptionProperties
from polars.io.partition import PartitionBy, SinkedPathsCallback
from polars.lazyframe.frame import LazyFrame
