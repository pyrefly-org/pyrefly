from __future__ import annotations
import contextlib
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Literal, TypedDict, get_args
from polars._dependencies import json
from polars._typing import EngineType
from polars._utils.expired import getattr_fallback, raise_for_removed_attributes
from polars._utils.monitoring import (
    MONITORING_ENV_VAR,
    MONITORING_ORGANIZATION_ENV_VAR,
    MONITORING_WORKSPACE_ENV_VAR,
    activate_monitoring,
)
from polars._utils.unstable import unstable
from polars._utils.various import normalize_filepath
from polars.lazyframe.engine import Engine
from polars.lazyframe.engine_config import (
    SUPPORTED_ENGINE_NAMES,
    get_engine_affinity_override,
    set_engine_affinity_override,
)
from collections.abc import Callable
from types import TracebackType
from typing import Self, TypeAlias, Unpack
from polars._typing import Alignment, EngineType, FloatFmt
from polars.io.cloud.credential_provider._providers import (
        CredentialProviderFunction,
    )

__all__ = ["Config"]


class Config(contextlib.ContextDecorator, metaclass=_Meta):
    def __init__(self, *, restore_defaults: bool = False, apply_on_context_enter: bool = False, **options: Unpack[ConfigParameters]) -> None: ...

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

    def __eq__(self, other: object) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    @classmethod
    def load(cls, cfg: str) -> Config: ...

    @classmethod
    def load_from_file(cls, file: Path | str) -> Config: ...

    @classmethod
    def restore_defaults(cls) -> type[Config]: ...

    @classmethod
    def save(cls, *, if_set: bool = False) -> str: ...

    @classmethod
    def save_to_file(cls, file: Path | str) -> None: ...

    @classmethod
    def state(cls, *, if_set: bool = False, env_only: bool = False) -> dict[str, str | None]: ...

    @classmethod
    def set_ascii_tables(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_decimal_separator(cls, separator: str | None = None) -> type[Config]: ...

    @classmethod
    def set_thousands_separator(cls, separator: str | bool | None = None) -> type[Config]: ...

    @classmethod
    def set_float_precision(cls, precision: int | None = None) -> type[Config]: ...

    @classmethod
    def set_fmt_float(cls, fmt: FloatFmt | None = "mixed") -> type[Config]: ...

    @classmethod
    def set_fmt_str_lengths(cls, n: int | None) -> type[Config]: ...

    @classmethod
    def set_fmt_table_cell_list_len(cls, n: int | None) -> type[Config]: ...

    @classmethod
    def set_streaming_chunk_size(cls, size: int | None) -> type[Config]: ...

    @classmethod
    def set_tbl_cell_alignment(cls, format: Alignment | None) -> type[Config]: ...

    @classmethod
    def set_tbl_cell_numeric_alignment(cls, format: Alignment | None) -> type[Config]: ...

    @classmethod
    def set_tbl_cols(cls, n: int | None) -> type[Config]: ...

    @classmethod
    def set_tbl_column_data_type_inline(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_dataframe_shape_below(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_formatting(cls, format: TableFormatNames | None = None, rounded_corners: bool | None = False) -> type[Config]: ...

    @classmethod
    def set_tbl_hide_column_data_types(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_hide_column_names(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_hide_dtype_separator(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_hide_dataframe_shape(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_tbl_rows(cls, n: int | None) -> type[Config]: ...

    @classmethod
    def set_tbl_width_chars(cls, width: int | None) -> type[Config]: ...

    @classmethod
    def set_trim_decimal_zeros(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_verbose(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def warn_unstable(cls, active: bool | None = True) -> type[Config]: ...

    @classmethod
    def set_expr_depth_warning(cls, limit: int) -> type[Config]: ...

    @classmethod
    def set_engine_affinity(cls, engine: EngineType | None = None) -> type[Config]: ...

    @classmethod
    def enable_monitoring(cls, active: bool | None = True, *, workspace: str | None = None, organization: str | None = None) -> type[Config]: ...

    @classmethod
    @unstable()
    def set_default_credential_provider(cls, credential_provider: CredentialProviderFunction | Literal["auto"] | None) -> type[Config]: ...

    @classmethod
    def reload_env_vars(cls) -> None: ...
