# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RoleReplaceParams"]


class RoleReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the role"""

    description: Optional[str]
    """Textual description of the role"""

    member_permissions: Optional[
        List[
            Optional[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
    ]
    """Permissions which belong to this role"""

    member_roles: Optional[List[str]]
    """Ids of the roles this role inherits from

    An inheriting role has all the permissions contained in its member roles, as
    well as all of their inherited permissions
    """

    org_name: Optional[str]
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, you
    may specify the name of the organization the role belongs in.
    """
