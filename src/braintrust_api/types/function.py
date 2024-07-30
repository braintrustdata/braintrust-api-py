# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Function",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataLocation",
    "FunctionDataCodeDataLocationPosition",
    "FunctionDataCodeDataLocationPositionScore",
    "FunctionDataCodeDataRuntimeContext",
    "FunctionDataGlobal",
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


class FunctionDataPrompt(BaseModel):
    type: Literal["prompt"]


class FunctionDataCodeDataLocationPositionScore(BaseModel):
    score: float


FunctionDataCodeDataLocationPosition = Union[Literal["task"], FunctionDataCodeDataLocationPositionScore]


class FunctionDataCodeDataLocation(BaseModel):
    eval_name: str

    position: FunctionDataCodeDataLocationPosition

    type: Literal["experiment"]


class FunctionDataCodeDataRuntimeContext(BaseModel):
    runtime: Literal["node"]

    version: str


class FunctionDataCodeData(BaseModel):
    bundle_id: str

    location: FunctionDataCodeDataLocation

    runtime_context: FunctionDataCodeDataRuntimeContext


class FunctionDataCode(BaseModel):
    data: FunctionDataCodeData

    type: Literal["code"]


class FunctionDataGlobal(BaseModel):
    name: str

    type: Literal["global"]


FunctionData = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal]


class PromptDataOptionsParamsOpenAIModelParamsFunctionCallName(BaseModel):
    name: str


PromptDataOptionsParamsOpenAIModelParamsFunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsFunctionCallName
]


class PromptDataOptionsParamsOpenAIModelParamsResponseFormat(BaseModel):
    type: Literal["json_object"]


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2Function(BaseModel):
    name: str


class PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2(BaseModel):
    function: PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2Function

    type: Literal["function"]


PromptDataOptionsParamsOpenAIModelParamsToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsOpenAIModelParamsToolChoiceUnionMember2
]


class PromptDataOptionsParamsOpenAIModelParams(BaseModel):
    frequency_penalty: Optional[float] = None

    function_call: Optional[PromptDataOptionsParamsOpenAIModelParamsFunctionCall] = None

    max_tokens: Optional[float] = None

    n: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[PromptDataOptionsParamsOpenAIModelParamsResponseFormat] = None

    stop: Optional[List[str]] = None

    temperature: Optional[float] = None

    tool_choice: Optional[PromptDataOptionsParamsOpenAIModelParamsToolChoice] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsAnthropicModelParams(BaseModel):
    max_tokens: float

    temperature: float

    max_tokens_to_sample: Optional[float] = None
    """This is a legacy parameter that should not be used."""

    stop_sequences: Optional[List[str]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsGoogleModelParams(BaseModel):
    max_output_tokens: Optional[float] = FieldInfo(alias="maxOutputTokens", default=None)

    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsWindowAIModelParams(BaseModel):
    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsJsCompletionParams(BaseModel):
    use_cache: Optional[bool] = None


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsOpenAIModelParams,
    PromptDataOptionsParamsAnthropicModelParams,
    PromptDataOptionsParamsGoogleModelParams,
    PromptDataOptionsParamsWindowAIModelParams,
    PromptDataOptionsParamsJsCompletionParams,
]


class PromptDataOptions(BaseModel):
    model: Optional[str] = None

    params: Optional[PromptDataOptionsParams] = None

    position: Optional[str] = None


class PromptDataOrigin(BaseModel):
    project_id: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_version: Optional[str] = None


class PromptDataPromptCompletion(BaseModel):
    content: str

    type: Literal["completion"]


class PromptDataPromptChatMessageSystem(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


class PromptDataPromptChatMessageUserContentArrayText(BaseModel):
    type: Literal["text"]

    text: Optional[str] = None


class PromptDataPromptChatMessageUserContentArrayImageURLImageURL(BaseModel):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class PromptDataPromptChatMessageUserContentArrayImageURL(BaseModel):
    image_url: PromptDataPromptChatMessageUserContentArrayImageURLImageURL

    type: Literal["image_url"]


PromptDataPromptChatMessageUserContentArray = Union[
    PromptDataPromptChatMessageUserContentArrayText, PromptDataPromptChatMessageUserContentArrayImageURL
]


class PromptDataPromptChatMessageUser(BaseModel):
    role: Literal["user"]

    content: Union[str, List[PromptDataPromptChatMessageUserContentArray], None] = None

    name: Optional[str] = None


class PromptDataPromptChatMessageAssistantFunctionCall(BaseModel):
    arguments: str

    name: str


class PromptDataPromptChatMessageAssistantToolCallFunction(BaseModel):
    arguments: str

    name: str


class PromptDataPromptChatMessageAssistantToolCall(BaseModel):
    id: str

    function: PromptDataPromptChatMessageAssistantToolCallFunction

    type: Literal["function"]


class PromptDataPromptChatMessageAssistant(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[PromptDataPromptChatMessageAssistantFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[PromptDataPromptChatMessageAssistantToolCall]] = None


class PromptDataPromptChatMessageTool(BaseModel):
    role: Literal["tool"]

    content: Optional[str] = None

    tool_call_id: Optional[str] = None


class PromptDataPromptChatMessageFunction(BaseModel):
    name: str

    role: Literal["function"]

    content: Optional[str] = None


class PromptDataPromptChatMessageFallback(BaseModel):
    role: Literal["model"]

    content: Optional[str] = None


PromptDataPromptChatMessage = Union[
    PromptDataPromptChatMessageSystem,
    PromptDataPromptChatMessageUser,
    PromptDataPromptChatMessageAssistant,
    PromptDataPromptChatMessageTool,
    PromptDataPromptChatMessageFunction,
    PromptDataPromptChatMessageFallback,
]


class PromptDataPromptChat(BaseModel):
    messages: List[PromptDataPromptChatMessage]

    type: Literal["chat"]

    tools: Optional[str] = None


class PromptDataPromptNullableVariant(BaseModel):
    pass


PromptDataPrompt = Union[PromptDataPromptCompletion, PromptDataPromptChat, Optional[PromptDataPromptNullableVariant]]


class PromptData(BaseModel):
    options: Optional[PromptDataOptions] = None

    origin: Optional[PromptDataOrigin] = None

    prompt: Optional[PromptDataPrompt] = None


class Function(BaseModel):
    id: str
    """Unique identifier for the prompt"""

    api_xact_id: str = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the prompt (see the `version`
    parameter)
    """

    function_data: FunctionData

    log_id: Literal["p"]
    """A literal 'p' which identifies the object as a project prompt"""

    name: str
    """Name of the prompt"""

    org_id: str
    """Unique identifier for the organization"""

    project_id: str
    """Unique identifier for the project that the prompt belongs under"""

    slug: str
    """Unique identifier for the prompt"""

    created: Optional[datetime] = None
    """Date of prompt creation"""

    description: Optional[str] = None
    """Textual description of the prompt"""

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the prompt"""

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
