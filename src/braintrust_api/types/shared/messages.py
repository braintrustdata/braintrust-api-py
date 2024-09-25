# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..image_url import ImageURL

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


class System(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


class UserContentArrayText(BaseModel):
    type: Literal["text"]

    text: Optional[str] = None


class UserContentArrayImageURL(BaseModel):
    image_url: ImageURL

    type: Literal["image_url"]


UserContentArray: TypeAlias = Union[UserContentArrayText, UserContentArrayImageURL]


class User(BaseModel):
    role: Literal["user"]

    content: Union[str, List[UserContentArray], None] = None

    name: Optional[str] = None


class AssistantFunctionCall(BaseModel):
    arguments: str

    name: str


class AssistantToolCallFunction(BaseModel):
    arguments: str

    name: str


class AssistantToolCall(BaseModel):
    id: str

    function: AssistantToolCallFunction

    type: Literal["function"]


class Assistant(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[AssistantFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[AssistantToolCall]] = None


class Tool(BaseModel):
    role: Literal["tool"]

    content: Optional[str] = None

    tool_call_id: Optional[str] = None


class Function(BaseModel):
    name: str

    role: Literal["function"]

    content: Optional[str] = None


class Fallback(BaseModel):
    role: Literal["model"]

    content: Optional[str] = None


Messages: TypeAlias = Union[System, User, Assistant, Tool, Function, Fallback]
