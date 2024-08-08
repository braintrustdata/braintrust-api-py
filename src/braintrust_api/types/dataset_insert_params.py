# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetInsertParams", "Event", "EventInsertDatasetEventReplace", "EventInsertDatasetEventMerge"]


class DatasetInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of dataset events to insert"""


class EventInsertDatasetEventReplace(TypedDict, total=False):
    id: Optional[str]
    """A unique identifier for the dataset event.

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
    """Pass `_object_delete=true` to mark the dataset event deleted.

    Deleted events will not show up in subsequent fetches for this dataset
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

    created: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp the dataset event was created"""

    expected: object
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object)
    """

    input: object
    """
    The argument that uniquely define an input case (an arbitrary, JSON serializable
    object)
    """

    metadata: Optional[Dict[str, object]]
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    tags: Optional[List[str]]
    """A list of tags to log"""


class EventInsertDatasetEventMerge(TypedDict, total=False):
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
    """A unique identifier for the dataset event.

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
    """Pass `_object_delete=true` to mark the dataset event deleted.

    Deleted events will not show up in subsequent fetches for this dataset
    """

    created: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp the dataset event was created"""

    expected: object
    """
    The output of your application, including post-processing (an arbitrary, JSON
    serializable object)
    """

    input: object
    """
    The argument that uniquely define an input case (an arbitrary, JSON serializable
    object)
    """

    metadata: Optional[Dict[str, object]]
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    tags: Optional[List[str]]
    """A list of tags to log"""


Event: TypeAlias = Union[EventInsertDatasetEventReplace, EventInsertDatasetEventMerge]
