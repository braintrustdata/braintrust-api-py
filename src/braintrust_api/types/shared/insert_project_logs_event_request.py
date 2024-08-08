# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .insert_project_logs_event import InsertProjectLogsEvent

__all__ = ["InsertProjectLogsEventRequest"]


class InsertProjectLogsEventRequest(BaseModel):
    events: List[InsertProjectLogsEvent]
    """A list of project logs events to insert"""
