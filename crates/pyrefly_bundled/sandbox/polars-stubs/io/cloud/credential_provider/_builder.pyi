from _typeshed import Incomplete

from __future__ import annotations
import abc
import os
import threading
from copy import copy
from typing import TYPE_CHECKING, Any, Final, Literal
import polars._utils.logging
from polars._utils.cache import LRUCache
from polars._utils.logging import eprint, verbose
from polars._utils.unstable import issue_unstable_warning
from polars.io.cloud._utils import POLARS_STORAGE_CONFIG_KEYS, NoPickleOption
from polars.io.cloud.credential_provider._providers import (
    CachedCredentialProvider,
    CachingCredentialProvider,
    CredentialProvider,
    CredentialProviderAWS,
    CredentialProviderAzure,
    CredentialProviderFunction,
    CredentialProviderGCP,
    UserProvidedGCPToken,
)
from collections.abc import Callable
from typing import TypeAlias
from polars._typing import StorageOptionsDict

AUTOINIT_IGNORED_KEYS: Final[frozenset[str]]
CredentialProviderBuilderReturn: TypeAlias = CredentialProvider | CredentialProviderFunction | None


class CredentialProviderBuilder:
    credential_provider_init: CredentialProviderBuilderImpl

    def __init__(self, credential_provider_init: CredentialProviderBuilderImpl) -> None: ...

    def build_credential_provider(self, clear_cached_credentials: bool = False) -> CredentialProviderBuilderReturn: ...

    @classmethod
    def from_initialized_provider(cls, credential_provider: CredentialProviderFunction) -> CredentialProviderBuilder: ...

    def stable_cache_key(self) -> bytes: ...

    def __getstate__(self) -> Any: ...

    def __setstate__(self, state: Any) -> None: ...

    def __repr__(self) -> str: ...


class CredentialProviderBuilderImpl(abc.ABC):
    @abc.abstractmethod
    def __call__(self) -> CredentialProviderFunction | None: ...

    @property
    @abc.abstractmethod
    def provider_repr(self) -> str: ...

    @abc.abstractmethod
    def stable_cache_key(self) -> bytes: ...

    def __repr__(self) -> str: ...


class InitializedCredentialProvider(CredentialProviderBuilderImpl):
    credential_provider: Incomplete

    def __init__(self, credential_provider: CredentialProviderFunction) -> None: ...

    def __call__(self) -> CredentialProviderBuilderReturn: ...

    def stable_cache_key(self) -> bytes: ...

    @property
    def provider_repr(self) -> str: ...


BUILT_PROVIDERS_LRU_CACHE: LRUCache[int | bytes, CredentialProviderBuilderReturn] | None = None
BUILT_PROVIDERS_LRU_CACHE_LOCK: threading.RLock


class AutoInit(CredentialProviderBuilderImpl):
    cls: Incomplete
    kw: dict[str, Any]

    def __init__(self, cls: Any, **kw: Any) -> None: ...

    def __call__(self) -> CredentialProviderFunction | None: ...

    def get_or_init_cache_key(self) -> bytes: ...

    def get_cache_key_impl(self) -> bytes: ...

    def stable_cache_key(self) -> bytes: ...

    @property
    def provider_repr(self) -> str: ...


DEFAULT_CREDENTIAL_PROVIDER: CredentialProviderFunction | Literal["auto"] | None = "auto"
