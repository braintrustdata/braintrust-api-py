# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .insert_dataset_event_merge import InsertDatasetEventMerge
from .insert_dataset_event_replace import InsertDatasetEventReplace

__all__ = ["InsertDatasetEventRequest", "Event"]

Event: TypeAlias = Union[InsertDatasetEventReplace, InsertDatasetEventMerge]


class InsertDatasetEventRequest(BaseModel):
    events: List[Event]
    """A list of dataset events to insert"""
