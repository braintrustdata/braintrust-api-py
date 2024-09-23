# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: str
    """Unique identifier for the organization"""

    name: str
    """Name of the organization"""

    api_url: Optional[str] = None

    created: Optional[datetime] = None
    """Date of organization creation"""

    is_universal_api: Optional[bool] = None

    proxy_url: Optional[str] = None

    realtime_url: Optional[str] = None
