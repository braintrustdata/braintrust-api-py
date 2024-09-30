# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

from ..types import role_list_params, role_create_params, role_update_params, role_replace_params
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
from ..types.shared.role import Role

__all__ = ["RolesResource", "AsyncRolesResource"]


class RolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return RolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return RolesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[Iterable[role_create_params.MemberPermission]] | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Create a new role.

        If there is an existing role with the same name as the one
        specified in the request, will return the existing role unmodified

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: (permission, restrict_object_type) tuples which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the role belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/role",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "org_name": org_name,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def retrieve(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        Get a role object by its id

        Args:
          role_id: Role id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._get(
            f"/v1/role/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def update(
        self,
        role_id: str,
        *,
        add_member_permissions: Optional[Iterable[role_update_params.AddMemberPermission]] | NotGiven = NOT_GIVEN,
        add_member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        remove_member_permissions: Optional[Iterable[role_update_params.RemoveMemberPermission]] | NotGiven = NOT_GIVEN,
        remove_member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Partially update a role object.

        Specify the fields to update in the payload. Any
        object-type fields will be deep-merged with existing content. Currently we do
        not support removing fields or setting them to null.

        Args:
          role_id: Role id

          add_member_permissions: A list of permissions to add to the role

          add_member_roles: A list of role IDs to add to the role's inheriting-from set

          description: Textual description of the role

          name: Name of the role

          remove_member_permissions: A list of permissions to remove from the role

          remove_member_roles: A list of role IDs to remove from the role's inheriting-from set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._patch(
            f"/v1/role/{role_id}",
            body=maybe_transform(
                {
                    "add_member_permissions": add_member_permissions,
                    "add_member_roles": add_member_roles,
                    "description": description,
                    "name": name,
                    "remove_member_permissions": remove_member_permissions,
                    "remove_member_roles": remove_member_roles,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        role_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[Role]:
        """List out all roles.

        The roles are sorted by creation date, with the most
        recently-created roles coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          role_name: Name of the role to search for

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
            "/v1/role",
            page=SyncListObjects[Role],
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
                        "role_name": role_name,
                        "starting_after": starting_after,
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            model=Role,
        )

    def delete(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        Delete a role object by its id

        Args:
          role_id: Role id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return self._delete(
            f"/v1/role/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def replace(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[Iterable[role_replace_params.MemberPermission]] | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Create or replace role.

        If there is an existing role with the same name as the
        one specified in the request, will replace the existing role with the provided
        fields

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: (permission, restrict_object_type) tuples which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the role belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/role",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "org_name": org_name,
                },
                role_replace_params.RoleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )


class AsyncRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncRolesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[Iterable[role_create_params.MemberPermission]] | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Create a new role.

        If there is an existing role with the same name as the one
        specified in the request, will return the existing role unmodified

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: (permission, restrict_object_type) tuples which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the role belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/role",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "org_name": org_name,
                },
                role_create_params.RoleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def retrieve(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        Get a role object by its id

        Args:
          role_id: Role id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._get(
            f"/v1/role/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def update(
        self,
        role_id: str,
        *,
        add_member_permissions: Optional[Iterable[role_update_params.AddMemberPermission]] | NotGiven = NOT_GIVEN,
        add_member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        remove_member_permissions: Optional[Iterable[role_update_params.RemoveMemberPermission]] | NotGiven = NOT_GIVEN,
        remove_member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Partially update a role object.

        Specify the fields to update in the payload. Any
        object-type fields will be deep-merged with existing content. Currently we do
        not support removing fields or setting them to null.

        Args:
          role_id: Role id

          add_member_permissions: A list of permissions to add to the role

          add_member_roles: A list of role IDs to add to the role's inheriting-from set

          description: Textual description of the role

          name: Name of the role

          remove_member_permissions: A list of permissions to remove from the role

          remove_member_roles: A list of role IDs to remove from the role's inheriting-from set

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._patch(
            f"/v1/role/{role_id}",
            body=await async_maybe_transform(
                {
                    "add_member_permissions": add_member_permissions,
                    "add_member_roles": add_member_roles,
                    "description": description,
                    "name": name,
                    "remove_member_permissions": remove_member_permissions,
                    "remove_member_roles": remove_member_roles,
                },
                role_update_params.RoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        role_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Role, AsyncListObjects[Role]]:
        """List out all roles.

        The roles are sorted by creation date, with the most
        recently-created roles coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          role_name: Name of the role to search for

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
            "/v1/role",
            page=AsyncListObjects[Role],
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
                        "role_name": role_name,
                        "starting_after": starting_after,
                    },
                    role_list_params.RoleListParams,
                ),
            ),
            model=Role,
        )

    async def delete(
        self,
        role_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        Delete a role object by its id

        Args:
          role_id: Role id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not role_id:
            raise ValueError(f"Expected a non-empty value for `role_id` but received {role_id!r}")
        return await self._delete(
            f"/v1/role/{role_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )

    async def replace(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[Iterable[role_replace_params.MemberPermission]] | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """Create or replace role.

        If there is an existing role with the same name as the
        one specified in the request, will replace the existing role with the provided
        fields

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: (permission, restrict_object_type) tuples which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the role belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/role",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "org_name": org_name,
                },
                role_replace_params.RoleReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Role,
        )


class RolesResourceWithRawResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            roles.update,
        )
        self.list = to_raw_response_wrapper(
            roles.list,
        )
        self.delete = to_raw_response_wrapper(
            roles.delete,
        )
        self.replace = to_raw_response_wrapper(
            roles.replace,
        )


class AsyncRolesResourceWithRawResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_raw_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            roles.update,
        )
        self.list = async_to_raw_response_wrapper(
            roles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            roles.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            roles.replace,
        )


class RolesResourceWithStreamingResponse:
    def __init__(self, roles: RolesResource) -> None:
        self._roles = roles

        self.create = to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            roles.update,
        )
        self.list = to_streamed_response_wrapper(
            roles.list,
        )
        self.delete = to_streamed_response_wrapper(
            roles.delete,
        )
        self.replace = to_streamed_response_wrapper(
            roles.replace,
        )


class AsyncRolesResourceWithStreamingResponse:
    def __init__(self, roles: AsyncRolesResource) -> None:
        self._roles = roles

        self.create = async_to_streamed_response_wrapper(
            roles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            roles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            roles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            roles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            roles.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            roles.replace,
        )
