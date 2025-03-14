# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Permission"]

Permission: TypeAlias = Literal[
    "create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"
]
