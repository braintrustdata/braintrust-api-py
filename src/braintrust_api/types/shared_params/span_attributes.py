# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["SpanAttributes"]


class SpanAttributesTyped(TypedDict, total=False):
    name: Optional[str]
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]]
    """Type of the span, for display purposes only"""


SpanAttributes: TypeAlias = Union[SpanAttributesTyped, Dict[str, Optional[object]]]
