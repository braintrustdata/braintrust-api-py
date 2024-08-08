# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .insert_experiment_event import InsertExperimentEvent

__all__ = ["InsertExperimentEventRequest"]


class InsertExperimentEventRequest(BaseModel):
    events: List[InsertExperimentEvent]
    """A list of experiment events to insert"""
