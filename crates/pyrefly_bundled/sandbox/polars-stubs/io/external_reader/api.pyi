from polars._typing import FileSource, SchemaDict
from polars._utils.wrap import wrap_ldf
from polars.io.external_reader._external_reader import FileReaderBuilder
from polars.io.scan_options._options import ScanOptions
from polars.lazyframe.frame import LazyFrame


def scan_external_reader(reader_builder: FileReaderBuilder, *, sources: FileSource, schema: SchemaDict, expand_paths: bool = False) -> LazyFrame: ...
