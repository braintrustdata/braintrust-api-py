# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from ...types import shared_params

__all__ = ["InsertProjectLogsEvent"]

InsertProjectLogsEvent: TypeAlias = Union[
    shared_params.InsertProjectLogsEventReplace, shared_params.InsertProjectLogsEventMerge
]
