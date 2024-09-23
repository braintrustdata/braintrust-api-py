# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.prompt_data import PromptData

__all__ = [
    "FunctionReplaceParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataCode",
    "FunctionDataCodeData",
    "FunctionDataCodeDataBundle",
    "FunctionDataCodeDataBundleLocation",
    "FunctionDataCodeDataBundleLocationPosition",
    "FunctionDataCodeDataBundleLocationPositionType",
    "FunctionDataCodeDataBundleLocationPositionScorer",
    "FunctionDataCodeDataBundleRuntimeContext",
    "FunctionDataCodeDataInline",
    "FunctionDataCodeDataInlineRuntimeContext",
    "FunctionDataGlobal",
    "Origin",
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

    function_type: Optional[Literal["task", "llm", "scorer"]]

    origin: Optional[Origin]

    prompt_data: Optional[PromptData]
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


FunctionDataCodeDataBundleLocationPosition: TypeAlias = Union[
    FunctionDataCodeDataBundleLocationPositionType, FunctionDataCodeDataBundleLocationPositionScorer
]


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


FunctionData: TypeAlias = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal]


class Origin(TypedDict, total=False):
    object_id: Required[str]
    """Id of the object the function is originating from"""

    object_type: Required[
        Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "group",
                "role",
                "org_member",
                "project_log",
                "org_project",
            ]
        ]
    ]
    """The object type that the ACL applies to"""

    internal: Optional[bool]
    """
    The function exists for internal purposes and should not be displayed in the
    list of functions.
    """
