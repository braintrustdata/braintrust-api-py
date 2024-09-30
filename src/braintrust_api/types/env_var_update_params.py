# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EnvVarUpdateParams"]


class EnvVarUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the environment variable"""

    value: Optional[str]
    """The value of the environment variable. Will be encrypted at rest."""
