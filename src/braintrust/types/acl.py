# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ACL", "Permission", "PermissionUnionMember1", "RestrictObjectType", "RestrictObjectTypeUnionMember1"]


class PermissionUnionMember1(BaseModel):
    pass


Permission = Union[
    Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"],
    Optional[PermissionUnionMember1],
]


class RestrictObjectTypeUnionMember1(BaseModel):
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


class ACL(BaseModel):
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

    created: Optional[datetime] = None
    """Date of acl creation"""

    group_id: Optional[str] = None
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Optional[Permission] = None
    """Permission the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    restrict_object_type: Optional[RestrictObjectType] = None
    """Optionally restricts the permission grant to just the specified object type"""

    role_id: Optional[str] = None
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str] = None
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """
