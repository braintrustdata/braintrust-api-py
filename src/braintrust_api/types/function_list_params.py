# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypedDict

__all__ = ["FunctionListParams"]


class FunctionListParams(TypedDict, total=False):
    ending_before: str
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    function_name: str
    """Name of the function to search for"""

    ids: Union[str, List[str]]
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: Optional[int]
    """Limit the number of objects to return"""

    org_name: str
    """Filter search results to within a particular organization"""

    project_id: str
    """Project id"""

    project_name: str
    """Name of the project to search for"""

    slug: str
    """Retrieve prompt with a specific slug"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """

    version: str
    """Retrieve prompt at a specific version.

    The version id can either be a transaction id (e.g. '1000192656880881099') or a
    version identifier (e.g. '81cd05ee665fdfb3').
    """
