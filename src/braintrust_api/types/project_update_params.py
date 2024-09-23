# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams", "Settings"]


class ProjectUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """Name of the project"""

    settings: Optional[Settings]
    """Project settings.

    Patch operations replace all settings, so make sure you include all settings you
    want to keep.
    """


class Settings(TypedDict, total=False):
    comparison_key: Optional[str]
    """The key used to join two experiments (defaults to `input`)."""
