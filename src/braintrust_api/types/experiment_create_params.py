# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared_params.repo_info import RepoInfo

__all__ = ["ExperimentCreateParams"]


class ExperimentCreateParams(TypedDict, total=False):
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

    ensure_new: Optional[bool]
    """
    Normally, creating an experiment with the same name as an existing experiment
    will return the existing one un-modified. But if `ensure_new` is true,
    registration will generate a new experiment with a unique name in case of a
    conflict.
    """

    metadata: Optional[Dict[str, Optional[object]]]
    """User-controlled metadata about the experiment"""

    name: Optional[str]
    """Name of the experiment. Within a project, experiment names are unique"""

    public: Optional[bool]
    """Whether or not the experiment is public.

    Public experiments can be viewed by anybody inside or outside the organization
    """

    repo_info: Optional[RepoInfo]
    """Metadata about the state of the repo when the experiment was created"""
