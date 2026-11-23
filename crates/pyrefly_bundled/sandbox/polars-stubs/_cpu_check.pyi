from _typeshed import Incomplete

from __future__ import annotations
import ctypes
import os
import platform
from ctypes import CFUNCTYPE, POINTER, c_long, c_size_t, c_uint32, c_ulong, c_void_p
from typing import ClassVar


def get_runtime_repr() -> str: ...


class CPUID_struct(ctypes.Structure):
    ...


class CPUID:
    addr: Incomplete
    func_ptr: _CFunctionType
    mmap: mmap
    win: Incomplete

    def __init__(self) -> None: ...

    def __call__(self, eax: int, ecx: int = 0) -> CPUID_struct: ...

    def __del__(self) -> None: ...


def check_cpu_flags(feature_flags: str) -> None: ...
