# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SpanAttributes"]


class SpanAttributes(BaseModel):
    name: Optional[str] = None
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]] = None
    """Type of the span, for display purposes only"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...
