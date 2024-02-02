# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LogFeedbackParams", "Feedback"]


class LogFeedbackParams(TypedDict, total=False):
    feedback: Required[List[Feedback]]
    """A list of project logs feedback items"""


class Feedback(TypedDict, total=False):
    id: Required[str]
    """The id of the project logs event to log feedback for.

    This is the row `id` returned by `POST /v1/project_logs/{project_id}/insert`
    """

    comment: Optional[str]
    """An optional comment string to log about the project logs event"""

    expected: object
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not
    """

    metadata: Optional[Dict[str, object]]
    """A dictionary with additional data about the feedback.

    If you have a `user_id`, you can log it here and access it in the Braintrust UI.
    """

    scores: Optional[Dict[str, Optional[float]]]
    """A dictionary of numeric values (between 0 and 1) to log.

    These scores will be merged into the existing scores for the project logs event
    """

    source: Optional[str]
    """The source of the feedback.

    Must be one of "external" (default), "app", or "api"
    """
