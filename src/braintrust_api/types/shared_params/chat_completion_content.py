# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias

from .chat_completion_content_part_text import ChatCompletionContentPartText
from .chat_completion_content_part_image import ChatCompletionContentPartImage

__all__ = ["ChatCompletionContent", "Array"]

Array: TypeAlias = Union[ChatCompletionContentPartText, ChatCompletionContentPartImage]

ChatCompletionContent: TypeAlias = Union[str, Iterable[Array]]
