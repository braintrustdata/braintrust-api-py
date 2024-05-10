# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ACLCreateParams",
    "CreateUserPermissionACL",
    "CreateUserPermissionACLRestrictObjectType",
    "CreateUserPermissionACLRestrictObjectTypeUnionMember1",
    "CreateUserRoleACL",
    "CreateUserRoleACLRestrictObjectType",
    "CreateUserRoleACLRestrictObjectTypeUnionMember1",
    "CreateGroupPermissionACL",
    "CreateGroupPermissionACLRestrictObjectType",
    "CreateGroupPermissionACLRestrictObjectTypeUnionMember1",
    "CreateGroupRoleACL",
    "CreateGroupRoleACLRestrictObjectType",
    "CreateGroupRoleACLRestrictObjectTypeUnionMember1",
]


class CreateUserPermissionACL(TypedDict, total=False):
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

    permission: Required[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ]
    """Permission the ACL grants"""

    user_id: Required[str]
    """Id of the user the ACL applies to"""

    restrict_object_type: CreateUserPermissionACLRestrictObjectType
    """Optionally restricts the permission grant to just the specified object type"""


class CreateUserPermissionACLRestrictObjectTypeUnionMember1(TypedDict, total=False):
    pass


CreateUserPermissionACLRestrictObjectType = Union[
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
    Optional[CreateUserPermissionACLRestrictObjectTypeUnionMember1],
]


class CreateUserRoleACL(TypedDict, total=False):
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

    role_id: Required[str]
    """Id of the role the ACL grants"""

    user_id: Required[str]
    """Id of the user the ACL applies to"""

    restrict_object_type: CreateUserRoleACLRestrictObjectType
    """Optionally restricts the permission grant to just the specified object type"""


class CreateUserRoleACLRestrictObjectTypeUnionMember1(TypedDict, total=False):
    pass


CreateUserRoleACLRestrictObjectType = Union[
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
    Optional[CreateUserRoleACLRestrictObjectTypeUnionMember1],
]


class CreateGroupPermissionACL(TypedDict, total=False):
    group_id: Required[str]
    """Id of the group the ACL applies to"""

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

    permission: Required[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ]
    """Permission the ACL grants"""

    restrict_object_type: CreateGroupPermissionACLRestrictObjectType
    """Optionally restricts the permission grant to just the specified object type"""


class CreateGroupPermissionACLRestrictObjectTypeUnionMember1(TypedDict, total=False):
    pass


CreateGroupPermissionACLRestrictObjectType = Union[
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
    Optional[CreateGroupPermissionACLRestrictObjectTypeUnionMember1],
]


class CreateGroupRoleACL(TypedDict, total=False):
    group_id: Required[str]
    """Id of the group the ACL applies to"""

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

    role_id: Required[str]
    """Id of the role the ACL grants"""

    restrict_object_type: CreateGroupRoleACLRestrictObjectType
    """Optionally restricts the permission grant to just the specified object type"""


class CreateGroupRoleACLRestrictObjectTypeUnionMember1(TypedDict, total=False):
    pass


CreateGroupRoleACLRestrictObjectType = Union[
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
    Optional[CreateGroupRoleACLRestrictObjectTypeUnionMember1],
]

ACLCreateParams = Union[CreateUserPermissionACL, CreateUserRoleACL, CreateGroupPermissionACL, CreateGroupRoleACL]
