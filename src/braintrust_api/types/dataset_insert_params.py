# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.insert_dataset_event_merge import InsertDatasetEventMerge
from .shared_params.insert_dataset_event_replace import InsertDatasetEventReplace

__all__ = ["DatasetInsertParams", "Event"]


class DatasetInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of dataset events to insert"""


Event: TypeAlias = Union[InsertDatasetEventReplace, InsertDatasetEventMerge]
