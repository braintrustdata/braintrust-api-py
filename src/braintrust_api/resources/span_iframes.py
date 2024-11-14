# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

import httpx

from ..types import (
    span_iframe_list_params,
    span_iframe_create_params,
    span_iframe_update_params,
    span_iframe_replace_params,
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
from ..types.shared.span_i_frame import SpanIFrame

__all__ = ["SpanIframesResource", "AsyncSpanIframesResource"]


class SpanIframesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpanIframesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return SpanIframesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpanIframesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return SpanIframesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        url: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Create a new span_iframe.

        If there is an existing span_iframe with the same name
        as the one specified in the request, will return the existing span_iframe
        unmodified

        Args:
          name: Name of the span iframe

          project_id: Unique identifier for the project that the span iframe belongs under

          url: URL to embed the project viewer in an iframe

          description: Textual description of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/span_iframe",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "url": url,
                    "description": description,
                    "post_message": post_message,
                },
                span_iframe_create_params.SpanIframeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    def retrieve(
        self,
        span_iframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """
        Get a span_iframe object by its id

        Args:
          span_iframe_id: SpanIframe id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return self._get(
            f"/v1/span_iframe/{span_iframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    def update(
        self,
        span_iframe_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Partially update a span_iframe object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          span_iframe_id: SpanIframe id

          name: Name of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          url: URL to embed the project viewer in an iframe

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return self._patch(
            f"/v1/span_iframe/{span_iframe_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "post_message": post_message,
                    "url": url,
                },
                span_iframe_update_params.SpanIframeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        span_iframe_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[SpanIFrame]:
        """List out all span_iframes.

        The span_iframes are sorted by creation date, with
        the most recently-created span_iframes coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          span_iframe_name: Name of the span_iframe to search for

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
            "/v1/span_iframe",
            page=SyncListObjects[SpanIFrame],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "span_iframe_name": span_iframe_name,
                        "starting_after": starting_after,
                    },
                    span_iframe_list_params.SpanIframeListParams,
                ),
            ),
            model=SpanIFrame,
        )

    def delete(
        self,
        span_iframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """
        Delete a span_iframe object by its id

        Args:
          span_iframe_id: SpanIframe id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return self._delete(
            f"/v1/span_iframe/{span_iframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    def replace(
        self,
        *,
        name: str,
        project_id: str,
        url: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Create or replace span_iframe.

        If there is an existing span_iframe with the same
        name as the one specified in the request, will replace the existing span_iframe
        with the provided fields

        Args:
          name: Name of the span iframe

          project_id: Unique identifier for the project that the span iframe belongs under

          url: URL to embed the project viewer in an iframe

          description: Textual description of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/span_iframe",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "url": url,
                    "description": description,
                    "post_message": post_message,
                },
                span_iframe_replace_params.SpanIframeReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )


class AsyncSpanIframesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpanIframesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSpanIframesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpanIframesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncSpanIframesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        url: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Create a new span_iframe.

        If there is an existing span_iframe with the same name
        as the one specified in the request, will return the existing span_iframe
        unmodified

        Args:
          name: Name of the span iframe

          project_id: Unique identifier for the project that the span iframe belongs under

          url: URL to embed the project viewer in an iframe

          description: Textual description of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/span_iframe",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "url": url,
                    "description": description,
                    "post_message": post_message,
                },
                span_iframe_create_params.SpanIframeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    async def retrieve(
        self,
        span_iframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """
        Get a span_iframe object by its id

        Args:
          span_iframe_id: SpanIframe id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return await self._get(
            f"/v1/span_iframe/{span_iframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    async def update(
        self,
        span_iframe_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Partially update a span_iframe object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          span_iframe_id: SpanIframe id

          name: Name of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          url: URL to embed the project viewer in an iframe

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return await self._patch(
            f"/v1/span_iframe/{span_iframe_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "post_message": post_message,
                    "url": url,
                },
                span_iframe_update_params.SpanIframeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        span_iframe_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SpanIFrame, AsyncListObjects[SpanIFrame]]:
        """List out all span_iframes.

        The span_iframes are sorted by creation date, with
        the most recently-created span_iframes coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          span_iframe_name: Name of the span_iframe to search for

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
            "/v1/span_iframe",
            page=AsyncListObjects[SpanIFrame],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "span_iframe_name": span_iframe_name,
                        "starting_after": starting_after,
                    },
                    span_iframe_list_params.SpanIframeListParams,
                ),
            ),
            model=SpanIFrame,
        )

    async def delete(
        self,
        span_iframe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """
        Delete a span_iframe object by its id

        Args:
          span_iframe_id: SpanIframe id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not span_iframe_id:
            raise ValueError(f"Expected a non-empty value for `span_iframe_id` but received {span_iframe_id!r}")
        return await self._delete(
            f"/v1/span_iframe/{span_iframe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )

    async def replace(
        self,
        *,
        name: str,
        project_id: str,
        url: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        post_message: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanIFrame:
        """Create or replace span_iframe.

        If there is an existing span_iframe with the same
        name as the one specified in the request, will replace the existing span_iframe
        with the provided fields

        Args:
          name: Name of the span iframe

          project_id: Unique identifier for the project that the span iframe belongs under

          url: URL to embed the project viewer in an iframe

          description: Textual description of the span iframe

          post_message: Whether to post messages to the iframe containing the span's data. This is
              useful when you want to render more data than fits in the URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/span_iframe",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "url": url,
                    "description": description,
                    "post_message": post_message,
                },
                span_iframe_replace_params.SpanIframeReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpanIFrame,
        )


class SpanIframesResourceWithRawResponse:
    def __init__(self, span_iframes: SpanIframesResource) -> None:
        self._span_iframes = span_iframes

        self.create = to_raw_response_wrapper(
            span_iframes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            span_iframes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            span_iframes.update,
        )
        self.list = to_raw_response_wrapper(
            span_iframes.list,
        )
        self.delete = to_raw_response_wrapper(
            span_iframes.delete,
        )
        self.replace = to_raw_response_wrapper(
            span_iframes.replace,
        )


class AsyncSpanIframesResourceWithRawResponse:
    def __init__(self, span_iframes: AsyncSpanIframesResource) -> None:
        self._span_iframes = span_iframes

        self.create = async_to_raw_response_wrapper(
            span_iframes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            span_iframes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            span_iframes.update,
        )
        self.list = async_to_raw_response_wrapper(
            span_iframes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            span_iframes.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            span_iframes.replace,
        )


class SpanIframesResourceWithStreamingResponse:
    def __init__(self, span_iframes: SpanIframesResource) -> None:
        self._span_iframes = span_iframes

        self.create = to_streamed_response_wrapper(
            span_iframes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            span_iframes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            span_iframes.update,
        )
        self.list = to_streamed_response_wrapper(
            span_iframes.list,
        )
        self.delete = to_streamed_response_wrapper(
            span_iframes.delete,
        )
        self.replace = to_streamed_response_wrapper(
            span_iframes.replace,
        )


class AsyncSpanIframesResourceWithStreamingResponse:
    def __init__(self, span_iframes: AsyncSpanIframesResource) -> None:
        self._span_iframes = span_iframes

        self.create = async_to_streamed_response_wrapper(
            span_iframes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            span_iframes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            span_iframes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            span_iframes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            span_iframes.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            span_iframes.replace,
        )
