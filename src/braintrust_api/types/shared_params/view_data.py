# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .view_data_search import ViewDataSearch

__all__ = ["ViewData"]


class ViewData(TypedDict, total=False):
    search: Optional[ViewDataSearch]
