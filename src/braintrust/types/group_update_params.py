# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the group"""

    member_groups: Optional[List[str]]
    """Ids of the groups this group inherits from

    An inheriting group has all the users contained in its member groups, as well as
    all of their inherited users
    """

    member_users: Optional[List[str]]
    """Ids of users which belong to this group"""

    name: Optional[str]
    """Name of the group"""
