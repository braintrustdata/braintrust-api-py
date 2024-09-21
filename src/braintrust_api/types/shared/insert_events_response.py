# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InsertEventsResponse"]

class InsertEventsResponse(BaseModel):
    row_ids: List[str]
    """
    The ids of all rows that were inserted, aligning one-to-one with the rows
    provided as input
    """