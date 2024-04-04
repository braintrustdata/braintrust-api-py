# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasetFetchPostParams", "Filter"]


class DatasetFetchPostParams(TypedDict, total=False):
    filters: Optional[Iterable[Filter]]
    """A list of filters on the events to fetch.

    Currently, only path-lookup type filters are supported, but we may add more in
    the future
    """

    limit: Optional[int]
    """
    Fetch queries may be paginated if the total result size is expected to be large
    (e.g. project_logs which accumulate over a long time). Note that fetch queries
    only support pagination in descending time order (from latest to earliest
    `_xact_id`. Furthermore, later pages may return rows which showed up in earlier
    pages, except with an earlier `_xact_id`. This happens because pagination occurs
    over the whole version history of the event log. You will most likely want to
    exclude any such duplicate, outdated rows (by `id`) from your combined result
    set.

    The `limit` parameter controls the number of full traces to return. So you may
    end up with more individual rows than the specified limit if you are fetching
    events containing traces.
    """

    max_root_span_id: Optional[str]
    """
    Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
    event fetches. Given a previous fetch with a list of rows, you can determine
    `max_root_span_id` as the maximum of the `root_span_id` field over all rows. See
    the documentation for `limit` for an overview of paginating fetch queries.
    """

    max_xact_id: Optional[int]
    """
    Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
    event fetches. Given a previous fetch with a list of rows, you can determine
    `max_xact_id` as the maximum of the `_xact_id` field over all rows. See the
    documentation for `limit` for an overview of paginating fetch queries.
    """

    version: Optional[int]
    """
    You may specify a version id to retrieve a snapshot of the events from a past
    time. The version id is essentially a filter on the latest event transaction id.
    You can use the `max_xact_id` returned by a past fetch as the version to
    reproduce that exact fetch.
    """


class Filter(TypedDict, total=False):
    path: Required[List[str]]
    """List of fields describing the path to the value to be checked against.

    For instance, if you wish to filter on the value of `c` in
    `{"input": {"a": {"b": {"c": "hello"}}}}`, pass `path=["input", "a", "b", "c"]`
    """

    type: Required[Literal["path_lookup"]]
    """Denotes the type of filter as a path-lookup filter"""

    value: object
    """
    The value to compare equality-wise against the event value at the specified
    `path`. The value must be a "primitive", that is, any JSON-serializable object
    except for objects and arrays. For instance, if you wish to filter on the value
    of "input.a.b.c" in the object `{"input": {"a": {"b": {"c": "hello"}}}}`, pass
    `value="hello"`
    """
