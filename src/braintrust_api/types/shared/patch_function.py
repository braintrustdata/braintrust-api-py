# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .prompt_data import PromptData

__all__ = [
    "PatchFunction",
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


class FunctionDataNullableVariant(BaseModel):
    pass


FunctionData: TypeAlias = Union[
    FunctionDataPrompt, FunctionDataCode, FunctionDataGlobal, Optional[FunctionDataNullableVariant]
]


class PatchFunction(BaseModel):
    description: Optional[str] = None
    """Textual description of the prompt"""

    function_data: Optional[FunctionData] = None

    name: Optional[str] = None
    """Name of the prompt"""

    prompt_data: Optional[PromptData] = None
    """The prompt, model, and its parameters"""

    tags: Optional[List[str]] = None
    """A list of tags for the prompt"""
