# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectSettings"]


class ProjectSettings(TypedDict, total=False):
    comparison_key: Optional[str]
    """The key used to join two experiments (defaults to `input`)."""
