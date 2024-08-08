# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PatchProjectTag"]


class PatchProjectTag(BaseModel):
    color: Optional[str] = None
    """Color of the tag for the UI"""

    description: Optional[str] = None
    """Textual description of the project tag"""

    name: Optional[str] = None
    """Name of the project tag"""
