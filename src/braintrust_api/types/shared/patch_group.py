# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PatchGroup"]


class PatchGroup(BaseModel):
    add_member_groups: Optional[List[str]] = None
    """A list of group IDs to add to the group's inheriting-from set"""

    add_member_users: Optional[List[str]] = None
    """A list of user IDs to add to the group"""

    description: Optional[str] = None
    """Textual description of the group"""

    name: Optional[str] = None
    """Name of the group"""

    remove_member_groups: Optional[List[str]] = None
    """A list of group IDs to remove from the group's inheriting-from set"""

    remove_member_users: Optional[List[str]] = None
    """A list of user IDs to remove from the group"""
