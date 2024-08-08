# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .insert_dataset_event_merge import InsertDatasetEventMerge
from .insert_dataset_event_replace import InsertDatasetEventReplace

__all__ = ["InsertDatasetEvent"]

InsertDatasetEvent: TypeAlias = Union[InsertDatasetEventReplace, InsertDatasetEventMerge]
