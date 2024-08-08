# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .feedback_project_logs_item import FeedbackProjectLogsItem

__all__ = ["FeedbackProjectLogsEventRequest"]


class FeedbackProjectLogsEventRequest(BaseModel):
    feedback: List[FeedbackProjectLogsItem]
    """A list of project logs feedback items"""
