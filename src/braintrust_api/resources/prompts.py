# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    prompt_list_params,
    prompt_create_params,
    prompt_update_params,
    prompt_replace_params,
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
from ..types.shared.prompt import Prompt
from ..types.shared_params.prompt_data import PromptData

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return PromptsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Create a new prompt.

        If there is an existing prompt in the project with the same
        slug as the one specified in the request, will return the existing prompt
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
            "/v1/prompt",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "function_type": function_type,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def retrieve(
        self,
        prompt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Get a prompt object by its id

        Args:
          prompt_id: Prompt id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return self._get(
            f"/v1/prompt/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def update(
        self,
        prompt_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        slug: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Partially update a prompt object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          prompt_id: Prompt id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

          slug: Unique identifier for the prompt

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return self._patch(
            f"/v1/prompt/{prompt_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "prompt_data": prompt_data,
                    "slug": slug,
                    "tags": tags,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
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
        prompt_name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[Prompt]:
        """List out all prompts.

        The prompts are sorted by creation date, with the most
        recently-created prompts coming first

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

          prompt_name: Name of the prompt to search for

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
            "/v1/prompt",
            page=SyncListObjects[Prompt],
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
                        "prompt_name": prompt_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            model=Prompt,
        )

    def delete(
        self,
        prompt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Delete a prompt object by its id

        Args:
          prompt_id: Prompt id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return self._delete(
            f"/v1/prompt/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    def replace(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Create or replace prompt.

        If there is an existing prompt in the project with the
        same slug as the one specified in the request, will replace the existing prompt
        with the provided fields

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
            "/v1/prompt",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "function_type": function_type,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_replace_params.PromptReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Create a new prompt.

        If there is an existing prompt in the project with the same
        slug as the one specified in the request, will return the existing prompt
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
            "/v1/prompt",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "function_type": function_type,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def retrieve(
        self,
        prompt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Get a prompt object by its id

        Args:
          prompt_id: Prompt id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return await self._get(
            f"/v1/prompt/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def update(
        self,
        prompt_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        slug: Optional[str] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Partially update a prompt object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          prompt_id: Prompt id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

          slug: Unique identifier for the prompt

          tags: A list of tags for the prompt

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return await self._patch(
            f"/v1/prompt/{prompt_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "prompt_data": prompt_data,
                    "slug": slug,
                    "tags": tags,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
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
        prompt_name: str | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Prompt, AsyncListObjects[Prompt]]:
        """List out all prompts.

        The prompts are sorted by creation date, with the most
        recently-created prompts coming first

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

          prompt_name: Name of the prompt to search for

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
            "/v1/prompt",
            page=AsyncListObjects[Prompt],
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
                        "prompt_name": prompt_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            model=Prompt,
        )

    async def delete(
        self,
        prompt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """
        Delete a prompt object by its id

        Args:
          prompt_id: Prompt id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        return await self._delete(
            f"/v1/prompt/{prompt_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )

    async def replace(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        function_type: Optional[Literal["llm", "scorer", "task", "tool"]] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Prompt:
        """Create or replace prompt.

        If there is an existing prompt in the project with the
        same slug as the one specified in the request, will replace the existing prompt
        with the provided fields

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
            "/v1/prompt",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "slug": slug,
                    "description": description,
                    "function_type": function_type,
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_replace_params.PromptReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Prompt,
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_raw_response_wrapper(
            prompts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prompts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            prompts.update,
        )
        self.list = to_raw_response_wrapper(
            prompts.list,
        )
        self.delete = to_raw_response_wrapper(
            prompts.delete,
        )
        self.replace = to_raw_response_wrapper(
            prompts.replace,
        )


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_raw_response_wrapper(
            prompts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prompts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            prompts.update,
        )
        self.list = async_to_raw_response_wrapper(
            prompts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prompts.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            prompts.replace,
        )


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_streamed_response_wrapper(
            prompts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prompts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            prompts.update,
        )
        self.list = to_streamed_response_wrapper(
            prompts.list,
        )
        self.delete = to_streamed_response_wrapper(
            prompts.delete,
        )
        self.replace = to_streamed_response_wrapper(
            prompts.replace,
        )


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_streamed_response_wrapper(
            prompts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prompts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            prompts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prompts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prompts.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            prompts.replace,
        )
