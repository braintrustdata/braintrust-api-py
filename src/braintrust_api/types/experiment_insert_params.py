# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ExperimentInsertParams", "Event"]

class ExperimentInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of experiment events to insert"""

Event: TypeAlias = Union[shared_params.InsertExperimentEventReplace, shared_params.InsertExperimentEventMerge]