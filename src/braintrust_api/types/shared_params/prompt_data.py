# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .messages import Messages
from .tool_choice_function import ToolChoiceFunction

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
    "OptionsParamsAnthropicModelParams",
    "OptionsParamsGoogleModelParams",
    "OptionsParamsWindowAIModelParams",
    "OptionsParamsJsCompletionParams",
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


class OptionsParamsOpenAIModelParamsFunctionCallFunction(TypedDict, total=False):
    name: Required[str]


OptionsParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], OptionsParamsOpenAIModelParamsFunctionCallFunction
]


class OptionsParamsOpenAIModelParamsResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class OptionsParamsOpenAIModelParamsToolChoiceFunction(TypedDict, total=False):
    function: Required[ToolChoiceFunction]

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


class Parser(TypedDict, total=False):
    choice_scores: Required[Dict[str, float]]

    type: Required[Literal["llm_classifier"]]

    use_cot: Required[bool]


class PromptCompletion(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptChat(TypedDict, total=False):
    messages: Required[Iterable[Messages]]

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
