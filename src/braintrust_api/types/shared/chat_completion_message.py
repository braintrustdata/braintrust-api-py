# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
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


class System(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


class User(BaseModel):
    role: Literal["user"]

    content: Optional[ChatCompletionContent] = None

    name: Optional[str] = None


class AssistantFunctionCall(BaseModel):
    arguments: str

    name: str


class Assistant(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[AssistantFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None


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


ChatCompletionMessage: TypeAlias = Union[System, User, Assistant, Tool, Function, Fallback]
