# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectTagUpdateParams"]


class ProjectTagUpdateParams(TypedDict, total=False):
    color: Optional[str]
    """Color of the tag for the UI"""

    description: Optional[str]
    """Textual description of the project tag"""

    name: Optional[str]
    """Name of the project tag"""
