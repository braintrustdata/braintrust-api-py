# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .prompt_options import PromptOptions
from .chat_completion_message import ChatCompletionMessage

__all__ = [
    "PromptData",
    "Origin",
    "Parser",
    "Prompt",
    "PromptCompletion",
    "PromptChat",
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


class PromptChat(TypedDict, total=False):
    messages: Required[Iterable[ChatCompletionMessage]]

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
