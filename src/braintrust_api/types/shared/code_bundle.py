# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "CodeBundle",
    "Location",
    "LocationExperiment",
    "LocationExperimentPosition",
    "LocationExperimentPositionType",
    "LocationExperimentPositionScorer",
    "LocationFunction",
    "RuntimeContext",
]


class LocationExperimentPositionType(BaseModel):
    type: Literal["task"]


class LocationExperimentPositionScorer(BaseModel):
    index: int

    type: Literal["scorer"]


LocationExperimentPosition: TypeAlias = Union[LocationExperimentPositionType, LocationExperimentPositionScorer]


class LocationExperiment(BaseModel):
    eval_name: str

    position: LocationExperimentPosition

    type: Literal["experiment"]


class LocationFunction(BaseModel):
    index: int

    type: Literal["function"]


Location: TypeAlias = Union[LocationExperiment, LocationFunction]


class RuntimeContext(BaseModel):
    runtime: Literal["node", "python"]

    version: str


class CodeBundle(BaseModel):
    bundle_id: str

    location: Location

    runtime_context: RuntimeContext

    preview: Optional[str] = None
    """A preview of the code"""
