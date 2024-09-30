# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the dataset"""

    metadata: Optional[Dict[str, Optional[object]]]
    """User-controlled metadata about the dataset"""

    name: Optional[str]
    """Name of the dataset. Within a project, dataset names are unique"""
