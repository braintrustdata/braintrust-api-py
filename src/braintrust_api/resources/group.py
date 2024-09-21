# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.shared.group import Group

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options, AsyncPaginator

from typing import Optional, List, Union

from ..pagination import SyncListObjects, AsyncListObjects

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import group_create_params
from ..types import group_update_params
from ..types import group_list_params
from ..types import group_replace_params

__all__ = ["GroupResource", "AsyncGroupResource"]

class GroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return GroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return GroupResourceWithStreamingResponse(self)

    def create(self,
    *,
    name: str,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Create a new group.

        If there is an existing group with the same name as the one
        specified in the request, will return the existing group unmodified

        Args:
          name: Name of the group

          description: Textual description of the group

          member_groups: Ids of the groups this group inherits from

              An inheriting group has all the users contained in its member groups, as well as
              all of their inherited users

          member_users: Ids of users which belong to this group

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the group belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/group",
            body=maybe_transform({
                "name": name,
                "description": description,
                "member_groups": member_groups,
                "member_users": member_users,
                "org_name": org_name,
            }, group_create_params.GroupCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    def retrieve(self,
    group_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """
        Get a group object by its id

        Args:
          group_id: Group id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return self._get(
            f"/v1/group/{group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    def update(self,
    group_id: str,
    *,
    add_member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    add_member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    remove_member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    remove_member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Partially update a group object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          group_id: Group id

          add_member_groups: A list of group IDs to add to the group's inheriting-from set

          add_member_users: A list of user IDs to add to the group

          description: Textual description of the group

          name: Name of the group

          remove_member_groups: A list of group IDs to remove from the group's inheriting-from set

          remove_member_users: A list of user IDs to remove from the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return self._patch(
            f"/v1/group/{group_id}",
            body=maybe_transform({
                "add_member_groups": add_member_groups,
                "add_member_users": add_member_users,
                "description": description,
                "name": name,
                "remove_member_groups": remove_member_groups,
                "remove_member_users": remove_member_users,
            }, group_update_params.GroupUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    def list(self,
    *,
    ending_before: str | NotGiven = NOT_GIVEN,
    group_name: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncListObjects[Group]:
        """List out all groups.

        The groups are sorted by creation date, with the most
        recently-created groups coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          group_name: Name of the group to search for

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
            "/v1/group",
            page = SyncListObjects[Group],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "group_name": group_name,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, group_list_params.GroupListParams)),
            model=Group,
        )

    def delete(self,
    group_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """
        Delete a group object by its id

        Args:
          group_id: Group id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return self._delete(
            f"/v1/group/{group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    def replace(self,
    *,
    name: str,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Create or replace group.

        If there is an existing group with the same name as the
        one specified in the request, will replace the existing group with the provided
        fields

        Args:
          name: Name of the group

          description: Textual description of the group

          member_groups: Ids of the groups this group inherits from

              An inheriting group has all the users contained in its member groups, as well as
              all of their inherited users

          member_users: Ids of users which belong to this group

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the group belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/group",
            body=maybe_transform({
                "name": name,
                "description": description,
                "member_groups": member_groups,
                "member_users": member_users,
                "org_name": org_name,
            }, group_replace_params.GroupReplaceParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

class AsyncGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncGroupResourceWithStreamingResponse(self)

    async def create(self,
    *,
    name: str,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Create a new group.

        If there is an existing group with the same name as the one
        specified in the request, will return the existing group unmodified

        Args:
          name: Name of the group

          description: Textual description of the group

          member_groups: Ids of the groups this group inherits from

              An inheriting group has all the users contained in its member groups, as well as
              all of their inherited users

          member_users: Ids of users which belong to this group

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the group belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/group",
            body=await async_maybe_transform({
                "name": name,
                "description": description,
                "member_groups": member_groups,
                "member_users": member_users,
                "org_name": org_name,
            }, group_create_params.GroupCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    async def retrieve(self,
    group_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """
        Get a group object by its id

        Args:
          group_id: Group id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return await self._get(
            f"/v1/group/{group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    async def update(self,
    group_id: str,
    *,
    add_member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    add_member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    remove_member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    remove_member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Partially update a group object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          group_id: Group id

          add_member_groups: A list of group IDs to add to the group's inheriting-from set

          add_member_users: A list of user IDs to add to the group

          description: Textual description of the group

          name: Name of the group

          remove_member_groups: A list of group IDs to remove from the group's inheriting-from set

          remove_member_users: A list of user IDs to remove from the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return await self._patch(
            f"/v1/group/{group_id}",
            body=await async_maybe_transform({
                "add_member_groups": add_member_groups,
                "add_member_users": add_member_users,
                "description": description,
                "name": name,
                "remove_member_groups": remove_member_groups,
                "remove_member_users": remove_member_users,
            }, group_update_params.GroupUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    def list(self,
    *,
    ending_before: str | NotGiven = NOT_GIVEN,
    group_name: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Group, AsyncListObjects[Group]]:
        """List out all groups.

        The groups are sorted by creation date, with the most
        recently-created groups coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          group_name: Name of the group to search for

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
            "/v1/group",
            page = AsyncListObjects[Group],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "group_name": group_name,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "starting_after": starting_after,
            }, group_list_params.GroupListParams)),
            model=Group,
        )

    async def delete(self,
    group_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """
        Delete a group object by its id

        Args:
          group_id: Group id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not group_id:
          raise ValueError(
            f'Expected a non-empty value for `group_id` but received {group_id!r}'
          )
        return await self._delete(
            f"/v1/group/{group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

    async def replace(self,
    *,
    name: str,
    description: Optional[str] | NotGiven = NOT_GIVEN,
    member_groups: Optional[List[str]] | NotGiven = NOT_GIVEN,
    member_users: Optional[List[str]] | NotGiven = NOT_GIVEN,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Group:
        """Create or replace group.

        If there is an existing group with the same name as the
        one specified in the request, will replace the existing group with the provided
        fields

        Args:
          name: Name of the group

          description: Textual description of the group

          member_groups: Ids of the groups this group inherits from

              An inheriting group has all the users contained in its member groups, as well as
              all of their inherited users

          member_users: Ids of users which belong to this group

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the group belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/group",
            body=await async_maybe_transform({
                "name": name,
                "description": description,
                "member_groups": member_groups,
                "member_users": member_users,
                "org_name": org_name,
            }, group_replace_params.GroupReplaceParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Group,
        )

class GroupResourceWithRawResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_raw_response_wrapper(
            group.create,
        )
        self.retrieve = to_raw_response_wrapper(
            group.retrieve,
        )
        self.update = to_raw_response_wrapper(
            group.update,
        )
        self.list = to_raw_response_wrapper(
            group.list,
        )
        self.delete = to_raw_response_wrapper(
            group.delete,
        )
        self.replace = to_raw_response_wrapper(
            group.replace,
        )

class AsyncGroupResourceWithRawResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_raw_response_wrapper(
            group.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            group.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            group.update,
        )
        self.list = async_to_raw_response_wrapper(
            group.list,
        )
        self.delete = async_to_raw_response_wrapper(
            group.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            group.replace,
        )

class GroupResourceWithStreamingResponse:
    def __init__(self, group: GroupResource) -> None:
        self._group = group

        self.create = to_streamed_response_wrapper(
            group.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            group.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            group.update,
        )
        self.list = to_streamed_response_wrapper(
            group.list,
        )
        self.delete = to_streamed_response_wrapper(
            group.delete,
        )
        self.replace = to_streamed_response_wrapper(
            group.replace,
        )

class AsyncGroupResourceWithStreamingResponse:
    def __init__(self, group: AsyncGroupResource) -> None:
        self._group = group

        self.create = async_to_streamed_response_wrapper(
            group.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            group.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            group.update,
        )
        self.list = async_to_streamed_response_wrapper(
            group.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            group.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            group.replace,
        )