# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.insert_dataset_event import InsertDatasetEvent

__all__ = ["DatasetInsertParams"]


class DatasetInsertParams(TypedDict, total=False):
    events: Required[Iterable[InsertDatasetEvent]]
    """A list of dataset events to insert"""
