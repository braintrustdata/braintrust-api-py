# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PathLookupFilter"]

class PathLookupFilter(BaseModel):
    path: List[str]
    """List of fields describing the path to the value to be checked against.

    For instance, if you wish to filter on the value of `c` in
    `{"input": {"a": {"b": {"c": "hello"}}}}`, pass `path=["input", "a", "b", "c"]`
    """

    type: Literal["path_lookup"]
    """Denotes the type of filter as a path-lookup filter"""

    value: Optional[object] = None
    """
    The value to compare equality-wise against the event value at the specified
    `path`. The value must be a "primitive", that is, any JSON-serializable object
    except for objects and arrays. For instance, if you wish to filter on the value
    of "input.a.b.c" in the object `{"input": {"a": {"b": {"c": "hello"}}}}`, pass
    `value="hello"`
    """