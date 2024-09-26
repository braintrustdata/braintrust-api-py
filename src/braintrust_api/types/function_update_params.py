# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..types.shared import CodeBundle
from .shared_params.prompt_data import PromptData

__all__ = [
    "FunctionUpdateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataInline",
    "FunctionDataCodeDataInlineRuntimeContext",
    "FunctionDataGlobal",
    "FunctionDataNullableVariant",
]


class FunctionUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Textual description of the prompt"""

    function_data: FunctionData

    name: Optional[str]
    """Name of the prompt"""

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


class FunctionDataPrompt(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataCodeDataInlineRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class FunctionDataCodeDataInline(TypedDict, total=False):
    code: Required[str]

    runtime_context: Required[FunctionDataCodeDataInlineRuntimeContext]

    type: Required[Literal["inline"]]


FunctionDataCodeData: TypeAlias = Union[CodeBundle, FunctionDataCodeDataInline]


class FunctionDataCode(TypedDict, total=False):
    data: Required[FunctionDataCodeData]

    type: Required[Literal["code"]]


class FunctionDataGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


class FunctionDataNullableVariant(TypedDict, total=False):
    pass


FunctionData: TypeAlias = Union[
    FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal, Optional[FunctionDataNullableVariant]
]
