# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .repo_info import RepoInfo

__all__ = ["PatchExperiment"]


class PatchExperiment(BaseModel):
    base_exp_id: Optional[str] = None
    """Id of default base experiment to compare against when viewing this experiment"""

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

    description: Optional[str] = None
    """Textual description of the experiment"""

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the experiment"""

    name: Optional[str] = None
    """Name of the experiment. Within a project, experiment names are unique"""

    public: Optional[bool] = None
    """Whether or not the experiment is public.

    Public experiments can be viewed by anybody inside or outside the organization
    """

    repo_info: Optional[RepoInfo] = None
    """Metadata about the state of the repo when the experiment was created"""
