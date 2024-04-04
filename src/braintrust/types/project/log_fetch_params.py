# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LogFetchParams"]


class LogFetchParams(TypedDict, total=False):
    limit: int
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

    max_root_span_id: str
    """
    Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
    event fetches. Given a previous fetch with a list of rows, you can determine
    `max_root_span_id` as the maximum of the `root_span_id` field over all rows. See
    the documentation for `limit` for an overview of paginating fetch queries.
    """

    max_xact_id: int
    """
    Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
    event fetches. Given a previous fetch with a list of rows, you can determine
    `max_xact_id` as the maximum of the `_xact_id` field over all rows. See the
    documentation for `limit` for an overview of paginating fetch queries.
    """

    version: int
    """
    You may specify a version id to retrieve a snapshot of the events from a past
    time. The version id is essentially a filter on the latest event transaction id.
    You can use the `max_xact_id` returned by a past fetch as the version to
    reproduce that exact fetch.
    """
