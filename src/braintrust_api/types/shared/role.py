# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Role", "MemberPermission"]


class MemberPermission(BaseModel):
    permission: Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    """Each permission permits a certain type of operation on an object in the system

    Permissions can be assigned to to objects on an individual basis, or grouped
    into roles
    """

    restrict_object_type: Optional[
        Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ]
    ] = None
    """The object type that the ACL applies to"""


class Role(BaseModel):
    id: str
    """Unique identifier for the role"""

    name: str
    """Name of the role"""

    created: Optional[datetime] = None
    """Date of role creation"""

    deleted_at: Optional[datetime] = None
    """Date of role deletion, or null if the role is still active"""

    description: Optional[str] = None
    """Textual description of the role"""

    member_permissions: Optional[List[MemberPermission]] = None
    """(permission, restrict_object_type) tuples which belong to this role"""

    member_roles: Optional[List[str]] = None
    """Ids of the roles this role inherits from

    An inheriting role has all the permissions contained in its member roles, as
    well as all of their inherited permissions
    """

    org_id: Optional[str] = None
    """Unique id for the organization that the role belongs under

    A null org_id indicates a system role, which may be assigned to anybody and
    inherited by any other role, but cannot be edited.

    It is forbidden to change the org after creating a role
    """

    user_id: Optional[str] = None
    """Identifies the user who created the role"""
