# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ACLCreateParams"]


class ACLCreateParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[
        Optional[
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
    ]
    """The object type that the ACL applies to"""

    group_id: Optional[str]
    """Id of the group the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """

    permission: Optional[
        Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
    ]
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
            "project_score",
            "project_tag",
            "group",
            "role",
        ]
    ]
    """Optionally restricts the permission grant to just the specified object type"""

    role_id: Optional[str]
    """Id of the role the ACL grants.

    Exactly one of `permission` and `role_id` will be provided
    """

    user_id: Optional[str]
    """Id of the user the ACL applies to.

    Exactly one of `user_id` and `group_id` will be provided
    """
