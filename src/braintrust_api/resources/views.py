# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    view_list_params,
    view_create_params,
    view_delete_params,
    view_update_params,
    view_replace_params,
    view_retrieve_params,
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
from ..types.shared.view import View
from ..types.shared_params.view_data import ViewData
from ..types.shared_params.view_options import ViewOptions

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
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
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ],
        deleted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Create a new view.

        If there is an existing view with the same name as the one
        specified in the request, will return the existing view unmodified

        Args:
          name: Name of the view

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          view_type: Type of table that the view corresponds to.

          deleted_at: Date of role deletion, or null if the role is still active

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/view",
            body=maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "view_type": view_type,
                    "deleted_at": deleted_at,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    def retrieve(
        self,
        view_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """
        Get a view object by its id

        Args:
          view_id: View id

          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            f"/v1/view/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "object_id": object_id,
                        "object_type": object_type,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
            ),
            cast_to=View,
        )

    def update(
        self,
        view_id: str,
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
        name: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Partially update a view object.

        Specify the fields to update in the payload. Any
        object-type fields will be deep-merged with existing content. Currently we do
        not support removing fields or setting them to null.

        Args:
          view_id: View id

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          name: Name of the view

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          view_type: Type of table that the view corresponds to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._patch(
            f"/v1/view/{view_id}",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "name": name,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
        view_name: str | NotGiven = NOT_GIVEN,
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[View]:
        """List out all views.

        The views are sorted by creation date, with the most
        recently-created views coming first

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

          view_name: Name of the view to search for

          view_type: Type of table that the view corresponds to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/view",
            page=SyncListObjects[View],
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
                        "view_name": view_name,
                        "view_type": view_type,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            model=View,
        )

    def delete(
        self,
        view_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """
        Delete a view object by its id

        Args:
          view_id: View id

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._delete(
            f"/v1/view/{view_id}",
            body=maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                },
                view_delete_params.ViewDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    def replace(
        self,
        *,
        name: str,
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
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ],
        deleted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Create or replace view.

        If there is an existing view with the same name as the
        one specified in the request, will replace the existing view with the provided
        fields

        Args:
          name: Name of the view

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          view_type: Type of table that the view corresponds to.

          deleted_at: Date of role deletion, or null if the role is still active

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/view",
            body=maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "view_type": view_type,
                    "deleted_at": deleted_at,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                },
                view_replace_params.ViewReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )


class AsyncViewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
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
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ],
        deleted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Create a new view.

        If there is an existing view with the same name as the one
        specified in the request, will return the existing view unmodified

        Args:
          name: Name of the view

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          view_type: Type of table that the view corresponds to.

          deleted_at: Date of role deletion, or null if the role is still active

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/view",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "view_type": view_type,
                    "deleted_at": deleted_at,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    async def retrieve(
        self,
        view_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """
        Get a view object by its id

        Args:
          view_id: View id

          object_id: The id of the object the ACL applies to

          object_type: The object type that the ACL applies to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            f"/v1/view/{view_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "object_id": object_id,
                        "object_type": object_type,
                    },
                    view_retrieve_params.ViewRetrieveParams,
                ),
            ),
            cast_to=View,
        )

    async def update(
        self,
        view_id: str,
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
        name: Optional[str] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Partially update a view object.

        Specify the fields to update in the payload. Any
        object-type fields will be deep-merged with existing content. Currently we do
        not support removing fields or setting them to null.

        Args:
          view_id: View id

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          name: Name of the view

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          view_type: Type of table that the view corresponds to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._patch(
            f"/v1/view/{view_id}",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                    "name": name,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
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
        view_name: str | NotGiven = NOT_GIVEN,
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[View, AsyncListObjects[View]]:
        """List out all views.

        The views are sorted by creation date, with the most
        recently-created views coming first

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

          view_name: Name of the view to search for

          view_type: Type of table that the view corresponds to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/view",
            page=AsyncListObjects[View],
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
                        "view_name": view_name,
                        "view_type": view_type,
                    },
                    view_list_params.ViewListParams,
                ),
            ),
            model=View,
        )

    async def delete(
        self,
        view_id: str,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """
        Delete a view object by its id

        Args:
          view_id: View id

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._delete(
            f"/v1/view/{view_id}",
            body=await async_maybe_transform(
                {
                    "object_id": object_id,
                    "object_type": object_type,
                },
                view_delete_params.ViewDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )

    async def replace(
        self,
        *,
        name: str,
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
        view_type: Optional[
            Literal["projects", "logs", "experiments", "datasets", "prompts", "playgrounds", "experiment", "dataset"]
        ],
        deleted_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        options: Optional[ViewOptions] | NotGiven = NOT_GIVEN,
        user_id: Optional[str] | NotGiven = NOT_GIVEN,
        view_data: Optional[ViewData] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> View:
        """Create or replace view.

        If there is an existing view with the same name as the
        one specified in the request, will replace the existing view with the provided
        fields

        Args:
          name: Name of the view

          object_id: The id of the object the view applies to

          object_type: The object type that the ACL applies to

          view_type: Type of table that the view corresponds to.

          deleted_at: Date of role deletion, or null if the role is still active

          options: Options for the view in the app

          user_id: Identifies the user who created the view

          view_data: The view definition

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/view",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "view_type": view_type,
                    "deleted_at": deleted_at,
                    "options": options,
                    "user_id": user_id,
                    "view_data": view_data,
                },
                view_replace_params.ViewReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=View,
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = to_raw_response_wrapper(
            views.update,
        )
        self.list = to_raw_response_wrapper(
            views.list,
        )
        self.delete = to_raw_response_wrapper(
            views.delete,
        )
        self.replace = to_raw_response_wrapper(
            views.replace,
        )


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_raw_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            views.update,
        )
        self.list = async_to_raw_response_wrapper(
            views.list,
        )
        self.delete = async_to_raw_response_wrapper(
            views.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            views.replace,
        )


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            views.update,
        )
        self.list = to_streamed_response_wrapper(
            views.list,
        )
        self.delete = to_streamed_response_wrapper(
            views.delete,
        )
        self.replace = to_streamed_response_wrapper(
            views.replace,
        )


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_streamed_response_wrapper(
            views.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            views.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            views.update,
        )
        self.list = async_to_streamed_response_wrapper(
            views.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            views.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            views.replace,
        )
