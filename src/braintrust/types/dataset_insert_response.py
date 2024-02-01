# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel

__all__ = ["DatasetInsertResponse"]


class DatasetInsertResponse(BaseModel):
    row_ids: List[str]
    """
    The ids of all rows that were inserted, aligning one-to-one with the rows
    provided as input
    """
