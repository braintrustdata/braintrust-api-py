# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .project_score_category_param import ProjectScoreCategoryParam

__all__ = ["ProjectScoreReplaceParams", "Categories", "CategoriesNullableVariant"]


class ProjectScoreReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the project score"""

    project_id: Required[str]
    """Unique identifier for the project that the project score belongs under"""

    score_type: Required[Optional[Literal["slider", "categorical", "weighted", "minimum"]]]
    """The type of the configured score"""

    categories: Categories
    """For categorical-type project scores, the list of all categories"""

    description: Optional[str]
    """Textual description of the project score"""


class CategoriesNullableVariant(TypedDict, total=False):
    pass


Categories: TypeAlias = Union[
    Iterable[ProjectScoreCategoryParam], Dict[str, float], List[str], Optional[CategoriesNullableVariant]
]
