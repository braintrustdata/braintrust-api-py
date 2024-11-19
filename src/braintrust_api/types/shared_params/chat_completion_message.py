# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .chat_completion_content import ChatCompletionContent
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall

__all__ = [
    "ChatCompletionMessage",
    "System",
    "User",
    "Assistant",
    "AssistantFunctionCall",
    "Tool",
    "Function",
    "Fallback",
]


class System(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class User(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: ChatCompletionContent

    name: str


class AssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class Assistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: Optional[AssistantFunctionCall]

    name: Optional[str]

    tool_calls: Optional[Iterable[ChatCompletionMessageToolCall]]


class Tool(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class Function(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class Fallback(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


ChatCompletionMessage: TypeAlias = Union[System, User, Assistant, Tool, Function, Fallback]
