# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...types import shared_params

__all__ = ["LogInsertParams"]


class LogInsertParams(TypedDict, total=False):
    events: Required[Iterable[shared_params.InsertProjectLogsEvent]]
    """A list of project logs events to insert"""
