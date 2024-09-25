# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionContentPartImage", "ImageURL"]


class ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class ChatCompletionContentPartImage(TypedDict, total=False):
    image_url: Required[ImageURL]

    type: Required[Literal["image_url"]]
