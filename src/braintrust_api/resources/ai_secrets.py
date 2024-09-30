# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

import httpx

from ..types import (
    ai_secret_list_params,
    ai_secret_create_params,
    ai_secret_update_params,
    ai_secret_replace_params,
    ai_secret_find_and_delete_params,
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
from ..types.shared.a_i_secret import AISecret

__all__ = ["AISecretsResource", "AsyncAISecretsResource"]


class AISecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AISecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AISecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AISecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AISecretsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Create a new ai_secret.

        If there is an existing ai_secret with the same name as
        the one specified in the request, will return the existing ai_secret unmodified

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/ai_secret",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_create_params.AISecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def retrieve(
        self,
        ai_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Get an ai_secret object by its id

        Args:
          ai_secret_id: AiSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return self._get(
            f"/v1/ai_secret/{ai_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def update(
        self,
        ai_secret_id: str,
        *,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Partially update an ai_secret object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          ai_secret_id: AiSecret id

          name: Name of the AI secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return self._patch(
            f"/v1/ai_secret/{ai_secret_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_update_params.AISecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def list(
        self,
        *,
        ai_secret_name: str | NotGiven = NOT_GIVEN,
        ai_secret_type: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[AISecret]:
        """List out all ai_secrets.

        The ai_secrets are sorted by creation date, with the
        most recently-created ai_secrets coming first

        Args:
          ai_secret_name: Name of the ai_secret to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

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
            "/v1/ai_secret",
            page=SyncListObjects[AISecret],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ai_secret_name": ai_secret_name,
                        "ai_secret_type": ai_secret_type,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "starting_after": starting_after,
                    },
                    ai_secret_list_params.AISecretListParams,
                ),
            ),
            model=AISecret,
        )

    def delete(
        self,
        ai_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Delete an ai_secret object by its id

        Args:
          ai_secret_id: AiSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return self._delete(
            f"/v1/ai_secret/{ai_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def find_and_delete(
        self,
        *,
        name: str,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Delete a single ai_secret

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/ai_secret",
            body=maybe_transform(
                {
                    "name": name,
                    "org_name": org_name,
                },
                ai_secret_find_and_delete_params.AISecretFindAndDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def replace(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Create or replace ai_secret.

        If there is an existing ai_secret with the same
        name as the one specified in the request, will replace the existing ai_secret
        with the provided fields

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/ai_secret",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_replace_params.AISecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )


class AsyncAISecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAISecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAISecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAISecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncAISecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Create a new ai_secret.

        If there is an existing ai_secret with the same name as
        the one specified in the request, will return the existing ai_secret unmodified

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/ai_secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_create_params.AISecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    async def retrieve(
        self,
        ai_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Get an ai_secret object by its id

        Args:
          ai_secret_id: AiSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return await self._get(
            f"/v1/ai_secret/{ai_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    async def update(
        self,
        ai_secret_id: str,
        *,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Partially update an ai_secret object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          ai_secret_id: AiSecret id

          name: Name of the AI secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return await self._patch(
            f"/v1/ai_secret/{ai_secret_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_update_params.AISecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    def list(
        self,
        *,
        ai_secret_name: str | NotGiven = NOT_GIVEN,
        ai_secret_type: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AISecret, AsyncListObjects[AISecret]]:
        """List out all ai_secrets.

        The ai_secrets are sorted by creation date, with the
        most recently-created ai_secrets coming first

        Args:
          ai_secret_name: Name of the ai_secret to search for

          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

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
            "/v1/ai_secret",
            page=AsyncListObjects[AISecret],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ai_secret_name": ai_secret_name,
                        "ai_secret_type": ai_secret_type,
                        "ending_before": ending_before,
                        "ids": ids,
                        "limit": limit,
                        "org_name": org_name,
                        "starting_after": starting_after,
                    },
                    ai_secret_list_params.AISecretListParams,
                ),
            ),
            model=AISecret,
        )

    async def delete(
        self,
        ai_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Delete an ai_secret object by its id

        Args:
          ai_secret_id: AiSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ai_secret_id:
            raise ValueError(f"Expected a non-empty value for `ai_secret_id` but received {ai_secret_id!r}")
        return await self._delete(
            f"/v1/ai_secret/{ai_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    async def find_and_delete(
        self,
        *,
        name: str,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """
        Delete a single ai_secret

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/ai_secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "org_name": org_name,
                },
                ai_secret_find_and_delete_params.AISecretFindAndDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )

    async def replace(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[object]]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AISecret:
        """Create or replace ai_secret.

        If there is an existing ai_secret with the same
        name as the one specified in the request, will replace the existing ai_secret
        with the provided fields

        Args:
          name: Name of the AI secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the AI Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/ai_secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                ai_secret_replace_params.AISecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AISecret,
        )


class AISecretsResourceWithRawResponse:
    def __init__(self, ai_secrets: AISecretsResource) -> None:
        self._ai_secrets = ai_secrets

        self.create = to_raw_response_wrapper(
            ai_secrets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ai_secrets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ai_secrets.update,
        )
        self.list = to_raw_response_wrapper(
            ai_secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            ai_secrets.delete,
        )
        self.find_and_delete = to_raw_response_wrapper(
            ai_secrets.find_and_delete,
        )
        self.replace = to_raw_response_wrapper(
            ai_secrets.replace,
        )


class AsyncAISecretsResourceWithRawResponse:
    def __init__(self, ai_secrets: AsyncAISecretsResource) -> None:
        self._ai_secrets = ai_secrets

        self.create = async_to_raw_response_wrapper(
            ai_secrets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ai_secrets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ai_secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            ai_secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ai_secrets.delete,
        )
        self.find_and_delete = async_to_raw_response_wrapper(
            ai_secrets.find_and_delete,
        )
        self.replace = async_to_raw_response_wrapper(
            ai_secrets.replace,
        )


class AISecretsResourceWithStreamingResponse:
    def __init__(self, ai_secrets: AISecretsResource) -> None:
        self._ai_secrets = ai_secrets

        self.create = to_streamed_response_wrapper(
            ai_secrets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ai_secrets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ai_secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            ai_secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            ai_secrets.delete,
        )
        self.find_and_delete = to_streamed_response_wrapper(
            ai_secrets.find_and_delete,
        )
        self.replace = to_streamed_response_wrapper(
            ai_secrets.replace,
        )


class AsyncAISecretsResourceWithStreamingResponse:
    def __init__(self, ai_secrets: AsyncAISecretsResource) -> None:
        self._ai_secrets = ai_secrets

        self.create = async_to_streamed_response_wrapper(
            ai_secrets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ai_secrets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ai_secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ai_secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ai_secrets.delete,
        )
        self.find_and_delete = async_to_streamed_response_wrapper(
            ai_secrets.find_and_delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            ai_secrets.replace,
        )
