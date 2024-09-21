# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["OrgSecretReplaceParams"]

class OrgSecretReplaceParams(TypedDict, total=False):
    name: Required[str]
    """Name of the org secret"""

    metadata: Optional[Dict[str, object]]

    org_name: Optional[str]
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, you
    may specify the name of the organization the Org Secret belongs in.
    """

    secret: Optional[str]
    """Secret value.

    If omitted in a PUT request, the existing secret value will be left intact, not
    replaced with null.
    """

    type: Optional[str]