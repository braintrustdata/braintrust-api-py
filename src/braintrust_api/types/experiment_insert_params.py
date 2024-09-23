# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.insert_experiment_event_merge import InsertExperimentEventMerge
from .shared_params.insert_experiment_event_replace import InsertExperimentEventReplace

__all__ = ["ExperimentInsertParams", "Event"]


class ExperimentInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of experiment events to insert"""


Event: TypeAlias = Union[InsertExperimentEventReplace, InsertExperimentEventMerge]
