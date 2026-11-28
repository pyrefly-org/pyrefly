from __future__ import annotations
import importlib
from typing import TYPE_CHECKING, Literal
from polars.io.cloud._utils import NoPickleOption
from polars.io.lance._scan_resolver import LanceScanResolver
import lance
import lancedb
from lance import LanceDataset
import polars as pl
from polars._typing import StorageOptionsDict
from polars.io.cloud.credential_provider._providers import (
        CredentialProviderFunction,
    )


def scan_lance(source: str | lance.LanceDataset | lancedb.Table, *, version: int | str | None = None, storage_options: StorageOptionsDict | None = None, credential_provider: CredentialProviderFunction | Literal["auto"] | None = "auto") -> pl.LazyFrame: ...
