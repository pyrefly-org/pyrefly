from __future__ import annotations
import contextlib
from typing import IO, TYPE_CHECKING, Literal
from polars._utils.unstable import unstable
from polars._utils.wrap import wrap_ldf
from polars.io._utils import get_sources
from polars.io.cloud.credential_provider._builder import (
    _init_credential_provider_builder,
)
from polars.io.scan_options._options import ScanOptions
from pathlib import Path
from polars._typing import StorageOptionsDict
from polars.dataframe.frame import DataFrame
from polars.io.cloud import CredentialProviderFunction
from polars.lazyframe.frame import LazyFrame


@unstable()
def read_lines(source: (str
        | Path
        | IO[str]
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[str]]
        | list[IO[bytes]]), *, name: str = "line", n_rows: int | None = None, row_index_name: str | None = None, row_index_offset: int = 0, glob: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None) -> DataFrame: ...


@unstable()
def scan_lines(source: (str
        | Path
        | IO[str]
        | IO[bytes]
        | bytes
        | list[str]
        | list[Path]
        | list[IO[str]]
        | list[IO[bytes]]), *, name: str = "line", n_rows: int | None = None, row_index_name: str | None = None, row_index_offset: int = 0, glob: bool = True, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", include_file_paths: str | None = None) -> LazyFrame: ...
