from typing import Literal
from _typeshed import Incomplete

from __future__ import annotations
import hashlib
import io
import itertools
import os
import re
import threading
import weakref
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath
from typing import TYPE_CHECKING, Any
from polars._utils.various import qualified_type_name
from collections.abc import Callable, Mapping
from pyiceberg.io import FileIO, InputFile, InputStream
from pyiceberg.table import StaticTable

ENV_METADATA_FILE_CACHE_MB: Literal['POLARS_ICEBERG_METADATA_FILE_CACHE_MB'] = "POLARS_ICEBERG_METADATA_FILE_CACHE_MB"
DEFAULT_METADATA_FILE_CACHE_MB: Literal[64] = 64


def plugin_storage_scope(file_io: FileIO, storage_options: Mapping[str, Any] | None) -> str | None: ...


@dataclass
class CacheStats:
    hits: int = 0
    misses: int = 0
    too_large: int = 0
    evicted: int = 0
    bypass: str | None = None

    def describe(self, cache: IcebergMetadataFileCache) -> str: ...

    def __init__(self, hits: int = ..., misses: int = ..., too_large: int = ..., evicted: int = ..., bypass: str | None = ...) -> None: ...


class IcebergMetadataFileCache:
    max_bytes: int

    def __init__(self, max_bytes: int) -> None: ...

    @property
    def enabled(self) -> bool: ...

    def __len__(self) -> int: ...

    @property
    def total_bytes(self) -> int: ...

    def plugin_cache(self) -> Any: ...

    def get(self, location: str) -> bytes | None: ...

    def put(self, location: str, data: bytes, stats: CacheStats | None = None) -> None: ...

    def get_or_fetch(self, location: str, fetch: Callable[[], bytes], stats: CacheStats) -> bytes: ...


def get_metadata_file_cache() -> IcebergMetadataFileCache: ...


def reset_metadata_file_cache() -> None: ...


def load_static_table(metadata_location: str, properties: dict[str, Any]) -> tuple[StaticTable, CacheStats]: ...


class CachedInputFile:
    def __init__(self, inner: FileIO, location: str, cache: IcebergMetadataFileCache, scope: str, stats: CacheStats) -> None: ...

    @property
    def location(self) -> str: ...

    def __len__(self) -> int: ...

    def exists(self) -> bool: ...

    def open(self, seekable: bool = True) -> InputStream: ...


class CachingFileIO:
    properties: Incomplete
    stats: CacheStats

    def __init__(self, inner: FileIO, cache: IcebergMetadataFileCache) -> None: ...

    @property
    def cache(self) -> IcebergMetadataFileCache: ...

    def new_input(self, location: str) -> InputFile: ...

    def __getattr__(self, name: str) -> Any: ...

    def __reduce__(self) -> tuple[Any, ...]: ...


def describe_metadata_file_cache(file_io: FileIO) -> str: ...


def with_metadata_file_cache(scan: Any) -> Any: ...
