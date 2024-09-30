# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .online_score_config import OnlineScoreConfig

__all__ = ["ProjectScoreConfig"]


class ProjectScoreConfig(BaseModel):
    destination: Optional[Literal["expected"]] = None

    multi_select: Optional[bool] = None

    online: Optional[OnlineScoreConfig] = None
