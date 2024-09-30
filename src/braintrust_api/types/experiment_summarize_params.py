# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExperimentSummarizeParams"]


class ExperimentSummarizeParams(TypedDict, total=False):
    comparison_experiment_id: str
    """The experiment to compare against, if summarizing scores and metrics.

    If omitted, will fall back to the `base_exp_id` stored in the experiment
    metadata, and then to the most recent experiment run in the same project. Must
    pass `summarize_scores=true` for this id to be used
    """

    summarize_scores: Optional[bool]
    """Whether to summarize the scores and metrics.

    If false (or omitted), only the metadata will be returned.
    """
