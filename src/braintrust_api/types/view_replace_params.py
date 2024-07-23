# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ViewReplaceParams", "Options", "ViewData", "ViewDataSearch"]


class ViewReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the view"""

    object_id: Required[str]
    """The id of the object the view applies to"""

    object_type: Required[
        Optional[
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
    ]
    """The object type that the ACL applies to"""

    view_type: Required[
        Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ]
    ]
    """Type of table that the view corresponds to."""

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Date of role deletion, or null if the role is still active"""

    options: Optional[Options]
    """Options for the view in the app"""

    user_id: Optional[str]
    """Identifies the user who created the view"""

    view_data: Optional[ViewData]
    """The view definition"""


class Options(TypedDict, total=False):
    column_order: Annotated[Optional[List[str]], PropertyInfo(alias="columnOrder")]

    column_sizing: Annotated[Optional[Dict[str, float]], PropertyInfo(alias="columnSizing")]

    column_visibility: Annotated[Optional[Dict[str, bool]], PropertyInfo(alias="columnVisibility")]


class ViewDataSearch(TypedDict, total=False):
    filter: Optional[Iterable[object]]

    match: Optional[Iterable[object]]

    sort: Optional[Iterable[object]]

    tag: Optional[Iterable[object]]


class ViewData(TypedDict, total=False):
    search: Optional[ViewDataSearch]
