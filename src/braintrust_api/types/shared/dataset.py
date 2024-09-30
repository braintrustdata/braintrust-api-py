# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Dataset"]


class Dataset(BaseModel):
    id: str
    """Unique identifier for the dataset"""

    name: str
    """Name of the dataset. Within a project, dataset names are unique"""

    project_id: str
    """Unique identifier for the project that the dataset belongs under"""

    created: Optional[datetime] = None
    """Date of dataset creation"""

    deleted_at: Optional[datetime] = None
    """Date of dataset deletion, or null if the dataset is still active"""

    description: Optional[str] = None
    """Textual description of the dataset"""

    metadata: Optional[Dict[str, Optional[object]]] = None
    """User-controlled metadata about the dataset"""

    user_id: Optional[str] = None
    """Identifies the user who created the dataset"""
