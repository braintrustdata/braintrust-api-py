# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PatchRole", "AddMemberPermission", "RemoveMemberPermission"]


class AddMemberPermission(BaseModel):
    permission: Optional[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ] = None
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


class RemoveMemberPermission(BaseModel):
    permission: Optional[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ] = None
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


class PatchRole(BaseModel):
    add_member_permissions: Optional[List[AddMemberPermission]] = None
    """A list of permissions to add to the role"""

    add_member_roles: Optional[List[str]] = None
    """A list of role IDs to add to the role's inheriting-from set"""

    description: Optional[str] = None
    """Textual description of the role"""

    name: Optional[str] = None
    """Name of the role"""

    remove_member_permissions: Optional[List[RemoveMemberPermission]] = None
    """A list of permissions to remove from the role"""

    remove_member_roles: Optional[List[str]] = None
    """A list of role IDs to remove from the role's inheriting-from set"""
