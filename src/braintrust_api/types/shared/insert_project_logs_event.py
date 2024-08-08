# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .insert_project_logs_event_merge import InsertProjectLogsEventMerge
from .insert_project_logs_event_replace import InsertProjectLogsEventReplace

__all__ = ["InsertProjectLogsEvent"]

InsertProjectLogsEvent: TypeAlias = Union[InsertProjectLogsEventReplace, InsertProjectLogsEventMerge]
