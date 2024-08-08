# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["InsertEventsResponse"]


class InsertEventsResponse(BaseModel):
    row_ids: List[str]
    """
    The ids of all rows that were inserted, aligning one-to-one with the rows
    provided as input
    """
