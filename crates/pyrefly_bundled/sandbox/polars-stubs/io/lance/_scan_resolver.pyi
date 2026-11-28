from _typeshed import Incomplete

from __future__ import annotations
import operator
from dataclasses import dataclass
from functools import reduce
from time import perf_counter
from typing import TYPE_CHECKING, Any
from polars._utils.logging import eprint
from polars.io.lance._reader import LanceReaderBuilder
from polars.lazyframe.resolver._resolver import (
    LazyFrameResolver,
    ResolvedLazyFrameProps,
)
from polars.schema import Schema
import lance
import pyarrow.compute as pc
import polars as pl
from polars._typing import StorageOptionsDict
from polars.io.cloud._utils import NoPickleOption
from polars.io.cloud.credential_provider._builder import CredentialProviderBuilder
from polars.lazyframe.resolver._resolver import (
        FilterExpr,
    )


@dataclass(kw_only=True)
class LanceScanResolver(LazyFrameResolver):
    dataset_: NoPickleOption[lance.LanceDataset]
    dataset_uri_: str | None
    version: int | str | None
    storage_options: StorageOptionsDict | None
    credential_provider_builder: CredentialProviderBuilder | None

    def schema(self) -> Schema: ...

    def cse_eq(self, other: object) -> bool: ...

    def resolve_lazyframe(self, *, projection: list[str] | None, limit: int | None, filters: list[FilterExpr], filter_columns: list[str], filter_drop_columns_idx: int | None, existing_resolved_version_key: str | None) -> pl.LazyFrame | tuple[pl.LazyFrame | None, ResolvedLazyFrameProps]: ...

    def dataset_uri(self) -> str: ...

    def dataset(self) -> lance.LanceDataset: ...

    def __getstate__(self) -> dict[str, Any]: ...

    def __setstate__(self, state: dict[str, Any]) -> None: ...

    __dict__: dict[str, Any]

    def __init__(self, *, dataset_: Incomplete, dataset_uri_: str | None, version: int | str | None, storage_options: dict[str, Any] | None, credential_provider_builder: CredentialProviderBuilder | None) -> None: ...


def is_filter_supported_by_lance(dataset: lance.LanceDataset, filter: pc.Expression) -> bool: ...
