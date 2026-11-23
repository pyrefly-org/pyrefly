from __future__ import annotations
import abc
import importlib.util
import json
import os
import subprocess
import sys
import zoneinfo
from collections.abc import Callable
from datetime import datetime
from functools import partial
from typing import (
    TYPE_CHECKING,
    Any,
    TypedDict,
    Union,
)
import polars._utils.logging
from polars._utils.logging import eprint, verbose
from polars.io.cloud._utils import NoPickleOption
from typing import TypeAlias
from polars._dependencies import boto3
from polars._utils.unstable import issue_unstable_warning

CredentialProviderFunctionReturn: TypeAlias = tuple[dict[str, str], int | None]
CredentialProviderFunction: TypeAlias = (Union[
    Callable[[], CredentialProviderFunctionReturn], "CredentialProvider"
])


class AWSAssumeRoleKWArgs(TypedDict):
    RoleArn: str
    RoleSessionName: str
    PolicyArns: list[dict[str, str]]
    Policy: str
    DurationSeconds: int
    Tags: list[dict[str, str]]
    TransitiveTagKeys: list[str]
    ExternalId: str
    SerialNumber: str
    TokenCode: str
    SourceIdentity: str
    ProvidedContexts: list[dict[str, str]]


class CredentialProvider(abc.ABC):
    @abc.abstractmethod
    def __call__(self) -> CredentialProviderFunctionReturn: ...


class CachingCredentialProvider(CredentialProvider, abc.ABC):
    def __init__(self) -> None: ...

    def __call__(self) -> CredentialProviderFunctionReturn: ...

    @abc.abstractmethod
    def retrieve_credentials_impl(self) -> CredentialProviderFunctionReturn: ...

    def clear_cached_credentials(self) -> None: ...

    def __repr__(self) -> str: ...


class CachedCredentialProvider(CachingCredentialProvider):
    def __init__(self, provider: CredentialProvider | CredentialProviderFunction) -> None: ...

    def retrieve_credentials_impl(self) -> CredentialProviderFunctionReturn: ...

    def __repr__(self) -> str: ...


class CredentialProviderAWS(CachingCredentialProvider):
    profile_name: str | None
    region_name: str | None
    assume_role: AWSAssumeRoleKWArgs | None

    def __init__(self, *, profile_name: str | None = None, region_name: str | None = None, assume_role: AWSAssumeRoleKWArgs | None = None, _auto_init_unhandled_key: str | None = None, _storage_options: dict[str, str | None] | None = None) -> None: ...

    def retrieve_credentials_impl(self) -> CredentialProviderFunctionReturn: ...

    class EmptyCredentialError(Exception):
        ...


class CredentialProviderAzure(CachingCredentialProvider):
    account_name: str | None
    scopes: list[str]
    tenant_id: str | None
    credential: Any | None

    def __init__(self, *, scopes: list[str] | None = None, tenant_id: str | None = None, credential: Any | None = None, _storage_account: str | None = None) -> None: ...

    def retrieve_credentials_impl(self) -> CredentialProviderFunctionReturn: ...


class CredentialProviderGCP(CachingCredentialProvider):
    def __init__(self, *, scopes: Any | None = None, request: Any | None = None, quota_project_id: Any | None = None, default_scopes: Any | None = None) -> None: ...

    def retrieve_credentials_impl(self) -> CredentialProviderFunctionReturn: ...


class UserProvidedGCPToken(CredentialProvider):
    token: str

    def __init__(self, token: str) -> None: ...

    def __call__(self) -> CredentialProviderFunctionReturn: ...
