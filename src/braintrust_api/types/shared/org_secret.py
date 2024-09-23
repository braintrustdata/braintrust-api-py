# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["OrgSecret"]


class OrgSecret(BaseModel):
    id: str
    """Unique identifier for the org secret"""

    name: str
    """Name of the org secret"""

    org_id: str
    """Unique identifier for the organization"""

    created: Optional[datetime] = None
    """Date of org secret creation"""

    metadata: Optional[Dict[str, object]] = None

    preview_secret: Optional[str] = None

    type: Optional[str] = None
