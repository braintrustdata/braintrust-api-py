# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .insert_dataset_event import InsertDatasetEvent
from .feedback_dataset_item import FeedbackDatasetItem
from .insert_experiment_event import InsertExperimentEvent
from .feedback_experiment_item import FeedbackExperimentItem
from .insert_project_logs_event import InsertProjectLogsEvent
from .feedback_project_logs_item import FeedbackProjectLogsItem

__all__ = ["CrossObjectInsertRequest", "Dataset", "Experiment", "ProjectLogs"]


class Dataset(BaseModel):
    events: Optional[List[InsertDatasetEvent]] = None
    """A list of dataset events to insert"""

    feedback: Optional[List[FeedbackDatasetItem]] = None
    """A list of dataset feedback items"""


class Experiment(BaseModel):
    events: Optional[List[InsertExperimentEvent]] = None
    """A list of experiment events to insert"""

    feedback: Optional[List[FeedbackExperimentItem]] = None
    """A list of experiment feedback items"""


class ProjectLogs(BaseModel):
    events: Optional[List[InsertProjectLogsEvent]] = None
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
