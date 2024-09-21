# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from .view_options import ViewOptions

from .view_data import ViewData

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["View"]

class View(BaseModel):
    id: str
    """Unique identifier for the view"""

    name: str
    """Name of the view"""

    object_id: str
    """The id of the object the view applies to"""

    object_type: Optional[Literal["organization", "project", "experiment", "dataset", "prompt", "prompt_session", "group", "role", "org_member", "project_log", "org_project"]] = None
    """The object type that the ACL applies to"""

    view_type: Optional[Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]] = None
    """Type of table that the view corresponds to."""

    created: Optional[datetime] = None
    """Date of view creation"""

    deleted_at: Optional[datetime] = None
    """Date of role deletion, or null if the role is still active"""

    options: Optional[ViewOptions] = None
    """Options for the view in the app"""

    user_id: Optional[str] = None
    """Identifies the user who created the view"""

    view_data: Optional[ViewData] = None
    """The view definition"""