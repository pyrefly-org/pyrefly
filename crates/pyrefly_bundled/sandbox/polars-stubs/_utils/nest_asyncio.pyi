from _typeshed import Incomplete

import asyncio
import asyncio.events as events
import os
import sys
import threading
from collections import deque
from contextlib import contextmanager, suppress
from heapq import heappop


def apply(loop: Incomplete = None, *, run_close_loop: bool = False, error_on_mispatched: bool = False) -> Incomplete: ...
