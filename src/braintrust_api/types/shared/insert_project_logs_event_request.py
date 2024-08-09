# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .insert_project_logs_event_merge import InsertProjectLogsEventMerge
from .insert_project_logs_event_replace import InsertProjectLogsEventReplace

__all__ = ["InsertProjectLogsEventRequest", "Event"]

Event: TypeAlias = Union[InsertProjectLogsEventReplace, InsertProjectLogsEventMerge]


class InsertProjectLogsEventRequest(BaseModel):
    events: List[Event]
    """A list of project logs events to insert"""
