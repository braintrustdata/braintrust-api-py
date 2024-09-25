# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.project_settings import ProjectSettings

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """Name of the project"""

    settings: Optional[ProjectSettings]
    """Project settings.

    Patch operations replace all settings, so make sure you include all settings you
    want to keep.
    """
