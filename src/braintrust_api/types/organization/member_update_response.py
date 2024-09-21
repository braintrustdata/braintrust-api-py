# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["MemberUpdateResponse"]

class MemberUpdateResponse(BaseModel):
    status: Literal["success"]

    send_email_error: Optional[str] = None
    """
    If invite emails failed to send for some reason, the patch operation will still
    complete, but we will return an error message here
    """