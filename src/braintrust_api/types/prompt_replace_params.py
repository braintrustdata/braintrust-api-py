# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PromptReplaceParams",
    "PromptData",
    "PromptDataOptions",
    "PromptDataOptionsParams",
    "PromptDataOptionsParamsOpenAIModelParams",
    "PromptDataOptionsParamsOpenAIModelParamsFunctionCall",
    "PromptDataOptionsParamsOpenAIModelParamsFunctionCallFunction",
    "PromptDataOptionsParamsOpenAIModelParamsResponseFormat",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoice",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunction",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunctionFunction",
    "PromptDataOptionsParamsAnthropicModelParams",
    "PromptDataOptionsParamsGoogleModelParams",
    "PromptDataOptionsParamsWindowAIModelParams",
    "PromptDataOptionsParamsJsCompletionParams",
    "PromptDataOrigin",
    "PromptDataPrompt",
    "PromptDataPromptCompletion",
    "PromptDataPromptChat",
    "PromptDataPromptChatMessage",
    "PromptDataPromptChatMessageSystem",
    "PromptDataPromptChatMessageUser",
    "PromptDataPromptChatMessageUserContentArray",
    "PromptDataPromptChatMessageUserContentArrayText",
    "PromptDataPromptChatMessageUserContentArrayImageURL",
    "PromptDataPromptChatMessageUserContentArrayImageURLImageURL",
    "PromptDataPromptChatMessageAssistant",
    "PromptDataPromptChatMessageAssistantFunctionCall",
    "PromptDataPromptChatMessageAssistantToolCall",
    "PromptDataPromptChatMessageAssistantToolCallFunction",
    "PromptDataPromptChatMessageTool",
    "PromptDataPromptChatMessageFunction",
    "PromptDataPromptChatMessageFallback",
    "PromptDataPromptNullableVariant",
]


class PromptReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the prompt"""

    project_id: Required[str]
    """Unique identifier for the project that the prompt belongs under"""

    slug: Required[str]
    """Unique identifier for the prompt"""

    description: Optional[str]
    """Textual description of the prompt"""

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


class PromptDataOptionsParamsOpenAIModelParamsFunctionCallFunction(TypedDict, total=False):
    name: Required[str]


PromptDataOptionsParamsOpenAIModelParamsFunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsFunctionCallFunction
]


class PromptDataOptionsParamsOpenAIModelParamsResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunctionFunction(TypedDict, total=False):
    name: Required[str]


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunction(TypedDict, total=False):
    function: Required[PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunctionFunction]

    type: Required[Literal["function"]]


PromptDataOptionsParamsOpenAIModelParamsToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsToolChoiceFunction
]


class PromptDataOptionsParamsOpenAIModelParams(TypedDict, total=False):
    frequency_penalty: float

    function_call: PromptDataOptionsParamsOpenAIModelParamsFunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: Optional[PromptDataOptionsParamsOpenAIModelParamsResponseFormat]

    stop: List[str]

    temperature: float

    tool_choice: PromptDataOptionsParamsOpenAIModelParamsToolChoice

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsAnthropicModelParams(TypedDict, total=False):
    max_tokens: Required[float]

    temperature: Required[float]

    max_tokens_to_sample: float
    """This is a legacy parameter that should not be used."""

    stop_sequences: List[str]

    top_k: float

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsGoogleModelParams(TypedDict, total=False):
    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class PromptDataOptionsParamsWindowAIModelParams(TypedDict, total=False):
    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    use_cache: bool


class PromptDataOptionsParamsJsCompletionParams(TypedDict, total=False):
    use_cache: bool


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsOpenAIModelParams,
    PromptDataOptionsParamsAnthropicModelParams,
    PromptDataOptionsParamsGoogleModelParams,
    PromptDataOptionsParamsWindowAIModelParams,
    PromptDataOptionsParamsJsCompletionParams,
]


class PromptDataOptions(TypedDict, total=False):
    model: str

    params: PromptDataOptionsParams

    position: str


class PromptDataOrigin(TypedDict, total=False):
    project_id: str

    prompt_id: str

    prompt_version: str


class PromptDataPromptCompletion(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptDataPromptChatMessageSystem(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptDataPromptChatMessageUserContentArrayText(TypedDict, total=False):
    type: Required[Literal["text"]]

    text: str


class PromptDataPromptChatMessageUserContentArrayImageURLImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptDataPromptChatMessageUserContentArrayImageURL(TypedDict, total=False):
    image_url: Required[PromptDataPromptChatMessageUserContentArrayImageURLImageURL]

    type: Required[Literal["image_url"]]


PromptDataPromptChatMessageUserContentArray = Union[
    PromptDataPromptChatMessageUserContentArrayText, PromptDataPromptChatMessageUserContentArrayImageURL
]


class PromptDataPromptChatMessageUser(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptDataPromptChatMessageUserContentArray]]

    name: str


class PromptDataPromptChatMessageAssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessageAssistantToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessageAssistantToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptDataPromptChatMessageAssistantToolCallFunction]

    type: Required[Literal["function"]]


class PromptDataPromptChatMessageAssistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptDataPromptChatMessageAssistantFunctionCall

    name: str

    tool_calls: Iterable[PromptDataPromptChatMessageAssistantToolCall]


class PromptDataPromptChatMessageTool(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class PromptDataPromptChatMessageFunction(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class PromptDataPromptChatMessageFallback(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


PromptDataPromptChatMessage = Union[
    PromptDataPromptChatMessageSystem,
    PromptDataPromptChatMessageUser,
    PromptDataPromptChatMessageAssistant,
    PromptDataPromptChatMessageTool,
    PromptDataPromptChatMessageFunction,
    PromptDataPromptChatMessageFallback,
]


class PromptDataPromptChat(TypedDict, total=False):
    messages: Required[Iterable[PromptDataPromptChatMessage]]

    type: Required[Literal["chat"]]

    tools: str


class PromptDataPromptNullableVariant(TypedDict, total=False):
    pass


PromptDataPrompt = Union[PromptDataPromptCompletion, PromptDataPromptChat, Optional[PromptDataPromptNullableVariant]]


class PromptData(TypedDict, total=False):
    options: Optional[PromptDataOptions]

    origin: Optional[PromptDataOrigin]

    prompt: PromptDataPrompt
