# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .online_score_config import OnlineScoreConfig

__all__ = ["ProjectScoreConfig"]


class ProjectScoreConfig(TypedDict, total=False):
    destination: Optional[Literal["expected"]]

    multi_select: Optional[bool]

    online: Optional[OnlineScoreConfig]
