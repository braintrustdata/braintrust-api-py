# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MemberUpdateResponse"]


class MemberUpdateResponse(BaseModel):
    status: Literal["success"]

    send_email_error: Optional[str] = None
    """
    If invite emails failed to send for some reason, the patch operation will still
    complete, but we will return an error message here
    """
