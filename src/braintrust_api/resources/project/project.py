# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .logs import LogsResource, AsyncLogsResource

from ..._compat import cached_property

from ...types.shared.project import Project

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing import Optional, Union, List

from ...pagination import SyncListObjects, AsyncListObjects

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types import project_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types import project_create_params
from ...types import project_update_params
from ...types import project_list_params
from .logs import LogsResource, AsyncLogsResource, LogsResourceWithRawResponse, AsyncLogsResourceWithRawResponse, LogsResourceWithStreamingResponse, AsyncLogsResourceWithStreamingResponse

__all__ = ["ProjectResource", "AsyncProjectResource"]

class ProjectResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        return ProjectResourceWithStreamingResponse(self)

    def create(self,
    *,
    name: str,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """Create a new project.

        If there is an existing project with the same name as the
        one specified in the request, will return the existing project unmodified

        Args:
          name: Name of the project

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the project belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/project",
            body=maybe_transform({
                "name": name,
                "org_name": org_name,
            }, project_create_params.ProjectCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def retrieve(self,
    project_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """
        Get a project object by its id

        Args:
          project_id: Project id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return self._get(
            f"/v1/project/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def update(self,
    project_id: str,
    *,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    settings: Optional[project_update_params.Settings] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """Partially update a project object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          project_id: Project id

          name: Name of the project

          settings: Project settings. Patch operations replace all settings, so make sure you
              include all settings you want to keep.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return self._patch(
            f"/v1/project/{project_id}",
            body=maybe_transform({
                "name": name,
                "settings": settings,
            }, project_update_params.ProjectUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def list(self,
    *,
    ending_before: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    project_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncListObjects[Project]:
        """List out all projects.

        The projects are sorted by creation date, with the most
        recently-created projects coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

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
            "/v1/project",
            page = SyncListObjects[Project],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "project_name": project_name,
                "starting_after": starting_after,
            }, project_list_params.ProjectListParams)),
            model=Project,
        )

    def delete(self,
    project_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """
        Delete a project object by its id

        Args:
          project_id: Project id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return self._delete(
            f"/v1/project/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        return AsyncProjectResourceWithStreamingResponse(self)

    async def create(self,
    *,
    name: str,
    org_name: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """Create a new project.

        If there is an existing project with the same name as the
        one specified in the request, will return the existing project unmodified

        Args:
          name: Name of the project

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the project belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/project",
            body=await async_maybe_transform({
                "name": name,
                "org_name": org_name,
            }, project_create_params.ProjectCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    async def retrieve(self,
    project_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """
        Get a project object by its id

        Args:
          project_id: Project id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return await self._get(
            f"/v1/project/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    async def update(self,
    project_id: str,
    *,
    name: Optional[str] | NotGiven = NOT_GIVEN,
    settings: Optional[project_update_params.Settings] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """Partially update a project object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          project_id: Project id

          name: Name of the project

          settings: Project settings. Patch operations replace all settings, so make sure you
              include all settings you want to keep.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return await self._patch(
            f"/v1/project/{project_id}",
            body=await async_maybe_transform({
                "name": name,
                "settings": settings,
            }, project_update_params.ProjectUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def list(self,
    *,
    ending_before: str | NotGiven = NOT_GIVEN,
    ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
    limit: int | NotGiven = NOT_GIVEN,
    org_name: str | NotGiven = NOT_GIVEN,
    project_name: str | NotGiven = NOT_GIVEN,
    starting_after: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Project, AsyncListObjects[Project]]:
        """List out all projects.

        The projects are sorted by creation date, with the most
        recently-created projects coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

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
            "/v1/project",
            page = AsyncListObjects[Project],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "ending_before": ending_before,
                "ids": ids,
                "limit": limit,
                "org_name": org_name,
                "project_name": project_name,
                "starting_after": starting_after,
            }, project_list_params.ProjectListParams)),
            model=Project,
        )

    async def delete(self,
    project_id: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Project:
        """
        Delete a project object by its id

        Args:
          project_id: Project id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
          raise ValueError(
            f'Expected a non-empty value for `project_id` but received {project_id!r}'
          )
        return await self._delete(
            f"/v1/project/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.create = to_raw_response_wrapper(
            project.create,
        )
        self.retrieve = to_raw_response_wrapper(
            project.retrieve,
        )
        self.update = to_raw_response_wrapper(
            project.update,
        )
        self.list = to_raw_response_wrapper(
            project.list,
        )
        self.delete = to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._project.logs)

class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.create = async_to_raw_response_wrapper(
            project.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            project.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            project.update,
        )
        self.list = async_to_raw_response_wrapper(
            project.list,
        )
        self.delete = async_to_raw_response_wrapper(
            project.delete,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._project.logs)

class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.create = to_streamed_response_wrapper(
            project.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            project.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            project.update,
        )
        self.list = to_streamed_response_wrapper(
            project.list,
        )
        self.delete = to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._project.logs)

class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.create = async_to_streamed_response_wrapper(
            project.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            project.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            project.update,
        )
        self.list = async_to_streamed_response_wrapper(
            project.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            project.delete,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._project.logs)