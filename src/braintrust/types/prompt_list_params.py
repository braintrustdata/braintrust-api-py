# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Union, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PromptListParams"]


class PromptListParams(TypedDict, total=False):
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

    prompt_name: str
    """Name of the prompt to search for"""

    slug: str
    """Retrieve prompt with a specific slug"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """

    version: str
    """Retrieve a snapshot of events from a past time

    The version id is essentially a filter on the latest event transaction id. You
    can use the `max_xact_id` returned by a past fetch as the version to reproduce
    that exact fetch.
    """
