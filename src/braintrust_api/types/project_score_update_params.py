# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .project_score_category_param import ProjectScoreCategoryParam

__all__ = ["ProjectScoreUpdateParams", "Categories", "CategoriesProjectScoreCategoryInfoData3"]


class ProjectScoreUpdateParams(TypedDict, total=False):
    categories: Categories
    """For categorical-type project scores, the list of all categories"""

    description: Optional[str]
    """Textual description of the project score"""

    name: Optional[str]
    """Name of the project score"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]]
    """The type of the configured score"""


class CategoriesProjectScoreCategoryInfoData3(TypedDict, total=False):
    pass


Categories = Union[
    Iterable[ProjectScoreCategoryParam], Dict[str, float], List[str], Optional[CategoriesProjectScoreCategoryInfoData3]
]
