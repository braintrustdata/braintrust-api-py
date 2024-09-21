# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreateAPIKeyOutput"]

class CreateAPIKeyOutput(BaseModel):
    id: str
    """Unique identifier for the api key"""

    key: str
    """The raw API key. It will only be exposed this one time"""

    name: str
    """Name of the api key"""

    preview_name: str

    created: Optional[datetime] = None
    """Date of api key creation"""

    org_id: Optional[str] = None
    """Unique identifier for the organization"""

    user_id: Optional[str] = None
    """Unique identifier for the user"""