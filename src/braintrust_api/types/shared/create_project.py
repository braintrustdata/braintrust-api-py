# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CreateProject"]


class CreateProject(BaseModel):
    name: str
    """Name of the project"""

    org_name: Optional[str] = None
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, you
    may specify the name of the organization the project belongs in.
    """
