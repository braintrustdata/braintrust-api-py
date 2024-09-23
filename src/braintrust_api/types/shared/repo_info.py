# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RepoInfo"]


class RepoInfo(BaseModel):
    author_email: Optional[str] = None
    """Email of the author of the most recent commit"""

    author_name: Optional[str] = None
    """Name of the author of the most recent commit"""

    branch: Optional[str] = None
    """Name of the branch the most recent commit belongs to"""

    commit: Optional[str] = None
    """SHA of most recent commit"""

    commit_message: Optional[str] = None
    """Most recent commit message"""

    commit_time: Optional[str] = None
    """Time of the most recent commit"""

    dirty: Optional[bool] = None
    """Whether or not the repo had uncommitted changes when snapshotted"""

    git_diff: Optional[str] = None
    """
    If the repo was dirty when run, this includes the diff between the current state
    of the repo and the most recent commit.
    """

    tag: Optional[str] = None
    """Name of the tag on the most recent commit"""
