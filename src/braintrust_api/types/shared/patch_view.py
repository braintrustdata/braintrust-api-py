# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .view_data import ViewData
from .view_options import ViewOptions

__all__ = ["PatchView"]


class PatchView(BaseModel):
    object_id: str
    """The id of the object the view applies to"""

    object_type: Optional[
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
    """The object type that the ACL applies to"""

    name: Optional[str] = None
    """Name of the view"""

    options: Optional[ViewOptions] = None
    """Options for the view in the app"""

    user_id: Optional[str] = None
    """Identifies the user who created the view"""

    view_data: Optional[ViewData] = None
    """The view definition"""

    view_type: Optional[
        Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
    ] = None
    """Type of table that the view corresponds to."""
