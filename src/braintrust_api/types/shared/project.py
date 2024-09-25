# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .project_settings import ProjectSettings

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """Unique identifier for the project"""

    name: str
    """Name of the project"""

    org_id: str
    """Unique id for the organization that the project belongs under"""

    created: Optional[datetime] = None
    """Date of project creation"""

    deleted_at: Optional[datetime] = None
    """Date of project deletion, or null if the project is still active"""

    settings: Optional[ProjectSettings] = None

    user_id: Optional[str] = None
    """Identifies the user who created the project"""
