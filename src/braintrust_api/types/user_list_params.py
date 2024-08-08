# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..types import shared_params
from .shared.org_name import OrgName
from .shared.ending_before import EndingBefore
from .shared.starting_after import StartingAfter
from .shared.app_limit_param import AppLimitParam

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    email: shared_params.UserEmail
    """Email of the user to search for.

    You may pass the param multiple times to filter for more than one email
    """

    ending_before: EndingBefore
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    family_name: shared_params.UserFamilyName
    """Family name of the user to search for.

    You may pass the param multiple times to filter for more than one family name
    """

    given_name: shared_params.UserGivenName
    """Given name of the user to search for.

    You may pass the param multiple times to filter for more than one given name
    """

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
