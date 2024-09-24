# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from ..types import function_update_params
from .shared_params.prompt_data import PromptData

__all__ = ["FunctionUpdateParams"]


class FunctionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    function_data: function_update_params.FunctionData

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""
