# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["ViewDataSearch"]


class ViewDataSearch(TypedDict, total=False):
    filter: Optional[Iterable[Optional[object]]]

    match: Optional[Iterable[Optional[object]]]

    sort: Optional[Iterable[Optional[object]]]

    tag: Optional[Iterable[Optional[object]]]
