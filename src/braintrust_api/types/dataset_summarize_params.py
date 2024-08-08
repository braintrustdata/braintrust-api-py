# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared.summarize_data import SummarizeData

__all__ = ["DatasetSummarizeParams"]


class DatasetSummarizeParams(TypedDict, total=False):
    summarize_data: SummarizeData
    """Whether to summarize the data.

    If false (or omitted), only the metadata will be returned.
    """
