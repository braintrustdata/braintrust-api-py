# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CreateProjectTag"]


class CreateProjectTag(BaseModel):
    name: str
    """Name of the project tag"""

    project_id: str
    """Unique identifier for the project that the project tag belongs under"""

    color: Optional[str] = None
    """Color of the tag for the UI"""

    description: Optional[str] = None
    """Textual description of the project tag"""
