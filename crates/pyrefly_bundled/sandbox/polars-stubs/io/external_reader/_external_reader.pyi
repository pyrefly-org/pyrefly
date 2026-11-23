from typing import Literal

from __future__ import annotations
import abc
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, TypeAlias
from collections.abc import Iterator, Sequence
from polars._typing import SchemaDict
from polars.dataframe.frame import DataFrame
from polars.lazyframe.resolver import FilterExpr

FilterSupport: TypeAlias = Literal["partial", "full"]


class FileReaderBuilder(abc.ABC):
    def reader_capabilities(self) -> ReaderCapabilities: ...

    @abc.abstractmethod
    def build_file_reader(self, source: str | bytes, multi_scan_context: dict[Any, Any]) -> FileReader: ...

    def explain_properties(self) -> dict[str, str]: ...


class FileReader(abc.ABC):
    @abc.abstractmethod
    def schema(self) -> SchemaDict: ...

    def fetch_metadata(self) -> None: ...

    def initialize_serial(self) -> None: ...

    @abc.abstractmethod
    def collect_batches(self, *, columns: Sequence[str], row_index: tuple[str, int] | None, pre_slice: tuple[int, int] | None, filters: Sequence[FilterExpr], num_pipelines: int) -> Iterator[DataFrame]: ...

    @abc.abstractmethod
    def n_rows_in_file(self, limit: int | None = None) -> int: ...

    def on_drop(self) -> None: ...


@dataclass
class ReaderCapabilities:
    row_index: bool = False
    pre_slice: bool = False
    negative_pre_slice: bool = False
    supported_filter: FilterSupport | None = None

    def __init__(self, row_index: bool = ..., pre_slice: bool = ..., negative_pre_slice: bool = ..., supported_filter: Literal['full', 'partial'] | None = ...) -> None: ...


def send_dfs(dfs_iter: Iterator[DataFrame], tx: Any) -> None: ...
