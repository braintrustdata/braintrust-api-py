# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .project_score_config import ProjectScoreConfig
from .project_score_category import ProjectScoreCategory

__all__ = ["ProjectScore", "Categories", "CategoriesNullableVariant"]


class CategoriesNullableVariant(BaseModel):
    pass


Categories: TypeAlias = Union[
    List[ProjectScoreCategory], Dict[str, float], List[str], Optional[CategoriesNullableVariant]
]


class ProjectScore(BaseModel):
    id: str
    """Unique identifier for the project score"""

    name: str
    """Name of the project score"""

    project_id: str
    """Unique identifier for the project that the project score belongs under"""

    score_type: Literal["slider", "categorical", "weighted", "minimum", "maximum", "online"]
    """The type of the configured score"""

    user_id: str

    categories: Optional[Categories] = None
    """For categorical-type project scores, the list of all categories"""

    config: Optional[ProjectScoreConfig] = None

    created: Optional[datetime] = None
    """Date of project score creation"""

    description: Optional[str] = None
    """Textual description of the project score"""

    position: Optional[str] = None
    """
    An optional LexoRank-based string that sets the sort position for the score in
    the UI
    """
