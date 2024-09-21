# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["OrganizationUpdateParams"]

class OrganizationUpdateParams(TypedDict, total=False):
    api_url: Optional[str]

    is_universal_api: Optional[bool]

    name: Optional[str]
    """Name of the organization"""

    proxy_url: Optional[str]

    realtime_url: Optional[str]