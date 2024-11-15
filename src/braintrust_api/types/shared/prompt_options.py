# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

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


class ParamsOpenAIModelParamsFunctionCallFunction(BaseModel):
    name: str


ParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], ParamsOpenAIModelParamsFunctionCallFunction
]


class ParamsOpenAIModelParamsResponseFormatJsonObject(BaseModel):
    type: Literal["json_object"]


class ParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema(BaseModel):
    name: str

    description: Optional[str] = None

    schema_: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="schema", default=None)

    strict: Optional[bool] = None


class ParamsOpenAIModelParamsResponseFormatJsonSchema(BaseModel):
    json_schema: ParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema

    type: Literal["json_schema"]


class ParamsOpenAIModelParamsResponseFormatText(BaseModel):
    type: Literal["text"]


class ParamsOpenAIModelParamsResponseFormatNullableVariant(BaseModel):
    pass


ParamsOpenAIModelParamsResponseFormat: TypeAlias = Union[
    ParamsOpenAIModelParamsResponseFormatJsonObject,
    ParamsOpenAIModelParamsResponseFormatJsonSchema,
    ParamsOpenAIModelParamsResponseFormatText,
    Optional[ParamsOpenAIModelParamsResponseFormatNullableVariant],
]


class ParamsOpenAIModelParamsToolChoiceFunctionFunction(BaseModel):
    name: str


class ParamsOpenAIModelParamsToolChoiceFunction(BaseModel):
    function: ParamsOpenAIModelParamsToolChoiceFunctionFunction

    type: Literal["function"]


ParamsOpenAIModelParamsToolChoice: TypeAlias = Union[
    Literal["auto"], Literal["none"], Literal["required"], ParamsOpenAIModelParamsToolChoiceFunction
]


class ParamsOpenAIModelParams(BaseModel):
    frequency_penalty: Optional[float] = None

    function_call: Optional[ParamsOpenAIModelParamsFunctionCall] = None

    max_tokens: Optional[float] = None

    n: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[ParamsOpenAIModelParamsResponseFormat] = None

    stop: Optional[List[str]] = None

    temperature: Optional[float] = None

    tool_choice: Optional[ParamsOpenAIModelParamsToolChoice] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class ParamsAnthropicModelParams(BaseModel):
    max_tokens: float

    temperature: float

    max_tokens_to_sample: Optional[float] = None
    """This is a legacy parameter that should not be used."""

    stop_sequences: Optional[List[str]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class ParamsGoogleModelParams(BaseModel):
    max_output_tokens: Optional[float] = FieldInfo(alias="maxOutputTokens", default=None)

    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    use_cache: Optional[bool] = None


class ParamsWindowAIModelParams(BaseModel):
    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    use_cache: Optional[bool] = None


class ParamsJsCompletionParams(BaseModel):
    use_cache: Optional[bool] = None


Params: TypeAlias = Union[
    ParamsOpenAIModelParams,
    ParamsAnthropicModelParams,
    ParamsGoogleModelParams,
    ParamsWindowAIModelParams,
    ParamsJsCompletionParams,
]


class PromptOptions(BaseModel):
    model: Optional[str] = None

    params: Optional[Params] = None

    position: Optional[str] = None
