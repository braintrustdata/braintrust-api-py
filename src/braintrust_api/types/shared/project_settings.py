# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProjectSettings"]


class ProjectSettings(BaseModel):
    comparison_key: Optional[str] = None
    """The key used to join two experiments (defaults to `input`)."""
