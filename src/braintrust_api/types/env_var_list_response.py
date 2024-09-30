# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.env_var import EnvVar

__all__ = ["EnvVarListResponse"]


class EnvVarListResponse(BaseModel):
    objects: List[EnvVar]
    """A list of env_var objects"""
