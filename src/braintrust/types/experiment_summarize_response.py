# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ExperimentSummarizeResponse", "Metrics", "Scores"]


class Metrics(BaseModel):
    improvements: int
    """Number of improvements in the metric"""

    metric: float
    """Average metric across all examples"""

    name: str
    """Name of the metric"""

    regressions: int
    """Number of regressions in the metric"""

    unit: str
    """Unit label for the metric"""

    diff: Optional[float] = None
    """Difference in metric between the current and comparison experiment"""


class Scores(BaseModel):
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


class ExperimentSummarizeResponse(BaseModel):
    experiment_name: str
    """Name of the experiment"""

    experiment_url: str
    """URL to the experiment's page in the Braintrust app"""

    project_name: str
    """Name of the project that the experiment belongs to"""

    project_url: str
    """URL to the project's page in the Braintrust app"""

    comparison_experiment_name: Optional[str] = None
    """The experiment which scores are baselined against"""

    metrics: Optional[Dict[str, Metrics]] = None
    """Summary of the experiment's metrics"""

    scores: Optional[Dict[str, Scores]] = None
    """Summary of the experiment's scores"""
