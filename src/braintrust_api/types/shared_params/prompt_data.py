# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .prompt_options import PromptOptions
from .chat_completion_content_part_text import ChatCompletionContentPartText
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall
from .chat_completion_content_part_image import ChatCompletionContentPartImage

__all__ = [
    "PromptData",
    "Origin",
    "Parser",
    "Prompt",
    "PromptCompletion",
    "PromptChat",
    "PromptChatMessage",
    "PromptChatMessageSystem",
    "PromptChatMessageUser",
    "PromptChatMessageUserContentArray",
    "PromptChatMessageAssistant",
    "PromptChatMessageAssistantFunctionCall",
    "PromptChatMessageTool",
    "PromptChatMessageFunction",
    "PromptChatMessageFallback",
    "PromptNullableVariant",
    "ToolFunction",
    "ToolFunctionFunction",
    "ToolFunctionGlobal",
]


class Origin(TypedDict, total=False):
    project_id: str

    prompt_id: str

    prompt_version: str


class Parser(TypedDict, total=False):
    choice_scores: Required[Dict[str, float]]

    type: Required[Literal["llm_classifier"]]

    use_cot: Required[bool]


class PromptCompletion(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptChatMessageSystem(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


PromptChatMessageUserContentArray: TypeAlias = Union[ChatCompletionContentPartText, ChatCompletionContentPartImage]


class PromptChatMessageUser(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptChatMessageUserContentArray]]

    name: str


class PromptChatMessageAssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptChatMessageAssistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: Optional[PromptChatMessageAssistantFunctionCall]

    name: Optional[str]

    tool_calls: Optional[Iterable[ChatCompletionMessageToolCall]]


class PromptChatMessageTool(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class PromptChatMessageFunction(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class PromptChatMessageFallback(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


PromptChatMessage: TypeAlias = Union[
    PromptChatMessageSystem,
    PromptChatMessageUser,
    PromptChatMessageAssistant,
    PromptChatMessageTool,
    PromptChatMessageFunction,
    PromptChatMessageFallback,
]


class PromptChat(TypedDict, total=False):
    messages: Required[Iterable[PromptChatMessage]]

    type: Required[Literal["chat"]]

    tools: str


class PromptNullableVariant(TypedDict, total=False):
    pass


Prompt: TypeAlias = Union[PromptCompletion, PromptChat, Optional[PromptNullableVariant]]


class ToolFunctionFunction(TypedDict, total=False):
    id: Required[str]

    type: Required[Literal["function"]]


class ToolFunctionGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


ToolFunction: TypeAlias = Union[ToolFunctionFunction, ToolFunctionGlobal]


class PromptData(TypedDict, total=False):
    options: Optional[PromptOptions]

    origin: Optional[Origin]

    parser: Optional[Parser]

    prompt: Prompt

    tool_functions: Optional[Iterable[ToolFunction]]
