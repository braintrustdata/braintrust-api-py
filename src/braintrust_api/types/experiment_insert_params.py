# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.insert_experiment_event import InsertExperimentEvent

__all__ = ["ExperimentInsertParams"]


class ExperimentInsertParams(TypedDict, total=False):
    events: Required[Iterable[InsertExperimentEvent]]
    """A list of experiment events to insert"""
