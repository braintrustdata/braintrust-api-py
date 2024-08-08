# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.acl_object_id import ACLObjectID
from .shared.acl_object_type import ACLObjectType

__all__ = ["ViewRetrieveParams"]


class ViewRetrieveParams(TypedDict, total=False):
    object_id: Required[ACLObjectID]
    """The id of the object the ACL applies to"""

    object_type: Required[Optional[ACLObjectType]]
    """The object type that the ACL applies to"""
