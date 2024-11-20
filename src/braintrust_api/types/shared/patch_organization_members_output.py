# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PatchOrganizationMembersOutput"]


class PatchOrganizationMembersOutput(BaseModel):
    org_id: str
    """The id of the org that was modified."""

    status: Literal["success"]

    send_email_error: Optional[str] = None
    """
    If invite emails failed to send for some reason, the patch operation will still
    complete, but we will return an error message here
    """
