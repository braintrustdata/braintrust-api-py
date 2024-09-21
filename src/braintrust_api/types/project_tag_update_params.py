# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ProjectTagUpdateParams"]

class ProjectTagUpdateParams(TypedDict, total=False):
    color: Optional[str]
    """Color of the tag for the UI"""

    description: Optional[str]
    """Textual description of the project tag"""

    name: Optional[str]
    """Name of the project tag"""