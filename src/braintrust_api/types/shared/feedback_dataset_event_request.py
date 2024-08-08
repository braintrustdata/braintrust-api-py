# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .feedback_dataset_item import FeedbackDatasetItem

__all__ = ["FeedbackDatasetEventRequest"]


class FeedbackDatasetEventRequest(BaseModel):
    feedback: List[FeedbackDatasetItem]
    """A list of dataset feedback items"""
