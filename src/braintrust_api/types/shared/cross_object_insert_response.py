# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .insert_events_response import InsertEventsResponse

__all__ = ["CrossObjectInsertResponse"]


class CrossObjectInsertResponse(BaseModel):
    dataset: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from dataset id to row ids for inserted `events`"""

    experiment: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from experiment id to row ids for inserted `events`"""

    project_logs: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from project id to row ids for inserted `events`"""
