# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.feedback_dataset_item import FeedbackDatasetItem

__all__ = ["DatasetFeedbackParams"]


class DatasetFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[FeedbackDatasetItem]]
    """A list of dataset feedback items"""
