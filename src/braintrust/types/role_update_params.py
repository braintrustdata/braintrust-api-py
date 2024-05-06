# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RoleUpdateParams"]


class RoleUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the role"""

    member_permissions: Optional[
        List[Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]]
    ]
    """Permissions which belong to this role"""

    member_roles: Optional[List[str]]
    """Ids of the roles this role inherits from

    An inheriting role has all the permissions contained in its member roles, as
    well as all of their inherited permissions
    """

    name: Optional[str]
    """Name of the role"""
