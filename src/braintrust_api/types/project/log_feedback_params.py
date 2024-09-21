# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from ..shared_params.feedback_project_logs_item import FeedbackProjectLogsItem

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["LogFeedbackParams"]

class LogFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[FeedbackProjectLogsItem]]
    """A list of project logs feedback items"""