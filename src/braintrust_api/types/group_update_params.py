# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    add_member_groups: Optional[List[str]]
    """A list of group IDs to add to the group's inheriting-from set"""

    add_member_users: Optional[List[str]]
    """A list of user IDs to add to the group"""

    description: Optional[str]
    """Textual description of the group"""

    name: Optional[str]
    """Name of the group"""

    remove_member_groups: Optional[List[str]]
    """A list of group IDs to remove from the group's inheriting-from set"""

    remove_member_users: Optional[List[str]]
    """A list of user IDs to remove from the group"""
