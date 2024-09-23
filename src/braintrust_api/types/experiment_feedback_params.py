# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.feedback_experiment_item import FeedbackExperimentItem

__all__ = ["ExperimentFeedbackParams"]


class ExperimentFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[FeedbackExperimentItem]]
    """A list of experiment feedback items"""
