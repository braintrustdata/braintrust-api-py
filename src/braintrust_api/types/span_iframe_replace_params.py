# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SpanIframeReplaceParams"]


class SpanIframeReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the span iframe"""

    project_id: Required[str]
    """Unique identifier for the project that the span iframe belongs under"""

    url: Required[str]
    """URL to embed the project viewer in an iframe"""

    description: Optional[str]
    """Textual description of the span iframe"""

    post_message: Optional[bool]
    """Whether to post messages to the iframe containing the span's data.

    This is useful when you want to render more data than fits in the URL.
    """
