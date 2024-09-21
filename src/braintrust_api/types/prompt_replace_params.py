# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional, List

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PromptReplaceParams"]

class PromptReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the prompt"""

    project_id: Required[str]
    """Unique identifier for the project that the prompt belongs under"""

    slug: Required[str]
    """Unique identifier for the prompt"""

    description: Optional[str]
    """Textual description of the prompt"""

    function_type: Optional[Literal["task", "llm", "scorer"]]

    prompt_data: Optional[shared_params.PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""