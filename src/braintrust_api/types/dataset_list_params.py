# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    dataset_name: str
    """Name of the dataset to search for"""

    ending_before: str
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    ids: Union[str, List[str]]
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: int
    """Limit the number of objects to return"""

    org_name: str
    """Filter search results to within a particular organization"""

    project_name: str
    """Name of the project to search for"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """