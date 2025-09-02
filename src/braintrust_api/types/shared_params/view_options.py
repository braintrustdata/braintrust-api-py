# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ViewOptions"]


class ViewOptions(TypedDict, total=False):
    column_order: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="columnOrder")]

    column_sizing: Annotated[Optional[Dict[str, float]], PropertyInfo(alias="columnSizing")]

    column_visibility: Annotated[Optional[Dict[str, bool]], PropertyInfo(alias="columnVisibility")]

    grouping: Optional[str]

    layout: Optional[str]

    row_height: Annotated[Optional[str], PropertyInfo(alias="rowHeight")]
