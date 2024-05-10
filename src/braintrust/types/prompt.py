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
    "PromptDataOptionsParamsUnionMember0",
    "PromptDataOptionsParamsUnionMember0FunctionCall",
    "PromptDataOptionsParamsUnionMember0FunctionCallName",
    "PromptDataOptionsParamsUnionMember0ResponseFormat",
    "PromptDataOptionsParamsUnionMember0ToolChoice",
    "PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2",
    "PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2Function",
    "PromptDataOptionsParamsUnionMember1",
    "PromptDataOptionsParamsUnionMember2",
    "PromptDataOptionsParamsUseCache",
    "PromptDataOrigin",
    "PromptDataPrompt",
    "PromptDataPromptUnionMember0",
    "PromptDataPromptUnionMember1",
    "PromptDataPromptUnionMember1Message",
    "PromptDataPromptUnionMember1MessageUnionMember0",
    "PromptDataPromptUnionMember1MessageUnionMember1",
    "PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1",
    "PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember0",
    "PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1",
    "PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1ImageURL",
    "PromptDataPromptUnionMember1MessageUnionMember2",
    "PromptDataPromptUnionMember1MessageUnionMember2FunctionCall",
    "PromptDataPromptUnionMember1MessageUnionMember2ToolCall",
    "PromptDataPromptUnionMember1MessageUnionMember2ToolCallFunction",
    "PromptDataPromptUnionMember1MessageUnionMember3",
    "PromptDataPromptUnionMember1MessageUnionMember4",
    "PromptDataPromptUnionMember2",
]


class PromptDataOptionsParamsUnionMember0FunctionCallName(BaseModel):
    name: str


PromptDataOptionsParamsUnionMember0FunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsUnionMember0FunctionCallName
]


class PromptDataOptionsParamsUnionMember0ResponseFormat(BaseModel):
    type: Literal["json_object"]


class PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2Function(BaseModel):
    name: str


class PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2(BaseModel):
    function: PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2Function

    type: Literal["function"]


PromptDataOptionsParamsUnionMember0ToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2
]


class PromptDataOptionsParamsUnionMember0(BaseModel):
    frequency_penalty: Optional[float] = None

    function_call: Optional[PromptDataOptionsParamsUnionMember0FunctionCall] = None

    max_tokens: Optional[float] = None

    n: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[PromptDataOptionsParamsUnionMember0ResponseFormat] = None

    stop: Optional[List[str]] = None

    temperature: Optional[float] = None

    tool_choice: Optional[PromptDataOptionsParamsUnionMember0ToolChoice] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsUnionMember1(BaseModel):
    max_tokens: float

    temperature: float

    max_tokens_to_sample: Optional[float] = None
    """This is a legacy parameter that should not be used."""

    stop_sequences: Optional[List[str]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsUnionMember2(BaseModel):
    temperature: float

    max_output_tokens: Optional[float] = FieldInfo(alias="maxOutputTokens", default=None)

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    use_cache: Optional[bool] = None


class PromptDataOptionsParamsUseCache(BaseModel):
    use_cache: Optional[bool] = None


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsUnionMember0,
    PromptDataOptionsParamsUnionMember1,
    PromptDataOptionsParamsUnionMember2,
    PromptDataOptionsParamsUseCache,
]


class PromptDataOptions(BaseModel):
    model: Optional[str] = None

    params: Optional[PromptDataOptionsParams] = None

    position: Optional[str] = None


class PromptDataOrigin(BaseModel):
    project_id: Optional[str] = None

    prompt_id: Optional[str] = None

    prompt_version: Optional[str] = None


class PromptDataPromptUnionMember0(BaseModel):
    content: str

    type: Literal["completion"]


class PromptDataPromptUnionMember1MessageUnionMember0(BaseModel):
    role: Literal["system"]

    content: Optional[str] = None

    name: Optional[str] = None


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember0(BaseModel):
    type: Literal["text"]

    text: Optional[str] = None


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1(BaseModel):
    image_url: PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1ImageURL

    type: Literal["image_url"]


PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1 = Union[
    PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember0,
    PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1,
]


class PromptDataPromptUnionMember1MessageUnionMember1(BaseModel):
    role: Literal["user"]

    content: Union[str, List[PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1], None] = None

    name: Optional[str] = None


class PromptDataPromptUnionMember1MessageUnionMember2FunctionCall(BaseModel):
    arguments: str

    name: str


class PromptDataPromptUnionMember1MessageUnionMember2ToolCallFunction(BaseModel):
    arguments: str

    name: str


class PromptDataPromptUnionMember1MessageUnionMember2ToolCall(BaseModel):
    id: str

    function: PromptDataPromptUnionMember1MessageUnionMember2ToolCallFunction

    type: Literal["function"]


class PromptDataPromptUnionMember1MessageUnionMember2(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[PromptDataPromptUnionMember1MessageUnionMember2FunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[PromptDataPromptUnionMember1MessageUnionMember2ToolCall]] = None


class PromptDataPromptUnionMember1MessageUnionMember3(BaseModel):
    role: Literal["tool"]

    tool_call_id: str

    content: Optional[str] = None


class PromptDataPromptUnionMember1MessageUnionMember4(BaseModel):
    name: str

    role: Literal["function"]

    content: Optional[str] = None


PromptDataPromptUnionMember1Message = Union[
    PromptDataPromptUnionMember1MessageUnionMember0,
    PromptDataPromptUnionMember1MessageUnionMember1,
    PromptDataPromptUnionMember1MessageUnionMember2,
    PromptDataPromptUnionMember1MessageUnionMember3,
    PromptDataPromptUnionMember1MessageUnionMember4,
]


class PromptDataPromptUnionMember1(BaseModel):
    messages: List[PromptDataPromptUnionMember1Message]

    type: Literal["chat"]

    tools: Optional[str] = None


class PromptDataPromptUnionMember2(BaseModel):
    pass


PromptDataPrompt = Union[
    PromptDataPromptUnionMember0, PromptDataPromptUnionMember1, Optional[PromptDataPromptUnionMember2]
]


class PromptData(BaseModel):
    options: Optional[PromptDataOptions] = None

    origin: Optional[PromptDataOrigin] = None

    prompt: Optional[PromptDataPrompt] = None


class Prompt(BaseModel):
    id: str
    """Unique identifier for the prompt"""

    api_xact_id: str = FieldInfo(alias="_xact_id")
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
