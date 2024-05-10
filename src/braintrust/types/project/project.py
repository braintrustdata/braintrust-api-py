# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

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

    user_id: Optional[str] = None
    """Identifies the user who created the project"""
