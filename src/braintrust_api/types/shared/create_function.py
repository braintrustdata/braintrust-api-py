# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .prompt_data import PromptData

__all__ = [
    "CreateFunction",
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


class CreateFunction(BaseModel):
    function_data: FunctionData

    name: str
    """Name of the prompt"""

    project_id: str
    """Unique identifier for the project that the prompt belongs under"""

    slug: str
    """Unique identifier for the prompt"""

    description: Optional[str] = None
    """Textual description of the prompt"""

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
