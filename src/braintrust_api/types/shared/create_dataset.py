# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CreateDataset"]


class CreateDataset(BaseModel):
    name: str
    """Name of the dataset. Within a project, dataset names are unique"""

    description: Optional[str] = None
    """Textual description of the dataset"""

    project_id: Optional[str] = None
    """Unique identifier for the project that the dataset belongs under"""
