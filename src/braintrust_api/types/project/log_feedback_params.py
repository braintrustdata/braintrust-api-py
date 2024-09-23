# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.feedback_project_logs_item import FeedbackProjectLogsItem

__all__ = ["LogFeedbackParams"]


class LogFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[FeedbackProjectLogsItem]]
    """A list of project logs feedback items"""
