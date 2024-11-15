# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PromptOptions",
    "Params",
    "ParamsOpenAIModelParams",
    "ParamsOpenAIModelParamsFunctionCall",
    "ParamsOpenAIModelParamsFunctionCallFunction",
    "ParamsOpenAIModelParamsResponseFormat",
    "ParamsOpenAIModelParamsResponseFormatJsonObject",
    "ParamsOpenAIModelParamsResponseFormatJsonSchema",
    "ParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema",
    "ParamsOpenAIModelParamsResponseFormatText",
    "ParamsOpenAIModelParamsResponseFormatNullableVariant",
    "ParamsOpenAIModelParamsToolChoice",
    "ParamsOpenAIModelParamsToolChoiceFunction",
    "ParamsOpenAIModelParamsToolChoiceFunctionFunction",
    "ParamsAnthropicModelParams",
    "ParamsGoogleModelParams",
    "ParamsWindowAIModelParams",
    "ParamsJsCompletionParams",
]


class ParamsOpenAIModelParamsFunctionCallFunction(TypedDict, total=False):
    name: Required[str]


ParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], ParamsOpenAIModelParamsFunctionCallFunction
]


class ParamsOpenAIModelParamsResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class ParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]

    description: str

    schema: Dict[str, Optional[object]]

    strict: Optional[bool]


class ParamsOpenAIModelParamsResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema]

    type: Required[Literal["json_schema"]]


class ParamsOpenAIModelParamsResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class ParamsOpenAIModelParamsResponseFormatNullableVariant(TypedDict, total=False):
    pass


ParamsOpenAIModelParamsResponseFormat: TypeAlias = Union[
    ParamsOpenAIModelParamsResponseFormatJsonObject,
    ParamsOpenAIModelParamsResponseFormatJsonSchema,
    ParamsOpenAIModelParamsResponseFormatText,
    Optional[ParamsOpenAIModelParamsResponseFormatNullableVariant],
]


class ParamsOpenAIModelParamsToolChoiceFunctionFunction(TypedDict, total=False):
    name: Required[str]


class ParamsOpenAIModelParamsToolChoiceFunction(TypedDict, total=False):
    function: Required[ParamsOpenAIModelParamsToolChoiceFunctionFunction]

    type: Required[Literal["function"]]


ParamsOpenAIModelParamsToolChoice: TypeAlias = Union[
    Literal["auto"], Literal["none"], Literal["required"], ParamsOpenAIModelParamsToolChoiceFunction
]


class ParamsOpenAIModelParams(TypedDict, total=False):
    frequency_penalty: float

    function_call: ParamsOpenAIModelParamsFunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: ParamsOpenAIModelParamsResponseFormat

    stop: List[str]

    temperature: float

    tool_choice: ParamsOpenAIModelParamsToolChoice

    top_p: float

    use_cache: bool


class ParamsAnthropicModelParams(TypedDict, total=False):
    max_tokens: Required[float]

    temperature: Required[float]

    max_tokens_to_sample: float
    """This is a legacy parameter that should not be used."""

    stop_sequences: List[str]

    top_k: float

    top_p: float

    use_cache: bool


class ParamsGoogleModelParams(TypedDict, total=False):
    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class ParamsWindowAIModelParams(TypedDict, total=False):
    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    use_cache: bool


class ParamsJsCompletionParams(TypedDict, total=False):
    use_cache: bool


Params: TypeAlias = Union[
    ParamsOpenAIModelParams,
    ParamsAnthropicModelParams,
    ParamsGoogleModelParams,
    ParamsWindowAIModelParams,
    ParamsJsCompletionParams,
]


class PromptOptions(TypedDict, total=False):
    model: str

    params: Params

    position: str
