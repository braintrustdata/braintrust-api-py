# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.project_score_config import ProjectScoreConfig
from .shared_params.project_score_category import ProjectScoreCategory

__all__ = ["ProjectScoreCreateParams"]


class ProjectScoreCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the project score"""

    project_id: Required[str]
    """Unique identifier for the project that the project score belongs under"""

    score_type: Required[Literal["slider", "categorical", "weighted", "minimum", "maximum", "online", "free-form"]]
    """The type of the configured score"""

    categories: Union[Iterable[ProjectScoreCategory], Dict[str, float], List[str], None]
    """For categorical-type project scores, the list of all categories"""

    config: Optional[ProjectScoreConfig]

    description: Optional[str]
    """Textual description of the project score"""
