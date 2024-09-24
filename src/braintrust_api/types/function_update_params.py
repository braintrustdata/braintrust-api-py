# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.prompt_data import PromptData

__all__ = [
    "FunctionUpdateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataBundle",
    "FunctionDataCodeDataBundleLocation",
    "FunctionDataCodeDataBundleLocationExperiment",
    "FunctionDataCodeDataBundleLocationExperimentPosition",
    "FunctionDataCodeDataBundleLocationExperimentPositionType",
    "FunctionDataCodeDataBundleLocationExperimentPositionScorer",
    "FunctionDataCodeDataBundleLocationFunction",
    "FunctionDataCodeDataBundleRuntimeContext",
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


class FunctionDataCodeDataBundleLocationExperimentPositionType(TypedDict, total=False):
    type: Required[Literal["task"]]


class FunctionDataCodeDataBundleLocationExperimentPositionScorer(TypedDict, total=False):
    index: Required[int]

    type: Required[Literal["scorer"]]


FunctionDataCodeDataBundleLocationExperimentPosition: TypeAlias = Union[
    FunctionDataCodeDataBundleLocationExperimentPositionType, FunctionDataCodeDataBundleLocationExperimentPositionScorer
]


class FunctionDataCodeDataBundleLocationExperiment(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataCodeDataBundleLocationExperimentPosition]

    type: Required[Literal["experiment"]]


class FunctionDataCodeDataBundleLocationFunction(TypedDict, total=False):
    index: Required[int]

    type: Required[Literal["function"]]


FunctionDataCodeDataBundleLocation: TypeAlias = Union[
    FunctionDataCodeDataBundleLocationExperiment, FunctionDataCodeDataBundleLocationFunction
]


class FunctionDataCodeDataBundleRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class FunctionDataCodeDataBundle(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[FunctionDataCodeDataBundleLocation]

    runtime_context: Required[FunctionDataCodeDataBundleRuntimeContext]

    type: Required[Literal["bundle"]]

    preview: Optional[str]
    """A preview of the code"""


class FunctionDataCodeDataInlineRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class FunctionDataCodeDataInline(TypedDict, total=False):
    code: Required[str]

    runtime_context: Required[FunctionDataCodeDataInlineRuntimeContext]

    type: Required[Literal["inline"]]


FunctionDataCodeData: TypeAlias = Union[FunctionDataCodeDataBundle, FunctionDataCodeDataInline]


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
