# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..types import Dataset
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["TopLevel", "AsyncTopLevel"]


class TopLevel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopLevelWithRawResponse:
        return TopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopLevelWithStreamingResponse:
        return TopLevelWithStreamingResponse(self)

    def datasets(
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


class AsyncTopLevel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopLevelWithRawResponse:
        return AsyncTopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopLevelWithStreamingResponse:
        return AsyncTopLevelWithStreamingResponse(self)

    async def datasets(
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


class TopLevelWithRawResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self._top_level = top_level

        self.datasets = to_raw_response_wrapper(
            top_level.datasets,
        )


class AsyncTopLevelWithRawResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self._top_level = top_level

        self.datasets = async_to_raw_response_wrapper(
            top_level.datasets,
        )


class TopLevelWithStreamingResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self._top_level = top_level

        self.datasets = to_streamed_response_wrapper(
            top_level.datasets,
        )


class AsyncTopLevelWithStreamingResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self._top_level = top_level

        self.datasets = async_to_streamed_response_wrapper(
            top_level.datasets,
        )
