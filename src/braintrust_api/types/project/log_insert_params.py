# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..shared_params.insert_project_logs_event_merge import InsertProjectLogsEventMerge
from ..shared_params.insert_project_logs_event_replace import InsertProjectLogsEventReplace

__all__ = ["LogInsertParams", "Event"]


class LogInsertParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of project logs events to insert"""


Event: TypeAlias = Union[InsertProjectLogsEventReplace, InsertProjectLogsEventMerge]
