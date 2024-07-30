# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectScoreUpdateParams", "Categories", "CategoriesCategorical", "CategoriesNullableVariant"]


class ProjectScoreUpdateParams(TypedDict, total=False):
    categories: Categories
    """For categorical-type project scores, the list of all categories"""

    description: Optional[str]
    """Textual description of the project score"""

    name: Optional[str]
    """Name of the project score"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]]
    """The type of the configured score"""


class CategoriesCategorical(TypedDict, total=False):
    name: Required[str]
    """Name of the category"""

    value: Required[float]
    """Numerical value of the category. Must be between 0 and 1, inclusive"""


class CategoriesNullableVariant(TypedDict, total=False):
    pass


Categories = Union[Iterable[CategoriesCategorical], Dict[str, float], List[str], Optional[CategoriesNullableVariant]]
