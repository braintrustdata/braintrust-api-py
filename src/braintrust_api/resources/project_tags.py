# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

import httpx

from ..types import (
    project_tag_list_params,
    project_tag_create_params,
    project_tag_update_params,
    project_tag_replace_params,
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
from ..types.shared.project_tag import ProjectTag

__all__ = ["ProjectTagsResource", "AsyncProjectTagsResource"]


class ProjectTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return ProjectTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return ProjectTagsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Create a new project_tag.

        If there is an existing project_tag in the project
        with the same name as the one specified in the request, will return the existing
        project_tag unmodified

        Args:
          name: Name of the project tag

          project_id: Unique identifier for the project that the project tag belongs under

          color: Color of the tag for the UI

          description: Textual description of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/project_tag",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "color": color,
                    "description": description,
                },
                project_tag_create_params.ProjectTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    def retrieve(
        self,
        project_tag_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """
        Get a project_tag object by its id

        Args:
          project_tag_id: ProjectTag id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return self._get(
            f"/v1/project_tag/{project_tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    def update(
        self,
        project_tag_id: str,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Partially update a project_tag object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          project_tag_id: ProjectTag id

          color: Color of the tag for the UI

          description: Textual description of the project tag

          name: Name of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return self._patch(
            f"/v1/project_tag/{project_tag_id}",
            body=maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "name": name,
                },
                project_tag_update_params.ProjectTagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        project_tag_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[ProjectTag]:
        """List out all project_tags.

        The project_tags are sorted by creation date, with
        the most recently-created project_tags coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_id: Project id

          project_name: Name of the project to search for

          project_tag_name: Name of the project_tag to search for

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
            "/v1/project_tag",
            page=SyncListObjects[ProjectTag],
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
                        "project_id": project_id,
                        "project_name": project_name,
                        "project_tag_name": project_tag_name,
                        "starting_after": starting_after,
                    },
                    project_tag_list_params.ProjectTagListParams,
                ),
            ),
            model=ProjectTag,
        )

    def delete(
        self,
        project_tag_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """
        Delete a project_tag object by its id

        Args:
          project_tag_id: ProjectTag id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return self._delete(
            f"/v1/project_tag/{project_tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    def replace(
        self,
        *,
        name: str,
        project_id: str,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Create or replace project_tag.

        If there is an existing project_tag in the
        project with the same name as the one specified in the request, will replace the
        existing project_tag with the provided fields

        Args:
          name: Name of the project tag

          project_id: Unique identifier for the project that the project tag belongs under

          color: Color of the tag for the UI

          description: Textual description of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/project_tag",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "color": color,
                    "description": description,
                },
                project_tag_replace_params.ProjectTagReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )


class AsyncProjectTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncProjectTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Create a new project_tag.

        If there is an existing project_tag in the project
        with the same name as the one specified in the request, will return the existing
        project_tag unmodified

        Args:
          name: Name of the project tag

          project_id: Unique identifier for the project that the project tag belongs under

          color: Color of the tag for the UI

          description: Textual description of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/project_tag",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "color": color,
                    "description": description,
                },
                project_tag_create_params.ProjectTagCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    async def retrieve(
        self,
        project_tag_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """
        Get a project_tag object by its id

        Args:
          project_tag_id: ProjectTag id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return await self._get(
            f"/v1/project_tag/{project_tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    async def update(
        self,
        project_tag_id: str,
        *,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Partially update a project_tag object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          project_tag_id: ProjectTag id

          color: Color of the tag for the UI

          description: Textual description of the project tag

          name: Name of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return await self._patch(
            f"/v1/project_tag/{project_tag_id}",
            body=await async_maybe_transform(
                {
                    "color": color,
                    "description": description,
                    "name": name,
                },
                project_tag_update_params.ProjectTagUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        project_tag_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProjectTag, AsyncListObjects[ProjectTag]]:
        """List out all project_tags.

        The project_tags are sorted by creation date, with
        the most recently-created project_tags coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_id: Project id

          project_name: Name of the project to search for

          project_tag_name: Name of the project_tag to search for

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
            "/v1/project_tag",
            page=AsyncListObjects[ProjectTag],
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
                        "project_id": project_id,
                        "project_name": project_name,
                        "project_tag_name": project_tag_name,
                        "starting_after": starting_after,
                    },
                    project_tag_list_params.ProjectTagListParams,
                ),
            ),
            model=ProjectTag,
        )

    async def delete(
        self,
        project_tag_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """
        Delete a project_tag object by its id

        Args:
          project_tag_id: ProjectTag id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_tag_id:
            raise ValueError(f"Expected a non-empty value for `project_tag_id` but received {project_tag_id!r}")
        return await self._delete(
            f"/v1/project_tag/{project_tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )

    async def replace(
        self,
        *,
        name: str,
        project_id: str,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectTag:
        """Create or replace project_tag.

        If there is an existing project_tag in the
        project with the same name as the one specified in the request, will replace the
        existing project_tag with the provided fields

        Args:
          name: Name of the project tag

          project_id: Unique identifier for the project that the project tag belongs under

          color: Color of the tag for the UI

          description: Textual description of the project tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/project_tag",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "color": color,
                    "description": description,
                },
                project_tag_replace_params.ProjectTagReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTag,
        )


class ProjectTagsResourceWithRawResponse:
    def __init__(self, project_tags: ProjectTagsResource) -> None:
        self._project_tags = project_tags

        self.create = to_raw_response_wrapper(
            project_tags.create,
        )
        self.retrieve = to_raw_response_wrapper(
            project_tags.retrieve,
        )
        self.update = to_raw_response_wrapper(
            project_tags.update,
        )
        self.list = to_raw_response_wrapper(
            project_tags.list,
        )
        self.delete = to_raw_response_wrapper(
            project_tags.delete,
        )
        self.replace = to_raw_response_wrapper(
            project_tags.replace,
        )


class AsyncProjectTagsResourceWithRawResponse:
    def __init__(self, project_tags: AsyncProjectTagsResource) -> None:
        self._project_tags = project_tags

        self.create = async_to_raw_response_wrapper(
            project_tags.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            project_tags.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            project_tags.update,
        )
        self.list = async_to_raw_response_wrapper(
            project_tags.list,
        )
        self.delete = async_to_raw_response_wrapper(
            project_tags.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            project_tags.replace,
        )


class ProjectTagsResourceWithStreamingResponse:
    def __init__(self, project_tags: ProjectTagsResource) -> None:
        self._project_tags = project_tags

        self.create = to_streamed_response_wrapper(
            project_tags.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            project_tags.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            project_tags.update,
        )
        self.list = to_streamed_response_wrapper(
            project_tags.list,
        )
        self.delete = to_streamed_response_wrapper(
            project_tags.delete,
        )
        self.replace = to_streamed_response_wrapper(
            project_tags.replace,
        )


class AsyncProjectTagsResourceWithStreamingResponse:
    def __init__(self, project_tags: AsyncProjectTagsResource) -> None:
        self._project_tags = project_tags

        self.create = async_to_streamed_response_wrapper(
            project_tags.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            project_tags.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            project_tags.update,
        )
        self.list = async_to_streamed_response_wrapper(
            project_tags.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            project_tags.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            project_tags.replace,
        )
