# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProjectTagReplaceParams"]


class ProjectTagReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the project tag"""

    project_id: Required[str]
    """Unique identifier for the project that the project tag belongs under"""

    color: Optional[str]
    """Color of the tag for the UI"""

    description: Optional[str]
    """Textual description of the project tag"""
