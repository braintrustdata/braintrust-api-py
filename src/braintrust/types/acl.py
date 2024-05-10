# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ACL",
    "UserPermissionACL",
    "UserPermissionACLRestrictObjectType",
    "UserPermissionACLRestrictObjectType_ReservedOnlyAllowNull",
    "UserRoleACL",
    "UserRoleACLRestrictObjectType",
    "UserRoleACLRestrictObjectType_ReservedOnlyAllowNull",
    "GroupPermissionACL",
    "GroupPermissionACLRestrictObjectType",
    "GroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull",
    "GroupRoleACL",
    "GroupRoleACLRestrictObjectType",
    "GroupRoleACLRestrictObjectType_ReservedOnlyAllowNull",
]


class UserPermissionACLRestrictObjectType_ReservedOnlyAllowNull(BaseModel):
    api_reserved_only_allow_null: Dict[str, object] = FieldInfo(alias="__reserved_only_allow_null")
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


UserPermissionACLRestrictObjectType = Union[
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
    Optional[UserPermissionACLRestrictObjectType_ReservedOnlyAllowNull],
]


class UserPermissionACL(BaseModel):
    id: str
    """Unique identifier for the acl"""

    api_object_org_id: str = FieldInfo(alias="_object_org_id")
    """The organization the ACL's referred object belongs to"""

    object_id: str
    """The id of the object the ACL applies to"""

    object_type: Literal[
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
    """The object type that the ACL applies to"""

    permission: Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    """Permission the ACL grants"""

    user_id: str
    """Id of the user the ACL applies to"""

    created: Optional[datetime] = None
    """Date of acl creation"""

    restrict_object_type: Optional[UserPermissionACLRestrictObjectType] = None
    """Optionally restricts the permission grant to just the specified object type"""


class UserRoleACLRestrictObjectType_ReservedOnlyAllowNull(BaseModel):
    api_reserved_only_allow_null: Dict[str, object] = FieldInfo(alias="__reserved_only_allow_null")
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


UserRoleACLRestrictObjectType = Union[
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
    Optional[UserRoleACLRestrictObjectType_ReservedOnlyAllowNull],
]


class UserRoleACL(BaseModel):
    id: str
    """Unique identifier for the acl"""

    api_object_org_id: str = FieldInfo(alias="_object_org_id")
    """The organization the ACL's referred object belongs to"""

    object_id: str
    """The id of the object the ACL applies to"""

    object_type: Literal[
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
    """The object type that the ACL applies to"""

    role_id: str
    """Id of the role the ACL grants"""

    user_id: str
    """Id of the user the ACL applies to"""

    created: Optional[datetime] = None
    """Date of acl creation"""

    restrict_object_type: Optional[UserRoleACLRestrictObjectType] = None
    """Optionally restricts the permission grant to just the specified object type"""


class GroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull(BaseModel):
    api_reserved_only_allow_null: Dict[str, object] = FieldInfo(alias="__reserved_only_allow_null")
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


GroupPermissionACLRestrictObjectType = Union[
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
    Optional[GroupPermissionACLRestrictObjectType_ReservedOnlyAllowNull],
]


class GroupPermissionACL(BaseModel):
    id: str
    """Unique identifier for the acl"""

    api_object_org_id: str = FieldInfo(alias="_object_org_id")
    """The organization the ACL's referred object belongs to"""

    group_id: str
    """Id of the group the ACL applies to"""

    object_id: str
    """The id of the object the ACL applies to"""

    object_type: Literal[
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
    """The object type that the ACL applies to"""

    permission: Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    """Permission the ACL grants"""

    created: Optional[datetime] = None
    """Date of acl creation"""

    restrict_object_type: Optional[GroupPermissionACLRestrictObjectType] = None
    """Optionally restricts the permission grant to just the specified object type"""


class GroupRoleACLRestrictObjectType_ReservedOnlyAllowNull(BaseModel):
    api_reserved_only_allow_null: Dict[str, object] = FieldInfo(alias="__reserved_only_allow_null")
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


GroupRoleACLRestrictObjectType = Union[
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
    Optional[GroupRoleACLRestrictObjectType_ReservedOnlyAllowNull],
]


class GroupRoleACL(BaseModel):
    id: str
    """Unique identifier for the acl"""

    api_object_org_id: str = FieldInfo(alias="_object_org_id")
    """The organization the ACL's referred object belongs to"""

    group_id: str
    """Id of the group the ACL applies to"""

    object_id: str
    """The id of the object the ACL applies to"""

    object_type: Literal[
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
    """The object type that the ACL applies to"""

    role_id: str
    """Id of the role the ACL grants"""

    created: Optional[datetime] = None
    """Date of acl creation"""

    restrict_object_type: Optional[GroupRoleACLRestrictObjectType] = None
    """Optionally restricts the permission grant to just the specified object type"""


ACL = Union[UserPermissionACL, UserRoleACL, GroupPermissionACL, GroupRoleACL]
