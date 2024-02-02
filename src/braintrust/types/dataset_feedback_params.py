# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetFeedbackParams", "Feedback"]


class DatasetFeedbackParams(TypedDict, total=False):
    feedback: Required[List[Feedback]]
    """A list of dataset feedback items"""


class Feedback(TypedDict, total=False):
    id: Required[str]
    """The id of the dataset event to log feedback for.

    This is the row `id` returned by `POST /v1/dataset/{dataset_id}/insert`
    """

    comment: Optional[str]
    """An optional comment string to log about the dataset event"""

    metadata: Optional[Dict[str, object]]
    """A dictionary with additional data about the feedback.

    If you have a `user_id`, you can log it here and access it in the Braintrust UI.
    """

    source: Optional[str]
    """The source of the feedback.

    Must be one of "external" (default), "app", or "api"
    """
