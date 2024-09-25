# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..image_url_param import ImageURLParam

__all__ = [
    "Messages",
    "System",
    "User",
    "UserContentArray",
    "UserContentArrayText",
    "UserContentArrayImageURL",
    "Assistant",
    "AssistantFunctionCall",
    "AssistantToolCall",
    "AssistantToolCallFunction",
    "Tool",
    "Function",
    "Fallback",
]


class System(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class UserContentArrayText(TypedDict, total=False):
    type: Required[Literal["text"]]

    text: str


class UserContentArrayImageURL(TypedDict, total=False):
    image_url: Required[ImageURLParam]

    type: Required[Literal["image_url"]]


UserContentArray: TypeAlias = Union[UserContentArrayText, UserContentArrayImageURL]


class User(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[UserContentArray]]

    name: str


class AssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class AssistantToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class AssistantToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[AssistantToolCallFunction]

    type: Required[Literal["function"]]


class Assistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: Optional[AssistantFunctionCall]

    name: Optional[str]

    tool_calls: Optional[Iterable[AssistantToolCall]]


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


Messages: TypeAlias = Union[System, User, Assistant, Tool, Function, Fallback]
