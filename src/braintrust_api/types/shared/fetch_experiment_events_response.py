# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from .experiment_event import ExperimentEvent

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FetchExperimentEventsResponse"]

class FetchExperimentEventsResponse(BaseModel):
    events: List[ExperimentEvent]
    """A list of fetched events"""

    cursor: Optional[str] = None
    """Pagination cursor

    Pass this string directly as the `cursor` param to your next fetch request to
    get the next page of results. Not provided if the returned result set is empty.
    """