# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["User"]


class User(BaseModel):
    id: str
    """Unique identifier for the user"""

    avatar_url: Optional[str] = None
    """URL of the user's Avatar image"""

    created: Optional[datetime] = None
    """Date of user creation"""

    email: Optional[str] = None
    """The user's email"""

    family_name: Optional[str] = None
    """Family name of the user"""

    given_name: Optional[str] = None
    """Given name of the user"""
