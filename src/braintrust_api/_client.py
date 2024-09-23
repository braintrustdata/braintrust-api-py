# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Braintrust",
    "AsyncBraintrust",
    "Client",
    "AsyncClient",
]


class Braintrust(SyncAPIClient):
    top_level: resources.TopLevelResource
    project: resources.ProjectResource
    experiment: resources.ExperimentResource
    dataset: resources.DatasetResource
    prompt: resources.PromptResource
    role: resources.RoleResource
    group: resources.GroupResource
    acl: resources.ACLResource
    user: resources.UserResource
    project_score: resources.ProjectScoreResource
    project_tag: resources.ProjectTagResource
    function: resources.FunctionResource
    view: resources.ViewResource
    organization: resources.OrganizationResource
    api_key_resource: resources.APIKeyResourceResource
    org_secret: resources.OrgSecretResource
    with_raw_response: BraintrustWithRawResponse
    with_streaming_response: BraintrustWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous braintrust client instance.

        This automatically infers the `api_key` argument from the `BRAINTRUST_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAINTRUST_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BRAINTRUST_BASE_URL")
        if base_url is None:
            base_url = f"https://api.braintrust.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.top_level = resources.TopLevelResource(self)
        self.project = resources.ProjectResource(self)
        self.experiment = resources.ExperimentResource(self)
        self.dataset = resources.DatasetResource(self)
        self.prompt = resources.PromptResource(self)
        self.role = resources.RoleResource(self)
        self.group = resources.GroupResource(self)
        self.acl = resources.ACLResource(self)
        self.user = resources.UserResource(self)
        self.project_score = resources.ProjectScoreResource(self)
        self.project_tag = resources.ProjectTagResource(self)
        self.function = resources.FunctionResource(self)
        self.view = resources.ViewResource(self)
        self.organization = resources.OrganizationResource(self)
        self.api_key_resource = resources.APIKeyResourceResource(self)
        self.org_secret = resources.OrgSecretResource(self)
        self.with_raw_response = BraintrustWithRawResponse(self)
        self.with_streaming_response = BraintrustWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBraintrust(AsyncAPIClient):
    top_level: resources.AsyncTopLevelResource
    project: resources.AsyncProjectResource
    experiment: resources.AsyncExperimentResource
    dataset: resources.AsyncDatasetResource
    prompt: resources.AsyncPromptResource
    role: resources.AsyncRoleResource
    group: resources.AsyncGroupResource
    acl: resources.AsyncACLResource
    user: resources.AsyncUserResource
    project_score: resources.AsyncProjectScoreResource
    project_tag: resources.AsyncProjectTagResource
    function: resources.AsyncFunctionResource
    view: resources.AsyncViewResource
    organization: resources.AsyncOrganizationResource
    api_key_resource: resources.AsyncAPIKeyResourceResource
    org_secret: resources.AsyncOrgSecretResource
    with_raw_response: AsyncBraintrustWithRawResponse
    with_streaming_response: AsyncBraintrustWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async braintrust client instance.

        This automatically infers the `api_key` argument from the `BRAINTRUST_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAINTRUST_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BRAINTRUST_BASE_URL")
        if base_url is None:
            base_url = f"https://api.braintrust.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.top_level = resources.AsyncTopLevelResource(self)
        self.project = resources.AsyncProjectResource(self)
        self.experiment = resources.AsyncExperimentResource(self)
        self.dataset = resources.AsyncDatasetResource(self)
        self.prompt = resources.AsyncPromptResource(self)
        self.role = resources.AsyncRoleResource(self)
        self.group = resources.AsyncGroupResource(self)
        self.acl = resources.AsyncACLResource(self)
        self.user = resources.AsyncUserResource(self)
        self.project_score = resources.AsyncProjectScoreResource(self)
        self.project_tag = resources.AsyncProjectTagResource(self)
        self.function = resources.AsyncFunctionResource(self)
        self.view = resources.AsyncViewResource(self)
        self.organization = resources.AsyncOrganizationResource(self)
        self.api_key_resource = resources.AsyncAPIKeyResourceResource(self)
        self.org_secret = resources.AsyncOrgSecretResource(self)
        self.with_raw_response = AsyncBraintrustWithRawResponse(self)
        self.with_streaming_response = AsyncBraintrustWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BraintrustWithRawResponse:
    def __init__(self, client: Braintrust) -> None:
        self.top_level = resources.TopLevelResourceWithRawResponse(client.top_level)
        self.project = resources.ProjectResourceWithRawResponse(client.project)
        self.experiment = resources.ExperimentResourceWithRawResponse(client.experiment)
        self.dataset = resources.DatasetResourceWithRawResponse(client.dataset)
        self.prompt = resources.PromptResourceWithRawResponse(client.prompt)
        self.role = resources.RoleResourceWithRawResponse(client.role)
        self.group = resources.GroupResourceWithRawResponse(client.group)
        self.acl = resources.ACLResourceWithRawResponse(client.acl)
        self.user = resources.UserResourceWithRawResponse(client.user)
        self.project_score = resources.ProjectScoreResourceWithRawResponse(client.project_score)
        self.project_tag = resources.ProjectTagResourceWithRawResponse(client.project_tag)
        self.function = resources.FunctionResourceWithRawResponse(client.function)
        self.view = resources.ViewResourceWithRawResponse(client.view)
        self.organization = resources.OrganizationResourceWithRawResponse(client.organization)
        self.api_key_resource = resources.APIKeyResourceResourceWithRawResponse(client.api_key_resource)
        self.org_secret = resources.OrgSecretResourceWithRawResponse(client.org_secret)


class AsyncBraintrustWithRawResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = resources.AsyncTopLevelResourceWithRawResponse(client.top_level)
        self.project = resources.AsyncProjectResourceWithRawResponse(client.project)
        self.experiment = resources.AsyncExperimentResourceWithRawResponse(client.experiment)
        self.dataset = resources.AsyncDatasetResourceWithRawResponse(client.dataset)
        self.prompt = resources.AsyncPromptResourceWithRawResponse(client.prompt)
        self.role = resources.AsyncRoleResourceWithRawResponse(client.role)
        self.group = resources.AsyncGroupResourceWithRawResponse(client.group)
        self.acl = resources.AsyncACLResourceWithRawResponse(client.acl)
        self.user = resources.AsyncUserResourceWithRawResponse(client.user)
        self.project_score = resources.AsyncProjectScoreResourceWithRawResponse(client.project_score)
        self.project_tag = resources.AsyncProjectTagResourceWithRawResponse(client.project_tag)
        self.function = resources.AsyncFunctionResourceWithRawResponse(client.function)
        self.view = resources.AsyncViewResourceWithRawResponse(client.view)
        self.organization = resources.AsyncOrganizationResourceWithRawResponse(client.organization)
        self.api_key_resource = resources.AsyncAPIKeyResourceResourceWithRawResponse(client.api_key_resource)
        self.org_secret = resources.AsyncOrgSecretResourceWithRawResponse(client.org_secret)


class BraintrustWithStreamedResponse:
    def __init__(self, client: Braintrust) -> None:
        self.top_level = resources.TopLevelResourceWithStreamingResponse(client.top_level)
        self.project = resources.ProjectResourceWithStreamingResponse(client.project)
        self.experiment = resources.ExperimentResourceWithStreamingResponse(client.experiment)
        self.dataset = resources.DatasetResourceWithStreamingResponse(client.dataset)
        self.prompt = resources.PromptResourceWithStreamingResponse(client.prompt)
        self.role = resources.RoleResourceWithStreamingResponse(client.role)
        self.group = resources.GroupResourceWithStreamingResponse(client.group)
        self.acl = resources.ACLResourceWithStreamingResponse(client.acl)
        self.user = resources.UserResourceWithStreamingResponse(client.user)
        self.project_score = resources.ProjectScoreResourceWithStreamingResponse(client.project_score)
        self.project_tag = resources.ProjectTagResourceWithStreamingResponse(client.project_tag)
        self.function = resources.FunctionResourceWithStreamingResponse(client.function)
        self.view = resources.ViewResourceWithStreamingResponse(client.view)
        self.organization = resources.OrganizationResourceWithStreamingResponse(client.organization)
        self.api_key_resource = resources.APIKeyResourceResourceWithStreamingResponse(client.api_key_resource)
        self.org_secret = resources.OrgSecretResourceWithStreamingResponse(client.org_secret)


class AsyncBraintrustWithStreamedResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = resources.AsyncTopLevelResourceWithStreamingResponse(client.top_level)
        self.project = resources.AsyncProjectResourceWithStreamingResponse(client.project)
        self.experiment = resources.AsyncExperimentResourceWithStreamingResponse(client.experiment)
        self.dataset = resources.AsyncDatasetResourceWithStreamingResponse(client.dataset)
        self.prompt = resources.AsyncPromptResourceWithStreamingResponse(client.prompt)
        self.role = resources.AsyncRoleResourceWithStreamingResponse(client.role)
        self.group = resources.AsyncGroupResourceWithStreamingResponse(client.group)
        self.acl = resources.AsyncACLResourceWithStreamingResponse(client.acl)
        self.user = resources.AsyncUserResourceWithStreamingResponse(client.user)
        self.project_score = resources.AsyncProjectScoreResourceWithStreamingResponse(client.project_score)
        self.project_tag = resources.AsyncProjectTagResourceWithStreamingResponse(client.project_tag)
        self.function = resources.AsyncFunctionResourceWithStreamingResponse(client.function)
        self.view = resources.AsyncViewResourceWithStreamingResponse(client.view)
        self.organization = resources.AsyncOrganizationResourceWithStreamingResponse(client.organization)
        self.api_key_resource = resources.AsyncAPIKeyResourceResourceWithStreamingResponse(client.api_key_resource)
        self.org_secret = resources.AsyncOrgSecretResourceWithStreamingResponse(client.org_secret)


Client = Braintrust

AsyncClient = AsyncBraintrust
