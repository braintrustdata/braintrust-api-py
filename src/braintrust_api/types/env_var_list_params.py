# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EnvVarListParams"]


class EnvVarListParams(TypedDict, total=False):
    env_var_name: str
    """Name of the env_var to search for"""

    ids: Union[str, List[str]]
    """Filter search results to a particular set of object IDs.

    To specify a list of IDs, include the query param multiple times
    """

    limit: Optional[int]
    """Limit the number of objects to return"""

    object_id: str
    """The id of the object the environment variable is scoped for"""

    object_type: Literal["organization", "project", "function"]
    """The type of the object the environment variable is scoped for"""
