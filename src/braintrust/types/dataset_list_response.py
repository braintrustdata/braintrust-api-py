# File generated from our OpenAPI spec by Stainless.

from typing import List

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["DatasetListResponse"]


class DatasetListResponse(BaseModel):
    objects: List[Dataset]
    """A list of dataset objects"""
