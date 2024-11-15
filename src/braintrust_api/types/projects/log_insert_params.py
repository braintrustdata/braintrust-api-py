# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.insert_project_logs_event import InsertProjectLogsEvent

__all__ = ["LogInsertParams"]


class LogInsertParams(TypedDict, total=False):
    events: Required[Iterable[InsertProjectLogsEvent]]
    """A list of project logs events to insert"""
