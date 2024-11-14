# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the dataset. Within a project, dataset names are unique"""

    project_id: Required[str]
    """Unique identifier for the project that the dataset belongs under"""

    description: Optional[str]
    """Textual description of the dataset"""

    metadata: Optional[Dict[str, Optional[object]]]
    """User-controlled metadata about the dataset"""
