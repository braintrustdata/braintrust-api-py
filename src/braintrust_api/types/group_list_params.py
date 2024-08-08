# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..types import shared_params
from .shared.org_name import OrgName
from .shared.group_name import GroupName
from .shared.ending_before import EndingBefore
from .shared.starting_after import StartingAfter
from .shared.app_limit_param import AppLimitParam

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    ending_before: EndingBefore
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    group_name: GroupName
    """Name of the group to search for"""

    ids: shared_params.IDs
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: AppLimitParam
    """Limit the number of objects to return"""

    org_name: OrgName
    """Filter search results to within a particular organization"""

    starting_after: StartingAfter
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """
