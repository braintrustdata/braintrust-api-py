# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["DatasetFeedbackParams"]

class DatasetFeedbackParams(TypedDict, total=False):
    feedback: Required[Iterable[shared_params.FeedbackDatasetItem]]
    """A list of dataset feedback items"""