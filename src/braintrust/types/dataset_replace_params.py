# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetReplaceParams"]


class DatasetReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the dataset. Within a project, dataset names are unique"""

    description: Optional[str]
    """Textual description of the dataset"""

    project_id: Optional[str]
    """Unique identifier for the project that the dataset belongs under"""
