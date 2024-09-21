# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScoreSummary"]

class ScoreSummary(BaseModel):
    improvements: int
    """Number of improvements in the score"""

    name: str
    """Name of the score"""

    regressions: int
    """Number of regressions in the score"""

    score: float
    """Average score across all examples"""

    diff: Optional[float] = None
    """Difference in score between the current and comparison experiment"""