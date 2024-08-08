# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RepoInfo"]


class RepoInfo(TypedDict, total=False):
    author_email: Optional[str]
    """Email of the author of the most recent commit"""

    author_name: Optional[str]
    """Name of the author of the most recent commit"""

    branch: Optional[str]
    """Name of the branch the most recent commit belongs to"""

    commit: Optional[str]
    """SHA of most recent commit"""

    commit_message: Optional[str]
    """Most recent commit message"""

    commit_time: Optional[str]
    """Time of the most recent commit"""

    dirty: Optional[bool]
    """Whether or not the repo had uncommitted changes when snapshotted"""

    git_diff: Optional[str]
    """
    If the repo was dirty when run, this includes the diff between the current state
    of the repo and the most recent commit.
    """

    tag: Optional[str]
    """Name of the tag on the most recent commit"""
