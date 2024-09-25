# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.code import Code
from .shared_params.prompt_data import PromptData

__all__ = [
    "FunctionCreateParams",
    "FunctionData",
    "FunctionDataPrompt",
    "FunctionDataGlobal",
    "FunctionSchema",
    "Origin",
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

    function_schema: Optional[FunctionSchema]
    """JSON schema for the function's parameters and return type"""

    function_type: Optional[Literal["llm", "scorer", "task", "tool"]]

    origin: Optional[Origin]

    prompt_data: Optional[PromptData]
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]]
    """A list of tags for the prompt"""


class FunctionDataPrompt(TypedDict, total=False):
    type: Required[Literal["prompt"]]


class FunctionDataGlobal(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["global"]]


FunctionData: TypeAlias = Union[FunctionDataPrompt, Code, FunctionDataGlobal]


class FunctionSchema(TypedDict, total=False):
    parameters: object

    returns: object


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
