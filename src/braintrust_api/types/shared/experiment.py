# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .repo_info import RepoInfo

__all__ = ["Experiment"]


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

    metadata: Optional[Dict[str, Optional[object]]] = None
    """User-controlled metadata about the experiment"""

    repo_info: Optional[RepoInfo] = None
    """Metadata about the state of the repo when the experiment was created"""

    user_id: Optional[str] = None
    """Identifies the user who created the experiment"""
