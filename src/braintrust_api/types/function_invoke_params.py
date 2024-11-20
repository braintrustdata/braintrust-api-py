# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.chat_completion_content_part_text import ChatCompletionContentPartText
from .shared_params.chat_completion_message_tool_call import ChatCompletionMessageToolCall
from .shared_params.chat_completion_content_part_image import ChatCompletionContentPartImage

__all__ = [
    "FunctionInvokeParams",
    "Message",
    "MessageSystem",
    "MessageUser",
    "MessageUserContentArray",
    "MessageAssistant",
    "MessageAssistantFunctionCall",
    "MessageTool",
    "MessageFunction",
    "MessageFallback",
    "Parent",
    "ParentSpanParentStruct",
    "ParentSpanParentStructRowIDs",
]


class FunctionInvokeParams(TypedDict, total=False):
    input: Optional[object]
    """Argument to the function, which can be any JSON serializable value"""

    messages: Iterable[Message]
    """If the function is an LLM, additional messages to pass along to it"""

    mode: Optional[Literal["auto", "parallel"]]
    """The mode format of the returned value (defaults to 'auto')"""

    parent: Parent
    """Options for tracing the function call"""

    stream: Optional[bool]
    """Whether to stream the response.

    If true, results will be returned in the Braintrust SSE format.
    """

    version: str
    """The version of the function"""


class MessageSystem(TypedDict, total=False):
    role: Required[Literal["system"]]

    content: str

    name: str


MessageUserContentArray: TypeAlias = Union[ChatCompletionContentPartText, ChatCompletionContentPartImage]


class MessageUser(TypedDict, total=False):
    role: Required[Literal["user"]]

    content: Union[str, Iterable[MessageUserContentArray]]

    name: str


class MessageAssistantFunctionCall(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageAssistant(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    function_call: Optional[MessageAssistantFunctionCall]

    name: Optional[str]

    tool_calls: Optional[Iterable[ChatCompletionMessageToolCall]]


class MessageTool(TypedDict, total=False):
    role: Required[Literal["tool"]]

    content: str

    tool_call_id: str


class MessageFunction(TypedDict, total=False):
    name: Required[str]

    role: Required[Literal["function"]]

    content: str


class MessageFallback(TypedDict, total=False):
    role: Required[Literal["model"]]

    content: Optional[str]


Message: TypeAlias = Union[MessageSystem, MessageUser, MessageAssistant, MessageTool, MessageFunction, MessageFallback]


class ParentSpanParentStructRowIDs(TypedDict, total=False):
    id: Required[str]
    """The id of the row"""

    root_span_id: Required[str]
    """The root_span_id of the row"""

    span_id: Required[str]
    """The span_id of the row"""


class ParentSpanParentStruct(TypedDict, total=False):
    object_id: Required[str]
    """The id of the container object you are logging to"""

    object_type: Required[Literal["project_logs", "experiment"]]

    propagated_event: Optional[Dict[str, Optional[object]]]
    """Include these properties in every span created under this parent"""

    row_ids: Optional[ParentSpanParentStructRowIDs]
    """Identifiers for the row to to log a subspan under"""


Parent: TypeAlias = Union[ParentSpanParentStruct, str]
