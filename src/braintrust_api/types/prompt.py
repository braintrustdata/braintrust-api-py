# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Prompt",
    "PromptData",
    "PromptDataOptions",
    "PromptDataOptionsParams",
    "PromptDataOptionsParamsPromptDataOptions0",
    "PromptDataOptionsParamsPromptDataOptions0FunctionCall",
    "PromptDataOptionsParamsPromptDataOptions0FunctionCallName",
    "PromptDataOptionsParamsPromptDataOptions0ResponseFormat",
    "PromptDataOptionsParamsPromptDataOptions0ToolChoice",
    "PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2",
    "PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2Function",
    "PromptDataOptionsParamsPromptDataOptions1",
    "PromptDataOptionsParamsPromptDataOptions2",
    "PromptDataOptionsParamsPromptDataOptions3",
    "PromptDataOptionsParamsJsCompletionParams",
    "PromptDataOrigin",
    "PromptDataPrompt",
    "PromptDataPromptPromptDataPrompt0",
    "PromptDataPromptPromptDataPrompt1",
    "PromptDataPromptPromptDataPrompt1Message",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage0",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArray",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2FunctionCall",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCall",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCallFunction",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage3",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage4",
    "PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage5",
    "PromptDataPromptPromptDataPrompt2",
]


class PromptDataOptionsParamsPromptDataOptions0FunctionCallName(BaseModel):
    name: str


PromptDataOptionsParamsPromptDataOptions0FunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsPromptDataOptions0FunctionCallName
]


class PromptDataOptionsParamsPromptDataOptions0ResponseFormat(BaseModel):
    type: Literal["json_object"]


class PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2Function(BaseModel):
    name: str


class PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2(BaseModel):
    function: PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2Function

    type: Literal["function"]


PromptDataOptionsParamsPromptDataOptions0ToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2
]


class PromptDataOptionsParamsPromptDataOptions0(BaseModel):
    frequency_penalty: Optional[float] = None

    function_call: Optional[PromptDataOptionsParamsPromptDataOptions0FunctionCall] = None

    max_tokens: Optional[float] = None

    n: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[PromptDataOptionsParamsPromptDataOptions0ResponseFormat] = None

    stop: Optional[List[str]] = None

    temperature: Optional[float] = None

    tool_choice: Optional[PromptDataOptionsParamsPromptDataOptions0ToolChoice] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsPromptDataOptions1(BaseModel):
    max_tokens: float

    temperature: float

    max_tokens_to_sample: Optional[float] = None
    """This is a legacy parameter that should not be used."""

    stop_sequences: Optional[List[str]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsPromptDataOptions2(BaseModel):
    max_output_tokens: Optional[float] = FieldInfo(alias="maxOutputTokens", default=None)

    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsPromptDataOptions3(BaseModel):
    temperature: Optional[float] = None

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsJsCompletionParams(BaseModel):
    use_cache: Optional[bool] = None


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsPromptDataOptions0,
    PromptDataOptionsParamsPromptDataOptions1,
    PromptDataOptionsParamsPromptDataOptions2,
    PromptDataOptionsParamsPromptDataOptions3,
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


class PromptDataPromptPromptDataPrompt0(BaseModel):
    content: str

    type: Literal["completion"]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage0(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent(
    BaseModel
):
    type: Literal["text"]

    text: Optional[str] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList(
    BaseModel
):
    image_url: PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL

    type: Literal["image_url"]


PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArray = Union[
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList,
]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1(BaseModel):
    role: Literal["user"]

    content: Union[str, List[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArray], None] = None

    name: Optional[str] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2FunctionCall(BaseModel):
    arguments: str

    name: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCallFunction(BaseModel):
    arguments: str

    name: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCall(BaseModel):
    id: str

    function: PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCallFunction

    type: Literal["function"]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2FunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCall]] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage3(BaseModel):
    role: Literal["tool"]

    content: Optional[str] = None

    tool_call_id: Optional[str] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage4(BaseModel):
    name: str

    role: Literal["function"]

    content: Optional[str] = None


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage5(BaseModel):
    role: Literal["model"]

    content: Optional[str] = None


PromptDataPromptPromptDataPrompt1Message = Union[
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage0,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage3,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage4,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage5,
]


class PromptDataPromptPromptDataPrompt1(BaseModel):
    messages: List[PromptDataPromptPromptDataPrompt1Message]

    type: Literal["chat"]

    tools: Optional[str] = None


class PromptDataPromptPromptDataPrompt2(BaseModel):
    pass


PromptDataPrompt = Union[
    PromptDataPromptPromptDataPrompt0, PromptDataPromptPromptDataPrompt1, Optional[PromptDataPromptPromptDataPrompt2]
]


class PromptData(BaseModel):
    options: Optional[PromptDataOptions] = None

    origin: Optional[PromptDataOrigin] = None

    prompt: Optional[PromptDataPrompt] = None


class Prompt(BaseModel):
    id: str
    """Unique identifier for the prompt"""

    xact_id: str = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the prompt (see the `version`
    parameter)
    """

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
