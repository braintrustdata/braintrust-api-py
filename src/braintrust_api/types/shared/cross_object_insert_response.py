# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Dict

from .insert_events_response import InsertEventsResponse

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CrossObjectInsertResponse"]

class CrossObjectInsertResponse(BaseModel):
    dataset: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from dataset id to row ids for inserted `events`"""

    experiment: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from experiment id to row ids for inserted `events`"""

    project_logs: Optional[Dict[str, InsertEventsResponse]] = None
    """A mapping from project id to row ids for inserted `events`"""