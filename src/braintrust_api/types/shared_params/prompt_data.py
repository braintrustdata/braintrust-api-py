# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .chat_completion_content_part_text import ChatCompletionContentPartText
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall
from .chat_completion_content_part_image import ChatCompletionContentPartImage

__all__ = [
    "PromptData",
    "Options",
    "OptionsParams",
    "OptionsParamsOpenAIModelParams",
    "OptionsParamsOpenAIModelParamsFunctionCall",
    "OptionsParamsOpenAIModelParamsFunctionCallFunction",
    "OptionsParamsOpenAIModelParamsResponseFormat",
    "OptionsParamsOpenAIModelParamsResponseFormatJsonObject",
    "OptionsParamsOpenAIModelParamsResponseFormatJsonSchema",
    "OptionsParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema",
    "OptionsParamsOpenAIModelParamsResponseFormatText",
    "OptionsParamsOpenAIModelParamsResponseFormatNullableVariant",
    "OptionsParamsOpenAIModelParamsToolChoice",
    "OptionsParamsOpenAIModelParamsToolChoiceFunction",
    "OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction",
    "OptionsParamsAnthropicModelParams",
    "OptionsParamsGoogleModelParams",
    "OptionsParamsWindowAIModelParams",
    "OptionsParamsJsCompletionParams",
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


class OptionsParamsOpenAIModelParamsFunctionCallFunction(TypedDict, total=False):
    name: Required[str]


OptionsParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], OptionsParamsOpenAIModelParamsFunctionCallFunction
]


class OptionsParamsOpenAIModelParamsResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class OptionsParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]

    description: str

    schema: Dict[str, Optional[object]]

    strict: Optional[bool]


class OptionsParamsOpenAIModelParamsResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[OptionsParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema]

    type: Required[Literal["json_schema"]]


class OptionsParamsOpenAIModelParamsResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class OptionsParamsOpenAIModelParamsResponseFormatNullableVariant(TypedDict, total=False):
    pass


OptionsParamsOpenAIModelParamsResponseFormat: TypeAlias = Union[
    OptionsParamsOpenAIModelParamsResponseFormatJsonObject,
    OptionsParamsOpenAIModelParamsResponseFormatJsonSchema,
    OptionsParamsOpenAIModelParamsResponseFormatText,
    Optional[OptionsParamsOpenAIModelParamsResponseFormatNullableVariant],
]


class OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction(TypedDict, total=False):
    name: Required[str]


class OptionsParamsOpenAIModelParamsToolChoiceFunction(TypedDict, total=False):
    function: Required[OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction]

    type: Required[Literal["function"]]


OptionsParamsOpenAIModelParamsToolChoice: TypeAlias = Union[
    Literal["auto"], Literal["none"], Literal["required"], OptionsParamsOpenAIModelParamsToolChoiceFunction
]


class OptionsParamsOpenAIModelParams(TypedDict, total=False):
    frequency_penalty: float

    function_call: OptionsParamsOpenAIModelParamsFunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: OptionsParamsOpenAIModelParamsResponseFormat

    stop: List[str]

    temperature: float

    tool_choice: OptionsParamsOpenAIModelParamsToolChoice

    top_p: float

    use_cache: bool


class OptionsParamsAnthropicModelParams(TypedDict, total=False):
    max_tokens: Required[float]

    temperature: Required[float]

    max_tokens_to_sample: float
    """This is a legacy parameter that should not be used."""

    stop_sequences: List[str]

    top_k: float

    top_p: float

    use_cache: bool


class OptionsParamsGoogleModelParams(TypedDict, total=False):
    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class OptionsParamsWindowAIModelParams(TypedDict, total=False):
    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    use_cache: bool


class OptionsParamsJsCompletionParams(TypedDict, total=False):
    use_cache: bool


OptionsParams: TypeAlias = Union[
    OptionsParamsOpenAIModelParams,
    OptionsParamsAnthropicModelParams,
    OptionsParamsGoogleModelParams,
    OptionsParamsWindowAIModelParams,
    OptionsParamsJsCompletionParams,
]


class Options(TypedDict, total=False):
    model: str

    params: OptionsParams

    position: str


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
    options: Optional[Options]

    origin: Optional[Origin]

    parser: Optional[Parser]

    prompt: Prompt

    tool_functions: Optional[Iterable[ToolFunction]]
