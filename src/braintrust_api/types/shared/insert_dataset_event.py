# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InsertDatasetEvent"]


class InsertDatasetEvent(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the dataset event.

    If you don't provide one, BrainTrust will generate one for you
    """

    is_merge: Optional[bool] = FieldInfo(alias="_is_merge", default=None)
    """
    The `_is_merge` field controls how the row is merged with any existing row with
    the same id in the DB. By default (or when set to `false`), the existing row is
    completely replaced by the new row. When set to `true`, the new row is
    deep-merged into the existing row, if one is found. If no existing row is found,
    the new row is inserted as is.

    For example, say there is an existing row in the DB
    `{"id": "foo", "input": {"a": 5, "b": 10}}`. If we merge a new row as
    `{"_is_merge": true, "id": "foo", "input": {"b": 11, "c": 20}}`, the new row
    will be `{"id": "foo", "input": {"a": 5, "b": 11, "c": 20}}`. If we replace the
    new row as `{"id": "foo", "input": {"b": 11, "c": 20}}`, the new row will be
    `{"id": "foo", "input": {"b": 11, "c": 20}}`
    """

    merge_paths: Optional[List[List[str]]] = FieldInfo(alias="_merge_paths", default=None)
    """
    The `_merge_paths` field allows controlling the depth of the merge, when
    `_is_merge=true`. `_merge_paths` is a list of paths, where each path is a list
    of field names. The deep merge will not descend below any of the specified merge
    paths.

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
    """Pass `_object_delete=true` to mark the dataset event deleted.

    Deleted events will not show up in subsequent fetches for this dataset
    """

    parent_id: Optional[str] = FieldInfo(alias="_parent_id", default=None)
    """Use the `_parent_id` field to create this row as a subspan of an existing row.

    Tracking hierarchical relationships are important for tracing (see the
    [guide](https://www.braintrust.dev/docs/guides/tracing) for full details).

    For example, say we have logged a row
    `{"id": "abc", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"_parent_id": "abc", "id": "llm_call", "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.

    If the row is being merged into an existing row, this field will be ignored.
    """

    created: Optional[datetime] = None
    """The timestamp the dataset event was created"""

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

    metadata: Optional[Dict[str, Optional[object]]] = None
    """
    A dictionary with additional data about the test example, model outputs, or just
    about anything else that's relevant, that you can use to help find and analyze
    examples later. For example, you could log the `prompt`, example's `id`, or
    anything else that would be useful to slice/dice later. The values in `metadata`
    can be any JSON-serializable type, but its keys must be strings
    """

    root_span_id: Optional[str] = None
    """
    Use span_id, root_span_id, and span_parents as a more explicit alternative to
    \\__parent_id. The span_id is a unique identifier describing the row's place in
    the a trace, and the root_span_id is a unique identifier for the whole trace.
    See the [guide](https://www.braintrust.dev/docs/guides/tracing) for full
    details.

    For example, say we have logged a row
    `{"id": "abc", "span_id": "span0", "root_span_id": "root_span0", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"id": "llm_call", "span_id": "span1", "root_span_id": "root_span0", "span_parents": ["span0"], "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.

    If the row is being merged into an existing row, this field will be ignored.
    """

    span_id: Optional[str] = None
    """
    Use span_id, root_span_id, and span_parents as a more explicit alternative to
    \\__parent_id. The span_id is a unique identifier describing the row's place in
    the a trace, and the root_span_id is a unique identifier for the whole trace.
    See the [guide](https://www.braintrust.dev/docs/guides/tracing) for full
    details.

    For example, say we have logged a row
    `{"id": "abc", "span_id": "span0", "root_span_id": "root_span0", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"id": "llm_call", "span_id": "span1", "root_span_id": "root_span0", "span_parents": ["span0"], "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.

    If the row is being merged into an existing row, this field will be ignored.
    """

    span_parents: Optional[List[str]] = None
    """
    Use span_id, root_span_id, and span_parents as a more explicit alternative to
    \\__parent_id. The span_id is a unique identifier describing the row's place in
    the a trace, and the root_span_id is a unique identifier for the whole trace.
    See the [guide](https://www.braintrust.dev/docs/guides/tracing) for full
    details.

    For example, say we have logged a row
    `{"id": "abc", "span_id": "span0", "root_span_id": "root_span0", "input": "foo", "output": "bar", "expected": "boo", "scores": {"correctness": 0.33}}`.
    We can create a sub-span of the parent row by logging
    `{"id": "llm_call", "span_id": "span1", "root_span_id": "root_span0", "span_parents": ["span0"], "input": {"prompt": "What comes after foo?"}, "output": "bar", "metrics": {"tokens": 1}}`.
    In the webapp, only the root span row `"abc"` will show up in the summary view.
    You can view the full trace hierarchy (in this case, the `"llm_call"` row) by
    clicking on the "abc" row.

    If the row is being merged into an existing row, this field will be ignored.
    """

    tags: Optional[List[str]] = None
    """A list of tags to log"""
