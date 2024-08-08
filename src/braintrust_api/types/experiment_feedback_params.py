# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..types import shared_params

__all__ = ["ExperimentFeedbackParams"]


class ExperimentFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[shared_params.FeedbackExperimentItem]]
    """A list of experiment feedback items"""
