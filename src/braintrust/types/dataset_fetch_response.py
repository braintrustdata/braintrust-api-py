# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, Dict, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DatasetFetchResponse", "Event"]


class Event(BaseModel):
    id: str
    """A unique identifier for the dataset event.

    If you don't provide one, BrainTrust will generate one for you
    """

    api_xact_id: str = FieldInfo(alias="_xact_id")
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

    root_span_id: str
    """The `span_id` of the root of the trace this dataset event belongs to"""

    span_id: str
    """
    A unique identifier used to link different dataset events together as part of a
    full trace. See the
    [tracing guide](https://www.braintrustdata.com/docs/guides/tracing) for full
    details on tracing
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

    metadata: Optional[Dict[str, object]] = None
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    project_id: Optional[str] = None
    """Unique identifier for the project that the dataset belongs under"""

    tags: Optional[List[str]] = None
    """A list of tags to log"""


class DatasetFetchResponse(BaseModel):
    events: List[Event]
    """A list of fetched events"""

    cursor: Optional[str] = None
    """Pagination cursor

    Pass this string directly as the `cursor` param to your next fetch request to
    get the next page of results. Not provided if the returned result set is empty.
    """
