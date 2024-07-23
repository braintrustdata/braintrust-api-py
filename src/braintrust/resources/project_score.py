# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    project_score_list_params,
    project_score_create_params,
    project_score_update_params,
    project_score_replace_params,
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
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.project_score import ProjectScore

__all__ = ["ProjectScoreResource", "AsyncProjectScoreResource"]


class ProjectScoreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectScoreResourceWithRawResponse:
        return ProjectScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectScoreResourceWithStreamingResponse:
        return ProjectScoreResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]],
        categories: project_score_create_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Create a new project_score.

        If there is an existing project_score in the project
        with the same name as the one specified in the request, will return the existing
        project_score unmodified

        Args:
          name: Name of the project score

          project_id: Unique identifier for the project that the project score belongs under

          score_type: The type of the configured score

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/project_score",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "score_type": score_type,
                    "categories": categories,
                    "description": description,
                },
                project_score_create_params.ProjectScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    def retrieve(
        self,
        project_score_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """
        Get a project_score object by its id

        Args:
          project_score_id: ProjectScore id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return self._get(
            f"/v1/project_score/{project_score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    def update(
        self,
        project_score_id: str,
        *,
        categories: project_score_update_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Partially update a project_score object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          project_score_id: ProjectScore id

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          name: Name of the project score

          score_type: The type of the configured score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return self._patch(
            f"/v1/project_score/{project_score_id}",
            body=maybe_transform(
                {
                    "categories": categories,
                    "description": description,
                    "name": name,
                    "score_type": score_type,
                },
                project_score_update_params.ProjectScoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        project_score_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[ProjectScore]:
        """List out all project_scores.

        The project_scores are sorted by creation date,
        with the most recently-created project_scores coming first

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

          project_score_name: Name of the project_score to search for

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
            "/v1/project_score",
            page=SyncListObjects[ProjectScore],
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
                        "project_name": project_name,
                        "project_score_name": project_score_name,
                        "starting_after": starting_after,
                    },
                    project_score_list_params.ProjectScoreListParams,
                ),
            ),
            model=ProjectScore,
        )

    def delete(
        self,
        project_score_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """
        Delete a project_score object by its id

        Args:
          project_score_id: ProjectScore id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return self._delete(
            f"/v1/project_score/{project_score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    def replace(
        self,
        *,
        name: str,
        project_id: str,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]],
        categories: project_score_replace_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Create or replace project_score.

        If there is an existing project_score in the
        project with the same name as the one specified in the request, will replace the
        existing project_score with the provided fields

        Args:
          name: Name of the project score

          project_id: Unique identifier for the project that the project score belongs under

          score_type: The type of the configured score

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/project_score",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "score_type": score_type,
                    "categories": categories,
                    "description": description,
                },
                project_score_replace_params.ProjectScoreReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )


class AsyncProjectScoreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectScoreResourceWithRawResponse:
        return AsyncProjectScoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectScoreResourceWithStreamingResponse:
        return AsyncProjectScoreResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]],
        categories: project_score_create_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Create a new project_score.

        If there is an existing project_score in the project
        with the same name as the one specified in the request, will return the existing
        project_score unmodified

        Args:
          name: Name of the project score

          project_id: Unique identifier for the project that the project score belongs under

          score_type: The type of the configured score

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/project_score",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "score_type": score_type,
                    "categories": categories,
                    "description": description,
                },
                project_score_create_params.ProjectScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    async def retrieve(
        self,
        project_score_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """
        Get a project_score object by its id

        Args:
          project_score_id: ProjectScore id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return await self._get(
            f"/v1/project_score/{project_score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    async def update(
        self,
        project_score_id: str,
        *,
        categories: project_score_update_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Partially update a project_score object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          project_score_id: ProjectScore id

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          name: Name of the project score

          score_type: The type of the configured score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return await self._patch(
            f"/v1/project_score/{project_score_id}",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "description": description,
                    "name": name,
                    "score_type": score_type,
                },
                project_score_update_params.ProjectScoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        project_score_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProjectScore, AsyncListObjects[ProjectScore]]:
        """List out all project_scores.

        The project_scores are sorted by creation date,
        with the most recently-created project_scores coming first

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

          project_score_name: Name of the project_score to search for

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
            "/v1/project_score",
            page=AsyncListObjects[ProjectScore],
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
                        "project_name": project_name,
                        "project_score_name": project_score_name,
                        "starting_after": starting_after,
                    },
                    project_score_list_params.ProjectScoreListParams,
                ),
            ),
            model=ProjectScore,
        )

    async def delete(
        self,
        project_score_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """
        Delete a project_score object by its id

        Args:
          project_score_id: ProjectScore id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_score_id:
            raise ValueError(f"Expected a non-empty value for `project_score_id` but received {project_score_id!r}")
        return await self._delete(
            f"/v1/project_score/{project_score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )

    async def replace(
        self,
        *,
        name: str,
        project_id: str,
        score_type: Optional[Literal["slider", "categorical", "weighted", "minimum"]],
        categories: project_score_replace_params.Categories | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectScore:
        """Create or replace project_score.

        If there is an existing project_score in the
        project with the same name as the one specified in the request, will replace the
        existing project_score with the provided fields

        Args:
          name: Name of the project score

          project_id: Unique identifier for the project that the project score belongs under

          score_type: The type of the configured score

          categories: For categorical-type project scores, the list of all categories

          description: Textual description of the project score

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/project_score",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "score_type": score_type,
                    "categories": categories,
                    "description": description,
                },
                project_score_replace_params.ProjectScoreReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectScore,
        )


class ProjectScoreResourceWithRawResponse:
    def __init__(self, project_score: ProjectScoreResource) -> None:
        self._project_score = project_score

        self.create = to_raw_response_wrapper(
            project_score.create,
        )
        self.retrieve = to_raw_response_wrapper(
            project_score.retrieve,
        )
        self.update = to_raw_response_wrapper(
            project_score.update,
        )
        self.list = to_raw_response_wrapper(
            project_score.list,
        )
        self.delete = to_raw_response_wrapper(
            project_score.delete,
        )
        self.replace = to_raw_response_wrapper(
            project_score.replace,
        )


class AsyncProjectScoreResourceWithRawResponse:
    def __init__(self, project_score: AsyncProjectScoreResource) -> None:
        self._project_score = project_score

        self.create = async_to_raw_response_wrapper(
            project_score.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            project_score.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            project_score.update,
        )
        self.list = async_to_raw_response_wrapper(
            project_score.list,
        )
        self.delete = async_to_raw_response_wrapper(
            project_score.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            project_score.replace,
        )


class ProjectScoreResourceWithStreamingResponse:
    def __init__(self, project_score: ProjectScoreResource) -> None:
        self._project_score = project_score

        self.create = to_streamed_response_wrapper(
            project_score.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            project_score.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            project_score.update,
        )
        self.list = to_streamed_response_wrapper(
            project_score.list,
        )
        self.delete = to_streamed_response_wrapper(
            project_score.delete,
        )
        self.replace = to_streamed_response_wrapper(
            project_score.replace,
        )


class AsyncProjectScoreResourceWithStreamingResponse:
    def __init__(self, project_score: AsyncProjectScoreResource) -> None:
        self._project_score = project_score

        self.create = async_to_streamed_response_wrapper(
            project_score.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            project_score.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            project_score.update,
        )
        self.list = async_to_streamed_response_wrapper(
            project_score.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            project_score.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            project_score.replace,
        )
