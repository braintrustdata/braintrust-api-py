# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.view_data import ViewData
from .shared_params.view_options import ViewOptions

__all__ = ["ViewUpdateParams"]


class ViewUpdateParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the view applies to"""

    object_type: Required[
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
    ]
    """The object type that the ACL applies to"""

    name: Optional[str]
    """Name of the view"""

    options: Optional[ViewOptions]
    """Options for the view in the app"""

    user_id: Optional[str]
    """Identifies the user who created the view"""

    view_data: Optional[ViewData]
    """The view definition"""

    view_type: Optional[
        Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
    ]
    """Type of table that the view corresponds to."""
