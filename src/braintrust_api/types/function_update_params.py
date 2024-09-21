# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required, TypeAlias

from typing import Optional, List, Union

from ..types import shared_params

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["FunctionUpdateParams", "FunctionData", "FunctionDataPrompt", "FunctionDataCode", "FunctionDataCodeData", "FunctionDataCodeDataBundle", "FunctionDataCodeDataBundleLocation", "FunctionDataCodeDataBundleLocationPosition", "FunctionDataCodeDataBundleLocationPositionType", "FunctionDataCodeDataBundleLocationPositionScorer", "FunctionDataCodeDataBundleRuntimeContext", "FunctionDataCodeDataInline", "FunctionDataCodeDataInlineRuntimeContext", "FunctionDataGlobal", "FunctionDataNullableVariant"]

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

class FunctionDataCodeDataBundleLocationPositionType(TypedDict, total=False):
    type: Required[Literal["task"]]

class FunctionDataCodeDataBundleLocationPositionScorer(TypedDict, total=False):
    index: Required[float]

    type: Required[Literal["scorer"]]

FunctionDataCodeDataBundleLocationPosition: TypeAlias = Union[FunctionDataCodeDataBundleLocationPositionType, FunctionDataCodeDataBundleLocationPositionScorer]

class FunctionDataCodeDataBundleLocation(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[FunctionDataCodeDataBundleLocationPosition]

    type: Required[Literal["experiment"]]

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

FunctionData: TypeAlias = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal, Optional[FunctionDataNullableVariant]]