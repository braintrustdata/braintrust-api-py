# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletionContentPartImage", "ImageURL"]


class ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class ChatCompletionContentPartImage(BaseModel):
    image_url: ImageURL

    type: Literal["image_url"]
