# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import log_fetch_params, log_insert_params, log_feedback_params, log_fetch_post_params
from ...types.shared.insert_events_response import InsertEventsResponse
from ...types.shared.feedback_response_schema import FeedbackResponseSchema
from ...types.shared_params.insert_project_logs_event import InsertProjectLogsEvent
from ...types.shared_params.feedback_project_logs_item import FeedbackProjectLogsItem
from ...types.shared.fetch_project_logs_events_response import FetchProjectLogsEventsResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def feedback(
        self,
        project_id: str,
        *,
        feedback: Iterable[FeedbackProjectLogsItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
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
        return self._post(
            f"/v1/project_logs/{project_id}/feedback",
            body=maybe_transform({"feedback": feedback}, log_feedback_params.LogFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    def fetch(
        self,
        project_id: str,
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
    ) -> FetchProjectLogsEventsResponse:
        """Fetch the events in a project logs.

        Equivalent to the POST form of the same
        path, but with the parameters in the URL query rather than in the request body.
        For more complex queries, use the `POST /btql` endpoint.

        Args:
          project_id: Project id

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
            cast_to=FetchProjectLogsEventsResponse,
        )

    def fetch_post(
        self,
        project_id: str,
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
    ) -> FetchProjectLogsEventsResponse:
        """Fetch the events in a project logs.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          project_id: Project id

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/v1/project_logs/{project_id}/fetch",
            body=maybe_transform(
                {
                    "cursor": cursor,
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
            cast_to=FetchProjectLogsEventsResponse,
        )

    def insert(
        self,
        project_id: str,
        *,
        events: Iterable[InsertProjectLogsEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
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
            cast_to=InsertEventsResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def feedback(
        self,
        project_id: str,
        *,
        feedback: Iterable[FeedbackProjectLogsItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
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
        return await self._post(
            f"/v1/project_logs/{project_id}/feedback",
            body=await async_maybe_transform({"feedback": feedback}, log_feedback_params.LogFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    async def fetch(
        self,
        project_id: str,
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
    ) -> FetchProjectLogsEventsResponse:
        """Fetch the events in a project logs.

        Equivalent to the POST form of the same
        path, but with the parameters in the URL query rather than in the request body.
        For more complex queries, use the `POST /btql` endpoint.

        Args:
          project_id: Project id

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v1/project_logs/{project_id}/fetch",
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
                    log_fetch_params.LogFetchParams,
                ),
            ),
            cast_to=FetchProjectLogsEventsResponse,
        )

    async def fetch_post(
        self,
        project_id: str,
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
    ) -> FetchProjectLogsEventsResponse:
        """Fetch the events in a project logs.

        Equivalent to the GET form of the same path,
        but with the parameters in the request body rather than in the URL query. For
        more complex queries, use the `POST /btql` endpoint.

        Args:
          project_id: Project id

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
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/v1/project_logs/{project_id}/fetch",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
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
            cast_to=FetchProjectLogsEventsResponse,
        )

    async def insert(
        self,
        project_id: str,
        *,
        events: Iterable[InsertProjectLogsEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
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
            body=await async_maybe_transform({"events": events}, log_insert_params.LogInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsertEventsResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
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


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
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


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
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


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
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
