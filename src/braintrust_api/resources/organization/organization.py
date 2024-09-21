# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .members import MembersResource, AsyncMembersResource

from ..._compat import cached_property

from ...types.shared.organization import Organization

from ..._base_client import make_request_options, AsyncPaginator

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Union, List

from ...pagination import SyncListObjects, AsyncListObjects

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types import organization_update_params
from ...types import organization_list_params
from .members import MembersResource, AsyncMembersResource, MembersResourceWithRawResponse, AsyncMembersResourceWithRawResponse, MembersResourceWithStreamingResponse, AsyncMembersResourceWithStreamingResponse

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]

class OrganizationResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        return OrganizationResourceWithStreamingResponse(self)

    def retrieve(self,
    organization_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """
        Get an organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return self._get(
            f"/v1/organization/{organization_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

    def update(self,
    organization_id: str,
    *,
    api_url: Optional[str] | NotGiven = NOT_GIVEN,
    is_universal_api: Optional[bool] | NotGiven = NOT_GIVEN,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    proxy_url: Optional[str] | NotGiven = NOT_GIVEN,
    realtime_url: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """Partially update an organization object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          organization_id: Organization id

          name: Name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return self._patch(
            f"/v1/organization/{organization_id}",
            body=maybe_transform({
                "api_url": api_url,
                "is_universal_api": is_universal_api,
                "name": name,
                "proxy_url": proxy_url,
                "realtime_url": realtime_url,
            }, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

    def list(self,
    *,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncListObjects[Organization]:
        """List out all organizations.

        The organizations are sorted by creation date, with
        the most recently-created organizations coming first

        Args:
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
            "/v1/organization",
            page = SyncListObjects[Organization],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, organization_list_params.OrganizationListParams)),
            model=Organization,
        )

    def delete(self,
    organization_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """
        Delete an organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return self._delete(
            f"/v1/organization/{organization_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        return AsyncOrganizationResourceWithStreamingResponse(self)

    async def retrieve(self,
    organization_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """
        Get an organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return await self._get(
            f"/v1/organization/{organization_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

    async def update(self,
    organization_id: str,
    *,
    api_url: Optional[str] | NotGiven = NOT_GIVEN,
    is_universal_api: Optional[bool] | NotGiven = NOT_GIVEN,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    proxy_url: Optional[str] | NotGiven = NOT_GIVEN,
    realtime_url: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """Partially update an organization object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          organization_id: Organization id

          name: Name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return await self._patch(
            f"/v1/organization/{organization_id}",
            body=await async_maybe_transform({
                "api_url": api_url,
                "is_universal_api": is_universal_api,
                "name": name,
                "proxy_url": proxy_url,
                "realtime_url": realtime_url,
            }, organization_update_params.OrganizationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

    def list(self,
    *,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Organization, AsyncListObjects[Organization]]:
        """List out all organizations.

        The organizations are sorted by creation date, with
        the most recently-created organizations coming first

        Args:
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
            "/v1/organization",
            page = AsyncListObjects[Organization],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, organization_list_params.OrganizationListParams)),
            model=Organization,
        )

    async def delete(self,
    organization_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Organization:
        """
        Delete an organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
          raise ValueError(
            f'Expected a non-empty value for `organization_id` but received {organization_id!r}'
          )
        return await self._delete(
            f"/v1/organization/{organization_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Organization,
        )

class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.retrieve = to_raw_response_wrapper(
            organization.retrieve,
        )
        self.update = to_raw_response_wrapper(
            organization.update,
        )
        self.list = to_raw_response_wrapper(
            organization.list,
        )
        self.delete = to_raw_response_wrapper(
            organization.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._organization.members)

class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.retrieve = async_to_raw_response_wrapper(
            organization.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            organization.update,
        )
        self.list = async_to_raw_response_wrapper(
            organization.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organization.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._organization.members)

class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

        self.retrieve = to_streamed_response_wrapper(
            organization.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            organization.update,
        )
        self.list = to_streamed_response_wrapper(
            organization.list,
        )
        self.delete = to_streamed_response_wrapper(
            organization.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._organization.members)

class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

        self.retrieve = async_to_streamed_response_wrapper(
            organization.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            organization.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organization.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organization.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._organization.members)