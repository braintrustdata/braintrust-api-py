# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletionMessageToolCall", "Function"]


class Function(BaseModel):
    arguments: str

    name: str


class ChatCompletionMessageToolCall(BaseModel):
    id: str

    function: Function

    type: Literal["function"]
