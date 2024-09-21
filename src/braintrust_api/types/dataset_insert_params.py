# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["DatasetInsertParams", "Event"]

class DatasetInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of dataset events to insert"""

Event: TypeAlias = Union[shared_params.InsertDatasetEventReplace, shared_params.InsertDatasetEventMerge]