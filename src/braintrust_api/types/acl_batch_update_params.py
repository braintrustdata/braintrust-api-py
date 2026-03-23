# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared.permission import Permission
from .shared.acl_object_type import ACLObjectType

__all__ = ["ACLBatchUpdateParams", "AddACL", "RemoveACL"]


class ACLBatchUpdateParams(TypedDict, total=False):
    add_acls: Optional[Iterable[AddACL]]
    """
    An ACL grants a certain permission or role to a certain user or group on an
    object.

    ACLs are inherited across the object hierarchy. So for example, if a user has
    read permissions on a project, they will also have read permissions on any
    experiment, dataset, etc. created within that project.

    To restrict a grant to a particular sub-object, you may specify
    `restrict_object_type` in the ACL, as part of a direct permission grant or as
    part of a role.
    """

    remove_acls: Optional[Iterable[RemoveACL]]
    """
    An ACL grants a certain permission or role to a certain user or group on an
    object.

    ACLs are inherited across the object hierarchy. So for example, if a user has
    read permissions on a project, they will also have read permissions on any
    experiment, dataset, etc. created within that project.

    To restrict a grant to a particular sub-object, you may specify
    `restrict_object_type` in the ACL, as part of a direct permission grant or as
    part of a role.
    """


class AddACL(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[ACLObjectType]
    """The object type that the ACL applies to"""

    group_id: Optional[str]
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Optional[Permission]
    """Permission the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    restrict_object_type: Optional[ACLObjectType]
    """
    When setting a permission directly, optionally restricts the permission grant to
    just the specified object type. Cannot be set alongside a `role_id`.
    """

    role_id: Optional[str]
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str]
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """


class RemoveACL(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[ACLObjectType]
    """The object type that the ACL applies to"""

    group_id: Optional[str]
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Optional[Permission]
    """Permission the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    restrict_object_type: Optional[ACLObjectType]
    """
    When setting a permission directly, optionally restricts the permission grant to
    just the specified object type. Cannot be set alongside a `role_id`.
    """

    role_id: Optional[str]
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str]
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """
