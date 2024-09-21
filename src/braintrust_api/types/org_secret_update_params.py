# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["OrgSecretUpdateParams"]

class OrgSecretUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]

    name: Optional[str]
    """Name of the org secret"""

    secret: Optional[str]

    type: Optional[str]