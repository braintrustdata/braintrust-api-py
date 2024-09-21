# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional, Dict

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ExperimentUpdateParams"]

class ExperimentUpdateParams(TypedDict, total=False):
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

    repo_info: Optional[shared_params.RepoInfo]
    """Metadata about the state of the repo when the experiment was created"""