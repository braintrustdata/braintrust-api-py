# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ACLListParams"]


class ACLListParams(TypedDict, total=False):
    object_id: Required[str]
    """The id of the object the ACL applies to"""

    object_type: Required[
        Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "project_score",
                "project_tag",
                "group",
                "role",
            ]
        ]
    ]
    """The object type that the ACL applies to"""

    ending_before: str
    """Pagination cursor id.

    For example, if the initial item in the last page you fetched had an id of
    `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
    pass one of `starting_after` and `ending_before`
    """

    limit: int
    """Limit the number of objects to return"""

    starting_after: str
    """Pagination cursor id.

    For example, if the final item in the last page you fetched had an id of `foo`,
    pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
    `starting_after` and `ending_before`
    """
