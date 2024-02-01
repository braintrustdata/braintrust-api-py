# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.project import (
    LogFetchResponse,
    LogInsertResponse,
    LogFetchPostResponse,
    log_fetch_params,
    log_insert_params,
    log_feedback_params,
    log_fetch_post_params,
)

__all__ = ["Logs", "AsyncLogs"]


class Logs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self)

    def feedback(
        self,
        project_id: str,
        *,
        feedback: List[log_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of project logs events

        Args:
          project_id: Project id

          feedback: A list of project logs feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/project_logs/{project_id}/feedback",
            body=maybe_transform({"feedback": feedback}, log_feedback_params.LogFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def fetch(
        self,
        project_id: str,
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
    ) -> LogFetchResponse:
        """Fetch the events in a project logs.

        Equivalent to the POST form of the same
        path, but with the parameters in the URL query rather than in the request body

        Args:
          project_id: Project id

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/v1/project_logs/{project_id}/fetch",
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
                    log_fetch_params.LogFetchParams,
                ),
            ),
            cast_to=LogFetchResponse,
        )

    def fetch_post(
        self,
        project_id: str,
        *,
        filters: Optional[List[log_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_xact_id: Optional[int] | NotGiven = NOT_GIVEN,
        version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogFetchPostResponse:
        """Fetch the events in a project logs.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query

        Args:
          project_id: Project id

          filters: A list of filters on the events to fetch. Currently, only path-lookup type
              filters are supported, but we may add more in the future

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/v1/project_logs/{project_id}/fetch",
            body=maybe_transform(
                {
                    "filters": filters,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                log_fetch_post_params.LogFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogFetchPostResponse,
        )

    def insert(
        self,
        project_id: str,
        *,
        events: List[log_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogInsertResponse:
        """
        Insert a set of events into the project logs

        Args:
          project_id: Project id

          events: A list of project logs events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/v1/project_logs/{project_id}/insert",
            body=maybe_transform({"events": events}, log_insert_params.LogInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogInsertResponse,
        )


class AsyncLogs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self)

    async def feedback(
        self,
        project_id: str,
        *,
        feedback: List[log_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of project logs events

        Args:
          project_id: Project id

          feedback: A list of project logs feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/project_logs/{project_id}/feedback",
            body=maybe_transform({"feedback": feedback}, log_feedback_params.LogFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fetch(
        self,
        project_id: str,
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
    ) -> LogFetchResponse:
        """Fetch the events in a project logs.

        Equivalent to the POST form of the same
        path, but with the parameters in the URL query rather than in the request body

        Args:
          project_id: Project id

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v1/project_logs/{project_id}/fetch",
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
                    log_fetch_params.LogFetchParams,
                ),
            ),
            cast_to=LogFetchResponse,
        )

    async def fetch_post(
        self,
        project_id: str,
        *,
        filters: Optional[List[log_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        max_root_span_id: Optional[str] | NotGiven = NOT_GIVEN,
        max_xact_id: Optional[int] | NotGiven = NOT_GIVEN,
        version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogFetchPostResponse:
        """Fetch the events in a project logs.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query

        Args:
          project_id: Project id

          filters: A list of filters on the events to fetch. Currently, only path-lookup type
              filters are supported, but we may add more in the future

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/v1/project_logs/{project_id}/fetch",
            body=maybe_transform(
                {
                    "filters": filters,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                log_fetch_post_params.LogFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogFetchPostResponse,
        )

    async def insert(
        self,
        project_id: str,
        *,
        events: List[log_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogInsertResponse:
        """
        Insert a set of events into the project logs

        Args:
          project_id: Project id

          events: A list of project logs events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/v1/project_logs/{project_id}/insert",
            body=maybe_transform({"events": events}, log_insert_params.LogInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogInsertResponse,
        )


class LogsWithRawResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

        self.feedback = to_raw_response_wrapper(
            logs.feedback,
        )
        self.fetch = to_raw_response_wrapper(
            logs.fetch,
        )
        self.fetch_post = to_raw_response_wrapper(
            logs.fetch_post,
        )
        self.insert = to_raw_response_wrapper(
            logs.insert,
        )


class AsyncLogsWithRawResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

        self.feedback = async_to_raw_response_wrapper(
            logs.feedback,
        )
        self.fetch = async_to_raw_response_wrapper(
            logs.fetch,
        )
        self.fetch_post = async_to_raw_response_wrapper(
            logs.fetch_post,
        )
        self.insert = async_to_raw_response_wrapper(
            logs.insert,
        )


class LogsWithStreamingResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

        self.feedback = to_streamed_response_wrapper(
            logs.feedback,
        )
        self.fetch = to_streamed_response_wrapper(
            logs.fetch,
        )
        self.fetch_post = to_streamed_response_wrapper(
            logs.fetch_post,
        )
        self.insert = to_streamed_response_wrapper(
            logs.insert,
        )


class AsyncLogsWithStreamingResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

        self.feedback = async_to_streamed_response_wrapper(
            logs.feedback,
        )
        self.fetch = async_to_streamed_response_wrapper(
            logs.fetch,
        )
        self.fetch_post = async_to_streamed_response_wrapper(
            logs.fetch_post,
        )
        self.insert = async_to_streamed_response_wrapper(
            logs.insert,
        )