# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .task import Task
from .scorer import Scorer
from ..._models import BaseModel

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


class DataBundleLocationExperiment(BaseModel):
    eval_name: str

    position: DataBundleLocationExperimentPosition

    type: Literal["experiment"]


class DataBundleLocationFunction(BaseModel):
    index: int

    type: Literal["function"]


DataBundleLocation: TypeAlias = Union[DataBundleLocationExperiment, DataBundleLocationFunction]


class DataBundleRuntimeContext(BaseModel):
    runtime: Literal["node", "python"]

    version: str


class DataBundle(BaseModel):
    bundle_id: str

    location: DataBundleLocation

    runtime_context: DataBundleRuntimeContext

    type: Literal["bundle"]

    preview: Optional[str] = None
    """A preview of the code"""


class DataInlineRuntimeContext(BaseModel):
    runtime: Literal["node", "python"]

    version: str


class DataInline(BaseModel):
    code: str

    runtime_context: DataInlineRuntimeContext

    type: Literal["inline"]


Data: TypeAlias = Union[DataBundle, DataInline]


class Code(BaseModel):
    data: Data

    type: Literal["code"]
