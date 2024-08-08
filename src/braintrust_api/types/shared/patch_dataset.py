# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["PatchDataset"]


class PatchDataset(BaseModel):
    description: Optional[str] = None
    """Textual description of the dataset"""

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the dataset"""

    name: Optional[str] = None
    """Name of the dataset. Within a project, dataset names are unique"""
