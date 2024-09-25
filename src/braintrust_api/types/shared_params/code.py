# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .task import Task
from .scorer import Scorer
from ..shared.task import Task
from ..shared.scorer import Scorer

__all__ = [
    "Code",
    "Data",
    "DataBundle",
    "DataBundleLocation",
    "DataBundleLocationExperiment",
    "DataBundleLocationExperimentPosition",
    "DataBundleLocationFunction",
    "DataBundleRuntimeContext",
    "DataInline",
    "DataInlineRuntimeContext",
]

DataBundleLocationExperimentPosition: TypeAlias = Union[Task, Scorer]


class DataBundleLocationExperiment(TypedDict, total=False):
    eval_name: Required[str]

    position: Required[DataBundleLocationExperimentPosition]

    type: Required[Literal["experiment"]]


class DataBundleLocationFunction(TypedDict, total=False):
    index: Required[int]

    type: Required[Literal["function"]]


DataBundleLocation: TypeAlias = Union[DataBundleLocationExperiment, DataBundleLocationFunction]


class DataBundleRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class DataBundle(TypedDict, total=False):
    bundle_id: Required[str]

    location: Required[DataBundleLocation]

    runtime_context: Required[DataBundleRuntimeContext]

    type: Required[Literal["bundle"]]

    preview: Optional[str]
    """A preview of the code"""


class DataInlineRuntimeContext(TypedDict, total=False):
    runtime: Required[Literal["node", "python"]]

    version: Required[str]


class DataInline(TypedDict, total=False):
    code: Required[str]

    runtime_context: Required[DataInlineRuntimeContext]

    type: Required[Literal["inline"]]


Data: TypeAlias = Union[DataBundle, DataInline]


class Code(TypedDict, total=False):
    data: Required[Data]

    type: Required[Literal["code"]]
