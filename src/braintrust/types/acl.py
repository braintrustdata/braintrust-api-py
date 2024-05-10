# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ACL",
    "UserPermissionACL",
    "UserPermissionACLRestrictObjectType",
    "UserPermissionACLRestrictObjectTypeUnionMember1",
    "UserRoleACL",
    "UserRoleACLRestrictObjectType",
    "UserRoleACLRestrictObjectTypeUnionMember1",
    "GroupPermissionACL",
    "GroupPermissionACLRestrictObjectType",
    "GroupPermissionACLRestrictObjectTypeUnionMember1",
    "GroupRoleACL",
    "GroupRoleACLRestrictObjectType",
    "GroupRoleACLRestrictObjectTypeUnionMember1",
]


class UserPermissionACLRestrictObjectTypeUnionMember1(BaseModel):
    pass


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
    Optional[UserPermissionACLRestrictObjectTypeUnionMember1],
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


class UserRoleACLRestrictObjectTypeUnionMember1(BaseModel):
    pass


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
    Optional[UserRoleACLRestrictObjectTypeUnionMember1],
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


class GroupPermissionACLRestrictObjectTypeUnionMember1(BaseModel):
    pass


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
    Optional[GroupPermissionACLRestrictObjectTypeUnionMember1],
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


class GroupRoleACLRestrictObjectTypeUnionMember1(BaseModel):
    pass


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
    Optional[GroupRoleACLRestrictObjectTypeUnionMember1],
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
