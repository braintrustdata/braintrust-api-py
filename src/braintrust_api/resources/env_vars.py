# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    env_var_list_params,
    env_var_create_params,
    env_var_update_params,
    env_var_replace_params,
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
from .._base_client import make_request_options
from ..types.shared.env_var import EnvVar
from ..types.env_var_list_response import EnvVarListResponse

__all__ = ["EnvVarsResource", "AsyncEnvVarsResource"]


class EnvVarsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvVarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return EnvVarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvVarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return EnvVarsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        object_id: str,
        object_type: Literal["organization", "project", "function"],
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Create a new env_var.

        If there is an existing env_var with the same name as the
        one specified in the request, will return the existing env_var unmodified

        Args:
          name: The name of the environment variable

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/env_var",
            body=maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "value": value,
                },
                env_var_create_params.EnvVarCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    def retrieve(
        self,
        env_var_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """
        Get an env_var object by its id

        Args:
          env_var_id: EnvVar id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return self._get(
            f"/v1/env_var/{env_var_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    def update(
        self,
        env_var_id: str,
        *,
        name: str,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Partially update an env_var object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          env_var_id: EnvVar id

          name: The name of the environment variable

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return self._patch(
            f"/v1/env_var/{env_var_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                env_var_update_params.EnvVarUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    def list(
        self,
        *,
        env_var_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        object_id: str | NotGiven = NOT_GIVEN,
        object_type: Literal["organization", "project", "function"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVarListResponse:
        """List out all env_vars.

        The env_vars are sorted by creation date, with the most
        recently-created env_vars coming first

        Args:
          env_var_name: Name of the env_var to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/env_var",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "env_var_name": env_var_name,
                        "ids": ids,
                        "limit": limit,
                        "object_id": object_id,
                        "object_type": object_type,
                    },
                    env_var_list_params.EnvVarListParams,
                ),
            ),
            cast_to=EnvVarListResponse,
        )

    def delete(
        self,
        env_var_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """
        Delete an env_var object by its id

        Args:
          env_var_id: EnvVar id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return self._delete(
            f"/v1/env_var/{env_var_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    def replace(
        self,
        *,
        name: str,
        object_id: str,
        object_type: Literal["organization", "project", "function"],
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Create or replace env_var.

        If there is an existing env_var with the same name as
        the one specified in the request, will replace the existing env_var with the
        provided fields

        Args:
          name: The name of the environment variable

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/env_var",
            body=maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "value": value,
                },
                env_var_replace_params.EnvVarReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )


class AsyncEnvVarsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvVarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvVarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvVarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncEnvVarsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        object_id: str,
        object_type: Literal["organization", "project", "function"],
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Create a new env_var.

        If there is an existing env_var with the same name as the
        one specified in the request, will return the existing env_var unmodified

        Args:
          name: The name of the environment variable

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/env_var",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "value": value,
                },
                env_var_create_params.EnvVarCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    async def retrieve(
        self,
        env_var_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """
        Get an env_var object by its id

        Args:
          env_var_id: EnvVar id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return await self._get(
            f"/v1/env_var/{env_var_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    async def update(
        self,
        env_var_id: str,
        *,
        name: str,
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Partially update an env_var object.

        Specify the fields to update in the payload.
        Any object-type fields will be deep-merged with existing content. Currently we
        do not support removing fields or setting them to null.

        Args:
          env_var_id: EnvVar id

          name: The name of the environment variable

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return await self._patch(
            f"/v1/env_var/{env_var_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                env_var_update_params.EnvVarUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    async def list(
        self,
        *,
        env_var_name: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        object_id: str | NotGiven = NOT_GIVEN,
        object_type: Literal["organization", "project", "function"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVarListResponse:
        """List out all env_vars.

        The env_vars are sorted by creation date, with the most
        recently-created env_vars coming first

        Args:
          env_var_name: Name of the env_var to search for

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/env_var",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "env_var_name": env_var_name,
                        "ids": ids,
                        "limit": limit,
                        "object_id": object_id,
                        "object_type": object_type,
                    },
                    env_var_list_params.EnvVarListParams,
                ),
            ),
            cast_to=EnvVarListResponse,
        )

    async def delete(
        self,
        env_var_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """
        Delete an env_var object by its id

        Args:
          env_var_id: EnvVar id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not env_var_id:
            raise ValueError(f"Expected a non-empty value for `env_var_id` but received {env_var_id!r}")
        return await self._delete(
            f"/v1/env_var/{env_var_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )

    async def replace(
        self,
        *,
        name: str,
        object_id: str,
        object_type: Literal["organization", "project", "function"],
        value: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvVar:
        """Create or replace env_var.

        If there is an existing env_var with the same name as
        the one specified in the request, will replace the existing env_var with the
        provided fields

        Args:
          name: The name of the environment variable

          object_id: The id of the object the environment variable is scoped for

          object_type: The type of the object the environment variable is scoped for

          value: The value of the environment variable. Will be encrypted at rest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/env_var",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "object_id": object_id,
                    "object_type": object_type,
                    "value": value,
                },
                env_var_replace_params.EnvVarReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvVar,
        )


class EnvVarsResourceWithRawResponse:
    def __init__(self, env_vars: EnvVarsResource) -> None:
        self._env_vars = env_vars

        self.create = to_raw_response_wrapper(
            env_vars.create,
        )
        self.retrieve = to_raw_response_wrapper(
            env_vars.retrieve,
        )
        self.update = to_raw_response_wrapper(
            env_vars.update,
        )
        self.list = to_raw_response_wrapper(
            env_vars.list,
        )
        self.delete = to_raw_response_wrapper(
            env_vars.delete,
        )
        self.replace = to_raw_response_wrapper(
            env_vars.replace,
        )


class AsyncEnvVarsResourceWithRawResponse:
    def __init__(self, env_vars: AsyncEnvVarsResource) -> None:
        self._env_vars = env_vars

        self.create = async_to_raw_response_wrapper(
            env_vars.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            env_vars.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            env_vars.update,
        )
        self.list = async_to_raw_response_wrapper(
            env_vars.list,
        )
        self.delete = async_to_raw_response_wrapper(
            env_vars.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            env_vars.replace,
        )


class EnvVarsResourceWithStreamingResponse:
    def __init__(self, env_vars: EnvVarsResource) -> None:
        self._env_vars = env_vars

        self.create = to_streamed_response_wrapper(
            env_vars.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            env_vars.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            env_vars.update,
        )
        self.list = to_streamed_response_wrapper(
            env_vars.list,
        )
        self.delete = to_streamed_response_wrapper(
            env_vars.delete,
        )
        self.replace = to_streamed_response_wrapper(
            env_vars.replace,
        )


class AsyncEnvVarsResourceWithStreamingResponse:
    def __init__(self, env_vars: AsyncEnvVarsResource) -> None:
        self._env_vars = env_vars

        self.create = async_to_streamed_response_wrapper(
            env_vars.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            env_vars.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            env_vars.update,
        )
        self.list = async_to_streamed_response_wrapper(
            env_vars.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            env_vars.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            env_vars.replace,
        )
