# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .insert_dataset_event import InsertDatasetEvent

__all__ = ["InsertDatasetEventRequest"]


class InsertDatasetEventRequest(BaseModel):
    events: List[InsertDatasetEvent]
    """A list of dataset events to insert"""
