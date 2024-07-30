# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FunctionCreateParams",
    "FunctionData",
    "FunctionDataType",
    "FunctionDataUnionMember1",
    "FunctionDataUnionMember1Data",
    "FunctionDataUnionMember1DataLocation",
    "FunctionDataUnionMember1DataLocationPosition",
    "FunctionDataUnionMember1DataLocationPositionScore",
    "FunctionDataUnionMember1DataRuntimeContext",
    "FunctionDataUnionMember2",
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
    "PromptDataOptionsParamsUnionMember3",
    "PromptDataOptionsParamsUseCache",
    "PromptDataOrigin",
    "PromptDataPrompt",
    "PromptDataPromptCompletion",
    "PromptDataPromptChat",
    "PromptDataPromptChatMessage",
    "PromptDataPromptChatMessageUnionMember0",
    "PromptDataPromptChatMessageUnionMember1",
    "PromptDataPromptChatMessageUnionMember1ContentUnionMember1",
    "PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember0",
    "PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1",
    "PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1ImageURL",
    "PromptDataPromptChatMessageUnionMember2",
    "PromptDataPromptChatMessageUnionMember2FunctionCall",
    "PromptDataPromptChatMessageUnionMember2ToolCall",
    "PromptDataPromptChatMessageUnionMember2ToolCallFunction",
    "PromptDataPromptChatMessageUnionMember3",
    "PromptDataPromptChatMessageUnionMember4",
    "PromptDataPromptChatMessageUnionMember5",
    "PromptDataPromptUnionMember2",
]


class FunctionCreateParams(TypedDict, total=False):
    function_data: Required[FunctionData]

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


class FunctionDataType(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataUnionMember1DataLocationPositionScore(TypedDict, total=False):
    score: Required[float]


FunctionDataUnionMember1DataLocationPosition = Union[Literal["task"], FunctionDataUnionMember1DataLocationPositionScore]


class FunctionDataUnionMember1DataLocation(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataUnionMember1DataLocationPosition]

    type: Required[Literal["experiment"]]


class FunctionDataUnionMember1DataRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node"]]

    version: Required[str]


class FunctionDataUnionMember1Data(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[FunctionDataUnionMember1DataLocation]

    runtime_context: Required[FunctionDataUnionMember1DataRuntimeContext]


class FunctionDataUnionMember1(TypedDict, total=False):
    data: Required[FunctionDataUnionMember1Data]

    type: Required[Literal["code"]]


class FunctionDataUnionMember2(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


FunctionData = Union[FunctionDataType, FunctionDataUnionMember1, FunctionDataUnionMember2]


class PromptDataOptionsParamsUnionMember0FunctionCallName(TypedDict, total=False):
    name: Required[str]


PromptDataOptionsParamsUnionMember0FunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsUnionMember0FunctionCallName
]


class PromptDataOptionsParamsUnionMember0ResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2Function(TypedDict, total=False):
    name: Required[str]


class PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2(TypedDict, total=False):
    function: Required[PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2Function]

    type: Required[Literal["function"]]


PromptDataOptionsParamsUnionMember0ToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsUnionMember0ToolChoiceUnionMember2
]


class PromptDataOptionsParamsUnionMember0(TypedDict, total=False):
    frequency_penalty: float

    function_call: PromptDataOptionsParamsUnionMember0FunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: Optional[PromptDataOptionsParamsUnionMember0ResponseFormat]

    stop: List[str]

    temperature: float

    tool_choice: PromptDataOptionsParamsUnionMember0ToolChoice

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsUnionMember1(TypedDict, total=False):
    max_tokens: Required[float]

    temperature: Required[float]

    max_tokens_to_sample: float
    """This is a legacy parameter that should not be used."""

    stop_sequences: List[str]

    top_k: float

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsUnionMember2(TypedDict, total=False):
    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class PromptDataOptionsParamsUnionMember3(TypedDict, total=False):
    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    use_cache: bool


class PromptDataOptionsParamsUseCache(TypedDict, total=False):
    use_cache: bool


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsUnionMember0,
    PromptDataOptionsParamsUnionMember1,
    PromptDataOptionsParamsUnionMember2,
    PromptDataOptionsParamsUnionMember3,
    PromptDataOptionsParamsUseCache,
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


class PromptDataPromptChatMessageUnionMember0(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember0(TypedDict, total=False):
    type: Required[Literal["text"]]

    text: str


class PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


PromptDataPromptChatMessageUnionMember1ContentUnionMember1 = Union[
    PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember0,
    PromptDataPromptChatMessageUnionMember1ContentUnionMember1UnionMember1,
]


class PromptDataPromptChatMessageUnionMember1(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptDataPromptChatMessageUnionMember1ContentUnionMember1]]

    name: str


class PromptDataPromptChatMessageUnionMember2FunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessageUnionMember2ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptChatMessageUnionMember2ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptDataPromptChatMessageUnionMember2ToolCallFunction]

    type: Required[Literal["function"]]


class PromptDataPromptChatMessageUnionMember2(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptDataPromptChatMessageUnionMember2FunctionCall

    name: str

    tool_calls: Iterable[PromptDataPromptChatMessageUnionMember2ToolCall]


class PromptDataPromptChatMessageUnionMember3(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class PromptDataPromptChatMessageUnionMember4(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class PromptDataPromptChatMessageUnionMember5(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


PromptDataPromptChatMessage = Union[
    PromptDataPromptChatMessageUnionMember0,
    PromptDataPromptChatMessageUnionMember1,
    PromptDataPromptChatMessageUnionMember2,
    PromptDataPromptChatMessageUnionMember3,
    PromptDataPromptChatMessageUnionMember4,
    PromptDataPromptChatMessageUnionMember5,
]


class PromptDataPromptChat(TypedDict, total=False):
    messages: Required[Iterable[PromptDataPromptChatMessage]]

    type: Required[Literal["chat"]]

    tools: str


class PromptDataPromptUnionMember2(TypedDict, total=False):
    pass


PromptDataPrompt = Union[PromptDataPromptCompletion, PromptDataPromptChat, Optional[PromptDataPromptUnionMember2]]


class PromptData(TypedDict, total=False):
    options: Optional[PromptDataOptions]

    origin: Optional[PromptDataOrigin]

    prompt: PromptDataPrompt
