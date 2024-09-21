# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Dict, Optional

from .project_score_category import ProjectScoreCategory

from ..._models import BaseModel

from typing_extensions import TypeAlias, Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectScore", "Categories", "CategoriesNullableVariant", "Config", "ConfigOnline", "ConfigOnlineScorer", "ConfigOnlineScorerFunction", "ConfigOnlineScorerGlobal"]

class CategoriesNullableVariant(BaseModel):
    pass

Categories: TypeAlias = Union[List[ProjectScoreCategory], Dict[str, float], List[str], Optional[CategoriesNullableVariant]]

class ConfigOnlineScorerFunction(BaseModel):
    id: str

    type: Literal["function"]

class ConfigOnlineScorerGlobal(BaseModel):
    name: str

    type: Literal["global"]

ConfigOnlineScorer: TypeAlias = Union[ConfigOnlineScorerFunction, ConfigOnlineScorerGlobal]

class ConfigOnline(BaseModel):
    sampling_rate: float
    """The sampling rate for online scoring"""

    scorers: List[ConfigOnlineScorer]
    """The list of scorers to use for online scoring"""

    apply_to_root_span: Optional[bool] = None
    """Whether to trigger online scoring on the root span of each trace"""

    apply_to_span_names: Optional[List[str]] = None
    """Trigger online scoring on any spans with a name in this list"""

class Config(BaseModel):
    destination: Optional[Literal["expected"]] = None

    multi_select: Optional[bool] = None

    online: Optional[ConfigOnline] = None

class ProjectScore(BaseModel):
    id: str
    """Unique identifier for the project score"""

    name: str
    """Name of the project score"""

    project_id: str
    """Unique identifier for the project that the project score belongs under"""

    score_type: Optional[Literal["slider", "categorical", "weighted", "minimum", "online"]] = None
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