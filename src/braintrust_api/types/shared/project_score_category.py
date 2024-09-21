# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectScoreCategory"]

class ProjectScoreCategory(BaseModel):
    name: str
    """Name of the category"""

    value: float
    """Numerical value of the category. Must be between 0 and 1, inclusive"""