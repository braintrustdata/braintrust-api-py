# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["OnlineScoreConfig", "Scorer", "ScorerFunction", "ScorerGlobal"]


class ScorerFunction(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["function"]]


class ScorerGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


Scorer: TypeAlias = Union[ScorerFunction, ScorerGlobal]


class OnlineScoreConfig(TypedDict, total=False):
    sampling_rate: Required[float]
    """The sampling rate for online scoring"""

    scorers: Required[Iterable[Scorer]]
    """The list of scorers to use for online scoring"""

    apply_to_root_span: Optional[bool]
    """Whether to trigger online scoring on the root span of each trace"""

    apply_to_span_names: Optional[List[str]]
    """Trigger online scoring on any spans with a name in this list"""
