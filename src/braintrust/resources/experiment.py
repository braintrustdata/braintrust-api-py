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
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.experiment import Experiment
from ..types.experiment_fetch_response import ExperimentFetchResponse
from ..types.experiment_insert_response import ExperimentInsertResponse
from ..types.experiment_summarize_response import ExperimentSummarizeResponse
from ..types.experiment_fetch_post_response import ExperimentFetchPostResponse

__all__ = ["ExperimentResource", "AsyncExperimentResource"]


class ExperimentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperimentResourceWithRawResponse:
        return ExperimentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentResourceWithStreamingResponse:
        return ExperimentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ensure_new: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[experiment_create_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[experiment_update_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        feedback: Iterable[experiment_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/experiment/{experiment_id}/feedback",
            body=maybe_transform({"feedback": feedback}, experiment_feedback_params.ExperimentFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def fetch(
        self,
        experiment_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentFetchResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body

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
            cast_to=ExperimentFetchResponse,
        )

    def fetch_post(
        self,
        experiment_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        filters: Optional[Iterable[experiment_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
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
    ) -> ExperimentFetchPostResponse:
        """Fetch the events in an experiment.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query

        Args:
          experiment_id: Experiment id

          cursor: An opaque string to be used as a cursor for the next page of results, in order
              from latest to earliest.

              The string can be obtained directly from the `cursor` property of the previous
              fetch query

          filters: A list of filters on the events to fetch. Currently, only path-lookup type
              filters are supported, but we may add more in the future

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
                    "filters": filters,
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
            cast_to=ExperimentFetchPostResponse,
        )

    def insert(
        self,
        experiment_id: str,
        *,
        events: Iterable[experiment_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentInsertResponse:
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
            cast_to=ExperimentInsertResponse,
        )

    def summarize(
        self,
        experiment_id: str,
        *,
        comparison_experiment_id: str | NotGiven = NOT_GIVEN,
        summarize_scores: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentSummarizeResponse:
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
            cast_to=ExperimentSummarizeResponse,
        )


class AsyncExperimentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperimentResourceWithRawResponse:
        return AsyncExperimentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentResourceWithStreamingResponse:
        return AsyncExperimentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        base_exp_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_version: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ensure_new: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[experiment_create_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        public: Optional[bool] | NotGiven = NOT_GIVEN,
        repo_info: Optional[experiment_update_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        feedback: Iterable[experiment_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/experiment/{experiment_id}/feedback",
            body=await async_maybe_transform(
                {"feedback": feedback}, experiment_feedback_params.ExperimentFeedbackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fetch(
        self,
        experiment_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentFetchResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body

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
            cast_to=ExperimentFetchResponse,
        )

    async def fetch_post(
        self,
        experiment_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        filters: Optional[Iterable[experiment_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
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
    ) -> ExperimentFetchPostResponse:
        """Fetch the events in an experiment.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query

        Args:
          experiment_id: Experiment id

          cursor: An opaque string to be used as a cursor for the next page of results, in order
              from latest to earliest.

              The string can be obtained directly from the `cursor` property of the previous
              fetch query

          filters: A list of filters on the events to fetch. Currently, only path-lookup type
              filters are supported, but we may add more in the future

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
                    "filters": filters,
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
            cast_to=ExperimentFetchPostResponse,
        )

    async def insert(
        self,
        experiment_id: str,
        *,
        events: Iterable[experiment_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentInsertResponse:
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
            cast_to=ExperimentInsertResponse,
        )

    async def summarize(
        self,
        experiment_id: str,
        *,
        comparison_experiment_id: str | NotGiven = NOT_GIVEN,
        summarize_scores: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentSummarizeResponse:
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
            cast_to=ExperimentSummarizeResponse,
        )


class ExperimentResourceWithRawResponse:
    def __init__(self, experiment: ExperimentResource) -> None:
        self._experiment = experiment

        self.create = to_raw_response_wrapper(
            experiment.create,
        )
        self.retrieve = to_raw_response_wrapper(
            experiment.retrieve,
        )
        self.update = to_raw_response_wrapper(
            experiment.update,
        )
        self.list = to_raw_response_wrapper(
            experiment.list,
        )
        self.delete = to_raw_response_wrapper(
            experiment.delete,
        )
        self.feedback = to_raw_response_wrapper(
            experiment.feedback,
        )
        self.fetch = to_raw_response_wrapper(
            experiment.fetch,
        )
        self.fetch_post = to_raw_response_wrapper(
            experiment.fetch_post,
        )
        self.insert = to_raw_response_wrapper(
            experiment.insert,
        )
        self.summarize = to_raw_response_wrapper(
            experiment.summarize,
        )


class AsyncExperimentResourceWithRawResponse:
    def __init__(self, experiment: AsyncExperimentResource) -> None:
        self._experiment = experiment

        self.create = async_to_raw_response_wrapper(
            experiment.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            experiment.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            experiment.update,
        )
        self.list = async_to_raw_response_wrapper(
            experiment.list,
        )
        self.delete = async_to_raw_response_wrapper(
            experiment.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            experiment.feedback,
        )
        self.fetch = async_to_raw_response_wrapper(
            experiment.fetch,
        )
        self.fetch_post = async_to_raw_response_wrapper(
            experiment.fetch_post,
        )
        self.insert = async_to_raw_response_wrapper(
            experiment.insert,
        )
        self.summarize = async_to_raw_response_wrapper(
            experiment.summarize,
        )


class ExperimentResourceWithStreamingResponse:
    def __init__(self, experiment: ExperimentResource) -> None:
        self._experiment = experiment

        self.create = to_streamed_response_wrapper(
            experiment.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            experiment.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            experiment.update,
        )
        self.list = to_streamed_response_wrapper(
            experiment.list,
        )
        self.delete = to_streamed_response_wrapper(
            experiment.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            experiment.feedback,
        )
        self.fetch = to_streamed_response_wrapper(
            experiment.fetch,
        )
        self.fetch_post = to_streamed_response_wrapper(
            experiment.fetch_post,
        )
        self.insert = to_streamed_response_wrapper(
            experiment.insert,
        )
        self.summarize = to_streamed_response_wrapper(
            experiment.summarize,
        )


class AsyncExperimentResourceWithStreamingResponse:
    def __init__(self, experiment: AsyncExperimentResource) -> None:
        self._experiment = experiment

        self.create = async_to_streamed_response_wrapper(
            experiment.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            experiment.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            experiment.update,
        )
        self.list = async_to_streamed_response_wrapper(
            experiment.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            experiment.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            experiment.feedback,
        )
        self.fetch = async_to_streamed_response_wrapper(
            experiment.fetch,
        )
        self.fetch_post = async_to_streamed_response_wrapper(
            experiment.fetch_post,
        )
        self.insert = async_to_streamed_response_wrapper(
            experiment.insert,
        )
        self.summarize = async_to_streamed_response_wrapper(
            experiment.summarize,
        )
