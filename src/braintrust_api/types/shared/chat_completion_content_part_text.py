# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletionContentPartText"]


class ChatCompletionContentPartText(BaseModel):
    type: Literal["text"]

    text: Optional[str] = None
