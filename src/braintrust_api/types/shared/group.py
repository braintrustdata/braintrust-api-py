# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """Unique identifier for the group"""

    name: str
    """Name of the group"""

    org_id: str
    """Unique id for the organization that the group belongs under

    It is forbidden to change the org after creating a group
    """

    created: Optional[datetime] = None
    """Date of group creation"""

    deleted_at: Optional[datetime] = None
    """Date of group deletion, or null if the group is still active"""

    description: Optional[str] = None
    """Textual description of the group"""

    member_groups: Optional[List[str]] = None
    """Ids of the groups this group inherits from

    An inheriting group has all the users contained in its member groups, as well as
    all of their inherited users
    """

    member_users: Optional[List[str]] = None
    """Ids of users which belong to this group"""

    user_id: Optional[str] = None
    """Identifies the user who created the group"""
