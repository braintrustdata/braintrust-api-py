# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import shared_params, organization_list_params, organization_update_params
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from ...pagination import SyncListObjects, AsyncListObjects
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.org_name import OrgName
from ...types.shared.organization import Organization
from ...types.shared.ending_before import EndingBefore
from ...types.shared.starting_after import StartingAfter
from ...types.shared.app_limit_param import AppLimitParam
from ...types.shared.organization_id import OrganizationID
from ...types.shared.organization_name import OrganizationName

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organization_id: OrganizationID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Get a organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/v1/organization/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def update(
        self,
        organization_id: OrganizationID,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """Partially update a organization object.

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
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._patch(
            f"/v1/organization/{organization_id}",
            body=maybe_transform(
                {
                    "api_url": api_url,
                    "is_universal_api": is_universal_api,
                    "name": name,
                    "proxy_url": proxy_url,
                    "realtime_url": realtime_url,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def list(
        self,
        *,
        ending_before: EndingBefore | NotGiven = NOT_GIVEN,
        ids: shared_params.IDs | NotGiven = NOT_GIVEN,
        limit: AppLimitParam | NotGiven = NOT_GIVEN,
        org_name: OrgName | NotGiven = NOT_GIVEN,
        organization_name: OrganizationName | NotGiven = NOT_GIVEN,
        starting_after: StartingAfter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[Organization]:
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

          organization_name: Name of the organization to search for

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
            page=SyncListObjects[Organization],
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
                        "organization_name": organization_name,
                        "starting_after": starting_after,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=Organization,
        )

    def delete(
        self,
        organization_id: OrganizationID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Delete a organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._delete(
            f"/v1/organization/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organization_id: OrganizationID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Get a organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/v1/organization/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    async def update(
        self,
        organization_id: OrganizationID,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """Partially update a organization object.

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
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._patch(
            f"/v1/organization/{organization_id}",
            body=await async_maybe_transform(
                {
                    "api_url": api_url,
                    "is_universal_api": is_universal_api,
                    "name": name,
                    "proxy_url": proxy_url,
                    "realtime_url": realtime_url,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )

    def list(
        self,
        *,
        ending_before: EndingBefore | NotGiven = NOT_GIVEN,
        ids: shared_params.IDs | NotGiven = NOT_GIVEN,
        limit: AppLimitParam | NotGiven = NOT_GIVEN,
        org_name: OrgName | NotGiven = NOT_GIVEN,
        organization_name: OrganizationName | NotGiven = NOT_GIVEN,
        starting_after: StartingAfter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Organization, AsyncListObjects[Organization]]:
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

          organization_name: Name of the organization to search for

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
            page=AsyncListObjects[Organization],
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
                        "organization_name": organization_name,
                        "starting_after": starting_after,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=Organization,
        )

    async def delete(
        self,
        organization_id: OrganizationID,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Organization:
        """
        Delete a organization object by its id

        Args:
          organization_id: Organization id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._delete(
            f"/v1/organization/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organization,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._organizations.members)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organizations.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._organizations.members)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = to_streamed_response_wrapper(
            organizations.delete,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._organizations.members)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organizations.delete,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._organizations.members)
