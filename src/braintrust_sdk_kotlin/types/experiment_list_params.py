# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExperimentListParams"]


class ExperimentListParams(TypedDict, total=False):
    ending_before: str
    """A cursor for pagination.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    experiment_name: str
    """Name of the experiment to search for"""

    limit: int
    """Limit the number of objects to return"""

    org_name: str
    """Filter search results to within a particular organization"""

    project_name: str
    """Name of the project to search for"""

    starting_after: str
    """A cursor for pagination.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """
