# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from .shared_params.insert_dataset_event_replace import InsertDatasetEventReplace

from .shared_params.insert_dataset_event_merge import InsertDatasetEventMerge

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["DatasetInsertParams", "Event"]

class DatasetInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of dataset events to insert"""

Event: TypeAlias = Union[InsertDatasetEventReplace, InsertDatasetEventMerge]