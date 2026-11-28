from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING
from polars.io.parquet.decryption import _check_bytes
from collections.abc import Mapping


class ParquetEncryptionProperties:
    def __init__(self, *, footer_key: bytes, column_keys: Mapping[str, bytes] | None = None, plaintext_footer: bool = False, aad_prefix: bytes | None = None, store_aad_prefix: bool = False) -> None: ...
