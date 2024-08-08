# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .insert_experiment_event_merge import InsertExperimentEventMerge
from .insert_experiment_event_replace import InsertExperimentEventReplace

__all__ = ["InsertExperimentEvent"]

InsertExperimentEvent: TypeAlias = Union[InsertExperimentEventReplace, InsertExperimentEventMerge]
