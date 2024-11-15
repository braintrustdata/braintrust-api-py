# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
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


class Origin(BaseModel):
    project_id: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_version: Optional[str] = None


class Parser(BaseModel):
    choice_scores: Dict[str, float]

    type: Literal["llm_classifier"]

    use_cot: bool


class PromptCompletion(BaseModel):
    content: str

    type: Literal["completion"]


class PromptChatMessageSystem(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


PromptChatMessageUserContentArray: TypeAlias = Union[ChatCompletionContentPartText, ChatCompletionContentPartImage]


class PromptChatMessageUser(BaseModel):
    role: Literal["user"]

    content: Union[str, List[PromptChatMessageUserContentArray], None] = None

    name: Optional[str] = None


class PromptChatMessageAssistantFunctionCall(BaseModel):
    arguments: str

    name: str


class PromptChatMessageAssistant(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[PromptChatMessageAssistantFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = None


class PromptChatMessageTool(BaseModel):
    role: Literal["tool"]

    content: Optional[str] = None

    tool_call_id: Optional[str] = None


class PromptChatMessageFunction(BaseModel):
    name: str

    role: Literal["function"]

    content: Optional[str] = None


class PromptChatMessageFallback(BaseModel):
    role: Literal["model"]

    content: Optional[str] = None


PromptChatMessage: TypeAlias = Union[
    PromptChatMessageSystem,
    PromptChatMessageUser,
    PromptChatMessageAssistant,
    PromptChatMessageTool,
    PromptChatMessageFunction,
    PromptChatMessageFallback,
]


class PromptChat(BaseModel):
    messages: List[PromptChatMessage]

    type: Literal["chat"]

    tools: Optional[str] = None


class PromptNullableVariant(BaseModel):
    pass


Prompt: TypeAlias = Union[PromptCompletion, PromptChat, Optional[PromptNullableVariant]]


class ToolFunctionFunction(BaseModel):
    id: str

    type: Literal["function"]


class ToolFunctionGlobal(BaseModel):
    name: str

    type: Literal["global"]


ToolFunction: TypeAlias = Union[ToolFunctionFunction, ToolFunctionGlobal]


class PromptData(BaseModel):
    options: Optional[PromptOptions] = None

    origin: Optional[Origin] = None

    parser: Optional[Parser] = None

    prompt: Optional[Prompt] = None

    tool_functions: Optional[List[ToolFunction]] = None
