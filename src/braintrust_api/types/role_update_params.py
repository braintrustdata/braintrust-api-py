# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared.permission import Permission
from .shared.acl_object_type import ACLObjectType

__all__ = ["RoleUpdateParams", "AddMemberPermission", "RemoveMemberPermission"]


class RoleUpdateParams(TypedDict, total=False):
    add_member_permissions: Optional[Iterable[AddMemberPermission]]
    """A list of permissions to add to the role"""

    add_member_roles: Optional[SequenceNotStr[str]]
    """A list of role IDs to add to the role's inheriting-from set"""

    description: Optional[str]
    """Textual description of the role"""

    name: Optional[str]
    """Name of the role"""

    remove_member_permissions: Optional[Iterable[RemoveMemberPermission]]
    """A list of permissions to remove from the role"""

    remove_member_roles: Optional[SequenceNotStr[str]]
    """A list of role IDs to remove from the role's inheriting-from set"""


class AddMemberPermission(TypedDict, total=False):
    permission: Required[Permission]
    """Each permission permits a certain type of operation on an object in the system

    Permissions can be assigned to to objects on an individual basis, or grouped
    into roles
    """

    restrict_object_type: Optional[ACLObjectType]
    """The object type that the ACL applies to"""


class RemoveMemberPermission(TypedDict, total=False):
    permission: Required[Permission]
    """Each permission permits a certain type of operation on an object in the system

    Permissions can be assigned to to objects on an individual basis, or grouped
    into roles
    """

    restrict_object_type: Optional[ACLObjectType]
    """The object type that the ACL applies to"""
