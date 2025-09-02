# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

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
    emails: Optional[SequenceNotStr[str]]
    """Emails of users to invite"""

    group_id: Optional[str]
    """Singular form of group_ids"""

    group_ids: Optional[SequenceNotStr[str]]
    """Optional list of group ids to add newly-invited users to."""

    group_name: Optional[str]
    """Singular form of group_names"""

    group_names: Optional[SequenceNotStr[str]]
    """Optional list of group names to add newly-invited users to."""

    ids: Optional[SequenceNotStr[str]]
    """Ids of existing users to invite"""

    send_invite_emails: Optional[bool]
    """If true, send invite emails to the users who wore actually added"""


class RemoveUsers(TypedDict, total=False):
    emails: Optional[SequenceNotStr[str]]
    """Emails of users to remove"""

    ids: Optional[SequenceNotStr[str]]
    """Ids of users to remove"""
