from __future__ import annotations
import os
import re
from hypothesis import settings
from polars._typing import ParametricProfileNames


def load_profile(profile: ParametricProfileNames | int = "fast", *, set_environment: bool = False) -> None: ...


def set_profile(profile: ParametricProfileNames | int) -> None: ...
