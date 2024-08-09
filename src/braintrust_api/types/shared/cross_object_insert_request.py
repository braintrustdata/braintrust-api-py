# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .feedback_dataset_item import FeedbackDatasetItem
from .feedback_experiment_item import FeedbackExperimentItem
from .feedback_project_logs_item import FeedbackProjectLogsItem
from .insert_dataset_event_merge import InsertDatasetEventMerge
from .insert_dataset_event_replace import InsertDatasetEventReplace
from .insert_experiment_event_merge import InsertExperimentEventMerge
from .insert_experiment_event_replace import InsertExperimentEventReplace
from .insert_project_logs_event_merge import InsertProjectLogsEventMerge
from .insert_project_logs_event_replace import InsertProjectLogsEventReplace

__all__ = [
    "CrossObjectInsertRequest",
    "Dataset",
    "DatasetEvent",
    "Experiment",
    "ExperimentEvent",
    "ProjectLogs",
    "ProjectLogsEvent",
]

DatasetEvent: TypeAlias = Union[InsertDatasetEventReplace, InsertDatasetEventMerge]


class Dataset(BaseModel):
    events: Optional[List[DatasetEvent]] = None
    """A list of dataset events to insert"""

    feedback: Optional[List[FeedbackDatasetItem]] = None
    """A list of dataset feedback items"""


ExperimentEvent: TypeAlias = Union[InsertExperimentEventReplace, InsertExperimentEventMerge]


class Experiment(BaseModel):
    events: Optional[List[ExperimentEvent]] = None
    """A list of experiment events to insert"""

    feedback: Optional[List[FeedbackExperimentItem]] = None
    """A list of experiment feedback items"""


ProjectLogsEvent: TypeAlias = Union[InsertProjectLogsEventReplace, InsertProjectLogsEventMerge]


class ProjectLogs(BaseModel):
    events: Optional[List[ProjectLogsEvent]] = None
    """A list of project logs events to insert"""

    feedback: Optional[List[FeedbackProjectLogsItem]] = None
    """A list of project logs feedback items"""


class CrossObjectInsertRequest(BaseModel):
    dataset: Optional[Dict[str, Dataset]] = None
    """A mapping from dataset id to a set of log events and feedback items to insert"""

    experiment: Optional[Dict[str, Experiment]] = None
    """
    A mapping from experiment id to a set of log events and feedback items to insert
    """

    project_logs: Optional[Dict[str, ProjectLogs]] = None
    """A mapping from project id to a set of log events and feedback items to insert"""
