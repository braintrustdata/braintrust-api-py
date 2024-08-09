# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .insert_experiment_event_merge import InsertExperimentEventMerge
from .insert_experiment_event_replace import InsertExperimentEventReplace

__all__ = ["InsertExperimentEventRequest", "Event"]

Event: TypeAlias = Union[InsertExperimentEventReplace, InsertExperimentEventMerge]


class InsertExperimentEventRequest(BaseModel):
    events: List[Event]
    """A list of experiment events to insert"""
