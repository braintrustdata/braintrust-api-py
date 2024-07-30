# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FunctionCreateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataFunctionData1",
    "FunctionDataFunctionData1Data",
    "FunctionDataFunctionData1DataLocation",
    "FunctionDataFunctionData1DataLocationPosition",
    "FunctionDataFunctionData1DataLocationPositionScore",
    "FunctionDataFunctionData1DataRuntimeContext",
    "FunctionDataFunctionData2",
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


class FunctionDataPrompt(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataFunctionData1DataLocationPositionScore(TypedDict, total=False):
    score: Required[float]


FunctionDataFunctionData1DataLocationPosition = Union[
    Literal["task"], FunctionDataFunctionData1DataLocationPositionScore
]


class FunctionDataFunctionData1DataLocation(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataFunctionData1DataLocationPosition]

    type: Required[Literal["experiment"]]


class FunctionDataFunctionData1DataRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node"]]

    version: Required[str]


class FunctionDataFunctionData1Data(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[FunctionDataFunctionData1DataLocation]

    runtime_context: Required[FunctionDataFunctionData1DataRuntimeContext]


class FunctionDataFunctionData1(TypedDict, total=False):
    data: Required[FunctionDataFunctionData1Data]

    type: Required[Literal["code"]]


class FunctionDataFunctionData2(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


FunctionData = Union[FunctionDataPrompt, FunctionDataFunctionData1, FunctionDataFunctionData2]


class PromptDataOptionsParamsPromptDataOptions0FunctionCallName(TypedDict, total=False):
    name: Required[str]


PromptDataOptionsParamsPromptDataOptions0FunctionCall = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsPromptDataOptions0FunctionCallName
]


class PromptDataOptionsParamsPromptDataOptions0ResponseFormat(TypedDict, total=False):
    type: Required[Literal["json_object"]]


class PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2Function(TypedDict, total=False):
    name: Required[str]


class PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2(TypedDict, total=False):
    function: Required[PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2Function]

    type: Required[Literal["function"]]


PromptDataOptionsParamsPromptDataOptions0ToolChoice = Union[
    Literal["auto"], Literal["none"], PromptDataOptionsParamsPromptDataOptions0ToolChoicePromptDataToolChoice2
]


class PromptDataOptionsParamsPromptDataOptions0(TypedDict, total=False):
    frequency_penalty: float

    function_call: PromptDataOptionsParamsPromptDataOptions0FunctionCall

    max_tokens: float

    n: float

    presence_penalty: float

    response_format: Optional[PromptDataOptionsParamsPromptDataOptions0ResponseFormat]

    stop: List[str]

    temperature: float

    tool_choice: PromptDataOptionsParamsPromptDataOptions0ToolChoice

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsPromptDataOptions1(TypedDict, total=False):
    max_tokens: Required[float]

    temperature: Required[float]

    max_tokens_to_sample: float
    """This is a legacy parameter that should not be used."""

    stop_sequences: List[str]

    top_k: float

    top_p: float

    use_cache: bool


class PromptDataOptionsParamsPromptDataOptions2(TypedDict, total=False):
    max_output_tokens: Annotated[float, PropertyInfo(alias="maxOutputTokens")]

    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    use_cache: bool


class PromptDataOptionsParamsPromptDataOptions3(TypedDict, total=False):
    temperature: float

    top_k: Annotated[float, PropertyInfo(alias="topK")]

    use_cache: bool


class PromptDataOptionsParamsJsCompletionParams(TypedDict, total=False):
    use_cache: bool


PromptDataOptionsParams = Union[
    PromptDataOptionsParamsPromptDataOptions0,
    PromptDataOptionsParamsPromptDataOptions1,
    PromptDataOptionsParamsPromptDataOptions2,
    PromptDataOptionsParamsPromptDataOptions3,
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


class PromptDataPromptPromptDataPrompt0(TypedDict, total=False):
    content: Required[str]

    type: Required[Literal["completion"]]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage0(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent(
    TypedDict, total=False
):
    type: Required[Literal["text"]]

    text: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["auto", "low", "high"]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList(
    TypedDict, total=False
):
    image_url: Required[
        PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageListImageURL
    ]

    type: Required[Literal["image_url"]]


PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArray = Union[
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageContent,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArrayPromptDataPromptMessageList,
]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1ContentArray]]

    name: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2FunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCallFunction]

    type: Required[Literal["function"]]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2FunctionCall

    name: str

    tool_calls: Iterable[PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2ToolCall]


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage3(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage4(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage5(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


PromptDataPromptPromptDataPrompt1Message = Union[
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage0,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage1,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage2,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage3,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage4,
    PromptDataPromptPromptDataPrompt1MessagePromptDataPromptMessage5,
]


class PromptDataPromptPromptDataPrompt1(TypedDict, total=False):
    messages: Required[Iterable[PromptDataPromptPromptDataPrompt1Message]]

    type: Required[Literal["chat"]]

    tools: str


class PromptDataPromptPromptDataPrompt2(TypedDict, total=False):
    pass


PromptDataPrompt = Union[
    PromptDataPromptPromptDataPrompt0, PromptDataPromptPromptDataPrompt1, Optional[PromptDataPromptPromptDataPrompt2]
]


class PromptData(TypedDict, total=False):
    options: Optional[PromptDataOptions]

    origin: Optional[PromptDataOrigin]

    prompt: PromptDataPrompt
