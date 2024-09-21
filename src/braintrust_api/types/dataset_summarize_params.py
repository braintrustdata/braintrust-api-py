# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["DatasetSummarizeParams"]

class DatasetSummarizeParams(TypedDict, total=False):
    summarize_data: bool
    """Whether to summarize the data.

    If false (or omitted), only the metadata will be returned.
    """