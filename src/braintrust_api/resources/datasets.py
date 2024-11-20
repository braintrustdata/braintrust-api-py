# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import (
    dataset_list_params,
    dataset_fetch_params,
    dataset_create_params,
    dataset_insert_params,
    dataset_update_params,
    dataset_feedback_params,
    dataset_summarize_params,
    dataset_fetch_post_params,
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
from ..types.shared.dataset import Dataset
from ..types.shared.insert_events_response import InsertEventsResponse
from ..types.shared.feedback_response_schema import FeedbackResponseSchema
from ..types.shared.summarize_dataset_response import SummarizeDatasetResponse
from ..types.shared_params.insert_dataset_event import InsertDatasetEvent
from ..types.shared_params.feedback_dataset_item import FeedbackDatasetItem
from ..types.shared.fetch_dataset_events_response import FetchDatasetEventsResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Create a new dataset.

        If there is an existing dataset in the project with the
        same name as the one specified in the request, will return the existing dataset
        unmodified

        Args:
          name: Name of the dataset. Within a project, dataset names are unique

          project_id: Unique identifier for the project that the dataset belongs under

          description: Textual description of the dataset

          metadata: User-controlled metadata about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/dataset",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                    "metadata": metadata,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """
        Get a dataset object by its id

        Args:
          dataset_id: Dataset id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Partially update a dataset object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          dataset_id: Dataset id

          description: Textual description of the dataset

          metadata: User-controlled metadata about the dataset

          name: Name of the dataset. Within a project, dataset names are unique

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._patch(
            f"/v1/dataset/{dataset_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def list(
        self,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncListObjects[Dataset]:
        """List out all datasets.

        The datasets are sorted by creation date, with the most
        recently-created datasets coming first

        Args:
          dataset_name: Name of the dataset to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

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
            "/v1/dataset",
            page=SyncListObjects[Dataset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_id": project_id,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    dataset_list_params.DatasetListParams,
                ),
            ),
            model=Dataset,
        )

    def delete(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """
        Delete a dataset object by its id

        Args:
          dataset_id: Dataset id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._delete(
            f"/v1/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def feedback(
        self,
        dataset_id: str,
        *,
        feedback: Iterable[FeedbackDatasetItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of dataset events

        Args:
          dataset_id: Dataset id

          feedback: A list of dataset feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/v1/dataset/{dataset_id}/feedback",
            body=maybe_transform({"feedback": feedback}, dataset_feedback_params.DatasetFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    def fetch(
        self,
        dataset_id: str,
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
    ) -> FetchDatasetEventsResponse:
        """Fetch the events in a dataset.

        Equivalent to the POST form of the same path, but
        with the parameters in the URL query rather than in the request body. For more
        complex queries, use the `POST /btql` endpoint.

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1/dataset/{dataset_id}/fetch",
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
                    dataset_fetch_params.DatasetFetchParams,
                ),
            ),
            cast_to=FetchDatasetEventsResponse,
        )

    def fetch_post(
        self,
        dataset_id: str,
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
    ) -> FetchDatasetEventsResponse:
        """Fetch the events in a dataset.

        Equivalent to the GET form of the same path, but
        with the parameters in the request body rather than in the URL query. For more
        complex queries, use the `POST /btql` endpoint.

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/v1/dataset/{dataset_id}/fetch",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                dataset_fetch_post_params.DatasetFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchDatasetEventsResponse,
        )

    def insert(
        self,
        dataset_id: str,
        *,
        events: Iterable[InsertDatasetEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the dataset

        Args:
          dataset_id: Dataset id

          events: A list of dataset events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/v1/dataset/{dataset_id}/insert",
            body=maybe_transform({"events": events}, dataset_insert_params.DatasetInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsertEventsResponse,
        )

    def summarize(
        self,
        dataset_id: str,
        *,
        summarize_data: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeDatasetResponse:
        """
        Summarize dataset

        Args:
          dataset_id: Dataset id

          summarize_data: Whether to summarize the data. If false (or omitted), only the metadata will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/v1/dataset/{dataset_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"summarize_data": summarize_data}, dataset_summarize_params.DatasetSummarizeParams
                ),
            ),
            cast_to=SummarizeDatasetResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Create a new dataset.

        If there is an existing dataset in the project with the
        same name as the one specified in the request, will return the existing dataset
        unmodified

        Args:
          name: Name of the dataset. Within a project, dataset names are unique

          project_id: Unique identifier for the project that the dataset belongs under

          description: Textual description of the dataset

          metadata: User-controlled metadata about the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/dataset",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "description": description,
                    "metadata": metadata,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    async def retrieve(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """
        Get a dataset object by its id

        Args:
          dataset_id: Dataset id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    async def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Partially update a dataset object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          dataset_id: Dataset id

          description: Textual description of the dataset

          metadata: User-controlled metadata about the dataset

          name: Name of the dataset. Within a project, dataset names are unique

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._patch(
            f"/v1/dataset/{dataset_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    def list(
        self,
        *,
        dataset_name: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[Dataset, AsyncListObjects[Dataset]]:
        """List out all datasets.

        The datasets are sorted by creation date, with the most
        recently-created datasets coming first

        Args:
          dataset_name: Name of the dataset to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

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
            "/v1/dataset",
            page=AsyncListObjects[Dataset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_name": dataset_name,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_id": project_id,
                        "project_name": project_name,
                        "starting_after": starting_after,
                    },
                    dataset_list_params.DatasetListParams,
                ),
            ),
            model=Dataset,
        )

    async def delete(
        self,
        dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """
        Delete a dataset object by its id

        Args:
          dataset_id: Dataset id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._delete(
            f"/v1/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )

    async def feedback(
        self,
        dataset_id: str,
        *,
        feedback: Iterable[FeedbackDatasetItem],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackResponseSchema:
        """
        Log feedback for a set of dataset events

        Args:
          dataset_id: Dataset id

          feedback: A list of dataset feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/v1/dataset/{dataset_id}/feedback",
            body=await async_maybe_transform({"feedback": feedback}, dataset_feedback_params.DatasetFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackResponseSchema,
        )

    async def fetch(
        self,
        dataset_id: str,
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
    ) -> FetchDatasetEventsResponse:
        """Fetch the events in a dataset.

        Equivalent to the POST form of the same path, but
        with the parameters in the URL query rather than in the request body. For more
        complex queries, use the `POST /btql` endpoint.

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1/dataset/{dataset_id}/fetch",
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
                    dataset_fetch_params.DatasetFetchParams,
                ),
            ),
            cast_to=FetchDatasetEventsResponse,
        )

    async def fetch_post(
        self,
        dataset_id: str,
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
    ) -> FetchDatasetEventsResponse:
        """Fetch the events in a dataset.

        Equivalent to the GET form of the same path, but
        with the parameters in the request body rather than in the URL query. For more
        complex queries, use the `POST /btql` endpoint.

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/v1/dataset/{dataset_id}/fetch",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                    "max_root_span_id": max_root_span_id,
                    "max_xact_id": max_xact_id,
                    "version": version,
                },
                dataset_fetch_post_params.DatasetFetchPostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FetchDatasetEventsResponse,
        )

    async def insert(
        self,
        dataset_id: str,
        *,
        events: Iterable[InsertDatasetEvent],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsertEventsResponse:
        """
        Insert a set of events into the dataset

        Args:
          dataset_id: Dataset id

          events: A list of dataset events to insert

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/v1/dataset/{dataset_id}/insert",
            body=await async_maybe_transform({"events": events}, dataset_insert_params.DatasetInsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InsertEventsResponse,
        )

    async def summarize(
        self,
        dataset_id: str,
        *,
        summarize_data: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizeDatasetResponse:
        """
        Summarize dataset

        Args:
          dataset_id: Dataset id

          summarize_data: Whether to summarize the data. If false (or omitted), only the metadata will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/v1/dataset/{dataset_id}/summarize",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"summarize_data": summarize_data}, dataset_summarize_params.DatasetSummarizeParams
                ),
            ),
            cast_to=SummarizeDatasetResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            datasets.update,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )
        self.feedback = to_raw_response_wrapper(
            datasets.feedback,
        )
        self.fetch = to_raw_response_wrapper(
            datasets.fetch,
        )
        self.fetch_post = to_raw_response_wrapper(
            datasets.fetch_post,
        )
        self.insert = to_raw_response_wrapper(
            datasets.insert,
        )
        self.summarize = to_raw_response_wrapper(
            datasets.summarize,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            datasets.feedback,
        )
        self.fetch = async_to_raw_response_wrapper(
            datasets.fetch,
        )
        self.fetch_post = async_to_raw_response_wrapper(
            datasets.fetch_post,
        )
        self.insert = async_to_raw_response_wrapper(
            datasets.insert,
        )
        self.summarize = async_to_raw_response_wrapper(
            datasets.summarize,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            datasets.feedback,
        )
        self.fetch = to_streamed_response_wrapper(
            datasets.fetch,
        )
        self.fetch_post = to_streamed_response_wrapper(
            datasets.fetch_post,
        )
        self.insert = to_streamed_response_wrapper(
            datasets.insert,
        )
        self.summarize = to_streamed_response_wrapper(
            datasets.summarize,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            datasets.feedback,
        )
        self.fetch = async_to_streamed_response_wrapper(
            datasets.fetch,
        )
        self.fetch_post = async_to_streamed_response_wrapper(
            datasets.fetch_post,
        )
        self.insert = async_to_streamed_response_wrapper(
            datasets.insert,
        )
        self.summarize = async_to_streamed_response_wrapper(
            datasets.summarize,
        )
