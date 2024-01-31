# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

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

__all__ = ["V1", "AsyncV1"]


class V1(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1WithRawResponse:
        return V1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1WithStreamingResponse:
        return V1WithStreamingResponse(self)

    def hello_world(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Default endpoint.

        Simply replies with 'Hello, World!'. Authorization is not
        required
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncV1(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1WithRawResponse:
        return AsyncV1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1WithStreamingResponse:
        return AsyncV1WithStreamingResponse(self)

    async def hello_world(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Default endpoint.

        Simply replies with 'Hello, World!'. Authorization is not
        required
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/v1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class V1WithRawResponse:
    def __init__(self, v1: V1) -> None:
        self._v1 = v1

        self.hello_world = to_raw_response_wrapper(
            v1.hello_world,
        )


class AsyncV1WithRawResponse:
    def __init__(self, v1: AsyncV1) -> None:
        self._v1 = v1

        self.hello_world = async_to_raw_response_wrapper(
            v1.hello_world,
        )


class V1WithStreamingResponse:
    def __init__(self, v1: V1) -> None:
        self._v1 = v1

        self.hello_world = to_streamed_response_wrapper(
            v1.hello_world,
        )


class AsyncV1WithStreamingResponse:
    def __init__(self, v1: AsyncV1) -> None:
        self._v1 = v1

        self.hello_world = async_to_streamed_response_wrapper(
            v1.hello_world,
        )
