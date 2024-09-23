# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .prompt_data import PromptData

__all__ = [
    "Function",
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


class FunctionDataPrompt(BaseModel):
    type: Literal["prompt"]


class FunctionDataCodeDataBundleLocationPositionType(BaseModel):
    type: Literal["task"]


class FunctionDataCodeDataBundleLocationPositionScorer(BaseModel):
    index: float

    type: Literal["scorer"]


FunctionDataCodeDataBundleLocationPosition: TypeAlias = Union[
    FunctionDataCodeDataBundleLocationPositionType, FunctionDataCodeDataBundleLocationPositionScorer
]


class FunctionDataCodeDataBundleLocation(BaseModel):
    eval_name: str

    position: FunctionDataCodeDataBundleLocationPosition

    type: Literal["experiment"]


class FunctionDataCodeDataBundleRuntimeContext(BaseModel):
    runtime: Literal["node", "python"]

    version: str


class FunctionDataCodeDataBundle(BaseModel):
    bundle_id: str

    location: FunctionDataCodeDataBundleLocation

    runtime_context: FunctionDataCodeDataBundleRuntimeContext

    type: Literal["bundle"]

    preview: Optional[str] = None
    """A preview of the code"""


class FunctionDataCodeDataInlineRuntimeContext(BaseModel):
    runtime: Literal["node", "python"]

    version: str


class FunctionDataCodeDataInline(BaseModel):
    code: str

    runtime_context: FunctionDataCodeDataInlineRuntimeContext

    type: Literal["inline"]


FunctionDataCodeData: TypeAlias = Union[FunctionDataCodeDataBundle, FunctionDataCodeDataInline]


class FunctionDataCode(BaseModel):
    data: FunctionDataCodeData

    type: Literal["code"]


class FunctionDataGlobal(BaseModel):
    name: str

    type: Literal["global"]


FunctionData: TypeAlias = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal]


class Origin(BaseModel):
    object_id: str
    """Id of the object the function is originating from"""

    object_type: Optional[
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
    ] = None
    """The object type that the ACL applies to"""

    internal: Optional[bool] = None
    """
    The function exists for internal purposes and should not be displayed in the
    list of functions.
    """


class Function(BaseModel):
    id: str
    """Unique identifier for the prompt"""

    xact_id: str = FieldInfo(alias="_xact_id")
    """
    The transaction id of an event is unique to the network operation that processed
    the event insertion. Transaction ids are monotonically increasing over time and
    can be used to retrieve a versioned snapshot of the prompt (see the `version`
    parameter)
    """

    function_data: FunctionData

    log_id: Literal["p"]
    """A literal 'p' which identifies the object as a project prompt"""

    name: str
    """Name of the prompt"""

    org_id: str
    """Unique identifier for the organization"""

    project_id: str
    """Unique identifier for the project that the prompt belongs under"""

    slug: str
    """Unique identifier for the prompt"""

    created: Optional[datetime] = None
    """Date of prompt creation"""

    description: Optional[str] = None
    """Textual description of the prompt"""

    function_type: Optional[Literal["task", "llm", "scorer"]] = None

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the prompt"""

    origin: Optional[Origin] = None

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
