# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["OnlineScoreConfig", "Scorer", "ScorerFunction", "ScorerGlobal"]


class ScorerFunction(BaseModel):
    id: str

    type: Literal["function"]


class ScorerGlobal(BaseModel):
    name: str

    type: Literal["global"]


Scorer: TypeAlias = Union[ScorerFunction, ScorerGlobal]


class OnlineScoreConfig(BaseModel):
    sampling_rate: float
    """The sampling rate for online scoring"""

    scorers: List[Scorer]
    """The list of scorers to use for online scoring"""

    apply_to_root_span: Optional[bool] = None
    """Whether to trigger online scoring on the root span of each trace"""

    apply_to_span_names: Optional[List[str]] = None
    """Trigger online scoring on any spans with a name in this list"""
