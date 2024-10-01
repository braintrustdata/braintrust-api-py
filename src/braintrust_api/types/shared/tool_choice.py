# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .function_tool_choice import FunctionToolChoice

__all__ = ["ToolChoice", "Function"]


class Function(BaseModel):
    function: FunctionToolChoice

    type: Literal["function"]


ToolChoice: TypeAlias = Union[Literal["auto"], Literal["none"], Function]
