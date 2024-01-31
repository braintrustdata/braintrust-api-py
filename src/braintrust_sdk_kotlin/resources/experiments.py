# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import ExperimentListResponse, experiment_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["Experiments", "AsyncExperiments"]


class Experiments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperimentsWithRawResponse:
        return ExperimentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentsWithStreamingResponse:
        return ExperimentsWithStreamingResponse(self)

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentListResponse:
        """List out all experiments.

        The experiments are sorted by creation date, with the
        most recently-created experiments coming first

        Args:
          ending_before: A cursor for pagination. For example, if the initial item in the last page you
              fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page.
              Note: you may only pass one of `starting_after` and `ending_before`

          experiment_name: Name of the experiment to search for

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

          starting_after: A cursor for pagination. For example, if the final item in the last page you
              fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page.
              Note: you may only pass one of `starting_after` and `ending_before`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/experiment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "experiment_name": experiment_name,
                        "limit": limit,
                        "org_name": org_name,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    experiment_list_params.ExperimentListParams,
                ),
            ),
            cast_to=ExperimentListResponse,
        )


class AsyncExperiments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperimentsWithRawResponse:
        return AsyncExperimentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentsWithStreamingResponse:
        return AsyncExperimentsWithStreamingResponse(self)

    async def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentListResponse:
        """List out all experiments.

        The experiments are sorted by creation date, with the
        most recently-created experiments coming first

        Args:
          ending_before: A cursor for pagination. For example, if the initial item in the last page you
              fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page.
              Note: you may only pass one of `starting_after` and `ending_before`

          experiment_name: Name of the experiment to search for

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

          starting_after: A cursor for pagination. For example, if the final item in the last page you
              fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page.
              Note: you may only pass one of `starting_after` and `ending_before`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/experiment",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "experiment_name": experiment_name,
                        "limit": limit,
                        "org_name": org_name,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    experiment_list_params.ExperimentListParams,
                ),
            ),
            cast_to=ExperimentListResponse,
        )


class ExperimentsWithRawResponse:
    def __init__(self, experiments: Experiments) -> None:
        self._experiments = experiments

        self.list = to_raw_response_wrapper(
            experiments.list,
        )


class AsyncExperimentsWithRawResponse:
    def __init__(self, experiments: AsyncExperiments) -> None:
        self._experiments = experiments

        self.list = async_to_raw_response_wrapper(
            experiments.list,
        )


class ExperimentsWithStreamingResponse:
    def __init__(self, experiments: Experiments) -> None:
        self._experiments = experiments

        self.list = to_streamed_response_wrapper(
            experiments.list,
        )


class AsyncExperimentsWithStreamingResponse:
    def __init__(self, experiments: AsyncExperiments) -> None:
        self._experiments = experiments

        self.list = async_to_streamed_response_wrapper(
            experiments.list,
        )
