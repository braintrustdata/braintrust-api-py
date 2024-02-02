# File generated from our OpenAPI spec by Stainless.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentFetchPostResponse", "Event", "EventContext", "EventMetrics", "EventSpanAttributes"]


class EventContext(BaseModel):
    caller_filename: Optional[str] = None
    """Name of the file in code where the experiment event was created"""

    caller_functionname: Optional[str] = None
    """The function in code which created the experiment event"""

    caller_lineno: Optional[int] = None
    """Line of code where the experiment event was created"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...


class EventMetrics(BaseModel):
    end: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the
    experiment event finished
    """

    start: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the
    experiment event started
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...


class EventSpanAttributes(BaseModel):
    name: Optional[str] = None
    """Name of the span, for display purposes only"""

    type: Optional[str] = None
    """Type of the span, for display purposes only"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...


class Event(BaseModel):
    id: str
    """A unique identifier for the experiment event.

    If you don't provide one, BrainTrust will generate one for you
    """

    api_xact_id: int = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the experiment (see the
    `version` parameter)
    """

    experiment_id: str
    """Unique identifier for the experiment"""

    project_id: str
    """Unique identifier for the project that the experiment belongs under"""

    root_span_id: str
    """The `span_id` of the root of the trace this experiment event belongs to"""

    span_id: str
    """
    A unique identifier used to link different experiment events together as part of
    a full trace. See the
    [tracing guide](https://www.braintrustdata.com/docs/guides/tracing) for full
    details on tracing
    """

    context: Optional[EventContext] = None
    """
    Context is additional information about the code that produced the experiment
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the
    experiment event
    """

    created: Optional[datetime] = None
    """The timestamp the experiment event was created"""

    dataset_record_id: Optional[str] = None
    """
    If the experiment is associated to a dataset, this is the event-level dataset id
    this experiment event is tied to
    """

    expected: Optional[object] = None
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not.
    Braintrust currently does not compare `output` to `expected` for you, since
    there are so many different ways to do that correctly. Instead, these values are
    just used to help you navigate your experiments while digging into analyses.
    However, we may later use these values to re-score outputs or fine-tune your
    models
    """

    input: Optional[object] = None
    """
    The arguments that uniquely define a test case (an arbitrary, JSON serializable
    object). Later on, Braintrust will use the `input` to know whether two test
    cases are the same between experiments, so they should not contain
    experiment-specific state. A simple rule of thumb is that if you run the same
    experiment twice, the `input` should be identical
    """

    metadata: Optional[Dict[str, object]] = None
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    metrics: Optional[EventMetrics] = None
    """
    Metrics are numerical measurements tracking the execution of the code that
    produced the experiment event. Use "start" and "end" to track the time span over
    which the experiment event was produced
    """

    output: Optional[object] = None
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object), that allows you to determine whether the result is correct
    or not. For example, in an app that generates SQL queries, the `output` should
    be the _result_ of the SQL query generated by the model, not the query itself,
    because there may be multiple valid queries that answer a single question
    """

    scores: Optional[Dict[str, Optional[float]]] = None
    """A dictionary of numeric values (between 0 and 1) to log.

    The scores should give you a variety of signals that help you determine how
    accurate the outputs are compared to what you expect and diagnose failures. For
    example, a summarization app might have one score that tells you how accurate
    the summary is, and another that measures the word similarity between the
    generated and grouth truth summary. The word similarity score could help you
    determine whether the summarization was covering similar concepts or not. You
    can use these scores to help you sort, filter, and compare experiments
    """

    span_attributes: Optional[EventSpanAttributes] = None
    """Human-identifying attributes of the span, such as name, type, etc."""

    span_parents: Optional[List[str]] = None
    """An array of the parent `span_ids` of this experiment event.

    This should be empty for the root span of a trace, and should most often contain
    just one parent element for subspans
    """


class ExperimentFetchPostResponse(BaseModel):
    events: List[Event]
    """A list of fetched events"""
