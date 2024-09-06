# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from ..types import shared_params

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the prompt"""

    project_id: Required[str]
    """Unique identifier for the project that the prompt belongs under"""

    slug: Required[str]
    """Unique identifier for the prompt"""

    description: Optional[str]
    """Textual description of the prompt"""

    prompt_data: Optional[shared_params.PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""
