# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ACLCreateParams",
    "CreateUserPermissionACL",
    "CreateUserPermissionACLRestrictObjectType",
    "CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull",
    "CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull",
    "CreateUserRoleACL",
    "CreateUserRoleACLRestrictObjectType",
    "CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull",
    "CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull",
    "CreateGroupPermissionACL",
    "CreateGroupPermissionACLRestrictObjectType",
    "CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull",
    "CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull",
    "CreateGroupRoleACL",
    "CreateGroupRoleACLRestrictObjectType",
    "CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull",
    "CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull",
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


class CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull(TypedDict, total=False):
    pass


class CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull(TypedDict, total=False):
    _reserved_only_allow_null: Required[
        Annotated[
            CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull,
            PropertyInfo(alias="__reserved_only_allow_null"),
        ]
    ]
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


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
    Optional[CreateUserPermissionACLRestrictObjectType_ReservedOnlyAllowNull],
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


class CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull(TypedDict, total=False):
    pass


class CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull(TypedDict, total=False):
    _reserved_only_allow_null: Required[
        Annotated[
            CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull,
            PropertyInfo(alias="__reserved_only_allow_null"),
        ]
    ]
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


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
    Optional[CreateUserRoleACLRestrictObjectType_ReservedOnlyAllowNull],
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


class CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull(TypedDict, total=False):
    pass


class CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull(TypedDict, total=False):
    _reserved_only_allow_null: Required[
        Annotated[
            CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull,
            PropertyInfo(alias="__reserved_only_allow_null"),
        ]
    ]
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


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
    Optional[CreateGroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull],
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


class CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull(TypedDict, total=False):
    pass


class CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull(TypedDict, total=False):
    _reserved_only_allow_null: Required[
        Annotated[
            CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull_ReservedOnlyAllowNull,
            PropertyInfo(alias="__reserved_only_allow_null"),
        ]
    ]
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


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
    Optional[CreateGroupRoleACLRestrictObjectType_ReservedOnlyAllowNull],
]

ACLCreateParams = Union[CreateUserPermissionACL, CreateUserRoleACL, CreateGroupPermissionACL, CreateGroupRoleACL]
