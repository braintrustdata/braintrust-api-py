# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

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


class LocationExperimentPositionType(TypedDict, total=False):
    type: Required[Literal["task"]]


class LocationExperimentPositionScorer(TypedDict, total=False):
    index: Required[int]

    type: Required[Literal["scorer"]]


LocationExperimentPosition: TypeAlias = Union[LocationExperimentPositionType, LocationExperimentPositionScorer]


class LocationExperiment(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[LocationExperimentPosition]

    type: Required[Literal["experiment"]]


class LocationFunction(TypedDict, total=False):
    index: Required[int]

    type: Required[Literal["function"]]


Location: TypeAlias = Union[LocationExperiment, LocationFunction]


class RuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class CodeBundle(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[Location]

    runtime_context: Required[RuntimeContext]

    preview: Optional[str]
    """A preview of the code"""
