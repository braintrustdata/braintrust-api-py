# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .function_tool_choice import FunctionToolChoice

__all__ = ["ToolChoice", "Function"]


class Function(TypedDict, total=False):
    function: Required[FunctionToolChoice]

    type: Required[Literal["function"]]


ToolChoice: TypeAlias = Union[Literal["auto"], Literal["none"], Function]
