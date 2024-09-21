# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, Iterable

from typing_extensions import TypedDict

__all__ = ["ViewDataSearch"]

class ViewDataSearch(TypedDict, total=False):
    filter: Optional[Iterable[object]]

    match: Optional[Iterable[object]]

    sort: Optional[Iterable[object]]

    tag: Optional[Iterable[object]]