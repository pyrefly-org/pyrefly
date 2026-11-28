from __future__ import annotations
import contextlib
import functools
from polars._utils.expired import RemovedParameter, removed_parameters


class QueryOptFlags:
    @removed_parameters(
        RemovedParameter(
            name="collapse_joins",
            deprecated_in="1.33.1",
            removed_in="2.0",
            hint="Use `predicate_pushdown` instead.",
        ),
    )
    def __init__(self, *, predicate_pushdown: None | bool = None, projection_pushdown: None | bool = None, simplify_expression: None | bool = None, slice_pushdown: None | bool = None, comm_subplan_elim: None | bool = None, comm_subexpr_elim: None | bool = None, cluster_with_columns: None | bool = None, check_order_observe: None | bool = None, fast_projection: None | bool = None, sort_collapse: None | bool = None, pre_partition_hive: None | bool = None, join_order: None | bool = None, row_estimate: None | bool = None) -> None: ...

    @staticmethod
    @removed_parameters(
        RemovedParameter(
            name="collapse_joins",
            deprecated_in="1.33.1",
            removed_in="2.0",
            hint="Use `predicate_pushdown` instead.",
        ),
    )
    def none(*, predicate_pushdown: None | bool = None, projection_pushdown: None | bool = None, simplify_expression: None | bool = None, slice_pushdown: None | bool = None, comm_subplan_elim: None | bool = None, comm_subexpr_elim: None | bool = None, cluster_with_columns: None | bool = None, check_order_observe: None | bool = None, fast_projection: None | bool = None, sort_collapse: None | bool = None, pre_partition_hive: None | bool = None, join_order: None | bool = None, row_estimate: None | bool = None) -> QueryOptFlags: ...

    @removed_parameters(
        RemovedParameter(
            name="collapse_joins",
            deprecated_in="1.33.1",
            removed_in="2.0",
            hint="Use `predicate_pushdown` instead.",
        ),
    )
    def update(self, *, predicate_pushdown: None | bool = None, projection_pushdown: None | bool = None, simplify_expression: None | bool = None, slice_pushdown: None | bool = None, comm_subplan_elim: None | bool = None, comm_subexpr_elim: None | bool = None, cluster_with_columns: None | bool = None, check_order_observe: None | bool = None, fast_projection: None | bool = None, sort_collapse: None | bool = None, pre_partition_hive: None | bool = None, join_order: None | bool = None, row_estimate: None | bool = None) -> QueryOptFlags: ...

    def __copy__(self) -> QueryOptFlags: ...

    def __deepcopy__(self) -> QueryOptFlags: ...

    def no_optimizations(self) -> None: ...

    @property
    def projection_pushdown(self) -> bool: ...

    @projection_pushdown.setter
    def projection_pushdown(self, value: bool) -> None: ...

    @property
    def predicate_pushdown(self) -> bool: ...

    @predicate_pushdown.setter
    def predicate_pushdown(self, value: bool) -> None: ...

    @property
    def cluster_with_columns(self) -> bool: ...

    @cluster_with_columns.setter
    def cluster_with_columns(self, value: bool) -> None: ...

    @property
    def simplify_expression(self) -> bool: ...

    @simplify_expression.setter
    def simplify_expression(self, value: bool) -> None: ...

    @property
    def slice_pushdown(self) -> bool: ...

    @slice_pushdown.setter
    def slice_pushdown(self, value: bool) -> None: ...

    @property
    def comm_subplan_elim(self) -> bool: ...

    @comm_subplan_elim.setter
    def comm_subplan_elim(self, value: bool) -> None: ...

    @property
    def comm_subexpr_elim(self) -> bool: ...

    @comm_subexpr_elim.setter
    def comm_subexpr_elim(self, value: bool) -> None: ...

    @property
    def check_order_observe(self) -> bool: ...

    @check_order_observe.setter
    def check_order_observe(self, value: bool) -> None: ...

    @property
    def fast_projection(self) -> bool: ...

    @fast_projection.setter
    def fast_projection(self, value: bool) -> None: ...

    @property
    def sort_collapse(self) -> bool: ...

    @sort_collapse.setter
    def sort_collapse(self, value: bool) -> None: ...

    @property
    def pre_partition_hive(self) -> bool: ...

    @pre_partition_hive.setter
    def pre_partition_hive(self, value: bool) -> None: ...

    @property
    def join_order(self) -> bool: ...

    @join_order.setter
    def join_order(self, value: bool) -> None: ...

    @property
    def row_estimate(self) -> bool: ...

    @row_estimate.setter
    def row_estimate(self, value: bool) -> None: ...

    def __str__(self) -> str: ...


DEFAULT_QUERY_OPT_FLAGS: QueryOptFlags
DEFAULT_QUERY_OPT_FLAGS: QueryOptFlags
REMOVED_OLD_OPT_FLAGS: list[RemovedParameter]
