# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionMessageToolCall", "Function"]


class Function(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class ChatCompletionMessageToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[Function]

    type: Required[Literal["function"]]
