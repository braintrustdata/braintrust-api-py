# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.permission import Permission
from .shared.acl_object_type import ACLObjectType

__all__ = ["ACLCreateParams"]


class ACLCreateParams(TypedDict, total=False):
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
