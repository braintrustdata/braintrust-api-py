# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .prompt_data_param import PromptDataParam

__all__ = [
    "FunctionReplaceParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataLocation",
    "FunctionDataCodeDataLocationPosition",
    "FunctionDataCodeDataLocationPositionScore",
    "FunctionDataCodeDataRuntimeContext",
    "FunctionDataGlobal",
]


class FunctionReplaceParams(TypedDict, total=False):
    function_data: Required[FunctionData]

    name: Required[str]
    """Name of the prompt"""

    project_id: Required[str]
    """Unique identifier for the project that the prompt belongs under"""

    slug: Required[str]
    """Unique identifier for the prompt"""

    description: Optional[str]
    """Textual description of the prompt"""

    prompt_data: Optional[PromptDataParam]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


class FunctionDataPrompt(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataCodeDataLocationPositionScore(TypedDict, total=False):
    score: Required[float]


FunctionDataCodeDataLocationPosition = Union[Literal["task"], FunctionDataCodeDataLocationPositionScore]


class FunctionDataCodeDataLocation(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataCodeDataLocationPosition]

    type: Required[Literal["experiment"]]


class FunctionDataCodeDataRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node"]]

    version: Required[str]


class FunctionDataCodeData(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[FunctionDataCodeDataLocation]

    runtime_context: Required[FunctionDataCodeDataRuntimeContext]


class FunctionDataCode(TypedDict, total=False):
    data: Required[FunctionDataCodeData]

    type: Required[Literal["code"]]


class FunctionDataGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


FunctionData = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal]
