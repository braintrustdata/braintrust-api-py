# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.role import Role

from .._utils import maybe_transform, async_maybe_transform

from typing import Optional, List, Union

from typing_extensions import Literal

from ..pagination import SyncListObjects, AsyncListObjects

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import role_create_params
from ..types import role_update_params
from ..types import role_list_params
from ..types import role_replace_params

__all__ = ["RoleResource", "AsyncRoleResource"]


class RoleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoleResourceWithRawResponse:
        return RoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoleResourceWithStreamingResponse:
        return RoleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
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

          member_permissions: Permissions which belong to this role

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
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
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

          description: Textual description of the role

          member_permissions: Permissions which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          name: Name of the role

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
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "name": name,
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
        limit: int | NotGiven = NOT_GIVEN,
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
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        NOTE: This operation is deprecated and will be removed in a future revision of
        the API. Create or replace a new role. If there is an existing role with the
        same name as the one specified in the request, will return the existing role
        unmodified, will replace the existing role with the provided fields

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: Permissions which belong to this role

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


class AsyncRoleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoleResourceWithRawResponse:
        return AsyncRoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoleResourceWithStreamingResponse:
        return AsyncRoleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
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

          member_permissions: Permissions which belong to this role

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
        description: Optional[str] | NotGiven = NOT_GIVEN,
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
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

          description: Textual description of the role

          member_permissions: Permissions which belong to this role

          member_roles: Ids of the roles this role inherits from

              An inheriting role has all the permissions contained in its member roles, as
              well as all of their inherited permissions

          name: Name of the role

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
                    "description": description,
                    "member_permissions": member_permissions,
                    "member_roles": member_roles,
                    "name": name,
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
        limit: int | NotGiven = NOT_GIVEN,
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
        member_permissions: Optional[
            List[
                Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        member_roles: Optional[List[str]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Role:
        """
        NOTE: This operation is deprecated and will be removed in a future revision of
        the API. Create or replace a new role. If there is an existing role with the
        same name as the one specified in the request, will return the existing role
        unmodified, will replace the existing role with the provided fields

        Args:
          name: Name of the role

          description: Textual description of the role

          member_permissions: Permissions which belong to this role

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


class RoleResourceWithRawResponse:
    def __init__(self, role: RoleResource) -> None:
        self._role = role

        self.create = to_raw_response_wrapper(
            role.create,
        )
        self.retrieve = to_raw_response_wrapper(
            role.retrieve,
        )
        self.update = to_raw_response_wrapper(
            role.update,
        )
        self.list = to_raw_response_wrapper(
            role.list,
        )
        self.delete = to_raw_response_wrapper(
            role.delete,
        )
        self.replace = to_raw_response_wrapper(
            role.replace,
        )


class AsyncRoleResourceWithRawResponse:
    def __init__(self, role: AsyncRoleResource) -> None:
        self._role = role

        self.create = async_to_raw_response_wrapper(
            role.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            role.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            role.update,
        )
        self.list = async_to_raw_response_wrapper(
            role.list,
        )
        self.delete = async_to_raw_response_wrapper(
            role.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            role.replace,
        )


class RoleResourceWithStreamingResponse:
    def __init__(self, role: RoleResource) -> None:
        self._role = role

        self.create = to_streamed_response_wrapper(
            role.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            role.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            role.update,
        )
        self.list = to_streamed_response_wrapper(
            role.list,
        )
        self.delete = to_streamed_response_wrapper(
            role.delete,
        )
        self.replace = to_streamed_response_wrapper(
            role.replace,
        )


class AsyncRoleResourceWithStreamingResponse:
    def __init__(self, role: AsyncRoleResource) -> None:
        self._role = role

        self.create = async_to_streamed_response_wrapper(
            role.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            role.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            role.update,
        )
        self.list = async_to_streamed_response_wrapper(
            role.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            role.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            role.replace,
        )
