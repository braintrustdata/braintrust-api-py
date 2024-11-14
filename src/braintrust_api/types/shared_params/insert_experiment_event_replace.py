# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InsertExperimentEventReplace", "Context", "Metrics", "SpanAttributes"]


class ContextTyped(TypedDict, total=False):
    caller_filename: Optional[str]
    """Name of the file in code where the experiment event was created"""

    caller_functionname: Optional[str]
    """The function in code which created the experiment event"""

    caller_lineno: Optional[int]
    """Line of code where the experiment event was created"""


Context: TypeAlias = Union[ContextTyped, Dict[str, Optional[object]]]


class MetricsTyped(TypedDict, total=False):
    caller_filename: Optional[object]
    """This metric is deprecated"""

    caller_functionname: Optional[object]
    """This metric is deprecated"""

    caller_lineno: Optional[object]
    """This metric is deprecated"""

    completion_tokens: Optional[int]
    """
    The number of tokens in the completion generated by the model (only set if this
    is an LLM span)
    """

    end: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the
    experiment event finished
    """

    prompt_tokens: Optional[int]
    """
    The number of tokens in the prompt used to generate the experiment event (only
    set if this is an LLM span)
    """

    start: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the
    experiment event started
    """

    tokens: Optional[int]
    """The total number of tokens in the input and output of the experiment event."""


Metrics: TypeAlias = Union[MetricsTyped, Dict[str, float]]


class SpanAttributesTyped(TypedDict, total=False):
    name: Optional[str]
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]]
    """Type of the span, for display purposes only"""


SpanAttributes: TypeAlias = Union[SpanAttributesTyped, Dict[str, Optional[object]]]


class InsertExperimentEventReplace(TypedDict, total=False):
    id: Optional[str]
    """A unique identifier for the experiment event.

    If you don't provide one, BrainTrust will generate one for you
    """

    _is_merge: Optional[bool]
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

    _object_delete: Optional[bool]
    """Pass `_object_delete=true` to mark the experiment event deleted.

    Deleted events will not show up in subsequent fetches for this experiment
    """

    _parent_id: Optional[str]
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

    context: Optional[Context]
    """
    Context is additional information about the code that produced the experiment
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the
    experiment event
    """

    created: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp the experiment event was created"""

    dataset_record_id: Optional[str]
    """
    If the experiment is associated to a dataset, this is the event-level dataset id
    this experiment event is tied to
    """

    error: Optional[object]
    """The error that occurred, if any."""

    expected: Optional[object]
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not.
    Braintrust currently does not compare `output` to `expected` for you, since
    there are so many different ways to do that correctly. Instead, these values are
    just used to help you navigate your experiments while digging into analyses.
    However, we may later use these values to re-score outputs or fine-tune your
    models
    """

    input: Optional[object]
    """
    The arguments that uniquely define a test case (an arbitrary, JSON serializable
    object). Later on, Braintrust will use the `input` to know whether two test
    cases are the same between experiments, so they should not contain
    experiment-specific state. A simple rule of thumb is that if you run the same
    experiment twice, the `input` should be identical
    """

    metadata: Optional[Dict[str, Optional[object]]]
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    metrics: Optional[Metrics]
    """
    Metrics are numerical measurements tracking the execution of the code that
    produced the experiment event. Use "start" and "end" to track the time span over
    which the experiment event was produced
    """

    output: Optional[object]
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object), that allows you to determine whether the result is correct
    or not. For example, in an app that generates SQL queries, the `output` should
    be the _result_ of the SQL query generated by the model, not the query itself,
    because there may be multiple valid queries that answer a single question
    """

    scores: Optional[Dict[str, Optional[float]]]
    """A dictionary of numeric values (between 0 and 1) to log.

    The scores should give you a variety of signals that help you determine how
    accurate the outputs are compared to what you expect and diagnose failures. For
    example, a summarization app might have one score that tells you how accurate
    the summary is, and another that measures the word similarity between the
    generated and grouth truth summary. The word similarity score could help you
    determine whether the summarization was covering similar concepts or not. You
    can use these scores to help you sort, filter, and compare experiments
    """

    span_attributes: Optional[SpanAttributes]
    """Human-identifying attributes of the span, such as name, type, etc."""

    tags: Optional[List[str]]
    """A list of tags to log"""
