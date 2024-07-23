# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FunctionFeedbackParams", "Feedback"]


class FunctionFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[Feedback]]
    """A list of function feedback items"""


class Feedback(TypedDict, total=False):
    id: Required[str]
    """The id of the function event to log feedback for.

    This is the row `id` returned by `POST /v1/function/{function_id}/insert`
    """

    comment: Optional[str]
    """An optional comment string to log about the function event"""

    metadata: Optional[Dict[str, object]]
    """A dictionary with additional data about the feedback.

    If you have a `user_id`, you can log it here and access it in the Braintrust UI.
    """

    source: Optional[Literal["app", "api", "external"]]
    """The source of the feedback.

    Must be one of "external" (default), "app", or "api"
    """
