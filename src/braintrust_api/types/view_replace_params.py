# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Optional, Union

from datetime import datetime

from .._utils import PropertyInfo

from .shared_params.view_options import ViewOptions

from .shared_params.view_data import ViewData

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ViewReplaceParams"]

class ViewReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the view"""

    object_id: Required[str]
    """The id of the object the view applies to"""

    object_type: Required[Optional[Literal["organization", "project", "experiment", "dataset", "prompt", "prompt_session", "group", "role", "org_member", "project_log", "org_project"]]]
    """The object type that the ACL applies to"""

    view_type: Required[Optional[Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]]]
    """Type of table that the view corresponds to."""

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format = "iso8601")]
    """Date of role deletion, or null if the role is still active"""

    options: Optional[ViewOptions]
    """Options for the view in the app"""

    user_id: Optional[str]
    """Identifies the user who created the view"""

    view_data: Optional[ViewData]
    """The view definition"""