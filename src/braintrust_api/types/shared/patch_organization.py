# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PatchOrganization"]


class PatchOrganization(BaseModel):
    api_url: Optional[str] = None

    is_universal_api: Optional[bool] = None

    name: Optional[str] = None
    """Name of the organization"""

    proxy_url: Optional[str] = None

    realtime_url: Optional[str] = None
