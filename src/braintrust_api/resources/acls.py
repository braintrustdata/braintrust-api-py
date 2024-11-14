# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    acl_list_params,
    acl_create_params,
    acl_batch_update_params,
    acl_find_and_delete_params,
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
from ..types.shared.acl import ACL
from ..types.shared.acl_batch_update_response import ACLBatchUpdateResponse

__all__ = ["ACLsResource", "AsyncACLsResource"]


class ACLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return ACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return ACLsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        permission: Optional[
            Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
        ]
        | NotGiven = NOT_GIVEN,
        restrict_object_type: Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "group",
                "role",
                "org_member",
                "project_log",
                "org_project",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """Create a new acl.

        If there is an existing acl with the same contents as the one
        specified in the request, will return the existing acl unmodified

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          group_id: Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          permission: Permission the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          restrict_object_type: When setting a permission directly, optionally restricts the permission grant to
              just the specified object type. Cannot be set alongside a `role_id`.

          role_id: Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          user_id: Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/acl",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "group_id": group_id,
                    "permission": permission,
                    "restrict_object_type": restrict_object_type,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    def retrieve(
        self,
        acl_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Get an acl object by its id

        Args:
          acl_id: Acl id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._get(
            f"/v1/acl/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    def list(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[ACL]:
        """List out all acls.

        The acls are sorted by creation date, with the most
        recently-created acls coming first

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

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
            "/v1/acl",
            page=SyncListObjects[ACL],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "object_id": object_id,
                        "object_type": object_type,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    acl_list_params.ACLListParams,
                ),
            ),
            model=ACL,
        )

    def delete(
        self,
        acl_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Delete an acl object by its id

        Args:
          acl_id: Acl id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._delete(
            f"/v1/acl/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    def batch_update(
        self,
        *,
        add_acls: Optional[Iterable[acl_batch_update_params.AddACL]] | NotGiven = NOT_GIVEN,
        remove_acls: Optional[Iterable[acl_batch_update_params.RemoveACL]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLBatchUpdateResponse:
        """Batch update acls.

        This operation is idempotent, so adding acls which already
        exist will have no effect, and removing acls which do not exist will have no
        effect.

        Args:
          add_acls: An ACL grants a certain permission or role to a certain user or group on an
              object.

              ACLs are inherited across the object hierarchy. So for example, if a user has
              read permissions on a project, they will also have read permissions on any
              experiment, dataset, etc. created within that project.

              To restrict a grant to a particular sub-object, you may specify
              `restrict_object_type` in the ACL, as part of a direct permission grant or as
              part of a role.

          remove_acls: An ACL grants a certain permission or role to a certain user or group on an
              object.

              ACLs are inherited across the object hierarchy. So for example, if a user has
              read permissions on a project, they will also have read permissions on any
              experiment, dataset, etc. created within that project.

              To restrict a grant to a particular sub-object, you may specify
              `restrict_object_type` in the ACL, as part of a direct permission grant or as
              part of a role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/acl/batch-update",
            body=maybe_transform(
                {
                    "add_acls": add_acls,
                    "remove_acls": remove_acls,
                },
                acl_batch_update_params.ACLBatchUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACLBatchUpdateResponse,
        )

    def find_and_delete(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        permission: Optional[
            Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
        ]
        | NotGiven = NOT_GIVEN,
        restrict_object_type: Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "group",
                "role",
                "org_member",
                "project_log",
                "org_project",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Delete a single acl

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          group_id: Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          permission: Permission the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          restrict_object_type: When setting a permission directly, optionally restricts the permission grant to
              just the specified object type. Cannot be set alongside a `role_id`.

          role_id: Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          user_id: Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/acl",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "group_id": group_id,
                    "permission": permission,
                    "restrict_object_type": restrict_object_type,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                acl_find_and_delete_params.ACLFindAndDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )


class AsyncACLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncACLsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        permission: Optional[
            Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
        ]
        | NotGiven = NOT_GIVEN,
        restrict_object_type: Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "group",
                "role",
                "org_member",
                "project_log",
                "org_project",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """Create a new acl.

        If there is an existing acl with the same contents as the one
        specified in the request, will return the existing acl unmodified

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          group_id: Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          permission: Permission the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          restrict_object_type: When setting a permission directly, optionally restricts the permission grant to
              just the specified object type. Cannot be set alongside a `role_id`.

          role_id: Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          user_id: Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/acl",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "group_id": group_id,
                    "permission": permission,
                    "restrict_object_type": restrict_object_type,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    async def retrieve(
        self,
        acl_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Get an acl object by its id

        Args:
          acl_id: Acl id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._get(
            f"/v1/acl/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    def list(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ACL, AsyncListObjects[ACL]]:
        """List out all acls.

        The acls are sorted by creation date, with the most
        recently-created acls coming first

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

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
            "/v1/acl",
            page=AsyncListObjects[ACL],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "object_id": object_id,
                        "object_type": object_type,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    acl_list_params.ACLListParams,
                ),
            ),
            model=ACL,
        )

    async def delete(
        self,
        acl_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Delete an acl object by its id

        Args:
          acl_id: Acl id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._delete(
            f"/v1/acl/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )

    async def batch_update(
        self,
        *,
        add_acls: Optional[Iterable[acl_batch_update_params.AddACL]] | NotGiven = NOT_GIVEN,
        remove_acls: Optional[Iterable[acl_batch_update_params.RemoveACL]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLBatchUpdateResponse:
        """Batch update acls.

        This operation is idempotent, so adding acls which already
        exist will have no effect, and removing acls which do not exist will have no
        effect.

        Args:
          add_acls: An ACL grants a certain permission or role to a certain user or group on an
              object.

              ACLs are inherited across the object hierarchy. So for example, if a user has
              read permissions on a project, they will also have read permissions on any
              experiment, dataset, etc. created within that project.

              To restrict a grant to a particular sub-object, you may specify
              `restrict_object_type` in the ACL, as part of a direct permission grant or as
              part of a role.

          remove_acls: An ACL grants a certain permission or role to a certain user or group on an
              object.

              ACLs are inherited across the object hierarchy. So for example, if a user has
              read permissions on a project, they will also have read permissions on any
              experiment, dataset, etc. created within that project.

              To restrict a grant to a particular sub-object, you may specify
              `restrict_object_type` in the ACL, as part of a direct permission grant or as
              part of a role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/acl/batch-update",
            body=await async_maybe_transform(
                {
                    "add_acls": add_acls,
                    "remove_acls": remove_acls,
                },
                acl_batch_update_params.ACLBatchUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACLBatchUpdateResponse,
        )

    async def find_and_delete(
        self,
        *,
        object_id: str,
        object_type: Literal[
            "organization",
            "project",
            "experiment",
            "dataset",
            "prompt",
            "prompt_session",
            "group",
            "role",
            "org_member",
            "project_log",
            "org_project",
        ],
        group_id: Optional[str] | NotGiven = NOT_GIVEN,
        permission: Optional[
            Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"]
        ]
        | NotGiven = NOT_GIVEN,
        restrict_object_type: Optional[
            Literal[
                "organization",
                "project",
                "experiment",
                "dataset",
                "prompt",
                "prompt_session",
                "group",
                "role",
                "org_member",
                "project_log",
                "org_project",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        role_id: Optional[str] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Delete a single acl

        Args:
          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          group_id: Id of the group the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          permission: Permission the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          restrict_object_type: When setting a permission directly, optionally restricts the permission grant to
              just the specified object type. Cannot be set alongside a `role_id`.

          role_id: Id of the role the ACL grants. Exactly one of `permission` and `role_id` will be
              provided

          user_id: Id of the user the ACL applies to. Exactly one of `user_id` and `group_id` will
              be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/acl",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "group_id": group_id,
                    "permission": permission,
                    "restrict_object_type": restrict_object_type,
                    "role_id": role_id,
                    "user_id": user_id,
                },
                acl_find_and_delete_params.ACLFindAndDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ACL,
        )


class ACLsResourceWithRawResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_raw_response_wrapper(
            acls.create,
        )
        self.retrieve = to_raw_response_wrapper(
            acls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            acls.list,
        )
        self.delete = to_raw_response_wrapper(
            acls.delete,
        )
        self.batch_update = to_raw_response_wrapper(
            acls.batch_update,
        )
        self.find_and_delete = to_raw_response_wrapper(
            acls.find_and_delete,
        )


class AsyncACLsResourceWithRawResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_raw_response_wrapper(
            acls.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            acls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            acls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            acls.delete,
        )
        self.batch_update = async_to_raw_response_wrapper(
            acls.batch_update,
        )
        self.find_and_delete = async_to_raw_response_wrapper(
            acls.find_and_delete,
        )


class ACLsResourceWithStreamingResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_streamed_response_wrapper(
            acls.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            acls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = to_streamed_response_wrapper(
            acls.delete,
        )
        self.batch_update = to_streamed_response_wrapper(
            acls.batch_update,
        )
        self.find_and_delete = to_streamed_response_wrapper(
            acls.find_and_delete,
        )


class AsyncACLsResourceWithStreamingResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_streamed_response_wrapper(
            acls.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            acls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            acls.delete,
        )
        self.batch_update = async_to_streamed_response_wrapper(
            acls.batch_update,
        )
        self.find_and_delete = async_to_streamed_response_wrapper(
            acls.find_and_delete,
        )
