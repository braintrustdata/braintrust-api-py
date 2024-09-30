# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EnvVarCreateParams"]


class EnvVarCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the environment variable"""

    object_id: Required[str]
    """The id of the object the environment variable is scoped for"""

    object_type: Required[Literal["organization", "project", "function"]]
    """The type of the object the environment variable is scoped for"""

    value: Optional[str]
    """The value of the environment variable. Will be encrypted at rest."""
