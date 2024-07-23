# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["View", "Options", "ViewData", "ViewDataSearch"]


class Options(BaseModel):
    column_order: Optional[List[str]] = FieldInfo(alias="columnOrder", default=None)

    column_sizing: Optional[Dict[str, float]] = FieldInfo(alias="columnSizing", default=None)

    column_visibility: Optional[Dict[str, bool]] = FieldInfo(alias="columnVisibility", default=None)


class ViewDataSearch(BaseModel):
    filter: Optional[List[object]] = None

    match: Optional[List[object]] = None

    sort: Optional[List[object]] = None

    tag: Optional[List[object]] = None


class ViewData(BaseModel):
    search: Optional[ViewDataSearch] = None


class View(BaseModel):
    id: str
    """Unique identifier for the view"""

    name: str
    """Name of the view"""

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

    view_type: Optional[
        Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
    ] = None
    """Type of table that the view corresponds to."""

    created: Optional[datetime] = None
    """Date of view creation"""

    deleted_at: Optional[datetime] = None
    """Date of role deletion, or null if the role is still active"""

    options: Optional[Options] = None
    """Options for the view in the app"""

    user_id: Optional[str] = None
    """Identifies the user who created the view"""

    view_data: Optional[ViewData] = None
    """The view definition"""
