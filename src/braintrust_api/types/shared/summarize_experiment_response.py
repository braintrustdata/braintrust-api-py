# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .score_summary import ScoreSummary
from .metric_summary import MetricSummary

__all__ = ["SummarizeExperimentResponse"]


class SummarizeExperimentResponse(BaseModel):
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

    metrics: Optional[Dict[str, MetricSummary]] = None
    """Summary of the experiment's metrics"""

    scores: Optional[Dict[str, ScoreSummary]] = None
    """Summary of the experiment's scores"""
