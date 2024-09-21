# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ViewDataSearch"]

class ViewDataSearch(BaseModel):
    filter: Optional[List[object]] = None

    match: Optional[List[object]] = None

    sort: Optional[List[object]] = None

    tag: Optional[List[object]] = None