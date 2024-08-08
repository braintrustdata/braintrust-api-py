# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .dataset_event import DatasetEvent

__all__ = ["FetchDatasetEventsResponse"]


class FetchDatasetEventsResponse(BaseModel):
    events: List[DatasetEvent]
    """A list of fetched events"""

    cursor: Optional[str] = None
    """Pagination cursor

    Pass this string directly as the `cursor` param to your next fetch request to
    get the next page of results. Not provided if the returned result set is empty.
    """
