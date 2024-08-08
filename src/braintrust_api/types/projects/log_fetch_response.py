# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogFetchResponse", "Event", "EventContext", "EventMetrics", "EventSpanAttributes"]


class EventContext(BaseModel):
    caller_filename: Optional[str] = None
    """Name of the file in code where the project logs event was created"""

    caller_functionname: Optional[str] = None
    """The function in code which created the project logs event"""

    caller_lineno: Optional[int] = None
    """Line of code where the project logs event was created"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EventMetrics(BaseModel):
    completion_tokens: Optional[int] = None
    """
    The number of tokens in the completion generated by the model (only set if this
    is an LLM span)
    """

    end: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the project
    logs event finished
    """

    prompt_tokens: Optional[int] = None
    """
    The number of tokens in the prompt used to generate the project logs event (only
    set if this is an LLM span)
    """

    start: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the project
    logs event started
    """

    tokens: Optional[int] = None
    """The total number of tokens in the input and output of the project logs event."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class EventSpanAttributes(BaseModel):
    name: Optional[str] = None
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]] = None
    """Type of the span, for display purposes only"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Event(BaseModel):
    id: str
    """A unique identifier for the project logs event.

    If you don't provide one, BrainTrust will generate one for you
    """

    xact_id: str = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the project logs (see the
    `version` parameter)
    """

    created: datetime
    """The timestamp the project logs event was created"""

    log_id: Literal["g"]
    """A literal 'g' which identifies the log as a project log"""

    org_id: str
    """Unique id for the organization that the project belongs under"""

    project_id: str
    """Unique identifier for the project"""

    root_span_id: str
    """The `span_id` of the root of the trace this project logs event belongs to"""

    span_id: str
    """
    A unique identifier used to link different project logs events together as part
    of a full trace. See the
    [tracing guide](https://www.braintrust.dev/docs/guides/tracing) for full details
    on tracing
    """

    context: Optional[EventContext] = None
    """
    Context is additional information about the code that produced the project logs
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the project
    logs event
    """

    expected: Optional[object] = None
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not.
    Braintrust currently does not compare `output` to `expected` for you, since
    there are so many different ways to do that correctly. Instead, these values are
    just used to help you navigate while digging into analyses. However, we may
    later use these values to re-score outputs or fine-tune your models.
    """

    input: Optional[object] = None
    """
    The arguments that uniquely define a user input (an arbitrary, JSON serializable
    object).
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
    produced the project logs event. Use "start" and "end" to track the time span
    over which the project logs event was produced
    """

    output: Optional[object] = None
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object), that allows you to determine whether the result is correct
    or not. For example, in an app that generates SQL queries, the `output` should
    be the _result_ of the SQL query generated by the model, not the query itself,
    because there may be multiple valid queries that answer a single question.
    """

    scores: Optional[Dict[str, Optional[float]]] = None
    """A dictionary of numeric values (between 0 and 1) to log.

    The scores should give you a variety of signals that help you determine how
    accurate the outputs are compared to what you expect and diagnose failures. For
    example, a summarization app might have one score that tells you how accurate
    the summary is, and another that measures the word similarity between the
    generated and grouth truth summary. The word similarity score could help you
    determine whether the summarization was covering similar concepts or not. You
    can use these scores to help you sort, filter, and compare logs.
    """

    span_attributes: Optional[EventSpanAttributes] = None
    """Human-identifying attributes of the span, such as name, type, etc."""

    span_parents: Optional[List[str]] = None
    """An array of the parent `span_ids` of this project logs event.

    This should be empty for the root span of a trace, and should most often contain
    just one parent element for subspans
    """

    tags: Optional[List[str]] = None
    """A list of tags to log"""


class LogFetchResponse(BaseModel):
    events: List[Event]
    """A list of fetched events"""

    cursor: Optional[str] = None
    """Pagination cursor

    Pass this string directly as the `cursor` param to your next fetch request to
    get the next page of results. Not provided if the returned result set is empty.
    """
