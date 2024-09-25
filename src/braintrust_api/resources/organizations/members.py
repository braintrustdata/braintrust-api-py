# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.organizations import member_update_params
from ...types.shared.patch_organization_members_output import PatchOrganizationMembersOutput

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        invite_users: Optional[member_update_params.InviteUsers] | NotGiven = NOT_GIVEN,
        org_id: Optional[str] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        remove_users: Optional[member_update_params.RemoveUsers] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatchOrganizationMembersOutput:
        """
        Modify organization membership

        Args:
          invite_users: Users to invite to the organization

          org_id: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, or in case you want to
              explicitly assert the organization you are modifying, you may specify the id of
              the organization.

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, or in case you want to
              explicitly assert the organization you are modifying, you may specify the name
              of the organization.

          remove_users: Users to remove from the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/organization/members",
            body=maybe_transform(
                {
                    "invite_users": invite_users,
                    "org_id": org_id,
                    "org_name": org_name,
                    "remove_users": remove_users,
                },
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatchOrganizationMembersOutput,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        invite_users: Optional[member_update_params.InviteUsers] | NotGiven = NOT_GIVEN,
        org_id: Optional[str] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        remove_users: Optional[member_update_params.RemoveUsers] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatchOrganizationMembersOutput:
        """
        Modify organization membership

        Args:
          invite_users: Users to invite to the organization

          org_id: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, or in case you want to
              explicitly assert the organization you are modifying, you may specify the id of
              the organization.

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, or in case you want to
              explicitly assert the organization you are modifying, you may specify the name
              of the organization.

          remove_users: Users to remove from the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/organization/members",
            body=await async_maybe_transform(
                {
                    "invite_users": invite_users,
                    "org_id": org_id,
                    "org_name": org_name,
                    "remove_users": remove_users,
                },
                member_update_params.MemberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatchOrganizationMembersOutput,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.update = to_raw_response_wrapper(
            members.update,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.update = async_to_raw_response_wrapper(
            members.update,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.update = to_streamed_response_wrapper(
            members.update,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.update = async_to_streamed_response_wrapper(
            members.update,
        )
