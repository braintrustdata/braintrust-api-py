# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from .shared_params.insert_experiment_event_replace import InsertExperimentEventReplace

from .shared_params.insert_experiment_event_merge import InsertExperimentEventMerge

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ExperimentInsertParams", "Event"]

class ExperimentInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of experiment events to insert"""

Event: TypeAlias = Union[InsertExperimentEventReplace, InsertExperimentEventMerge]