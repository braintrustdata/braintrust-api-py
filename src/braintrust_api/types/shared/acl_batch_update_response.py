# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .acl import ACL
from ..._models import BaseModel

__all__ = ["ACLBatchUpdateResponse"]


class ACLBatchUpdateResponse(BaseModel):
    added_acls: List[ACL]
    """
    An ACL grants a certain permission or role to a certain user or group on an
    object.

    ACLs are inherited across the object hierarchy. So for example, if a user has
    read permissions on a project, they will also have read permissions on any
    experiment, dataset, etc. created within that project.

    To restrict a grant to a particular sub-object, you may specify
    `restrict_object_type` in the ACL, as part of a direct permission grant or as
    part of a role.
    """

    removed_acls: List[ACL]
    """
    An ACL grants a certain permission or role to a certain user or group on an
    object.

    ACLs are inherited across the object hierarchy. So for example, if a user has
    read permissions on a project, they will also have read permissions on any
    experiment, dataset, etc. created within that project.

    To restrict a grant to a particular sub-object, you may specify
    `restrict_object_type` in the ACL, as part of a direct permission grant or as
    part of a role.
    """
