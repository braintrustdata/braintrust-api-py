# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the dataset. Within a project, dataset names are unique"""

    description: Optional[str]
    """Textual description of the dataset"""

    project_id: Optional[str]
    """Unique identifier for the project that the dataset belongs under"""
