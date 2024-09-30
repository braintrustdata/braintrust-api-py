# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InsertExperimentEventMerge", "Context", "Metrics", "SpanAttributes"]


class Context(BaseModel):
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
        def __getattr__(self, attr: str) -> Optional[object]: ...


class Metrics(BaseModel):
    completion_tokens: Optional[int] = None
    """
    The number of tokens in the completion generated by the model (only set if this
    is an LLM span)
    """

    end: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the
    experiment event finished
    """

    prompt_tokens: Optional[int] = None
    """
    The number of tokens in the prompt used to generate the experiment event (only
    set if this is an LLM span)
    """

    start: Optional[float] = None
    """
    A unix timestamp recording when the section of code which produced the
    experiment event started
    """

    tokens: Optional[int] = None
    """The total number of tokens in the input and output of the experiment event."""

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


class InsertExperimentEventMerge(BaseModel):
    is_merge: bool = FieldInfo(alias="_is_merge")
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

    id: Optional[str] = None
    """A unique identifier for the experiment event.

    If you don't provide one, BrainTrust will generate one for you
    """

    merge_paths: Optional[List[List[str]]] = FieldInfo(alias="_merge_paths", default=None)
    """The `_merge_paths` field allows controlling the depth of the merge.

    It can only be specified alongside `_is_merge=true`. `_merge_paths` is a list of
    paths, where each path is a list of field names. The deep merge will not descend
    below any of the specified merge paths.

    For example, say there is an existing row in the DB
    `{"id": "foo", "input": {"a": {"b": 10}, "c": {"d": 20}}, "output": {"a": 20}}`.
    If we merge a new row as
    `{"_is_merge": true, "_merge_paths": [["input", "a"], ["output"]], "input": {"a": {"q": 30}, "c": {"e": 30}, "bar": "baz"}, "output": {"d": 40}}`,
    the new row will be
    `{"id": "foo": "input": {"a": {"q": 30}, "c": {"d": 20, "e": 30}, "bar": "baz"}, "output": {"d": 40}}`.
    In this case, due to the merge paths, we have replaced `input.a` and `output`,
    but have still deep-merged `input` and `input.c`.
    """

    object_delete: Optional[bool] = FieldInfo(alias="_object_delete", default=None)
    """Pass `_object_delete=true` to mark the experiment event deleted.

    Deleted events will not show up in subsequent fetches for this experiment
    """

    context: Optional[Context] = None
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

    error: Optional[object] = None
    """The error that occurred, if any."""

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

    span_attributes: Optional[SpanAttributes] = None
    """Human-identifying attributes of the span, such as name, type, etc."""

    tags: Optional[List[str]] = None
    """A list of tags to log"""
