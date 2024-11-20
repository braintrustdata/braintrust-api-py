# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedbackDatasetItem"]


class FeedbackDatasetItem(TypedDict, total=False):
    id: Required[str]
    """The id of the dataset event to log feedback for.

    This is the row `id` returned by `POST /v1/dataset/{dataset_id}/insert`
    """

    comment: Optional[str]
    """An optional comment string to log about the dataset event"""

    metadata: Optional[Dict[str, Optional[object]]]
    """A dictionary with additional data about the feedback.

    If you have a `user_id`, you can log it here and access it in the Braintrust UI.
    Note, this metadata does not correspond to the main event itself, but rather the
    audit log attached to the event.
    """

    source: Optional[Literal["app", "api", "external"]]
    """The source of the feedback.

    Must be one of "external" (default), "app", or "api"
    """

    tags: Optional[List[str]]
    """A list of tags to log"""
