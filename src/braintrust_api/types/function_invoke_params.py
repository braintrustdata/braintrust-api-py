# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["FunctionInvokeParams", "Parent", "ParentSpanParentStruct", "ParentSpanParentStructRowIDs"]


class FunctionInvokeParams(TypedDict, total=False):
    input: object
    """Argument to the function, which can be any JSON serializable value"""

    parent: Parent
    """Options for tracing the function call"""

    stream: bool
    """Whether to stream the response.

    If true, results will be returned in the Braintrust SSE format.
    """

    version: str
    """The version of the function"""


class ParentSpanParentStructRowIDs(TypedDict, total=False):
    id: Required[str]
    """The id of the row"""

    root_span_id: Required[str]
    """The root_span_id of the row"""

    span_id: Required[str]
    """The span_id of the row"""


class ParentSpanParentStruct(TypedDict, total=False):
    object_id: Required[str]
    """The id of the container object you are logging to"""

    object_type: Required[Literal["project_logs", "experiment"]]

    propagated_event: Optional[Dict[str, object]]
    """Include these properties in every span created under this parent"""

    row_ids: Optional[ParentSpanParentStructRowIDs]
    """Identifiers for the row to to log a subspan under"""


Parent: TypeAlias = Union[ParentSpanParentStruct, str]
