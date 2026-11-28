from __future__ import annotations
from abc import ABC, abstractmethod
from functools import partial
from typing import IO, TYPE_CHECKING, Any, ClassVar, Literal, overload
from polars._dependencies import import_optional
from polars._utils.async_ import _AioDataFrameResult, _GeventDataFrameResult
from polars._utils.unstable import issue_unstable_warning
from polars._utils.wrap import wrap_df
from polars._warnings import issue_warning
from polars.lazyframe.in_process import InProcessQuery
from polars.lazyframe.query_result import SingleNodeQueryResult
from polars.lazyframe.sink_plan import (
    _sink_batches_plan,
    _sink_csv_plan,
    _sink_ipc_plan,
    _sink_ndjson_plan,
    _sink_parquet_plan,
)
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path
from rmm.mr import DeviceMemoryResource
from polars._plr import PyCollectBatches
from polars._typing import (
        ArrowSchemaExportable,
        AsyncResult,
        CsvQuoteStyle,
        IpcCompression,
        ParquetCompression,
        ParquetMetadata,
        PostOptCallback,
        StorageOptionsDict,
        SyncOnCloseMethod,
    )
from polars.dataframe import DataFrame
from polars.interchange.protocol import CompatLevel
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.encryption import ParquetEncryptionProperties
from polars.io.partition import PartitionBy, SinkedPathsCallback
from polars.lazyframe.frame import LazyFrame
from polars.lazyframe.opt_flags import QueryOptFlags
from polars.lazyframe.query_result import QueryResult


class Engine(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    def plan_engine(self) -> str: ...

    def __repr__(self) -> str: ...

    @overload
    def collect(self, lf: LazyFrame, *, optimizations: QueryOptFlags, background: Literal[False] = ..., post_opt_callback: PostOptCallback | None = ...) -> DataFrame: ...

    @overload
    def collect(self, lf: LazyFrame, *, optimizations: QueryOptFlags, background: Literal[True], post_opt_callback: PostOptCallback | None = ...) -> InProcessQuery: ...

    @overload
    def collect(self, lf: LazyFrame, *, optimizations: QueryOptFlags, background: bool, post_opt_callback: PostOptCallback | None = ...) -> DataFrame | InProcessQuery: ...

    @abstractmethod
    def execute(self, lf: LazyFrame, *, optimizations: QueryOptFlags) -> QueryResult: ...

    def collect_async(self, lf: LazyFrame, *, optimizations: QueryOptFlags, gevent: bool = False) -> AsyncResult[DataFrame]: ...

    def collect_batches(self, lf: LazyFrame, *, optimizations: QueryOptFlags, maintain_order: bool = True, chunk_size: int | None = None, lazy: bool = False) -> _CollectBatches: ...

    def collect_all(self, lfs: Iterable[LazyFrame], *, optimizations: QueryOptFlags) -> list[DataFrame]: ...

    def collect_all_async(self, lfs: Iterable[LazyFrame], *, optimizations: QueryOptFlags, gevent: bool = False) -> AsyncResult[list[DataFrame]]: ...

    def sink_parquet(self, lf: LazyFrame, path: str | Path | IO[bytes] | PartitionBy, *, compression: ParquetCompression, compression_level: int | None, statistics: bool | str | dict[str, bool], row_group_size: int | None, data_page_size: int | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, metadata: ParquetMetadata | None, arrow_schema: ArrowSchemaExportable | None, encryption: ParquetEncryptionProperties | None, mkdir: bool, optimizations: QueryOptFlags, sinked_paths_callback: SinkedPathsCallback | None) -> None: ...

    def sink_ipc(self, lf: LazyFrame, path: str | Path | IO[bytes] | PartitionBy, *, compression: IpcCompression | None, compat_level: CompatLevel | None, record_batch_size: int | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, mkdir: bool, optimizations: QueryOptFlags, _record_batch_statistics: bool, sinked_paths_callback: SinkedPathsCallback | None) -> None: ...

    def sink_csv(self, lf: LazyFrame, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, include_bom: bool, compression: Literal["uncompressed", "gzip", "zstd"], compression_level: int | None, check_extension: bool, include_header: bool, separator: str, line_terminator: str, quote_char: str, batch_size: int, datetime_format: str | None, date_format: str | None, time_format: str | None, float_scientific: bool | None, float_precision: int | None, decimal_comma: bool, null_value: str | None, quote_style: CsvQuoteStyle | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, mkdir: bool, optimizations: QueryOptFlags) -> None: ...

    def sink_ndjson(self, lf: LazyFrame, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, compression: Literal["uncompressed", "gzip", "zstd"], compression_level: int | None, check_extension: bool, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, mkdir: bool, optimizations: QueryOptFlags) -> None: ...

    def sink_batches(self, lf: LazyFrame, function: Callable[[DataFrame], bool | None], *, chunk_size: int | None, maintain_order: bool, optimizations: QueryOptFlags) -> None: ...


class InMemoryEngine(_LocalEngine):
    ...


class StreamingEngine(_LocalEngine):
    ...


class GPUEngine(_LocalEngine):
    device: int | None
    memory_resource: DeviceMemoryResource | None
    raise_on_fail: bool
    config: Mapping[str, Any]

    def __init__(self, *, device: int | None = None, memory_resource: Any | None = None, raise_on_fail: bool = False, monitoring: bool = False, **kwargs: Any) -> None: ...
