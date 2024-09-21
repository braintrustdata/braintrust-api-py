# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .view_data_search_param import ViewDataSearchParam

__all__ = ["ViewDataParam"]


class ViewDataParam(TypedDict, total=False):
    search: Optional[ViewDataSearchParam]
