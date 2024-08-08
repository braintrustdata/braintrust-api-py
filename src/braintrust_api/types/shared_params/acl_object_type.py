# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["ACLObjectType"]

ACLObjectType: TypeAlias = Optional[
    Literal[
        "organization",
        "project",
        "experiment",
        "dataset",
        "prompt",
        "prompt_session",
        "group",
        "role",
        "org_member",
        "project_log",
        "org_project",
    ]
]
