# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MetricSummary"]


class MetricSummary(BaseModel):
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
