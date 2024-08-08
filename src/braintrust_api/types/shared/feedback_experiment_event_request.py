# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .feedback_experiment_item import FeedbackExperimentItem

__all__ = ["FeedbackExperimentEventRequest"]


class FeedbackExperimentEventRequest(BaseModel):
    feedback: List[FeedbackExperimentItem]
    """A list of experiment feedback items"""
