# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SpanIframeUpdateParams"]


class SpanIframeUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """Name of the span iframe"""

    post_message: Optional[bool]
    """Whether to post messages to the iframe containing the span's data.

    This is useful when you want to render more data than fits in the URL.
    """

    url: Optional[str]
    """URL to embed the project viewer in an iframe"""
