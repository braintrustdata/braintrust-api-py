# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel
from .experiment import Experiment

__all__ = ["ExperimentListResponse"]


class ExperimentListResponse(BaseModel):
    objects: List[Experiment]
    """A list of experiment objects"""
