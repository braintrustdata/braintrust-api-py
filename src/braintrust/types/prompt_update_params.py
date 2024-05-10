# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PromptUpdateParams",
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
    "PromptDataPrompt_ReservedOnlyAllowNull",
]


class PromptUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


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
    temperature: Required[float]

    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class PromptDataOptionsParamsUseCache(TypedDict, total=False):
    use_cache: bool


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsUnionMember0,
    PromptDataOptionsParamsUnionMember1,
    PromptDataOptionsParamsUnionMember2,
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


class PromptDataPromptUnionMember0(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptDataPromptUnionMember1MessageUnionMember0(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember0(TypedDict, total=False):
    type: Required[Literal["text"]]

    text: str


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1 = Union[
    PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember0,
    PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1UnionMember1,
]


class PromptDataPromptUnionMember1MessageUnionMember1(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptDataPromptUnionMember1MessageUnionMember1ContentUnionMember1]]

    name: str


class PromptDataPromptUnionMember1MessageUnionMember2FunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptUnionMember1MessageUnionMember2ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptUnionMember1MessageUnionMember2ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptDataPromptUnionMember1MessageUnionMember2ToolCallFunction]

    type: Required[Literal["function"]]


class PromptDataPromptUnionMember1MessageUnionMember2(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptDataPromptUnionMember1MessageUnionMember2FunctionCall

    name: str

    tool_calls: Iterable[PromptDataPromptUnionMember1MessageUnionMember2ToolCall]


class PromptDataPromptUnionMember1MessageUnionMember3(TypedDict, total=False):
    role: Required[Literal["tool"]]

    tool_call_id: Required[str]

    content: str


class PromptDataPromptUnionMember1MessageUnionMember4(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


PromptDataPromptUnionMember1Message = Union[
    PromptDataPromptUnionMember1MessageUnionMember0,
    PromptDataPromptUnionMember1MessageUnionMember1,
    PromptDataPromptUnionMember1MessageUnionMember2,
    PromptDataPromptUnionMember1MessageUnionMember3,
    PromptDataPromptUnionMember1MessageUnionMember4,
]


class PromptDataPromptUnionMember1(TypedDict, total=False):
    messages: Required[Iterable[PromptDataPromptUnionMember1Message]]

    type: Required[Literal["chat"]]

    tools: str


class PromptDataPrompt_ReservedOnlyAllowNull(TypedDict, total=False):
    _reserved_only_allow_null: Required[Annotated[Dict[str, object], PropertyInfo(alias="__reserved_only_allow_null")]]
    """This is just a placeholder nullable object.

    Only pass null, not the object itself
    """


PromptDataPrompt = Union[
    PromptDataPromptUnionMember0, PromptDataPromptUnionMember1, Optional[PromptDataPrompt_ReservedOnlyAllowNull]
]


class PromptData(TypedDict, total=False):
    options: Optional[PromptDataOptions]

    origin: Optional[PromptDataOrigin]

    prompt: PromptDataPrompt
