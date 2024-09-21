# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.shared.create_api_key_output import CreateAPIKeyOutput

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options, AsyncPaginator

from typing import Optional, Union, List

from ..types.shared.api_key import APIKey

from ..pagination import SyncListObjects, AsyncListObjects

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import api_key_resource_create_params
from ..types import api_key_resource_list_params

__all__ = ["APIKeyResourceResource", "AsyncAPIKeyResourceResource"]

class APIKeyResourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeyResourceResourceWithRawResponse:
        return APIKeyResourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeyResourceResourceWithStreamingResponse:
        return APIKeyResourceResourceWithStreamingResponse(self)

    def create(self,
    *,
    name: str,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> CreateAPIKeyOutput:
        """Create a new api_key.

        It is possible to have multiple API keys with the same
        name. There is no de-duplication

        Args:
          name: Name of the api key. Does not have to be unique

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the API key belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/api_key",
            body=maybe_transform({
                "name": name,
                "org_name": org_name,
            }, api_key_resource_create_params.APIKeyResourceCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CreateAPIKeyOutput,
        )

    def retrieve(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> APIKey:
        """
        Get an api_key object by its id

        Args:
          api_key_id: ApiKey id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        return self._get(
            f"/v1/api_key/{api_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

    def list(self,
    *,
    api_key_name: str | NotGiven = NOT_GIVEN,
    ending_before: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncListObjects[APIKey]:
        """List out all api_keys.

        The api_keys are sorted by creation date, with the most
        recently-created api_keys coming first

        Args:
          api_key_name: Name of the api_key to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

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
            "/v1/api_key",
            page = SyncListObjects[APIKey],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "api_key_name": api_key_name,
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, api_key_resource_list_params.APIKeyResourceListParams)),
            model=APIKey,
        )

    def delete(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> APIKey:
        """
        Delete an api_key object by its id

        Args:
          api_key_id: ApiKey id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        return self._delete(
            f"/v1/api_key/{api_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

class AsyncAPIKeyResourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeyResourceResourceWithRawResponse:
        return AsyncAPIKeyResourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeyResourceResourceWithStreamingResponse:
        return AsyncAPIKeyResourceResourceWithStreamingResponse(self)

    async def create(self,
    *,
    name: str,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> CreateAPIKeyOutput:
        """Create a new api_key.

        It is possible to have multiple API keys with the same
        name. There is no de-duplication

        Args:
          name: Name of the api key. Does not have to be unique

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the API key belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/api_key",
            body=await async_maybe_transform({
                "name": name,
                "org_name": org_name,
            }, api_key_resource_create_params.APIKeyResourceCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CreateAPIKeyOutput,
        )

    async def retrieve(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> APIKey:
        """
        Get an api_key object by its id

        Args:
          api_key_id: ApiKey id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        return await self._get(
            f"/v1/api_key/{api_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

    def list(self,
    *,
    api_key_name: str | NotGiven = NOT_GIVEN,
    ending_before: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[APIKey, AsyncListObjects[APIKey]]:
        """List out all api_keys.

        The api_keys are sorted by creation date, with the most
        recently-created api_keys coming first

        Args:
          api_key_name: Name of the api_key to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

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
            "/v1/api_key",
            page = AsyncListObjects[APIKey],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "api_key_name": api_key_name,
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, api_key_resource_list_params.APIKeyResourceListParams)),
            model=APIKey,
        )

    async def delete(self,
    api_key_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> APIKey:
        """
        Delete an api_key object by its id

        Args:
          api_key_id: ApiKey id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not api_key_id:
          raise ValueError(
            f'Expected a non-empty value for `api_key_id` but received {api_key_id!r}'
          )
        return await self._delete(
            f"/v1/api_key/{api_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=APIKey,
        )

class APIKeyResourceResourceWithRawResponse:
    def __init__(self, api_key_resource: APIKeyResourceResource) -> None:
        self._api_key_resource = api_key_resource

        self.create = to_raw_response_wrapper(
            api_key_resource.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_key_resource.retrieve,
        )
        self.list = to_raw_response_wrapper(
            api_key_resource.list,
        )
        self.delete = to_raw_response_wrapper(
            api_key_resource.delete,
        )

class AsyncAPIKeyResourceResourceWithRawResponse:
    def __init__(self, api_key_resource: AsyncAPIKeyResourceResource) -> None:
        self._api_key_resource = api_key_resource

        self.create = async_to_raw_response_wrapper(
            api_key_resource.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_key_resource.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            api_key_resource.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_key_resource.delete,
        )

class APIKeyResourceResourceWithStreamingResponse:
    def __init__(self, api_key_resource: APIKeyResourceResource) -> None:
        self._api_key_resource = api_key_resource

        self.create = to_streamed_response_wrapper(
            api_key_resource.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_key_resource.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            api_key_resource.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_key_resource.delete,
        )

class AsyncAPIKeyResourceResourceWithStreamingResponse:
    def __init__(self, api_key_resource: AsyncAPIKeyResourceResource) -> None:
        self._api_key_resource = api_key_resource

        self.create = async_to_streamed_response_wrapper(
            api_key_resource.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_key_resource.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            api_key_resource.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_key_resource.delete,
        )