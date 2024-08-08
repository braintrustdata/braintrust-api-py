# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .prompt_data import PromptData

__all__ = ["PatchPrompt"]


class PatchPrompt(BaseModel):
    description: Optional[str] = None
    """Textual description of the prompt"""

    name: Optional[str] = None
    """Name of the prompt"""

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
