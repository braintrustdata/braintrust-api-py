# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObjectReference"]


class ObjectReference(TypedDict, total=False):
    id: Required[str]
    """ID of the original event."""

    _xact_id: Required[str]
    """Transaction ID of the original event."""

    object_id: Required[str]
    """ID of the object the event is originating from."""

    object_type: Required[Literal["experiment", "dataset", "prompt", "function", "prompt_session", "project_logs"]]
    """Type of the object the event is originating from."""

    created: Optional[str]
    """Created timestamp of the original event. Used to help sort in the UI"""
