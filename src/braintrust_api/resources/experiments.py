# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import (
    experiment_list_params,
    experiment_fetch_params,
    experiment_create_params,
    experiment_insert_params,
    experiment_update_params,
    experiment_feedback_params,
    experiment_summarize_params,
    experiment_fetch_post_params,
)
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
from ..pagination import SyncListObjects, AsyncListObjects
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.experiment import Experiment
from ..types.shared_params.repo_info import RepoInfo
from ..types.shared.insert_events_response import InsertEventsResponse
from ..types.shared.feedback_response_schema import FeedbackResponseSchema
from ..types.shared.summarize_experiment_response import SummarizeExperimentResponse
from ..types.shared_params.insert_experiment_event import InsertExperimentEvent
from ..types.shared_params.feedback_experiment_item import FeedbackExperimentItem
from ..types.shared.fetch_experiment_events_response import FetchExperimentEventsResponse

__all__ = ["ExperimentsResource", "AsyncExperimentsResource"]


class ExperimentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperimentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return ExperimentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return ExperimentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ensure_new: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """Create a new experiment.

        If there is an existing experiment in the project with
        the same name as the one specified in the request, will return the existing
        experiment unmodified

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

          base_exp_id: Id of default base experiment to compare against when viewing this experiment

          dataset_id: Identifier of the linked dataset, or null if the experiment is not linked to a
              dataset

          dataset_version: Version number of the linked dataset the experiment was run against. This can be
              used to reproduce the experiment after the dataset has been modified.

          description: Textual description of the experiment

          ensure_new: Normally, creating an experiment with the same name as an existing experiment
              will return the existing one un-modified. But if `ensure_new` is true,
              registration will generate a new experiment with a unique name in case of a
              conflict.

          metadata: User-controlled metadata about the experiment

          name: Name of the experiment. Within a project, experiment names are unique

          public: Whether or not the experiment is public. Public experiments can be viewed by
              anybody inside or outside the organization

          repo_info: Metadata about the state of the repo when the experiment was created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/experiment",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
                    "ensure_new": ensure_new,
                    "metadata": metadata,
                    "name": name,
                    "public": public,
                    "repo_info": repo_info,
                },
                experiment_create_params.ExperimentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    def retrieve(
        self,
        experiment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """
        Get an experiment object by its id

        Args:
          experiment_id: Experiment id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._get(
            f"/v1/experiment/{experiment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    def update(
        self,
        experiment_id: str,
        *,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """Partially update an experiment object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          experiment_id: Experiment id

          base_exp_id: Id of default base experiment to compare against when viewing this experiment

          dataset_id: Identifier of the linked dataset, or null if the experiment is not linked to a
              dataset

          dataset_version: Version number of the linked dataset the experiment was run against. This can be
              used to reproduce the experiment after the dataset has been modified.

          description: Textual description of the experiment

          metadata: User-controlled metadata about the experiment

          name: Name of the experiment. Within a project, experiment names are unique

          public: Whether or not the experiment is public. Public experiments can be viewed by
              anybody inside or outside the organization

          repo_info: Metadata about the state of the repo when the experiment was created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._patch(
            f"/v1/experiment/{experiment_id}",
            body=maybe_transform(
                {
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                    "public": public,
                    "repo_info": repo_info,
                },
                experiment_update_params.ExperimentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[Experiment]:
        """List out all experiments.

        The experiments are sorted by creation date, with the
        most recently-created experiments coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          experiment_name: Name of the experiment to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_id: Project id

          project_name: Name of the project to search for

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/experiment",
            page=SyncListObjects[Experiment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "experiment_name": experiment_name,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_id": project_id,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    experiment_list_params.ExperimentListParams,
                ),
            ),
            model=Experiment,
        )

    def delete(
        self,
        experiment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """
        Delete an experiment object by its id

        Args:
          experiment_id: Experiment id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._delete(
            f"/v1/experiment/{experiment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    def feedback(
        self,
        experiment_id: str,
        *,
        feedback: Iterable[FeedbackExperimentItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of experiment events

        Args:
          experiment_id: Experiment id

          feedback: A list of experiment feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._post(
            f"/v1/experiment/{experiment_id}/feedback",
            body=maybe_transform({"feedback": feedback}, experiment_feedback_params.ExperimentFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    def fetch(
        self,
        experiment_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FetchExperimentEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          experiment_id: Experiment id

          limit: limit the number of traces fetched

              Fetch queries may be paginated if the total result size is expected to be large
              (e.g. project_logs which accumulate over a long time). Note that fetch queries
              only support pagination in descending time order (from latest to earliest
              `_xact_id`. Furthermore, later pages may return rows which showed up in earlier
              pages, except with an earlier `_xact_id`. This happens because pagination occurs
              over the whole version history of the event log. You will most likely want to
              exclude any such duplicate, outdated rows (by `id`) from your combined result
              set.

              The `limit` parameter controls the number of full traces to return. So you may
              end up with more individual rows than the specified limit if you are fetching
              events containing traces.

          max_root_span_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          max_xact_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._get(
            f"/v1/experiment/{experiment_id}/fetch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "max_root_span_id": max_root_span_id,
                        "max_xact_id": max_xact_id,
                        "version": version,
                    },
                    experiment_fetch_params.ExperimentFetchParams,
                ),
            ),
            cast_to=FetchExperimentEventsResponse,
        )

    def fetch_post(
        self,
        experiment_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_xact_id: Optional[str] | NotGiven = NOT_GIVEN,
        version: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FetchExperimentEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          experiment_id: Experiment id

          cursor: An opaque string to be used as a cursor for the next page of results, in order
              from latest to earliest.

              The string can be obtained directly from the `cursor` property of the previous
              fetch query

          limit: limit the number of traces fetched

              Fetch queries may be paginated if the total result size is expected to be large
              (e.g. project_logs which accumulate over a long time). Note that fetch queries
              only support pagination in descending time order (from latest to earliest
              `_xact_id`. Furthermore, later pages may return rows which showed up in earlier
              pages, except with an earlier `_xact_id`. This happens because pagination occurs
              over the whole version history of the event log. You will most likely want to
              exclude any such duplicate, outdated rows (by `id`) from your combined result
              set.

              The `limit` parameter controls the number of full traces to return. So you may
              end up with more individual rows than the specified limit if you are fetching
              events containing traces.

          max_root_span_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          max_xact_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._post(
            f"/v1/experiment/{experiment_id}/fetch",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                experiment_fetch_post_params.ExperimentFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchExperimentEventsResponse,
        )

    def insert(
        self,
        experiment_id: str,
        *,
        events: Iterable[InsertExperimentEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the experiment

        Args:
          experiment_id: Experiment id

          events: A list of experiment events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._post(
            f"/v1/experiment/{experiment_id}/insert",
            body=maybe_transform({"events": events}, experiment_insert_params.ExperimentInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsertEventsResponse,
        )

    def summarize(
        self,
        experiment_id: str,
        *,
        comparison_experiment_id: str | NotGiven = NOT_GIVEN,
        summarize_scores: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeExperimentResponse:
        """
        Summarize experiment

        Args:
          experiment_id: Experiment id

          comparison_experiment_id: The experiment to compare against, if summarizing scores and metrics. If
              omitted, will fall back to the `base_exp_id` stored in the experiment metadata,
              and then to the most recent experiment run in the same project. Must pass
              `summarize_scores=true` for this id to be used

          summarize_scores: Whether to summarize the scores and metrics. If false (or omitted), only the
              metadata will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return self._get(
            f"/v1/experiment/{experiment_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comparison_experiment_id": comparison_experiment_id,
                        "summarize_scores": summarize_scores,
                    },
                    experiment_summarize_params.ExperimentSummarizeParams,
                ),
            ),
            cast_to=SummarizeExperimentResponse,
        )


class AsyncExperimentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperimentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncExperimentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ensure_new: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """Create a new experiment.

        If there is an existing experiment in the project with
        the same name as the one specified in the request, will return the existing
        experiment unmodified

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

          base_exp_id: Id of default base experiment to compare against when viewing this experiment

          dataset_id: Identifier of the linked dataset, or null if the experiment is not linked to a
              dataset

          dataset_version: Version number of the linked dataset the experiment was run against. This can be
              used to reproduce the experiment after the dataset has been modified.

          description: Textual description of the experiment

          ensure_new: Normally, creating an experiment with the same name as an existing experiment
              will return the existing one un-modified. But if `ensure_new` is true,
              registration will generate a new experiment with a unique name in case of a
              conflict.

          metadata: User-controlled metadata about the experiment

          name: Name of the experiment. Within a project, experiment names are unique

          public: Whether or not the experiment is public. Public experiments can be viewed by
              anybody inside or outside the organization

          repo_info: Metadata about the state of the repo when the experiment was created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/experiment",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
                    "ensure_new": ensure_new,
                    "metadata": metadata,
                    "name": name,
                    "public": public,
                    "repo_info": repo_info,
                },
                experiment_create_params.ExperimentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    async def retrieve(
        self,
        experiment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """
        Get an experiment object by its id

        Args:
          experiment_id: Experiment id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._get(
            f"/v1/experiment/{experiment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    async def update(
        self,
        experiment_id: str,
        *,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[RepoInfo] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """Partially update an experiment object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          experiment_id: Experiment id

          base_exp_id: Id of default base experiment to compare against when viewing this experiment

          dataset_id: Identifier of the linked dataset, or null if the experiment is not linked to a
              dataset

          dataset_version: Version number of the linked dataset the experiment was run against. This can be
              used to reproduce the experiment after the dataset has been modified.

          description: Textual description of the experiment

          metadata: User-controlled metadata about the experiment

          name: Name of the experiment. Within a project, experiment names are unique

          public: Whether or not the experiment is public. Public experiments can be viewed by
              anybody inside or outside the organization

          repo_info: Metadata about the state of the repo when the experiment was created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._patch(
            f"/v1/experiment/{experiment_id}",
            body=await async_maybe_transform(
                {
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                    "public": public,
                    "repo_info": repo_info,
                },
                experiment_update_params.ExperimentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        experiment_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Experiment, AsyncListObjects[Experiment]]:
        """List out all experiments.

        The experiments are sorted by creation date, with the
        most recently-created experiments coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          experiment_name: Name of the experiment to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_id: Project id

          project_name: Name of the project to search for

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/experiment",
            page=AsyncListObjects[Experiment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "experiment_name": experiment_name,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_id": project_id,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    experiment_list_params.ExperimentListParams,
                ),
            ),
            model=Experiment,
        )

    async def delete(
        self,
        experiment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Experiment:
        """
        Delete an experiment object by its id

        Args:
          experiment_id: Experiment id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._delete(
            f"/v1/experiment/{experiment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
        )

    async def feedback(
        self,
        experiment_id: str,
        *,
        feedback: Iterable[FeedbackExperimentItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of experiment events

        Args:
          experiment_id: Experiment id

          feedback: A list of experiment feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._post(
            f"/v1/experiment/{experiment_id}/feedback",
            body=await async_maybe_transform(
                {"feedback": feedback}, experiment_feedback_params.ExperimentFeedbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    async def fetch(
        self,
        experiment_id: str,
        *,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FetchExperimentEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          experiment_id: Experiment id

          limit: limit the number of traces fetched

              Fetch queries may be paginated if the total result size is expected to be large
              (e.g. project_logs which accumulate over a long time). Note that fetch queries
              only support pagination in descending time order (from latest to earliest
              `_xact_id`. Furthermore, later pages may return rows which showed up in earlier
              pages, except with an earlier `_xact_id`. This happens because pagination occurs
              over the whole version history of the event log. You will most likely want to
              exclude any such duplicate, outdated rows (by `id`) from your combined result
              set.

              The `limit` parameter controls the number of full traces to return. So you may
              end up with more individual rows than the specified limit if you are fetching
              events containing traces.

          max_root_span_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          max_xact_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._get(
            f"/v1/experiment/{experiment_id}/fetch",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "max_root_span_id": max_root_span_id,
                        "max_xact_id": max_xact_id,
                        "version": version,
                    },
                    experiment_fetch_params.ExperimentFetchParams,
                ),
            ),
            cast_to=FetchExperimentEventsResponse,
        )

    async def fetch_post(
        self,
        experiment_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_xact_id: Optional[str] | NotGiven = NOT_GIVEN,
        version: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FetchExperimentEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          experiment_id: Experiment id

          cursor: An opaque string to be used as a cursor for the next page of results, in order
              from latest to earliest.

              The string can be obtained directly from the `cursor` property of the previous
              fetch query

          limit: limit the number of traces fetched

              Fetch queries may be paginated if the total result size is expected to be large
              (e.g. project_logs which accumulate over a long time). Note that fetch queries
              only support pagination in descending time order (from latest to earliest
              `_xact_id`. Furthermore, later pages may return rows which showed up in earlier
              pages, except with an earlier `_xact_id`. This happens because pagination occurs
              over the whole version history of the event log. You will most likely want to
              exclude any such duplicate, outdated rows (by `id`) from your combined result
              set.

              The `limit` parameter controls the number of full traces to return. So you may
              end up with more individual rows than the specified limit if you are fetching
              events containing traces.

          max_root_span_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          max_xact_id: DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in
              favor of the explicit 'cursor' returned by object fetch requests. Please prefer
              the 'cursor' argument going forwards.

              Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

              Since a paginated fetch query returns results in order from latest to earliest,
              the cursor for the next page can be found as the row with the minimum (earliest)
              value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit`
              for an overview of paginating fetch queries.

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._post(
            f"/v1/experiment/{experiment_id}/fetch",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                experiment_fetch_post_params.ExperimentFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchExperimentEventsResponse,
        )

    async def insert(
        self,
        experiment_id: str,
        *,
        events: Iterable[InsertExperimentEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the experiment

        Args:
          experiment_id: Experiment id

          events: A list of experiment events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._post(
            f"/v1/experiment/{experiment_id}/insert",
            body=await async_maybe_transform({"events": events}, experiment_insert_params.ExperimentInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsertEventsResponse,
        )

    async def summarize(
        self,
        experiment_id: str,
        *,
        comparison_experiment_id: str | NotGiven = NOT_GIVEN,
        summarize_scores: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeExperimentResponse:
        """
        Summarize experiment

        Args:
          experiment_id: Experiment id

          comparison_experiment_id: The experiment to compare against, if summarizing scores and metrics. If
              omitted, will fall back to the `base_exp_id` stored in the experiment metadata,
              and then to the most recent experiment run in the same project. Must pass
              `summarize_scores=true` for this id to be used

          summarize_scores: Whether to summarize the scores and metrics. If false (or omitted), only the
              metadata will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not experiment_id:
            raise ValueError(f"Expected a non-empty value for `experiment_id` but received {experiment_id!r}")
        return await self._get(
            f"/v1/experiment/{experiment_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "comparison_experiment_id": comparison_experiment_id,
                        "summarize_scores": summarize_scores,
                    },
                    experiment_summarize_params.ExperimentSummarizeParams,
                ),
            ),
            cast_to=SummarizeExperimentResponse,
        )


class ExperimentsResourceWithRawResponse:
    def __init__(self, experiments: ExperimentsResource) -> None:
        self._experiments = experiments

        self.create = to_raw_response_wrapper(
            experiments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            experiments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            experiments.update,
        )
        self.list = to_raw_response_wrapper(
            experiments.list,
        )
        self.delete = to_raw_response_wrapper(
            experiments.delete,
        )
        self.feedback = to_raw_response_wrapper(
            experiments.feedback,
        )
        self.fetch = to_raw_response_wrapper(
            experiments.fetch,
        )
        self.fetch_post = to_raw_response_wrapper(
            experiments.fetch_post,
        )
        self.insert = to_raw_response_wrapper(
            experiments.insert,
        )
        self.summarize = to_raw_response_wrapper(
            experiments.summarize,
        )


class AsyncExperimentsResourceWithRawResponse:
    def __init__(self, experiments: AsyncExperimentsResource) -> None:
        self._experiments = experiments

        self.create = async_to_raw_response_wrapper(
            experiments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            experiments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            experiments.update,
        )
        self.list = async_to_raw_response_wrapper(
            experiments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            experiments.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            experiments.feedback,
        )
        self.fetch = async_to_raw_response_wrapper(
            experiments.fetch,
        )
        self.fetch_post = async_to_raw_response_wrapper(
            experiments.fetch_post,
        )
        self.insert = async_to_raw_response_wrapper(
            experiments.insert,
        )
        self.summarize = async_to_raw_response_wrapper(
            experiments.summarize,
        )


class ExperimentsResourceWithStreamingResponse:
    def __init__(self, experiments: ExperimentsResource) -> None:
        self._experiments = experiments

        self.create = to_streamed_response_wrapper(
            experiments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            experiments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            experiments.update,
        )
        self.list = to_streamed_response_wrapper(
            experiments.list,
        )
        self.delete = to_streamed_response_wrapper(
            experiments.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            experiments.feedback,
        )
        self.fetch = to_streamed_response_wrapper(
            experiments.fetch,
        )
        self.fetch_post = to_streamed_response_wrapper(
            experiments.fetch_post,
        )
        self.insert = to_streamed_response_wrapper(
            experiments.insert,
        )
        self.summarize = to_streamed_response_wrapper(
            experiments.summarize,
        )


class AsyncExperimentsResourceWithStreamingResponse:
    def __init__(self, experiments: AsyncExperimentsResource) -> None:
        self._experiments = experiments

        self.create = async_to_streamed_response_wrapper(
            experiments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            experiments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            experiments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            experiments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            experiments.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            experiments.feedback,
        )
        self.fetch = async_to_streamed_response_wrapper(
            experiments.fetch,
        )
        self.fetch_post = async_to_streamed_response_wrapper(
            experiments.fetch_post,
        )
        self.insert = async_to_streamed_response_wrapper(
            experiments.insert,
        )
        self.summarize = async_to_streamed_response_wrapper(
            experiments.summarize,
        )
