# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import eval_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared_params.repo_info import RepoInfo
from ..types.shared.summarize_experiment_response import SummarizeExperimentResponse

__all__ = ["EvalsResource", "AsyncEvalsResource"]


class EvalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return EvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return EvalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: eval_create_params.Data,
        project_id: str,
        scores: Iterable[eval_create_params.Score],
        task: eval_create_params.Task,
        base_experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        base_experiment_name: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        git_metadata_settings: Optional[eval_create_params.GitMetadataSettings] | NotGiven = NOT_GIVEN,
        is_public: Optional[bool] | NotGiven = NOT_GIVEN,
        max_concurrency: Optional[float] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        api_timeout: Optional[float] | NotGiven = NOT_GIVEN,
        trial_count: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeExperimentResponse:
        """Launch an evaluation.

        This is the API-equivalent of the `Eval` function that is
        built into the Braintrust SDK. In the Eval API, you provide pointers to a
        dataset, task function, and scoring functions. The API will then run the
        evaluation, create an experiment, and return the results along with a link to
        the experiment. To learn more about evals, see the
        [Evals guide](https://www.braintrust.dev/docs/guides/evals).

        Args:
          data: The dataset to use

          project_id: Unique identifier for the project to run the eval in

          scores: The functions to score the eval on

          task: The function to evaluate

          base_experiment_id: An optional experiment id to use as a base. If specified, the new experiment
              will be summarized and compared to this experiment.

          base_experiment_name: An optional experiment name to use as a base. If specified, the new experiment
              will be summarized and compared to this experiment.

          experiment_name: An optional name for the experiment created by this eval. If it conflicts with
              an existing experiment, it will be suffixed with a unique identifier.

          git_metadata_settings: Optional settings for collecting git metadata. By default, will collect all git
              metadata fields allowed in org-level settings.

          is_public: Whether the experiment should be public. Defaults to false.

          max_concurrency: The maximum number of tasks/scorers that will be run concurrently. Defaults to
              undefined, in which case there is no max concurrency.

          metadata: Optional experiment-level metadata to store about the evaluation. You can later
              use this to slice & dice across experiments.

          repo_info: Metadata about the state of the repo when the experiment was created

          stream: Whether to stream the results of the eval. If true, the request will return two
              events: one to indicate the experiment has started, and another upon completion.
              If false, the request will return the evaluation's summary upon completion.

          api_timeout: The maximum duration, in milliseconds, to run the evaluation. Defaults to
              undefined, in which case there is no timeout.

          trial_count: The number of times to run the evaluator per input. This is useful for
              evaluating applications that have non-deterministic behavior and gives you both
              a stronger aggregate measure and a sense of the variance in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/eval",
            body=maybe_transform(
                {
                    "data": data,
                    "project_id": project_id,
                    "scores": scores,
                    "task": task,
                    "base_experiment_id": base_experiment_id,
                    "base_experiment_name": base_experiment_name,
                    "experiment_name": experiment_name,
                    "git_metadata_settings": git_metadata_settings,
                    "is_public": is_public,
                    "max_concurrency": max_concurrency,
                    "metadata": metadata,
                    "repo_info": repo_info,
                    "stream": stream,
                    "api_timeout": api_timeout,
                    "trial_count": trial_count,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizeExperimentResponse,
        )


class AsyncEvalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncEvalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: eval_create_params.Data,
        project_id: str,
        scores: Iterable[eval_create_params.Score],
        task: eval_create_params.Task,
        base_experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        base_experiment_name: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        git_metadata_settings: Optional[eval_create_params.GitMetadataSettings] | NotGiven = NOT_GIVEN,
        is_public: Optional[bool] | NotGiven = NOT_GIVEN,
        max_concurrency: Optional[float] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, Optional[object]] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        api_timeout: Optional[float] | NotGiven = NOT_GIVEN,
        trial_count: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeExperimentResponse:
        """Launch an evaluation.

        This is the API-equivalent of the `Eval` function that is
        built into the Braintrust SDK. In the Eval API, you provide pointers to a
        dataset, task function, and scoring functions. The API will then run the
        evaluation, create an experiment, and return the results along with a link to
        the experiment. To learn more about evals, see the
        [Evals guide](https://www.braintrust.dev/docs/guides/evals).

        Args:
          data: The dataset to use

          project_id: Unique identifier for the project to run the eval in

          scores: The functions to score the eval on

          task: The function to evaluate

          base_experiment_id: An optional experiment id to use as a base. If specified, the new experiment
              will be summarized and compared to this experiment.

          base_experiment_name: An optional experiment name to use as a base. If specified, the new experiment
              will be summarized and compared to this experiment.

          experiment_name: An optional name for the experiment created by this eval. If it conflicts with
              an existing experiment, it will be suffixed with a unique identifier.

          git_metadata_settings: Optional settings for collecting git metadata. By default, will collect all git
              metadata fields allowed in org-level settings.

          is_public: Whether the experiment should be public. Defaults to false.

          max_concurrency: The maximum number of tasks/scorers that will be run concurrently. Defaults to
              undefined, in which case there is no max concurrency.

          metadata: Optional experiment-level metadata to store about the evaluation. You can later
              use this to slice & dice across experiments.

          repo_info: Metadata about the state of the repo when the experiment was created

          stream: Whether to stream the results of the eval. If true, the request will return two
              events: one to indicate the experiment has started, and another upon completion.
              If false, the request will return the evaluation's summary upon completion.

          api_timeout: The maximum duration, in milliseconds, to run the evaluation. Defaults to
              undefined, in which case there is no timeout.

          trial_count: The number of times to run the evaluator per input. This is useful for
              evaluating applications that have non-deterministic behavior and gives you both
              a stronger aggregate measure and a sense of the variance in the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/eval",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "project_id": project_id,
                    "scores": scores,
                    "task": task,
                    "base_experiment_id": base_experiment_id,
                    "base_experiment_name": base_experiment_name,
                    "experiment_name": experiment_name,
                    "git_metadata_settings": git_metadata_settings,
                    "is_public": is_public,
                    "max_concurrency": max_concurrency,
                    "metadata": metadata,
                    "repo_info": repo_info,
                    "stream": stream,
                    "api_timeout": api_timeout,
                    "trial_count": trial_count,
                },
                eval_create_params.EvalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizeExperimentResponse,
        )


class EvalsResourceWithRawResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_raw_response_wrapper(
            evals.create,
        )


class AsyncEvalsResourceWithRawResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_raw_response_wrapper(
            evals.create,
        )


class EvalsResourceWithStreamingResponse:
    def __init__(self, evals: EvalsResource) -> None:
        self._evals = evals

        self.create = to_streamed_response_wrapper(
            evals.create,
        )


class AsyncEvalsResourceWithStreamingResponse:
    def __init__(self, evals: AsyncEvalsResource) -> None:
        self._evals = evals

        self.create = async_to_streamed_response_wrapper(
            evals.create,
        )
