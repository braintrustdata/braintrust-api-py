# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PatchProject", "Settings"]


class Settings(BaseModel):
    comparison_key: Optional[str] = None
    """The key used to join two experiments (defaults to `input`)."""


class PatchProject(BaseModel):
    name: Optional[str] = None
    """Name of the project"""

    settings: Optional[Settings] = None
    """Project settings.

    Patch operations replace all settings, so make sure you include all settings you
    want to keep.
    """
