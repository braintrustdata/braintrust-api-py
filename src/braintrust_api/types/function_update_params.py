# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = [
    "FunctionUpdateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataLocation",
    "FunctionDataCodeDataLocationPosition",
    "FunctionDataCodeDataLocationPositionScore",
    "FunctionDataCodeDataRuntimeContext",
    "FunctionDataGlobal",
    "FunctionDataNullableVariant",
]


class FunctionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    function_data: FunctionData

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[shared_params.PromptData]
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


class FunctionDataNullableVariant(TypedDict, total=False):
    pass


FunctionData = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal, Optional[FunctionDataNullableVariant]]
