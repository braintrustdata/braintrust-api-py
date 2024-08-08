# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PromptData",
    "Options",
    "OptionsParams",
    "OptionsParamsOpenAIModelParams",
    "OptionsParamsOpenAIModelParamsFunctionCall",
    "OptionsParamsOpenAIModelParamsFunctionCallFunction",
    "OptionsParamsOpenAIModelParamsResponseFormat",
    "OptionsParamsOpenAIModelParamsToolChoice",
    "OptionsParamsOpenAIModelParamsToolChoiceFunction",
    "OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction",
    "OptionsParamsAnthropicModelParams",
    "OptionsParamsGoogleModelParams",
    "OptionsParamsWindowAIModelParams",
    "OptionsParamsJsCompletionParams",
    "Origin",
    "Prompt",
    "PromptCompletion",
    "PromptChat",
    "PromptChatMessage",
    "PromptChatMessageSystem",
    "PromptChatMessageUser",
    "PromptChatMessageUserContentArray",
    "PromptChatMessageUserContentArrayText",
    "PromptChatMessageUserContentArrayImageURL",
    "PromptChatMessageUserContentArrayImageURLImageURL",
    "PromptChatMessageAssistant",
    "PromptChatMessageAssistantFunctionCall",
    "PromptChatMessageAssistantToolCall",
    "PromptChatMessageAssistantToolCallFunction",
    "PromptChatMessageTool",
    "PromptChatMessageFunction",
    "PromptChatMessageFallback",
    "PromptNullableVariant",
]


class OptionsParamsOpenAIModelParamsFunctionCallFunction(TypedDict, total=False):
    name: Required[str]


OptionsParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], OptionsParamsOpenAIModelParamsFunctionCallFunction
]


class OptionsParamsOpenAIModelParamsResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction(TypedDict, total=False):
    name: Required[str]


class OptionsParamsOpenAIModelParamsToolChoiceFunction(TypedDict, total=False):
    function: Required[OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction]

    type: Required[Literal["function"]]


OptionsParamsOpenAIModelParamsToolChoice: TypeAlias = Union[
    Literal["auto"], Literal["none"], OptionsParamsOpenAIModelParamsToolChoiceFunction
]


class OptionsParamsOpenAIModelParams(TypedDict, total=False):
    frequency_penalty: float

    function_call: OptionsParamsOpenAIModelParamsFunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: Optional[OptionsParamsOpenAIModelParamsResponseFormat]

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


class PromptCompletion(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptChatMessageSystem(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptChatMessageUserContentArrayText(TypedDict, total=False):
    type: Required[Literal["text"]]

    text: str


class PromptChatMessageUserContentArrayImageURLImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptChatMessageUserContentArrayImageURL(TypedDict, total=False):
    image_url: Required[PromptChatMessageUserContentArrayImageURLImageURL]

    type: Required[Literal["image_url"]]


PromptChatMessageUserContentArray: TypeAlias = Union[
    PromptChatMessageUserContentArrayText, PromptChatMessageUserContentArrayImageURL
]


class PromptChatMessageUser(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptChatMessageUserContentArray]]

    name: str


class PromptChatMessageAssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptChatMessageAssistantToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptChatMessageAssistantToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptChatMessageAssistantToolCallFunction]

    type: Required[Literal["function"]]


class PromptChatMessageAssistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptChatMessageAssistantFunctionCall

    name: str

    tool_calls: Iterable[PromptChatMessageAssistantToolCall]


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


class PromptData(TypedDict, total=False):
    options: Optional[Options]

    origin: Optional[Origin]

    prompt: Prompt
