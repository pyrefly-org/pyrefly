from _typeshed import Incomplete

from __future__ import annotations
import contextlib
import queue
import threading
from concurrent.futures import CancelledError, ThreadPoolExecutor
from typing import TYPE_CHECKING, Any
import polars._utils.logging
from polars._utils.logging import eprint
from polars.io.external_reader import (
    FileReader,
    FileReaderBuilder,
)
from polars.io.external_reader._external_reader import ReaderCapabilities
from collections.abc import Iterator, Sequence
from concurrent.futures import Future
import lance
import pyarrow as pa
import pyarrow.compute as pc
import polars as pl
from polars._typing import SchemaDict
from polars.io.external_reader import (
        FilterExpr,
    )

CX_LOCK: threading.RLock
CX_PREV_READER_START_EVENT_KEY: object
CX_THREADPOOL_KEY: object
CX_ERROR_KEY: object
CX_INFLIGHT_ROWS_KEY: object
CX_CONSUMED_ROWS_KEY: object
CX_TARGET_INFLIGHT_ROWS_KEY: object
TARGET_MORSEL_SIZE: int = 100_000


class LanceReaderBuilder(FileReaderBuilder):
    dataset: Incomplete
    filter: Incomplete
    projected_schema: Mapping[str, DataType | DataTypeClass]

    def __init__(self, *, dataset: lance.LanceDataset, projected_schema: SchemaDict, filter: pc.Expression | None = None) -> None: ...

    def explain_properties(self) -> dict[str, str]: ...

    def reader_capabilities(self) -> ReaderCapabilities: ...

    def build_file_reader(self, source: str | bytes, multi_scan_context: dict[Any, Any]) -> LanceFragmentReader: ...


class LanceFragmentReader(FileReader):
    consumed_rows_queue: Queue[int] | None
    dataset: Incomplete
    filter: Incomplete
    fragment_ids: Sequence[int]
    fragments_cached: Incomplete
    multi_scan_context: dict[Any, Any]
    n_physical_rows_cached: int | None
    n_rows_in_file_cached: int | None
    prev_reader_start_event: Incomplete
    projected_schema: Mapping[str, DataType | DataTypeClass]
    this_reader_inflight_rows: int
    this_reader_start_event: Event

    def __init__(self, *, dataset: lance.LanceDataset, fragment_ids: Sequence[int], projected_schema: SchemaDict, filter: pc.Expression | None, multi_scan_context: dict[Any, Any]) -> None: ...

    def initialize_serial(self) -> None: ...

    def on_drop(self) -> None: ...

    def schema(self) -> SchemaDict: ...

    def collect_batches(self, *, columns: Sequence[str] = (), row_index: tuple[str, int] | None = None, pre_slice: tuple[int, int] | None = None, filters: Sequence[FilterExpr] = (), num_pipelines: int) -> Iterator[pl.DataFrame]: ...

    def n_rows_in_file(self, limit: int | None = None) -> int: ...

    def n_physical_rows(self) -> int: ...

    def get_fragments(self) -> list[lance.LanceFragment]: ...


def send_arrow_batches(*, fut_queue: queue.Queue[Future[pl.DataFrame] | None], batches_iter: Iterator[pa.RecordBatch], conversion_threadpool: ThreadPoolExecutor, slice_offset: int, row_index: tuple[str, int] | None, rx_closed: threading.Event, multi_scan_context: dict[Any, Any]) -> None: ...


def process_arrow_batch_to_polars_df(*, pyarrow_batch: pa.RecordBatch, phys_position: int, batch_slice_offset: int, row_index: tuple[str, int] | None) -> pl.DataFrame: ...


class ThreadPoolSubmitError(Exception):
    ...
