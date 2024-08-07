# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.prompt_data import PromptData

__all__ = [
    "Function",
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


class FunctionDataPrompt(BaseModel):
    type: Literal["prompt"]


class FunctionDataCodeDataLocationPositionScore(BaseModel):
    score: float


FunctionDataCodeDataLocationPosition: TypeAlias = Union[Literal["task"], FunctionDataCodeDataLocationPositionScore]


class FunctionDataCodeDataLocation(BaseModel):
    eval_name: str

    position: FunctionDataCodeDataLocationPosition

    type: Literal["experiment"]


class FunctionDataCodeDataRuntimeContext(BaseModel):
    runtime: Literal["node"]

    version: str


class FunctionDataCodeData(BaseModel):
    bundle_id: str

    location: FunctionDataCodeDataLocation

    runtime_context: FunctionDataCodeDataRuntimeContext


class FunctionDataCode(BaseModel):
    data: FunctionDataCodeData

    type: Literal["code"]


class FunctionDataGlobal(BaseModel):
    name: str

    type: Literal["global"]


FunctionData: TypeAlias = Union[FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal]


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

    metadata: Optional[Dict[str, object]] = None
    """User-controlled metadata about the prompt"""

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
