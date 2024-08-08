# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PatchOrganizationMembers", "InviteUsers", "RemoveUsers"]


class InviteUsers(BaseModel):
    emails: Optional[List[str]] = None
    """Emails of users to invite"""

    group_id: Optional[str] = None
    """Optional id of a group to add newly-invited users to.

    Cannot specify both a group id and a group name.
    """

    group_name: Optional[str] = None
    """Optional name of a group to add newly-invited users to.

    Cannot specify both a group id and a group name.
    """

    ids: Optional[List[str]] = None
    """Ids of existing users to invite"""

    send_invite_emails: Optional[bool] = None
    """If true, send invite emails to the users who wore actually added"""


class RemoveUsers(BaseModel):
    emails: Optional[List[str]] = None
    """Emails of users to remove"""

    ids: Optional[List[str]] = None
    """Ids of users to remove"""


class PatchOrganizationMembers(BaseModel):
    invite_users: Optional[InviteUsers] = None
    """Users to invite to the organization"""

    org_id: Optional[str] = None
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, or in
    case you want to explicitly assert the organization you are modifying, you may
    specify the id of the organization.
    """

    org_name: Optional[str] = None
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, or in
    case you want to explicitly assert the organization you are modifying, you may
    specify the name of the organization.
    """

    remove_users: Optional[RemoveUsers] = None
    """Users to remove from the organization"""
