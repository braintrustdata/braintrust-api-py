# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

from .shared.view_type import ViewType
from .shared.acl_object_type import ACLObjectType

__all__ = ["ViewListParams"]


class ViewListParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[ACLObjectType]
    """The object type that the ACL applies to"""

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

    limit: Optional[int]
    """Limit the number of objects to return"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """

    view_name: str
    """Name of the view to search for"""

    view_type: Optional[ViewType]
    """Type of table that the view corresponds to."""
