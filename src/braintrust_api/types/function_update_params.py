# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FunctionUpdateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataLocation",
    "FunctionDataCodeDataLocationPosition",
    "FunctionDataCodeDataLocationPositionScore",
    "FunctionDataCodeDataRuntimeContext",
    "FunctionDataGlobal",
    "FunctionDataNullableVariant",
    "PromptData",
    "PromptDataOptions",
    "PromptDataOptionsParams",
    "PromptDataOptionsParamsOpenAIModelParams",
    "PromptDataOptionsParamsOpenAIModelParamsFunctionCall",
    "PromptDataOptionsParamsOpenAIModelParamsFunctionCallName",
    "PromptDataOptionsParamsOpenAIModelParamsResponseFormat",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoice",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2",
    "PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2Function",
    "PromptDataOptionsParamsAnthropicModelParams",
    "PromptDataOptionsParamsGoogleModelParams",
    "PromptDataOptionsParamsWindowAIModelParams",
    "PromptDataOptionsParamsJsCompletionParams",
    "PromptDataOrigin",
    "PromptDataPrompt",
    "PromptDataPromptCompletion",
    "PromptDataPromptChat",
    "PromptDataPromptChatMessage",
    "PromptDataPromptChatMessagePromptDataPromptMessage0",
    "PromptDataPromptChatMessagePromptDataPromptMessage1",
    "PromptDataPromptChatMessagePromptDataPromptMessage1ContentArray",
    "PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent",
    "PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList",
    "PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL",
    "PromptDataPromptChatMessagePromptDataPromptMessage2",
    "PromptDataPromptChatMessagePromptDataPromptMessage2FunctionCall",
    "PromptDataPromptChatMessagePromptDataPromptMessage2ToolCall",
    "PromptDataPromptChatMessagePromptDataPromptMessage2ToolCallFunction",
    "PromptDataPromptChatMessagePromptDataPromptMessage3",
    "PromptDataPromptChatMessagePromptDataPromptMessage4",
    "PromptDataPromptChatMessagePromptDataPromptMessage5",
    "PromptDataPromptNullableVariant",
]


class FunctionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    function_data: FunctionData

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


class FunctionDataPrompt(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataCodeDataLocationPositionScore(TypedDict, total=False):
    score: Required[float]


FunctionDataCodeDataLocationPosition = Union[Literal["task"], FunctionDataCodeDataLocationPositionScore]


class FunctionDataCodeDataLocation(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataCodeDataLocationPosition]

    type: Required[Literal["experiment"]]


class FunctionDataCodeDataRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node"]]

    version: Required[str]


class FunctionDataCodeData(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[FunctionDataCodeDataLocation]

    runtime_context: Required[FunctionDataCodeDataRuntimeContext]


class FunctionDataCode(TypedDict, total=False):
    data: Required[FunctionDataCodeData]

    type: Required[Literal["code"]]


class FunctionDataGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


class FunctionDataNullableVariant(TypedDict, total=False):
    pass


FunctionData = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal, Optional[FunctionDataNullableVariant]]


class PromptDataOptionsParamsOpenAIModelParamsFunctionCallName(TypedDict, total=False):
    name: Required[str]


PromptDataOptionsParamsOpenAIModelParamsFunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsFunctionCallName
]


class PromptDataOptionsParamsOpenAIModelParamsResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2Function(TypedDict, total=False):
    name: Required[str]


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2(TypedDict, total=False):
    function: Required[PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2Function]

    type: Required[Literal["function"]]


PromptDataOptionsParamsOpenAIModelParamsToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2
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


class PromptDataPromptChatMessagePromptDataPromptMessage0(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent(
    TypedDict, total=False
):
    type: Required[Literal["text"]]

    text: str


class PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList(
    TypedDict, total=False
):
    image_url: Required[
        PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL
    ]

    type: Required[Literal["image_url"]]


PromptDataPromptChatMessagePromptDataPromptMessage1ContentArray = Union[
    PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent,
    PromptDataPromptChatMessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList,
]


class PromptDataPromptChatMessagePromptDataPromptMessage1(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptDataPromptChatMessagePromptDataPromptMessage1ContentArray]]

    name: str


class PromptDataPromptChatMessagePromptDataPromptMessage2FunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessagePromptDataPromptMessage2ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessagePromptDataPromptMessage2ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptDataPromptChatMessagePromptDataPromptMessage2ToolCallFunction]

    type: Required[Literal["function"]]


class PromptDataPromptChatMessagePromptDataPromptMessage2(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptDataPromptChatMessagePromptDataPromptMessage2FunctionCall

    name: str

    tool_calls: Iterable[PromptDataPromptChatMessagePromptDataPromptMessage2ToolCall]


class PromptDataPromptChatMessagePromptDataPromptMessage3(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class PromptDataPromptChatMessagePromptDataPromptMessage4(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class PromptDataPromptChatMessagePromptDataPromptMessage5(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


PromptDataPromptChatMessage = Union[
    PromptDataPromptChatMessagePromptDataPromptMessage0,
    PromptDataPromptChatMessagePromptDataPromptMessage1,
    PromptDataPromptChatMessagePromptDataPromptMessage2,
    PromptDataPromptChatMessagePromptDataPromptMessage3,
    PromptDataPromptChatMessagePromptDataPromptMessage4,
    PromptDataPromptChatMessagePromptDataPromptMessage5,
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
