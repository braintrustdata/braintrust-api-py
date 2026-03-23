# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectReference"]


class ObjectReference(BaseModel):
    id: str
    """ID of the original event."""

    xact_id: str = FieldInfo(alias="_xact_id")
    """Transaction ID of the original event."""

    object_id: str
    """ID of the object the event is originating from."""

    object_type: Literal["experiment", "dataset", "prompt", "function", "prompt_session", "project_logs"]
    """Type of the object the event is originating from."""

    created: Optional[str] = None
    """Created timestamp of the original event. Used to help sort in the UI"""
