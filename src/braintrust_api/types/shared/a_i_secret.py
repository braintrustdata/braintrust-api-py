# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AISecret"]


class AISecret(BaseModel):
    id: str
    """Unique identifier for the AI secret"""

    name: str
    """Name of the AI secret"""

    org_id: str
    """Unique identifier for the organization"""

    created: Optional[datetime] = None
    """Date of AI secret creation"""

    metadata: Optional[Dict[str, Optional[object]]] = None

    preview_secret: Optional[str] = None

    type: Optional[str] = None
