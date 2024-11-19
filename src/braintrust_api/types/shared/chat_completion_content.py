# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .chat_completion_content_part import ChatCompletionContentPart

__all__ = ["ChatCompletionContent"]

ChatCompletionContent: TypeAlias = Union[str, List[ChatCompletionContentPart]]
