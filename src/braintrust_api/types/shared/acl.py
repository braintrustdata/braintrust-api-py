# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ACL"]


class ACL(BaseModel):
    id: str
    """Unique identifier for the acl"""

    object_org_id: str = FieldInfo(alias="_object_org_id")
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
        "group",
        "role",
        "org_member",
        "project_log",
        "org_project",
    ]
    """The object type that the ACL applies to"""

    created: Optional[datetime] = None
    """Date of acl creation"""

    group_id: Optional[str] = None
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Optional[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ] = None
    """Permission the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
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
    """
    When setting a permission directly, optionally restricts the permission grant to
    just the specified object type. Cannot be set alongside a `role_id`.
    """

    role_id: Optional[str] = None
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str] = None
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """
