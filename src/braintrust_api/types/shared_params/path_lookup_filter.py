# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from typing_extensions import Literal, TypedDict, Required

__all__ = ["PathLookupFilter"]

class PathLookupFilter(TypedDict, total=False):
    path: Required[List[str]]
    """List of fields describing the path to the value to be checked against.

    For instance, if you wish to filter on the value of `c` in
    `{"input": {"a": {"b": {"c": "hello"}}}}`, pass `path=["input", "a", "b", "c"]`
    """

    type: Required[Literal["path_lookup"]]
    """Denotes the type of filter as a path-lookup filter"""

    value: object
    """
    The value to compare equality-wise against the event value at the specified
    `path`. The value must be a "primitive", that is, any JSON-serializable object
    except for objects and arrays. For instance, if you wish to filter on the value
    of "input.a.b.c" in the object `{"input": {"a": {"b": {"c": "hello"}}}}`, pass
    `value="hello"`
    """