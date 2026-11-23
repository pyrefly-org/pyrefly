from __future__ import annotations
from typing import IO, TYPE_CHECKING, Any, Literal, get_args
from polars._dependencies import import_optional, polars_cloud
from polars._typing import EngineTypeName, ScalingMode
from polars._utils.various import qualified_type_name
from polars.lazyframe.engine import Engine
from collections.abc import Mapping
from pathlib import Path
import polars_cloud as pc
from polars._typing import (
        ArrowSchemaExportable,
        CsvQuoteStyle,
        IpcCompression,
        ParquetCompression,
        ParquetMetadata,
        PlanTypePreference,
        PostOptCallback,
        StorageOptionsDict,
        SyncOnCloseMethod,
    )
from polars.dataframe import DataFrame
from polars.interchange.protocol import CompatLevel
from polars.io.cloud import CredentialProviderFunction
from polars.io.parquet.encryption import ParquetEncryptionProperties
from polars.io.partition import PartitionBy, SinkedPathsCallback
from polars.lazyframe.engine import _CollectBatches
from polars.lazyframe.frame import LazyFrame
from polars.lazyframe.opt_flags import QueryOptFlags
from polars.lazyframe.query_result import QueryResult


class RemoteEngine(Engine):
    context: pc.ClientContext | None
    scaling_mode: ScalingMode
    engine: EngineTypeName
    plan_type: PlanTypePreference
    n_retries: int
    labels: list[str] | None
    config: Mapping[str, Any]

    def __init__(self, context: pc.ClientContext | None = None, *, scaling_mode: ScalingMode = "auto", engine: EngineTypeName = "auto", plan_type: PlanTypePreference = "dot", n_retries: int = 0, labels: list[str] | str | None = None, **kwargs: Any) -> None: ...

    @property
    def name(self) -> str: ...

    @property
    def plan_engine(self) -> str: ...

    def execute(self, lf: LazyFrame, *, optimizations: QueryOptFlags) -> QueryResult: ...

    def collect(self, lf: LazyFrame, *, optimizations: QueryOptFlags, background: bool = False, post_opt_callback: PostOptCallback | None = None) -> DataFrame: ...

    def collect_batches(self, lf: LazyFrame, *, optimizations: QueryOptFlags, maintain_order: bool = True, chunk_size: int | None = None, lazy: bool = False) -> _CollectBatches: ...

    def sink_parquet(self, lf: LazyFrame, path: str | Path | IO[bytes] | PartitionBy, *, compression: ParquetCompression, compression_level: int | None, statistics: bool | str | dict[str, bool], row_group_size: int | None, data_page_size: int | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, metadata: ParquetMetadata | None, arrow_schema: ArrowSchemaExportable | None, encryption: ParquetEncryptionProperties | None, mkdir: bool, optimizations: QueryOptFlags, sinked_paths_callback: SinkedPathsCallback | None) -> None: ...

    def sink_ipc(self, lf: LazyFrame, path: str | Path | IO[bytes] | PartitionBy, *, compression: IpcCompression | None, compat_level: CompatLevel | None, record_batch_size: int | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, mkdir: bool, optimizations: QueryOptFlags, _record_batch_statistics: bool, sinked_paths_callback: SinkedPathsCallback | None) -> None: ...

    def sink_csv(self, lf: LazyFrame, path: str | Path | IO[bytes] | IO[str] | PartitionBy, *, include_bom: bool, compression: Literal["uncompressed", "gzip", "zstd"], compression_level: int | None, check_extension: bool, include_header: bool, separator: str, line_terminator: str, quote_char: str, batch_size: int, datetime_format: str | None, date_format: str | None, time_format: str | None, float_scientific: bool | None, float_precision: int | None, decimal_comma: bool, null_value: str | None, quote_style: CsvQuoteStyle | None, maintain_order: bool, storage_options: StorageOptionsDict | None, credential_provider: CredentialProviderFunction | Literal["auto"] | None, sync_on_close: SyncOnCloseMethod | None, mkdir: bool, optimizations: QueryOptFlags) -> None: ...
