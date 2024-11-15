# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatasetEvent", "Origin"]


class Origin(BaseModel):
    id: str
    """ID of the original event."""

    xact_id: str = FieldInfo(alias="_xact_id")
    """Transaction ID of the original event."""

    object_id: str
    """ID of the object the event is originating from."""

    object_type: Literal["experiment", "dataset", "prompt", "function", "prompt_session", "project_logs"]
    """Type of the object the event is originating from."""


class DatasetEvent(BaseModel):
    id: str
    """A unique identifier for the dataset event.

    If you don't provide one, BrainTrust will generate one for you
    """

    xact_id: str = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the dataset (see the `version`
    parameter)
    """

    created: datetime
    """The timestamp the dataset event was created"""

    dataset_id: str
    """Unique identifier for the dataset"""

    project_id: str
    """Unique identifier for the project that the dataset belongs under"""

    root_span_id: str
    """A unique identifier for the trace this dataset event belongs to"""

    span_id: str
    """
    A unique identifier used to link different dataset events together as part of a
    full trace. See the
    [tracing guide](https://www.braintrust.dev/docs/guides/tracing) for full details
    on tracing
    """

    expected: Optional[object] = None
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object)
    """

    input: Optional[object] = None
    """
    The argument that uniquely define an input case (an arbitrary, JSON serializable
    object)
    """

    is_root: Optional[bool] = None
    """Whether this span is a root span"""

    metadata: Optional[Dict[str, Optional[object]]] = None
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    origin: Optional[Origin] = None
    """Indicates the event was copied from another object."""

    tags: Optional[List[str]] = None
    """A list of tags to log"""
