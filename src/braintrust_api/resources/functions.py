# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    function_list_params,
    function_create_params,
    function_invoke_params,
    function_update_params,
    function_replace_params,
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
from ..types.shared.function import Function
from ..types.shared_params.prompt_data import PromptData

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        function_data: function_create_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_schema: Optional[function_create_params.FunctionSchema] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        origin: Optional[function_create_params.Origin] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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

          function_schema: JSON schema for the function's parameters and return type

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
                    "function_schema": function_schema,
                    "function_type": function_type,
                    "origin": origin,
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
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
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

          project_id: Project id

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
                        "project_id": project_id,
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

    def invoke(
        self,
        function_id: str,
        *,
        input: Optional[object] | NotGiven = NOT_GIVEN,
        messages: Iterable[function_invoke_params.Message] | NotGiven = NOT_GIVEN,
        mode: Optional[Literal["auto", "parallel"]] | NotGiven = NOT_GIVEN,
        parent: function_invoke_params.Parent | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Invoke a function.

        Args:
          function_id: Function id

          input: Argument to the function, which can be any JSON serializable value

          messages: If the function is an LLM, additional messages to pass along to it

          mode: The mode format of the returned value (defaults to 'auto')

          parent: Options for tracing the function call

          stream: Whether to stream the response. If true, results will be returned in the
              Braintrust SSE format.

          version: The version of the function

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._post(
            f"/v1/function/{function_id}/invoke",
            body=maybe_transform(
                {
                    "input": input,
                    "messages": messages,
                    "mode": mode,
                    "parent": parent,
                    "stream": stream,
                    "version": version,
                },
                function_invoke_params.FunctionInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def replace(
        self,
        *,
        function_data: function_replace_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_schema: Optional[function_replace_params.FunctionSchema] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        origin: Optional[function_replace_params.Origin] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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

          function_schema: JSON schema for the function's parameters and return type

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
                    "function_schema": function_schema,
                    "function_type": function_type,
                    "origin": origin,
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


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        function_data: function_create_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_schema: Optional[function_create_params.FunctionSchema] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        origin: Optional[function_create_params.Origin] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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

          function_schema: JSON schema for the function's parameters and return type

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
                    "function_schema": function_schema,
                    "function_type": function_type,
                    "origin": origin,
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
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
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

          project_id: Project id

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
                        "project_id": project_id,
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

    async def invoke(
        self,
        function_id: str,
        *,
        input: Optional[object] | NotGiven = NOT_GIVEN,
        messages: Iterable[function_invoke_params.Message] | NotGiven = NOT_GIVEN,
        mode: Optional[Literal["auto", "parallel"]] | NotGiven = NOT_GIVEN,
        parent: function_invoke_params.Parent | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Invoke a function.

        Args:
          function_id: Function id

          input: Argument to the function, which can be any JSON serializable value

          messages: If the function is an LLM, additional messages to pass along to it

          mode: The mode format of the returned value (defaults to 'auto')

          parent: Options for tracing the function call

          stream: Whether to stream the response. If true, results will be returned in the
              Braintrust SSE format.

          version: The version of the function

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._post(
            f"/v1/function/{function_id}/invoke",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "messages": messages,
                    "mode": mode,
                    "parent": parent,
                    "stream": stream,
                    "version": version,
                },
                function_invoke_params.FunctionInvokeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def replace(
        self,
        *,
        function_data: function_replace_params.FunctionData,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_schema: Optional[function_replace_params.FunctionSchema] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        origin: Optional[function_replace_params.Origin] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
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

          function_schema: JSON schema for the function's parameters and return type

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
                    "function_schema": function_schema,
                    "function_type": function_type,
                    "origin": origin,
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


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            functions.update,
        )
        self.list = to_raw_response_wrapper(
            functions.list,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )
        self.invoke = to_raw_response_wrapper(
            functions.invoke,
        )
        self.replace = to_raw_response_wrapper(
            functions.replace,
        )


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_raw_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            functions.update,
        )
        self.list = async_to_raw_response_wrapper(
            functions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )
        self.invoke = async_to_raw_response_wrapper(
            functions.invoke,
        )
        self.replace = async_to_raw_response_wrapper(
            functions.replace,
        )


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.create = to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            functions.update,
        )
        self.list = to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )
        self.invoke = to_streamed_response_wrapper(
            functions.invoke,
        )
        self.replace = to_streamed_response_wrapper(
            functions.replace,
        )


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.create = async_to_streamed_response_wrapper(
            functions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            functions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            functions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
        self.invoke = async_to_streamed_response_wrapper(
            functions.invoke,
        )
        self.replace = async_to_streamed_response_wrapper(
            functions.replace,
        )
