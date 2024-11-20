# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FeedbackExperimentItem"]


class FeedbackExperimentItem(BaseModel):
    id: str
    """The id of the experiment event to log feedback for.

    This is the row `id` returned by `POST /v1/experiment/{experiment_id}/insert`
    """

    comment: Optional[str] = None
    """An optional comment string to log about the experiment event"""

    expected: Optional[object] = None
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not
    """

    metadata: Optional[Dict[str, Optional[object]]] = None
    """A dictionary with additional data about the feedback.

    If you have a `user_id`, you can log it here and access it in the Braintrust UI.
    Note, this metadata does not correspond to the main event itself, but rather the
    audit log attached to the event.
    """

    scores: Optional[Dict[str, Optional[float]]] = None
    """A dictionary of numeric values (between 0 and 1) to log.

    These scores will be merged into the existing scores for the experiment event
    """

    source: Optional[Literal["app", "api", "external"]] = None
    """The source of the feedback.

    Must be one of "external" (default), "app", or "api"
    """

    tags: Optional[List[str]] = None
    """A list of tags to log"""
