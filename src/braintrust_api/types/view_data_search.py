# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ViewDataSearch"]


class ViewDataSearch(BaseModel):
    filter: Optional[List[object]] = None

    match: Optional[List[object]] = None

    sort: Optional[List[object]] = None

    tag: Optional[List[object]] = None
