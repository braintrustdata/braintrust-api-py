# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import (
    Experiment,
    ExperimentInsertResponse,
    ExperimentFetchEventsResponse,
    experiment_create_params,
    experiment_insert_params,
    experiment_update_params,
    experiment_feedback_params,
    experiment_fetch_events_params,
    experiment_update_partial_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
        the same name as the one specified in the request, will create a new experiment
        from `name`, suffixed with a unique identifier

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

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
        return self._post(
            "/v1/experiment",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
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
        *,
        project_id: str,
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
        """Create or replace a new experiment.

        If there is an existing experiment in the
        project with the same name as the one specified in the request, will replace the
        existing experiment with the provided fields

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

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
        return self._put(
            "/v1/experiment",
            body=maybe_transform(
                {
                    "project_id": project_id,
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
        feedback: List[experiment_feedback_params.Feedback],
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

    def fetch_events(
        self,
        experiment_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: int | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentFetchEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body

        Args:
          experiment_id: Experiment id

          limit: Fetch queries may be paginated if the total result size is expected to be large
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

          max_root_span_id: Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
              event fetches. Given a previous fetch with a list of rows, you can determine
              `max_root_span_id` as the maximum of the `root_span_id` field over all rows. See
              the documentation for `limit` for an overview of paginating fetch queries.

          max_xact_id: Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
              event fetches. Given a previous fetch with a list of rows, you can determine
              `max_xact_id` as the maximum of the `_xact_id` field over all rows. See the
              documentation for `limit` for an overview of paginating fetch queries.

          version: You may specify a version id to retrieve a snapshot of the events from a past
              time. The version id is essentially a filter on the latest event transaction id.
              You can use the `max_xact_id` returned by a past fetch as the version to
              reproduce that exact fetch.

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
                    experiment_fetch_events_params.ExperimentFetchEventsParams,
                ),
            ),
            cast_to=ExperimentFetchEventsResponse,
        )

    def insert(
        self,
        experiment_id: str,
        *,
        events: List[experiment_insert_params.Event],
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

    def update_partial(
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
        repo_info: Optional[experiment_update_partial_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        Currently we do not support removing fields or setting them to null. As a
        workaround, you may retrieve the full object with `GET /experiment/{id}` and
        then replace it with `PUT /experiment`.

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
                experiment_update_partial_params.ExperimentUpdatePartialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
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
        the same name as the one specified in the request, will create a new experiment
        from `name`, suffixed with a unique identifier

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

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
        return await self._post(
            "/v1/experiment",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "base_exp_id": base_exp_id,
                    "dataset_id": dataset_id,
                    "dataset_version": dataset_version,
                    "description": description,
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
        *,
        project_id: str,
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
        """Create or replace a new experiment.

        If there is an existing experiment in the
        project with the same name as the one specified in the request, will replace the
        existing experiment with the provided fields

        Args:
          project_id: Unique identifier for the project that the experiment belongs under

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
        return await self._put(
            "/v1/experiment",
            body=maybe_transform(
                {
                    "project_id": project_id,
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
        feedback: List[experiment_feedback_params.Feedback],
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
            body=maybe_transform({"feedback": feedback}, experiment_feedback_params.ExperimentFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fetch_events(
        self,
        experiment_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_root_span_id: str | NotGiven = NOT_GIVEN,
        max_xact_id: int | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentFetchEventsResponse:
        """Fetch the events in an experiment.

        Equivalent to the POST form of the same path,
        but with the parameters in the URL query rather than in the request body

        Args:
          experiment_id: Experiment id

          limit: Fetch queries may be paginated if the total result size is expected to be large
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

          max_root_span_id: Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
              event fetches. Given a previous fetch with a list of rows, you can determine
              `max_root_span_id` as the maximum of the `root_span_id` field over all rows. See
              the documentation for `limit` for an overview of paginating fetch queries.

          max_xact_id: Together, `max_xact_id` and `max_root_span_id` form a cursor for paginating
              event fetches. Given a previous fetch with a list of rows, you can determine
              `max_xact_id` as the maximum of the `_xact_id` field over all rows. See the
              documentation for `limit` for an overview of paginating fetch queries.

          version: You may specify a version id to retrieve a snapshot of the events from a past
              time. The version id is essentially a filter on the latest event transaction id.
              You can use the `max_xact_id` returned by a past fetch as the version to
              reproduce that exact fetch.

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
                query=maybe_transform(
                    {
                        "limit": limit,
                        "max_root_span_id": max_root_span_id,
                        "max_xact_id": max_xact_id,
                        "version": version,
                    },
                    experiment_fetch_events_params.ExperimentFetchEventsParams,
                ),
            ),
            cast_to=ExperimentFetchEventsResponse,
        )

    async def insert(
        self,
        experiment_id: str,
        *,
        events: List[experiment_insert_params.Event],
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
            body=maybe_transform({"events": events}, experiment_insert_params.ExperimentInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExperimentInsertResponse,
        )

    async def update_partial(
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
        repo_info: Optional[experiment_update_partial_params.RepoInfo] | NotGiven = NOT_GIVEN,
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
        Currently we do not support removing fields or setting them to null. As a
        workaround, you may retrieve the full object with `GET /experiment/{id}` and
        then replace it with `PUT /experiment`.

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
                experiment_update_partial_params.ExperimentUpdatePartialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Experiment,
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
        self.delete = to_raw_response_wrapper(
            experiment.delete,
        )
        self.feedback = to_raw_response_wrapper(
            experiment.feedback,
        )
        self.fetch_events = to_raw_response_wrapper(
            experiment.fetch_events,
        )
        self.insert = to_raw_response_wrapper(
            experiment.insert,
        )
        self.update_partial = to_raw_response_wrapper(
            experiment.update_partial,
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
        self.delete = async_to_raw_response_wrapper(
            experiment.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            experiment.feedback,
        )
        self.fetch_events = async_to_raw_response_wrapper(
            experiment.fetch_events,
        )
        self.insert = async_to_raw_response_wrapper(
            experiment.insert,
        )
        self.update_partial = async_to_raw_response_wrapper(
            experiment.update_partial,
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
        self.delete = to_streamed_response_wrapper(
            experiment.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            experiment.feedback,
        )
        self.fetch_events = to_streamed_response_wrapper(
            experiment.fetch_events,
        )
        self.insert = to_streamed_response_wrapper(
            experiment.insert,
        )
        self.update_partial = to_streamed_response_wrapper(
            experiment.update_partial,
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
        self.delete = async_to_streamed_response_wrapper(
            experiment.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            experiment.feedback,
        )
        self.fetch_events = async_to_streamed_response_wrapper(
            experiment.fetch_events,
        )
        self.insert = async_to_streamed_response_wrapper(
            experiment.insert,
        )
        self.update_partial = async_to_streamed_response_wrapper(
            experiment.update_partial,
        )
