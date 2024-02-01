# File generated from our OpenAPI spec by Stainless.

from typing import List

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    objects: List[Project]
    """A list of project objects"""
