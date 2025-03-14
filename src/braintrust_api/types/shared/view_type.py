# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["ViewType"]

ViewType: TypeAlias = Optional[
    Literal[
        "projects",
        "experiments",
        "experiment",
        "playgrounds",
        "playground",
        "datasets",
        "dataset",
        "prompts",
        "tools",
        "scorers",
        "logs",
    ]
]
