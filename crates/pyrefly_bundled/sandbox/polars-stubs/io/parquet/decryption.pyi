from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Any
from polars._utils.various import qualified_type_name
from collections.abc import Mapping


class ParquetDecryptionProperties:
    def __init__(self, *, footer_key: bytes, column_keys: Mapping[str, bytes] | None = None, aad_prefix: bytes | None = None, verify_footer_signature: bool = True) -> None: ...
