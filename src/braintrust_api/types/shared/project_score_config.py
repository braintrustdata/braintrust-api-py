# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .online_score_config import OnlineScoreConfig

__all__ = ["ProjectScoreConfig"]


class ProjectScoreConfig(BaseModel):
    destination: Optional[str] = None

    multi_select: Optional[bool] = None

    online: Optional[OnlineScoreConfig] = None
