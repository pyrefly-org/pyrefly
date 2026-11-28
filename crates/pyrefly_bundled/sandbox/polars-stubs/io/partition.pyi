from __future__ import annotations
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Literal, TypeAlias
from polars._utils.parse.expr import parse_into_list_of_expressions
from polars._utils.unstable import issue_unstable_warning
import contextlib
from pathlib import Path
from polars import DataFrame
from collections.abc import Sequence
from typing import IO
from polars._typing import StorageOptionsDict, SyncOnCloseMethod
from polars.expr import Expr
from polars.io.cloud.credential_provider._builder import CredentialProviderBuilder


class PartitionBy:
    def __init__(self, base_path: str | Path, *, file_path_provider: (Callable[
            [FileProviderArgs], str | Path | IO[bytes] | IO[str]
        ]
        | _InternalPlPathProviderConfig
        | None) = None, key: str | Expr | Sequence[str | Expr] | Mapping[str, Expr] | None = None, include_key: bool | None = None, max_rows_per_file: int | None = None, approximate_bytes_per_file: int | Literal["auto"] | None = "auto") -> None: ...


@dataclass(kw_only=True)
class FileProviderArgs:
    index_in_partition: int
    partition_keys: DataFrame

    def __init__(self, *, index_in_partition: int, partition_keys: DataFrame) -> None: ...


@dataclass(kw_only=True)
class SinkedPathsCallbackArgs:
    paths: list[SinkedPath]

    def __init__(self, *, paths: list[SinkedPath]) -> None: ...


@dataclass(kw_only=True)
class SinkedPath:
    path: str
    num_rows: int
    num_bytes: int

    def __init__(self, *, path: str, num_rows: int, num_bytes: int) -> None: ...


SinkedPathsCallback: TypeAlias = Callable[[SinkedPathsCallbackArgs], None]
