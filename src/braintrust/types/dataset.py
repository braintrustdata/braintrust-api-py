# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["Dataset"]


class Dataset(BaseModel):
    id: str
    """Unique identifier for the dataset"""

    name: str
    """Name of the dataset. Within a project, dataset names are unique"""

    created: Optional[datetime] = None
    """Date of dataset creation"""

    deleted_at: Optional[datetime] = None
    """Date of dataset deletion, or null if the dataset is still active"""

    description: Optional[str] = None
    """Textual description of the dataset"""

    project_id: Optional[str] = None
    """Unique identifier for the project that the dataset belongs under"""

    user_id: Optional[str] = None
    """Identifies the user who created the dataset"""
