# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["GroupCreateParams"]

class GroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the group"""

    description: Optional[str]
    """Textual description of the group"""

    member_groups: Optional[List[str]]
    """Ids of the groups this group inherits from

    An inheriting group has all the users contained in its member groups, as well as
    all of their inherited users
    """

    member_users: Optional[List[str]]
    """Ids of users which belong to this group"""

    org_name: Optional[str]
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, you
    may specify the name of the organization the group belongs in.
    """