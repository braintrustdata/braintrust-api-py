# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "LogInsertParams",
    "Event",
    "EventInsertProjectLogsEventReplace",
    "EventInsertProjectLogsEventReplaceContext",
    "EventInsertProjectLogsEventReplaceMetrics",
    "EventInsertProjectLogsEventReplaceSpanAttributes",
    "EventInsertProjectLogsEventMerge",
    "EventInsertProjectLogsEventMergeContext",
    "EventInsertProjectLogsEventMergeMetrics",
    "EventInsertProjectLogsEventMergeSpanAttributes",
]


class LogInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of project logs events to insert"""


class EventInsertProjectLogsEventReplaceContext(TypedDict, total=False):
    caller_filename: Optional[str]
    """Name of the file in code where the project logs event was created"""

    caller_functionname: Optional[str]
    """The function in code which created the project logs event"""

    caller_lineno: Optional[int]
    """Line of code where the project logs event was created"""


class EventInsertProjectLogsEventReplaceMetrics(TypedDict, total=False):
    end: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the project
    logs event finished
    """

    start: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the project
    logs event started
    """


class EventInsertProjectLogsEventReplaceSpanAttributes(TypedDict, total=False):
    name: Optional[str]
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]]
    """Type of the span, for display purposes only"""


class EventInsertProjectLogsEventReplace(TypedDict, total=False):
    id: Optional[str]
    """A unique identifier for the project logs event.

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
    """Pass `_object_delete=true` to mark the project logs event deleted.

    Deleted events will not show up in subsequent fetches for this project logs
    """

    _parent_id: Optional[str]
    """Use the `_parent_id` field to create this row as a subspan of an existing row.

    It cannot be specified alongside `_is_merge=true`. Tracking hierarchical
    relationships are important for tracing (see the
    [guide](https://www.braintrustdata.com/docs/guides/tracing) for full details).

    For example, say we have logged a row
    `{"id": "abc", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"_parent_id": "abc", "id": "llm_call", "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.
    """

    context: Optional[EventInsertProjectLogsEventReplaceContext]
    """
    Context is additional information about the code that produced the project logs
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the project
    logs event
    """

    expected: object
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not.
    Braintrust currently does not compare `output` to `expected` for you, since
    there are so many different ways to do that correctly. Instead, these values are
    just used to help you navigate while digging into analyses. However, we may
    later use these values to re-score outputs or fine-tune your models.
    """

    input: object
    """
    The arguments that uniquely define a user input(an arbitrary, JSON serializable
    object).
    """

    metadata: Optional[Dict[str, object]]
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    metrics: Optional[EventInsertProjectLogsEventReplaceMetrics]
    """
    Metrics are numerical measurements tracking the execution of the code that
    produced the project logs event. Use "start" and "end" to track the time span
    over which the project logs event was produced
    """

    output: object
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object), that allows you to determine whether the result is correct
    or not. For example, in an app that generates SQL queries, the `output` should
    be the _result_ of the SQL query generated by the model, not the query itself,
    because there may be multiple valid queries that answer a single question.
    """

    scores: Optional[Dict[str, Optional[float]]]
    """A dictionary of numeric values (between 0 and 1) to log.

    The scores should give you a variety of signals that help you determine how
    accurate the outputs are compared to what you expect and diagnose failures. For
    example, a summarization app might have one score that tells you how accurate
    the summary is, and another that measures the word similarity between the
    generated and grouth truth summary. The word similarity score could help you
    determine whether the summarization was covering similar concepts or not. You
    can use these scores to help you sort, filter, and compare logs.
    """

    span_attributes: Optional[EventInsertProjectLogsEventReplaceSpanAttributes]
    """Human-identifying attributes of the span, such as name, type, etc."""


class EventInsertProjectLogsEventMergeContext(TypedDict, total=False):
    caller_filename: Optional[str]
    """Name of the file in code where the project logs event was created"""

    caller_functionname: Optional[str]
    """The function in code which created the project logs event"""

    caller_lineno: Optional[int]
    """Line of code where the project logs event was created"""


class EventInsertProjectLogsEventMergeMetrics(TypedDict, total=False):
    end: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the project
    logs event finished
    """

    start: Optional[float]
    """
    A unix timestamp recording when the section of code which produced the project
    logs event started
    """


class EventInsertProjectLogsEventMergeSpanAttributes(TypedDict, total=False):
    name: Optional[str]
    """Name of the span, for display purposes only"""

    type: Optional[Literal["llm", "score", "function", "eval", "task", "tool"]]
    """Type of the span, for display purposes only"""


class EventInsertProjectLogsEventMerge(TypedDict, total=False):
    _is_merge: Required[bool]
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

    id: Optional[str]
    """A unique identifier for the project logs event.

    If you don't provide one, BrainTrust will generate one for you
    """

    _merge_paths: Optional[Iterable[List[str]]]
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

    _object_delete: Optional[bool]
    """Pass `_object_delete=true` to mark the project logs event deleted.

    Deleted events will not show up in subsequent fetches for this project logs
    """

    context: Optional[EventInsertProjectLogsEventMergeContext]
    """
    Context is additional information about the code that produced the project logs
    event. It is essentially the textual counterpart to `metrics`. Use the
    `caller_*` attributes to track the location in code which produced the project
    logs event
    """

    expected: object
    """
    The ground truth value (an arbitrary, JSON serializable object) that you'd
    compare to `output` to determine if your `output` value is correct or not.
    Braintrust currently does not compare `output` to `expected` for you, since
    there are so many different ways to do that correctly. Instead, these values are
    just used to help you navigate while digging into analyses. However, we may
    later use these values to re-score outputs or fine-tune your models.
    """

    input: object
    """
    The arguments that uniquely define a user input(an arbitrary, JSON serializable
    object).
    """

    metadata: Optional[Dict[str, object]]
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    metrics: Optional[EventInsertProjectLogsEventMergeMetrics]
    """
    Metrics are numerical measurements tracking the execution of the code that
    produced the project logs event. Use "start" and "end" to track the time span
    over which the project logs event was produced
    """

    output: object
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object), that allows you to determine whether the result is correct
    or not. For example, in an app that generates SQL queries, the `output` should
    be the _result_ of the SQL query generated by the model, not the query itself,
    because there may be multiple valid queries that answer a single question.
    """

    scores: Optional[Dict[str, Optional[float]]]
    """A dictionary of numeric values (between 0 and 1) to log.

    The scores should give you a variety of signals that help you determine how
    accurate the outputs are compared to what you expect and diagnose failures. For
    example, a summarization app might have one score that tells you how accurate
    the summary is, and another that measures the word similarity between the
    generated and grouth truth summary. The word similarity score could help you
    determine whether the summarization was covering similar concepts or not. You
    can use these scores to help you sort, filter, and compare logs.
    """

    span_attributes: Optional[EventInsertProjectLogsEventMergeSpanAttributes]
    """Human-identifying attributes of the span, such as name, type, etc."""


Event = Union[EventInsertProjectLogsEventReplace, EventInsertProjectLogsEventMerge]
