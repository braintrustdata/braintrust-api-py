# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Experiment", "RepoInfo"]


class RepoInfo(BaseModel):
    author_email: Optional[str] = None
    """Email of the author of the most recent commit"""

    author_name: Optional[str] = None
    """Name of the author of the most recent commit"""

    branch: Optional[str] = None
    """Name of the branch the most recent commit belongs to"""

    commit: Optional[str] = None
    """SHA of most recent commit"""

    commit_message: Optional[str] = None
    """Most recent commit message"""

    commit_time: Optional[str] = None
    """Time of the most recent commit"""

    dirty: Optional[bool] = None
    """Whether or not the repo had uncommitted changes when snapshotted"""

    git_diff: Optional[str] = None
    """
    If the repo was dirty when run, this includes the diff between the current state
    of the repo and the most recent commit.
    """

    tag: Optional[str] = None
    """Name of the tag on the most recent commit"""


class Experiment(BaseModel):
    id: str
    """Unique identifier for the experiment"""

    name: str
    """Name of the experiment. Within a project, experiment names are unique"""

    project_id: str
    """Unique identifier for the project that the experiment belongs under"""

    public: bool
    """Whether or not the experiment is public.

    Public experiments can be viewed by anybody inside or outside the organization
    """

    base_exp_id: Optional[str] = None
    """Id of default base experiment to compare against when viewing this experiment"""

    commit: Optional[str] = None
    """Commit, taken directly from `repo_info.commit`"""

    created: Optional[datetime] = None
    """Date of experiment creation"""

    dataset_id: Optional[str] = None
    """
    Identifier of the linked dataset, or null if the experiment is not linked to a
    dataset
    """

    dataset_version: Optional[str] = None
    """Version number of the linked dataset the experiment was run against.

    This can be used to reproduce the experiment after the dataset has been
    modified.
    """

    deleted_at: Optional[datetime] = None
    """Date of experiment deletion, or null if the experiment is still active"""

    description: Optional[str] = None
    """Textual description of the experiment"""

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the experiment"""

    repo_info: Optional[RepoInfo] = None
    """Metadata about the state of the repo when the experiment was created"""

    user_id: Optional[str] = None
    """Identifies the user who created the experiment"""
