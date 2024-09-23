# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

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
