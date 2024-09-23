# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

import httpx

from ..types import (
    org_secret_list_params,
    org_secret_create_params,
    org_secret_update_params,
    org_secret_replace_params,
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
from ..types.shared.org_secret import OrgSecret

__all__ = ["OrgSecretResource", "AsyncOrgSecretResource"]


class OrgSecretResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return OrgSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return OrgSecretResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Create a new org_secret.

        If there is an existing org_secret with the same name
        as the one specified in the request, will return the existing org_secret
        unmodified

        Args:
          name: Name of the org secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the Org Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/org_secret",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_create_params.OrgSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    def retrieve(
        self,
        org_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """
        Get an org_secret object by its id

        Args:
          org_secret_id: OrgSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return self._get(
            f"/v1/org_secret/{org_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    def update(
        self,
        org_secret_id: str,
        *,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Partially update an org_secret object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          org_secret_id: OrgSecret id

          name: Name of the org secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return self._patch(
            f"/v1/org_secret/{org_secret_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_update_params.OrgSecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        org_secret_name: str | NotGiven = NOT_GIVEN,
        org_secret_type: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListObjects[OrgSecret]:
        """List out all org_secrets.

        The org_secrets are sorted by creation date, with the
        most recently-created org_secrets coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          org_secret_name: Name of the org_secret to search for

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
            "/v1/org_secret",
            page=SyncListObjects[OrgSecret],
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
                        "org_secret_name": org_secret_name,
                        "org_secret_type": org_secret_type,
                        "starting_after": starting_after,
                    },
                    org_secret_list_params.OrgSecretListParams,
                ),
            ),
            model=OrgSecret,
        )

    def delete(
        self,
        org_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """
        Delete an org_secret object by its id

        Args:
          org_secret_id: OrgSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return self._delete(
            f"/v1/org_secret/{org_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    def replace(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Create or replace org_secret.

        If there is an existing org_secret with the same
        name as the one specified in the request, will replace the existing org_secret
        with the provided fields

        Args:
          name: Name of the org secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the Org Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/org_secret",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_replace_params.OrgSecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )


class AsyncOrgSecretResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/braintrustdata/braintrust-api-py#with_streaming_response
        """
        return AsyncOrgSecretResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Create a new org_secret.

        If there is an existing org_secret with the same name
        as the one specified in the request, will return the existing org_secret
        unmodified

        Args:
          name: Name of the org secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the Org Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/org_secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_create_params.OrgSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    async def retrieve(
        self,
        org_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """
        Get an org_secret object by its id

        Args:
          org_secret_id: OrgSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return await self._get(
            f"/v1/org_secret/{org_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    async def update(
        self,
        org_secret_id: str,
        *,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Partially update an org_secret object.

        Specify the fields to update in the
        payload. Any object-type fields will be deep-merged with existing content.
        Currently we do not support removing fields or setting them to null.

        Args:
          org_secret_id: OrgSecret id

          name: Name of the org secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return await self._patch(
            f"/v1/org_secret/{org_secret_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_update_params.OrgSecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        ids: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        org_name: str | NotGiven = NOT_GIVEN,
        org_secret_name: str | NotGiven = NOT_GIVEN,
        org_secret_type: Union[str, List[str]] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrgSecret, AsyncListObjects[OrgSecret]]:
        """List out all org_secrets.

        The org_secrets are sorted by creation date, with the
        most recently-created org_secrets coming first

        Args:
          ending_before: Pagination cursor id.

              For example, if the initial item in the last page you fetched had an id of
              `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only
              pass one of `starting_after` and `ending_before`

          ids: Filter search results to a particular set of object IDs. To specify a list of
              IDs, include the query param multiple times

          limit: Limit the number of objects to return

          org_name: Filter search results to within a particular organization

          org_secret_name: Name of the org_secret to search for

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
            "/v1/org_secret",
            page=AsyncListObjects[OrgSecret],
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
                        "org_secret_name": org_secret_name,
                        "org_secret_type": org_secret_type,
                        "starting_after": starting_after,
                    },
                    org_secret_list_params.OrgSecretListParams,
                ),
            ),
            model=OrgSecret,
        )

    async def delete(
        self,
        org_secret_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """
        Delete an org_secret object by its id

        Args:
          org_secret_id: OrgSecret id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_secret_id:
            raise ValueError(f"Expected a non-empty value for `org_secret_id` but received {org_secret_id!r}")
        return await self._delete(
            f"/v1/org_secret/{org_secret_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )

    async def replace(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        org_name: Optional[str] | NotGiven = NOT_GIVEN,
        secret: Optional[str] | NotGiven = NOT_GIVEN,
        type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgSecret:
        """Create or replace org_secret.

        If there is an existing org_secret with the same
        name as the one specified in the request, will replace the existing org_secret
        with the provided fields

        Args:
          name: Name of the org secret

          org_name: For nearly all users, this parameter should be unnecessary. But in the rare case
              that your API key belongs to multiple organizations, you may specify the name of
              the organization the Org Secret belongs in.

          secret: Secret value. If omitted in a PUT request, the existing secret value will be
              left intact, not replaced with null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/org_secret",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "org_name": org_name,
                    "secret": secret,
                    "type": type,
                },
                org_secret_replace_params.OrgSecretReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSecret,
        )


class OrgSecretResourceWithRawResponse:
    def __init__(self, org_secret: OrgSecretResource) -> None:
        self._org_secret = org_secret

        self.create = to_raw_response_wrapper(
            org_secret.create,
        )
        self.retrieve = to_raw_response_wrapper(
            org_secret.retrieve,
        )
        self.update = to_raw_response_wrapper(
            org_secret.update,
        )
        self.list = to_raw_response_wrapper(
            org_secret.list,
        )
        self.delete = to_raw_response_wrapper(
            org_secret.delete,
        )
        self.replace = to_raw_response_wrapper(
            org_secret.replace,
        )


class AsyncOrgSecretResourceWithRawResponse:
    def __init__(self, org_secret: AsyncOrgSecretResource) -> None:
        self._org_secret = org_secret

        self.create = async_to_raw_response_wrapper(
            org_secret.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            org_secret.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            org_secret.update,
        )
        self.list = async_to_raw_response_wrapper(
            org_secret.list,
        )
        self.delete = async_to_raw_response_wrapper(
            org_secret.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            org_secret.replace,
        )


class OrgSecretResourceWithStreamingResponse:
    def __init__(self, org_secret: OrgSecretResource) -> None:
        self._org_secret = org_secret

        self.create = to_streamed_response_wrapper(
            org_secret.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            org_secret.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            org_secret.update,
        )
        self.list = to_streamed_response_wrapper(
            org_secret.list,
        )
        self.delete = to_streamed_response_wrapper(
            org_secret.delete,
        )
        self.replace = to_streamed_response_wrapper(
            org_secret.replace,
        )


class AsyncOrgSecretResourceWithStreamingResponse:
    def __init__(self, org_secret: AsyncOrgSecretResource) -> None:
        self._org_secret = org_secret

        self.create = async_to_streamed_response_wrapper(
            org_secret.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            org_secret.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            org_secret.update,
        )
        self.list = async_to_streamed_response_wrapper(
            org_secret.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            org_secret.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            org_secret.replace,
        )
