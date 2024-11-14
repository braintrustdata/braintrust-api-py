# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
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


class OptionsParamsOpenAIModelParamsFunctionCallFunction(BaseModel):
    name: str


OptionsParamsOpenAIModelParamsFunctionCall: TypeAlias = Union[
    Literal["auto"], Literal["none"], OptionsParamsOpenAIModelParamsFunctionCallFunction
]


class OptionsParamsOpenAIModelParamsResponseFormatJsonObject(BaseModel):
    type: Literal["json_object"]


class OptionsParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema(BaseModel):
    name: str

    description: Optional[str] = None

    schema_: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="schema", default=None)

    strict: Optional[bool] = None


class OptionsParamsOpenAIModelParamsResponseFormatJsonSchema(BaseModel):
    json_schema: OptionsParamsOpenAIModelParamsResponseFormatJsonSchemaJsonSchema

    type: Literal["json_schema"]


class OptionsParamsOpenAIModelParamsResponseFormatText(BaseModel):
    type: Literal["text"]


class OptionsParamsOpenAIModelParamsResponseFormatNullableVariant(BaseModel):
    pass


OptionsParamsOpenAIModelParamsResponseFormat: TypeAlias = Union[
    OptionsParamsOpenAIModelParamsResponseFormatJsonObject,
    OptionsParamsOpenAIModelParamsResponseFormatJsonSchema,
    OptionsParamsOpenAIModelParamsResponseFormatText,
    Optional[OptionsParamsOpenAIModelParamsResponseFormatNullableVariant],
]


class OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction(BaseModel):
    name: str


class OptionsParamsOpenAIModelParamsToolChoiceFunction(BaseModel):
    function: OptionsParamsOpenAIModelParamsToolChoiceFunctionFunction

    type: Literal["function"]


OptionsParamsOpenAIModelParamsToolChoice: TypeAlias = Union[
    Literal["auto"], Literal["none"], Literal["required"], OptionsParamsOpenAIModelParamsToolChoiceFunction
]


class OptionsParamsOpenAIModelParams(BaseModel):
    frequency_penalty: Optional[float] = None

    function_call: Optional[OptionsParamsOpenAIModelParamsFunctionCall] = None

    max_tokens: Optional[float] = None

    n: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[OptionsParamsOpenAIModelParamsResponseFormat] = None

    stop: Optional[List[str]] = None

    temperature: Optional[float] = None

    tool_choice: Optional[OptionsParamsOpenAIModelParamsToolChoice] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class OptionsParamsAnthropicModelParams(BaseModel):
    max_tokens: float

    temperature: float

    max_tokens_to_sample: Optional[float] = None
    """This is a legacy parameter that should not be used."""

    stop_sequences: Optional[List[str]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class OptionsParamsGoogleModelParams(BaseModel):
    max_output_tokens: Optional[float] = FieldInfo(alias="maxOutputTokens", default=None)

    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    use_cache: Optional[bool] = None


class OptionsParamsWindowAIModelParams(BaseModel):
    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    use_cache: Optional[bool] = None


class OptionsParamsJsCompletionParams(BaseModel):
    use_cache: Optional[bool] = None


OptionsParams: TypeAlias = Union[
    OptionsParamsOpenAIModelParams,
    OptionsParamsAnthropicModelParams,
    OptionsParamsGoogleModelParams,
    OptionsParamsWindowAIModelParams,
    OptionsParamsJsCompletionParams,
]


class Options(BaseModel):
    model: Optional[str] = None

    params: Optional[OptionsParams] = None

    position: Optional[str] = None


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
    options: Optional[Options] = None

    origin: Optional[Origin] = None

    parser: Optional[Parser] = None

    prompt: Optional[Prompt] = None

    tool_functions: Optional[List[ToolFunction]] = None
