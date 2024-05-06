# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    dataset_list_params,
    dataset_fetch_params,
    dataset_create_params,
    dataset_insert_params,
    dataset_update_params,
    dataset_replace_params,
    dataset_feedback_params,
    dataset_fetch_post_params,
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
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.dataset import Dataset
from ..types.dataset_fetch_response import DatasetFetchResponse
from ..types.dataset_insert_response import DatasetInsertResponse
from ..types.dataset_fetch_post_response import DatasetFetchPostResponse

__all__ = ["DatasetResource", "AsyncDatasetResource"]


class DatasetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetResourceWithRawResponse:
        return DatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetResourceWithStreamingResponse:
        return DatasetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
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

          description: Textual description of the dataset

          project_id: Unique identifier for the project that the dataset belongs under

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
                    "description": description,
                    "project_id": project_id,
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
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
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
        do not support removing fields or setting them to null. As a workaround, you may
        retrieve the full object with `GET /dataset/{id}` and then replace it with
        `PUT /dataset`.

        Args:
          dataset_id: Dataset id

          name: Name of the dataset. Within a project, dataset names are unique

          description: Textual description of the dataset

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
                    "name": name,
                    "description": description,
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
    ) -> SyncListObjects[Dataset]:
        """List out all datasets.

        The datasets are sorted by creation date, with the most
        recently-created datasets coming first

        Args:
          dataset_name: Name of the dataset to search for

          ending_before: A cursor for pagination. For example, if the initial item in the last page you
              fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page.
              Note: you may only pass one of `starting_after` and `ending_before`

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
                        "limit": limit,
                        "org_name": org_name,
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
        feedback: Iterable[dataset_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/dataset/{dataset_id}/feedback",
            body=maybe_transform({"feedback": feedback}, dataset_feedback_params.DatasetFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def fetch(
        self,
        dataset_id: str,
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
    ) -> DatasetFetchResponse:
        """Fetch the events in a dataset.

        Equivalent to the POST form of the same path, but
        with the parameters in the URL query rather than in the request body

        Args:
          dataset_id: Dataset id

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
            cast_to=DatasetFetchResponse,
        )

    def fetch_post(
        self,
        dataset_id: str,
        *,
        filters: Optional[Iterable[dataset_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
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
    ) -> DatasetFetchPostResponse:
        """Fetch the events in a dataset.

        Equivalent to the GET form of the same path, but
        with the parameters in the request body rather than in the URL query

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/v1/dataset/{dataset_id}/fetch",
            body=maybe_transform(
                {
                    "filters": filters,
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
            cast_to=DatasetFetchPostResponse,
        )

    def insert(
        self,
        dataset_id: str,
        *,
        events: Iterable[dataset_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetInsertResponse:
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
            cast_to=DatasetInsertResponse,
        )

    def replace(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Create or replace a new dataset.

        If there is an existing dataset in the project
        with the same name as the one specified in the request, will replace the
        existing dataset with the provided fields

        Args:
          name: Name of the dataset. Within a project, dataset names are unique

          description: Textual description of the dataset

          project_id: Unique identifier for the project that the dataset belongs under

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/dataset",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "project_id": project_id,
                },
                dataset_replace_params.DatasetReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )


class AsyncDatasetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetResourceWithRawResponse:
        return AsyncDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetResourceWithStreamingResponse:
        return AsyncDatasetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
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

          description: Textual description of the dataset

          project_id: Unique identifier for the project that the dataset belongs under

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
                    "description": description,
                    "project_id": project_id,
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
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
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
        do not support removing fields or setting them to null. As a workaround, you may
        retrieve the full object with `GET /dataset/{id}` and then replace it with
        `PUT /dataset`.

        Args:
          dataset_id: Dataset id

          name: Name of the dataset. Within a project, dataset names are unique

          description: Textual description of the dataset

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
                    "name": name,
                    "description": description,
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
    ) -> AsyncPaginator[Dataset, AsyncListObjects[Dataset]]:
        """List out all datasets.

        The datasets are sorted by creation date, with the most
        recently-created datasets coming first

        Args:
          dataset_name: Name of the dataset to search for

          ending_before: A cursor for pagination. For example, if the initial item in the last page you
              fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page.
              Note: you may only pass one of `starting_after` and `ending_before`

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
                        "limit": limit,
                        "org_name": org_name,
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
        feedback: Iterable[dataset_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/dataset/{dataset_id}/feedback",
            body=await async_maybe_transform({"feedback": feedback}, dataset_feedback_params.DatasetFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def fetch(
        self,
        dataset_id: str,
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
    ) -> DatasetFetchResponse:
        """Fetch the events in a dataset.

        Equivalent to the POST form of the same path, but
        with the parameters in the URL query rather than in the request body

        Args:
          dataset_id: Dataset id

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
            cast_to=DatasetFetchResponse,
        )

    async def fetch_post(
        self,
        dataset_id: str,
        *,
        filters: Optional[Iterable[dataset_fetch_post_params.Filter]] | NotGiven = NOT_GIVEN,
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
    ) -> DatasetFetchPostResponse:
        """Fetch the events in a dataset.

        Equivalent to the GET form of the same path, but
        with the parameters in the request body rather than in the URL query

        Args:
          dataset_id: Dataset id

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/v1/dataset/{dataset_id}/fetch",
            body=await async_maybe_transform(
                {
                    "filters": filters,
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
            cast_to=DatasetFetchPostResponse,
        )

    async def insert(
        self,
        dataset_id: str,
        *,
        events: Iterable[dataset_insert_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetInsertResponse:
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
            cast_to=DatasetInsertResponse,
        )

    async def replace(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Dataset:
        """Create or replace a new dataset.

        If there is an existing dataset in the project
        with the same name as the one specified in the request, will replace the
        existing dataset with the provided fields

        Args:
          name: Name of the dataset. Within a project, dataset names are unique

          description: Textual description of the dataset

          project_id: Unique identifier for the project that the dataset belongs under

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/dataset",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "project_id": project_id,
                },
                dataset_replace_params.DatasetReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dataset,
        )


class DatasetResourceWithRawResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_raw_response_wrapper(
            dataset.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dataset.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dataset.update,
        )
        self.list = to_raw_response_wrapper(
            dataset.list,
        )
        self.delete = to_raw_response_wrapper(
            dataset.delete,
        )
        self.feedback = to_raw_response_wrapper(
            dataset.feedback,
        )
        self.fetch = to_raw_response_wrapper(
            dataset.fetch,
        )
        self.fetch_post = to_raw_response_wrapper(
            dataset.fetch_post,
        )
        self.insert = to_raw_response_wrapper(
            dataset.insert,
        )
        self.replace = to_raw_response_wrapper(
            dataset.replace,
        )


class AsyncDatasetResourceWithRawResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_raw_response_wrapper(
            dataset.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dataset.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dataset.update,
        )
        self.list = async_to_raw_response_wrapper(
            dataset.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dataset.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            dataset.feedback,
        )
        self.fetch = async_to_raw_response_wrapper(
            dataset.fetch,
        )
        self.fetch_post = async_to_raw_response_wrapper(
            dataset.fetch_post,
        )
        self.insert = async_to_raw_response_wrapper(
            dataset.insert,
        )
        self.replace = async_to_raw_response_wrapper(
            dataset.replace,
        )


class DatasetResourceWithStreamingResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_streamed_response_wrapper(
            dataset.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dataset.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dataset.update,
        )
        self.list = to_streamed_response_wrapper(
            dataset.list,
        )
        self.delete = to_streamed_response_wrapper(
            dataset.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            dataset.feedback,
        )
        self.fetch = to_streamed_response_wrapper(
            dataset.fetch,
        )
        self.fetch_post = to_streamed_response_wrapper(
            dataset.fetch_post,
        )
        self.insert = to_streamed_response_wrapper(
            dataset.insert,
        )
        self.replace = to_streamed_response_wrapper(
            dataset.replace,
        )


class AsyncDatasetResourceWithStreamingResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_streamed_response_wrapper(
            dataset.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dataset.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dataset.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dataset.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dataset.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            dataset.feedback,
        )
        self.fetch = async_to_streamed_response_wrapper(
            dataset.fetch,
        )
        self.fetch_post = async_to_streamed_response_wrapper(
            dataset.fetch_post,
        )
        self.insert = async_to_streamed_response_wrapper(
            dataset.insert,
        )
        self.replace = async_to_streamed_response_wrapper(
            dataset.replace,
        )
