# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..types import shared_params

__all__ = ["ExperimentInsertParams"]


class ExperimentInsertParams(TypedDict, total=False):
    events: Required[Iterable[shared_params.InsertExperimentEvent]]
    """A list of experiment events to insert"""
