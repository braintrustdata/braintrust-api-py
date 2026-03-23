# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectSettings", "SpanFieldOrder"]


class SpanFieldOrder(BaseModel):
    column_id: str

    object_type: str

    position: str

    layout: Optional[Literal["full", "two_column"]] = None


class ProjectSettings(BaseModel):
    baseline_experiment_id: Optional[str] = None
    """The id of the experiment to use as the default baseline for comparisons"""

    comparison_key: Optional[str] = None
    """The key used to join two experiments (defaults to `input`)"""

    span_field_order: Optional[List[SpanFieldOrder]] = FieldInfo(alias="spanFieldOrder", default=None)
    """The order of the fields to display in the trace view"""
