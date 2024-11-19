# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .chat_completion_content_part_text import ChatCompletionContentPartText
from .chat_completion_content_part_image import ChatCompletionContentPartImage

__all__ = ["ChatCompletionContent", "Array"]

Array: TypeAlias = Union[ChatCompletionContentPartText, ChatCompletionContentPartImage]

ChatCompletionContent: TypeAlias = Union[str, List[Array]]
