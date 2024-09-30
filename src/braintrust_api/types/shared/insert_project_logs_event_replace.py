# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InsertProjectLogsEventReplace", "Context", "Metrics", "SpanAttributes"]


class Context(BaseModel):
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
        def __getattr__(self, attr: str) -> Optional[object]: ...


class Metrics(BaseModel):
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
        def __getattr__(self, attr: str) -> Optional[object]: ...


class SpanAttributes(BaseModel):
    name: Optional[str] = None
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]] = None
    """Type of the span, for display purposes only"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class InsertProjectLogsEventReplace(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the project logs event.

    If you don't provide one, BrainTrust will generate one for you
    """

    is_merge: Optional[bool] = FieldInfo(alias="_is_merge", default=None)
    """
    The `_is_merge` field controls how the row is merged with any existing row with
    the same id in the DB. By default (or when set to `false`), the existing row is
    completely replaced by the new row. When set to `true`, the new row is
    deep-merged into the existing row

    For example, say there is an existing row in the DB
    `{"id": "foo", "input": {"a": 5, "b": 10}}`. If we merge a new row as
    `{"_is_merge": true, "id": "foo", "input": {"b": 11, "c": 20}}`, the new row
    will be `{"id": "foo", "input": {"a": 5, "b": 11, "c": 20}}`. If we replace the
    new row as `{"id": "foo", "input": {"b": 11, "c": 20}}`, the new row will be
    `{"id": "foo", "input": {"b": 11, "c": 20}}`
    """

    object_delete: Optional[bool] = FieldInfo(alias="_object_delete", default=None)
    """Pass `_object_delete=true` to mark the project logs event deleted.

    Deleted events will not show up in subsequent fetches for this project logs
    """

    parent_id: Optional[str] = FieldInfo(alias="_parent_id", default=None)
    """Use the `_parent_id` field to create this row as a subspan of an existing row.

    It cannot be specified alongside `_is_merge=true`. Tracking hierarchical
    relationships are important for tracing (see the
    [guide](https://www.braintrust.dev/docs/guides/tracing) for full details).

    For example, say we have logged a row
    `{"id": "abc", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"_parent_id": "abc", "id": "llm_call", "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.
    """

    context: Optional[Context] = None
    """
    Context is additional information about the code that produced the project logs
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the project
    logs event
    """

    created: Optional[datetime] = None
    """The timestamp the project logs event was created"""

    error: Optional[object] = None
    """The error that occurred, if any."""

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

    metadata: Optional[Dict[str, Optional[object]]] = None
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    metrics: Optional[Metrics] = None
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

    span_attributes: Optional[SpanAttributes] = None
    """Human-identifying attributes of the span, such as name, type, etc."""

    tags: Optional[List[str]] = None
    """A list of tags to log"""
