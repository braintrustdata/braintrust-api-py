# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EnvVar"]


class EnvVar(BaseModel):
    id: str
    """Unique identifier for the environment variable"""

    name: str
    """The name of the environment variable"""

    object_id: str
    """The id of the object the environment variable is scoped for"""

    object_type: Literal["organization", "project", "function"]
    """The type of the object the environment variable is scoped for"""

    created: Optional[datetime] = None
    """Date of environment variable creation"""

    used: Optional[datetime] = None
    """Date the environment variable was last used"""
