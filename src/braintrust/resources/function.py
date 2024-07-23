# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

from ..types import (
    function_list_params,
    function_create_params,
    function_update_params,
    function_replace_params,
    function_feedback_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.function import Function

__all__ = ["FunctionResource", "AsyncFunctionResource"]


class FunctionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionResourceWithRawResponse:
        return FunctionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionResourceWithStreamingResponse:
        return FunctionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        function_data: function_create_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_create_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Create a new function.

        If there is an existing function in the project with the
        same slug as the one specified in the request, will return the existing function
        unmodified

        Args:
          name: Name of the prompt

          project_id: Unique identifier for the project that the prompt belongs under

          slug: Unique identifier for the prompt

          description: Textual description of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/function",
            body=maybe_transform(
                {
                    "function_data": function_data,
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Get a function object by its id

        Args:
          function_id: Function id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            f"/v1/function/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def update(
        self,
        function_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_data: function_update_params.FunctionData | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_update_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Partially update a function object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          function_id: Function id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._patch(
            f"/v1/function/{function_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "function_data": function_data,
                    "name": name,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        function_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[Function]:
        """List out all functions.

        The functions are sorted by creation date, with the most
        recently-created functions coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          function_name: Name of the function to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

          slug: Retrieve prompt with a specific slug

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          version: Retrieve prompt at a specific version.

              The version id can either be a transaction id (e.g. '1000192656880881099') or a
              version identifier (e.g. '81cd05ee665fdfb3').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/function",
            page=SyncListObjects[Function],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_name": function_name,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_name": project_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            model=Function,
        )

    def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Delete a function object by its id

        Args:
          function_id: Function id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._delete(
            f"/v1/function/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def feedback(
        self,
        function_id: str,
        *,
        feedback: Iterable[function_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of function events

        Args:
          function_id: Function id

          feedback: A list of function feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/function/{function_id}/feedback",
            body=maybe_transform({"feedback": feedback}, function_feedback_params.FunctionFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        *,
        function_data: function_replace_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_replace_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Create or replace function.

        If there is an existing function in the project with
        the same slug as the one specified in the request, will replace the existing
        function with the provided fields

        Args:
          name: Name of the prompt

          project_id: Unique identifier for the project that the prompt belongs under

          slug: Unique identifier for the prompt

          description: Textual description of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/function",
            body=maybe_transform(
                {
                    "function_data": function_data,
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_replace_params.FunctionReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )


class AsyncFunctionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionResourceWithRawResponse:
        return AsyncFunctionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionResourceWithStreamingResponse:
        return AsyncFunctionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        function_data: function_create_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_create_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Create a new function.

        If there is an existing function in the project with the
        same slug as the one specified in the request, will return the existing function
        unmodified

        Args:
          name: Name of the prompt

          project_id: Unique identifier for the project that the prompt belongs under

          slug: Unique identifier for the prompt

          description: Textual description of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/function",
            body=await async_maybe_transform(
                {
                    "function_data": function_data,
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_create_params.FunctionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    async def retrieve(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Get a function object by its id

        Args:
          function_id: Function id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            f"/v1/function/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    async def update(
        self,
        function_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_data: function_update_params.FunctionData | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_update_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Partially update a function object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          function_id: Function id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._patch(
            f"/v1/function/{function_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "function_data": function_data,
                    "name": name,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_update_params.FunctionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        function_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Function, AsyncListObjects[Function]]:
        """List out all functions.

        The functions are sorted by creation date, with the most
        recently-created functions coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          function_name: Name of the function to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          project_name: Name of the project to search for

          slug: Retrieve prompt with a specific slug

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          version: Retrieve prompt at a specific version.

              The version id can either be a transaction id (e.g. '1000192656880881099') or a
              version identifier (e.g. '81cd05ee665fdfb3').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/function",
            page=AsyncListObjects[Function],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "function_name": function_name,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "project_name": project_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    function_list_params.FunctionListParams,
                ),
            ),
            model=Function,
        )

    async def delete(
        self,
        function_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """
        Delete a function object by its id

        Args:
          function_id: Function id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._delete(
            f"/v1/function/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )

    async def feedback(
        self,
        function_id: str,
        *,
        feedback: Iterable[function_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of function events

        Args:
          function_id: Function id

          feedback: A list of function feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/function/{function_id}/feedback",
            body=await async_maybe_transform({"feedback": feedback}, function_feedback_params.FunctionFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        *,
        function_data: function_replace_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[function_replace_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Function:
        """Create or replace function.

        If there is an existing function in the project with
        the same slug as the one specified in the request, will replace the existing
        function with the provided fields

        Args:
          name: Name of the prompt

          project_id: Unique identifier for the project that the prompt belongs under

          slug: Unique identifier for the prompt

          description: Textual description of the prompt

          prompt_data: The prompt, model, and its parameters

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/function",
            body=await async_maybe_transform(
                {
                    "function_data": function_data,
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                function_replace_params.FunctionReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Function,
        )


class FunctionResourceWithRawResponse:
    def __init__(self, function: FunctionResource) -> None:
        self._function = function

        self.create = to_raw_response_wrapper(
            function.create,
        )
        self.retrieve = to_raw_response_wrapper(
            function.retrieve,
        )
        self.update = to_raw_response_wrapper(
            function.update,
        )
        self.list = to_raw_response_wrapper(
            function.list,
        )
        self.delete = to_raw_response_wrapper(
            function.delete,
        )
        self.feedback = to_raw_response_wrapper(
            function.feedback,
        )
        self.replace = to_raw_response_wrapper(
            function.replace,
        )


class AsyncFunctionResourceWithRawResponse:
    def __init__(self, function: AsyncFunctionResource) -> None:
        self._function = function

        self.create = async_to_raw_response_wrapper(
            function.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            function.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            function.update,
        )
        self.list = async_to_raw_response_wrapper(
            function.list,
        )
        self.delete = async_to_raw_response_wrapper(
            function.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            function.feedback,
        )
        self.replace = async_to_raw_response_wrapper(
            function.replace,
        )


class FunctionResourceWithStreamingResponse:
    def __init__(self, function: FunctionResource) -> None:
        self._function = function

        self.create = to_streamed_response_wrapper(
            function.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            function.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            function.update,
        )
        self.list = to_streamed_response_wrapper(
            function.list,
        )
        self.delete = to_streamed_response_wrapper(
            function.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            function.feedback,
        )
        self.replace = to_streamed_response_wrapper(
            function.replace,
        )


class AsyncFunctionResourceWithStreamingResponse:
    def __init__(self, function: AsyncFunctionResource) -> None:
        self._function = function

        self.create = async_to_streamed_response_wrapper(
            function.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            function.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            function.update,
        )
        self.list = async_to_streamed_response_wrapper(
            function.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            function.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            function.feedback,
        )
        self.replace = async_to_streamed_response_wrapper(
            function.replace,
        )
