# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["MemberUpdateParams", "InviteUsers", "RemoveUsers"]


class MemberUpdateParams(TypedDict, total=False):
    invite_users: Optional[InviteUsers]
    """Users to invite to the organization"""

    org_id: Optional[str]
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, or in
    case you want to explicitly assert the organization you are modifying, you may
    specify the id of the organization.
    """

    org_name: Optional[str]
    """For nearly all users, this parameter should be unnecessary.

    But in the rare case that your API key belongs to multiple organizations, or in
    case you want to explicitly assert the organization you are modifying, you may
    specify the name of the organization.
    """

    remove_users: Optional[RemoveUsers]
    """Users to remove from the organization"""


class InviteUsers(TypedDict, total=False):
    emails: Optional[List[str]]
    """Emails of users to invite"""

    group_id: Optional[str]
    """Optional id of a group to add newly-invited users to.

    Cannot specify both a group id and a group name.
    """

    group_name: Optional[str]
    """Optional name of a group to add newly-invited users to.

    Cannot specify both a group id and a group name.
    """

    ids: Optional[List[str]]
    """Ids of existing users to invite"""

    send_invite_emails: Optional[bool]
    """If true, send invite emails to the users who wore actually added"""


class RemoveUsers(TypedDict, total=False):
    emails: Optional[List[str]]
    """Emails of users to remove"""

    ids: Optional[List[str]]
    """Ids of users to remove"""
