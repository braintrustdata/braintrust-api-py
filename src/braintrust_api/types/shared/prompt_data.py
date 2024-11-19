# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .prompt_options import PromptOptions
from .chat_completion_message import ChatCompletionMessage

__all__ = [
    "PromptData",
    "Origin",
    "Parser",
    "Prompt",
    "PromptCompletion",
    "PromptChat",
    "PromptNullableVariant",
    "ToolFunction",
    "ToolFunctionFunction",
    "ToolFunctionGlobal",
]


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


class PromptChat(BaseModel):
    messages: List[ChatCompletionMessage]

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
    options: Optional[PromptOptions] = None

    origin: Optional[Origin] = None

    parser: Optional[Parser] = None

    prompt: Optional[Prompt] = None

    tool_functions: Optional[List[ToolFunction]] = None
