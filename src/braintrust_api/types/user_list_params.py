# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    email: Union[str, List[str]]
    """Email of the user to search for.

    You may pass the param multiple times to filter for more than one email
    """

    ending_before: str
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    family_name: Union[str, List[str]]
    """Family name of the user to search for.

    You may pass the param multiple times to filter for more than one family name
    """

    given_name: Union[str, List[str]]
    """Given name of the user to search for.

    You may pass the param multiple times to filter for more than one given name
    """

    ids: Union[str, List[str]]
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: Optional[int]
    """Limit the number of objects to return"""

    org_name: str
    """Filter search results to within a particular organization"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """
