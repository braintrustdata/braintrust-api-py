# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SpanIFrame"]


class SpanIFrame(BaseModel):
    id: str
    """Unique identifier for the span iframe"""

    name: str
    """Name of the span iframe"""

    project_id: str
    """Unique identifier for the project that the span iframe belongs under"""

    url: str
    """URL to embed the project viewer in an iframe"""

    created: Optional[datetime] = None
    """Date of span iframe creation"""

    deleted_at: Optional[datetime] = None
    """Date of span iframe deletion, or null if the span iframe is still active"""

    description: Optional[str] = None
    """Textual description of the span iframe"""

    post_message: Optional[bool] = None
    """Whether to post messages to the iframe containing the span's data.

    This is useful when you want to render more data than fits in the URL.
    """

    user_id: Optional[str] = None
    """Identifies the user who created the span iframe"""
