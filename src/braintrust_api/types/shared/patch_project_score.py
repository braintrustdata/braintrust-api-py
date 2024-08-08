# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .project_score_category import ProjectScoreCategory

__all__ = ["PatchProjectScore", "Categories", "CategoriesNullableVariant"]


class CategoriesNullableVariant(BaseModel):
    pass


Categories: TypeAlias = Union[
    List[ProjectScoreCategory], Dict[str, float], List[str], Optional[CategoriesNullableVariant]
]


class PatchProjectScore(BaseModel):
    categories: Optional[Categories] = None
    """For categorical-type project scores, the list of all categories"""

    description: Optional[str] = None
    """Textual description of the project score"""

    name: Optional[str] = None
    """Name of the project score"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]] = None
    """The type of the configured score"""
