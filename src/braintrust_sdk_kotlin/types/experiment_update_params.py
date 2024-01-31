# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExperimentUpdateParams", "RepoInfo"]


class ExperimentUpdateParams(TypedDict, total=False):
    project_id: Required[str]
    """Unique identifier for the project that the experiment belongs under"""

    base_exp_id: Optional[str]
    """Id of default base experiment to compare against when viewing this experiment"""

    dataset_id: Optional[str]
    """
    Identifier of the linked dataset, or null if the experiment is not linked to a
    dataset
    """

    dataset_version: Optional[str]
    """Version number of the linked dataset the experiment was run against.

    This can be used to reproduce the experiment after the dataset has been
    modified.
    """

    description: Optional[str]
    """Textual description of the experiment"""

    metadata: Optional[Dict[str, object]]
    """User-controlled metadata about the experiment"""

    name: Optional[str]
    """Name of the experiment. Within a project, experiment names are unique"""

    public: Optional[bool]
    """Whether or not the experiment is public.

    Public experiments can be viewed by anybody inside or outside the organization
    """

    repo_info: Optional[RepoInfo]
    """Metadata about the state of the repo when the experiment was created"""


class RepoInfo(TypedDict, total=False):
    author_email: Optional[str]
    """Email of the author of the most recent commit"""

    author_name: Optional[str]
    """Name of the author of the most recent commit"""

    branch: Optional[str]
    """Name of the branch the most recent commit belongs to"""

    commit: Optional[str]
    """SHA of most recent commit"""

    commit_message: Optional[str]
    """Most recent commit message"""

    commit_time: Optional[str]
    """Time of the most recent commit"""

    dirty: Optional[bool]
    """Whether or not the repo had uncommitted changes when snapshotted"""

    git_diff: Optional[str]
    """
    If the repo was dirty when run, this includes the diff between the current state
    of the repo and the most recent commit.
    """

    tag: Optional[str]
    """Name of the tag on the most recent commit"""
