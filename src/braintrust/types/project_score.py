# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectScore", "Categories", "CategoriesUnionMember0", "CategoriesUnionMember3", "Config"]


class CategoriesUnionMember0(BaseModel):
    name: str
    """Name of the category"""

    value: float
    """Numerical value of the category. Must be between 0 and 1, inclusive"""


class CategoriesUnionMember3(BaseModel):
    pass


Categories = Union[List[CategoriesUnionMember0], Dict[str, float], List[str], Optional[CategoriesUnionMember3]]


class Config(BaseModel):
    destination: Optional[Literal["expected"]] = None

    multi_select: Optional[bool] = None


class ProjectScore(BaseModel):
    id: str
    """Unique identifier for the project score"""

    name: str
    """Name of the project score"""

    project_id: str
    """Unique identifier for the project that the project score belongs under"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]] = None
    """The type of the configured score"""

    user_id: str

    categories: Optional[Categories] = None
    """For categorical-type project scores, the list of all categories"""

    config: Optional[Config] = None

    created: Optional[datetime] = None
    """Date of project score creation"""

    description: Optional[str] = None
    """Textual description of the project score"""

    position: Optional[str] = None
    """
    An optional LexoRank-based string that sets the sort position for the score in
    the UI
    """
