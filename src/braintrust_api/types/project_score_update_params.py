# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, TypedDict

from .shared_params.project_score_config import ProjectScoreConfig
from .shared_params.project_score_category import ProjectScoreCategory

__all__ = ["ProjectScoreUpdateParams"]


class ProjectScoreUpdateParams(TypedDict, total=False):
    categories: Union[Iterable[ProjectScoreCategory], Dict[str, float], List[str], None]
    """For categorical-type project scores, the list of all categories"""

    config: Optional[ProjectScoreConfig]

    description: Optional[str]
    """Textual description of the project score"""

    name: Optional[str]
    """Name of the project score"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum", "maximum", "online", "free-form"]]
    """The type of the configured score"""
