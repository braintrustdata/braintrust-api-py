# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str
    """Unique identifier for the api key"""

    name: str
    """Name of the api key"""

    preview_name: str

    created: Optional[datetime] = None
    """Date of api key creation"""

    org_id: Optional[str] = None
    """Unique identifier for the organization"""

    user_id: Optional[str] = None
    """Unique identifier for the user"""
