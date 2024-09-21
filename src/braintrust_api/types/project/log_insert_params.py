# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union

from ..shared_params.insert_project_logs_event_replace import InsertProjectLogsEventReplace

from ..shared_params.insert_project_logs_event_merge import InsertProjectLogsEventMerge

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["LogInsertParams", "Event"]

class LogInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of project logs events to insert"""

Event: TypeAlias = Union[InsertProjectLogsEventReplace, InsertProjectLogsEventMerge]