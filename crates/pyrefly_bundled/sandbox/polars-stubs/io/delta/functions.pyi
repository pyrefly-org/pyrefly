from __future__ import annotations
import importlib
import importlib.util
from typing import TYPE_CHECKING, Any
from polars._utils.expired import RemovedParameter, removed_parameters
from polars._utils.wrap import wrap_ldf
from polars.io.cloud._utils import NoPickleOption
from polars.io.delta._dataset import DeltaDataset
from datetime import datetime
from pathlib import Path
from typing import Literal
from deltalake import DeltaTable
from polars import DataFrame, LazyFrame
from polars._typing import StorageOptionsDict
from polars.io.cloud import CredentialProviderFunction


@removed_parameters(
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
def read_delta(source: str | Path | DeltaTable, *, version: int | str | datetime | None = None, columns: list[str] | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", delta_table_options: dict[str, Any] | None = None, use_pyarrow: bool = False, pyarrow_options: dict[str, Any] | None = None) -> DataFrame: ...


@removed_parameters(
    RemovedParameter(
        name="rechunk",
        removed_in="2.0",
        hint="call `rechunk()` on the resulting Dataframe if you need contiguous memory.",
    ),
)
def scan_delta(source: str | Path | DeltaTable, *, version: int | str | datetime | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto", delta_table_options: dict[str, Any] | None = None, use_pyarrow: bool = False, pyarrow_options: dict[str, Any] | None = None) -> LazyFrame: ...
