# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ViewDeleteParams"]

class ViewDeleteParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the view applies to"""

    object_type: Required[Optional[Literal["organization", "project", "experiment", "dataset", "prompt", "prompt_session", "group", "role", "org_member", "project_log", "org_project"]]]
    """The object type that the ACL applies to"""