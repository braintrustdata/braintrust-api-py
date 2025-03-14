# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProjectSettings", "SpanFieldOrder"]


class SpanFieldOrder(TypedDict, total=False):
    column_id: Required[str]

    object_type: Required[str]

    position: Required[str]

    layout: Optional[Literal["full", "two_column"]]


class ProjectSettings(TypedDict, total=False):
    baseline_experiment_id: Optional[str]
    """The id of the experiment to use as the default baseline for comparisons"""

    comparison_key: Optional[str]
    """The key used to join two experiments (defaults to `input`)"""

    span_field_order: Annotated[Optional[Iterable[SpanFieldOrder]], PropertyInfo(alias="spanFieldOrder")]
    """The order of the fields to display in the trace view"""
