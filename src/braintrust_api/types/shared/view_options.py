# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ViewOptions"]


class ViewOptions(BaseModel):
    column_order: Optional[List[str]] = FieldInfo(alias="columnOrder", default=None)

    column_sizing: Optional[Dict[str, float]] = FieldInfo(alias="columnSizing", default=None)

    column_visibility: Optional[Dict[str, bool]] = FieldInfo(alias="columnVisibility", default=None)
