# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectScoreCategory"]


class ProjectScoreCategory(TypedDict, total=False):
    name: Required[str]
    """Name of the category"""

    value: Required[float]
    """Numerical value of the category. Must be between 0 and 1, inclusive"""
