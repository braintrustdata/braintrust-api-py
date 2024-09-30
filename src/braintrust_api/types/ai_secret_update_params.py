# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["AISecretUpdateParams"]


class AISecretUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, Optional[object]]]

    name: Optional[str]
    """Name of the AI secret"""

    secret: Optional[str]

    type: Optional[str]
