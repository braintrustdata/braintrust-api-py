# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ACLReplaceParams",
    "Permission",
    "PermissionUnionMember1",
    "RestrictObjectType",
    "RestrictObjectTypeUnionMember1",
]


class ACLReplaceParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[
        Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "project_score",
            "project_tag",
            "group",
            "role",
        ]
    ]
    """The object type that the ACL applies to"""

    group_id: Optional[str]
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Permission
    """Permission the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    restrict_object_type: RestrictObjectType
    """Optionally restricts the permission grant to just the specified object type"""

    role_id: Optional[str]
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str]
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """


class PermissionUnionMember1(TypedDict, total=False):
    pass


Permission = Union[
    Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"],
    Optional[PermissionUnionMember1],
]


class RestrictObjectTypeUnionMember1(TypedDict, total=False):
    pass


RestrictObjectType = Union[
    Literal[
        "organization",
        "project",
        "experiment",
        "dataset",
        "prompt",
        "prompt_session",
        "project_score",
        "project_tag",
        "group",
        "role",
    ],
    Optional[RestrictObjectTypeUnionMember1],
]
