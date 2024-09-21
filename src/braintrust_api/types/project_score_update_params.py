# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, TypeAlias

from typing import Optional, Iterable, Dict, List, Union

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ProjectScoreUpdateParams", "Categories", "CategoriesNullableVariant"]

class ProjectScoreUpdateParams(TypedDict, total=False):
    categories: Categories
    """For categorical-type project scores, the list of all categories"""

    description: Optional[str]
    """Textual description of the project score"""

    name: Optional[str]
    """Name of the project score"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum", "online"]]
    """The type of the configured score"""

class CategoriesNullableVariant(TypedDict, total=False):
    pass

Categories: TypeAlias = Union[Iterable[shared_params.ProjectScoreCategory], Dict[str, float], List[str], Optional[CategoriesNullableVariant]]