# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["Position", "Type", "Scorer"]


class Type(BaseModel):
    type: Literal["task"]


class Scorer(BaseModel):
    index: int

    type: Literal["scorer"]


Position: TypeAlias = Union[Type, Scorer]
