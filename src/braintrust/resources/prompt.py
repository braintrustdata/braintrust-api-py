# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

from ..types import (
    prompt_list_params,
    prompt_create_params,
    prompt_update_params,
    prompt_replace_params,
    prompt_feedback_params,
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
from ..types.prompt_list_response import PromptListResponse
from ..types.prompt_create_response import PromptCreateResponse
from ..types.prompt_delete_response import PromptDeleteResponse
from ..types.prompt_update_response import PromptUpdateResponse
from ..types.prompt_replace_response import PromptReplaceResponse
from ..types.prompt_retrieve_response import PromptRetrieveResponse

__all__ = ["PromptResource", "AsyncPromptResource"]


class PromptResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptResourceWithRawResponse:
        return PromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptResourceWithStreamingResponse:
        return PromptResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_create_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptCreateResponse:
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
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptCreateResponse,
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
    ) -> PromptRetrieveResponse:
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
            cast_to=PromptRetrieveResponse,
        )

    def update(
        self,
        prompt_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_update_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptUpdateResponse:
        """Partially update a prompt object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          prompt_id: Prompt id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

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
                    "tags": tags,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptUpdateResponse,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
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
    ) -> SyncListObjects[PromptListResponse]:
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

          project_name: Name of the project to search for

          prompt_name: Name of the prompt to search for

          slug: Retrieve prompt with a specific slug

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/prompt",
            page=SyncListObjects[PromptListResponse],
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
                        "prompt_name": prompt_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            model=PromptListResponse,
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
    ) -> PromptDeleteResponse:
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
            cast_to=PromptDeleteResponse,
        )

    def feedback(
        self,
        prompt_id: str,
        *,
        feedback: Iterable[prompt_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of prompt events

        Args:
          prompt_id: Prompt id

          feedback: A list of prompt feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/prompt/{prompt_id}/feedback",
            body=maybe_transform({"feedback": feedback}, prompt_feedback_params.PromptFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_replace_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptReplaceResponse:
        """
        NOTE: This operation is deprecated and will be removed in a future revision of
        the API. Create or replace a new prompt. If there is an existing prompt in the
        project with the same slug as the one specified in the request, will return the
        existing prompt unmodified, will replace the existing prompt with the provided
        fields

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
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_replace_params.PromptReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptReplaceResponse,
        )


class AsyncPromptResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptResourceWithRawResponse:
        return AsyncPromptResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptResourceWithStreamingResponse:
        return AsyncPromptResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_create_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptCreateResponse:
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
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptCreateResponse,
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
    ) -> PromptRetrieveResponse:
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
            cast_to=PromptRetrieveResponse,
        )

    async def update(
        self,
        prompt_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_update_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptUpdateResponse:
        """Partially update a prompt object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          prompt_id: Prompt id

          description: Textual description of the prompt

          name: Name of the prompt

          prompt_data: The prompt, model, and its parameters

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
                    "tags": tags,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptUpdateResponse,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[PromptListResponse, AsyncListObjects[PromptListResponse]]:
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

          project_name: Name of the project to search for

          prompt_name: Name of the prompt to search for

          slug: Retrieve prompt with a specific slug

          starting_after: Pagination cursor id.

              For example, if the final item in the last page you fetched had an id of `foo`,
              pass `starting_after=foo` to fetch the next page. Note: you may only pass one of
              `starting_after` and `ending_before`

          version: Retrieve a snapshot of events from a past time

              The version id is essentially a filter on the latest event transaction id. You
              can use the `max_xact_id` returned by a past fetch as the version to reproduce
              that exact fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/prompt",
            page=AsyncListObjects[PromptListResponse],
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
                        "prompt_name": prompt_name,
                        "slug": slug,
                        "starting_after": starting_after,
                        "version": version,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            model=PromptListResponse,
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
    ) -> PromptDeleteResponse:
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
            cast_to=PromptDeleteResponse,
        )

    async def feedback(
        self,
        prompt_id: str,
        *,
        feedback: Iterable[prompt_feedback_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Log feedback for a set of prompt events

        Args:
          prompt_id: Prompt id

          feedback: A list of prompt feedback items

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not prompt_id:
            raise ValueError(f"Expected a non-empty value for `prompt_id` but received {prompt_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/prompt/{prompt_id}/feedback",
            body=await async_maybe_transform({"feedback": feedback}, prompt_feedback_params.PromptFeedbackParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        *,
        name: str,
        project_id: str,
        slug: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        prompt_data: Optional[prompt_replace_params.PromptData] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptReplaceResponse:
        """
        NOTE: This operation is deprecated and will be removed in a future revision of
        the API. Create or replace a new prompt. If there is an existing prompt in the
        project with the same slug as the one specified in the request, will return the
        existing prompt unmodified, will replace the existing prompt with the provided
        fields

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
                    "prompt_data": prompt_data,
                    "tags": tags,
                },
                prompt_replace_params.PromptReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptReplaceResponse,
        )


class PromptResourceWithRawResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.create = to_raw_response_wrapper(
            prompt.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prompt.retrieve,
        )
        self.update = to_raw_response_wrapper(
            prompt.update,
        )
        self.list = to_raw_response_wrapper(
            prompt.list,
        )
        self.delete = to_raw_response_wrapper(
            prompt.delete,
        )
        self.feedback = to_raw_response_wrapper(
            prompt.feedback,
        )
        self.replace = to_raw_response_wrapper(
            prompt.replace,
        )


class AsyncPromptResourceWithRawResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.create = async_to_raw_response_wrapper(
            prompt.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prompt.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            prompt.update,
        )
        self.list = async_to_raw_response_wrapper(
            prompt.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prompt.delete,
        )
        self.feedback = async_to_raw_response_wrapper(
            prompt.feedback,
        )
        self.replace = async_to_raw_response_wrapper(
            prompt.replace,
        )


class PromptResourceWithStreamingResponse:
    def __init__(self, prompt: PromptResource) -> None:
        self._prompt = prompt

        self.create = to_streamed_response_wrapper(
            prompt.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prompt.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            prompt.update,
        )
        self.list = to_streamed_response_wrapper(
            prompt.list,
        )
        self.delete = to_streamed_response_wrapper(
            prompt.delete,
        )
        self.feedback = to_streamed_response_wrapper(
            prompt.feedback,
        )
        self.replace = to_streamed_response_wrapper(
            prompt.replace,
        )


class AsyncPromptResourceWithStreamingResponse:
    def __init__(self, prompt: AsyncPromptResource) -> None:
        self._prompt = prompt

        self.create = async_to_streamed_response_wrapper(
            prompt.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prompt.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            prompt.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prompt.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prompt.delete,
        )
        self.feedback = async_to_streamed_response_wrapper(
            prompt.feedback,
        )
        self.replace = async_to_streamed_response_wrapper(
            prompt.replace,
        )
