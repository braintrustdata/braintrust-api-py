# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from ..types import shared_params

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[shared_params.PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""
