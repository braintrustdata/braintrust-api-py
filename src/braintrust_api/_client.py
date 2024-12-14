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
    projects: resources.ProjectsResource
    experiments: resources.ExperimentsResource
    datasets: resources.DatasetsResource
    prompts: resources.PromptsResource
    roles: resources.RolesResource
    groups: resources.GroupsResource
    acls: resources.ACLsResource
    users: resources.UsersResource
    project_scores: resources.ProjectScoresResource
    project_tags: resources.ProjectTagsResource
    span_iframes: resources.SpanIframesResource
    functions: resources.FunctionsResource
    views: resources.ViewsResource
    organizations: resources.OrganizationsResource
    api_keys: resources.APIKeysResource
    ai_secrets: resources.AISecretsResource
    env_vars: resources.EnvVarsResource
    evals: resources.EvalsResource
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
        self.projects = resources.ProjectsResource(self)
        self.experiments = resources.ExperimentsResource(self)
        self.datasets = resources.DatasetsResource(self)
        self.prompts = resources.PromptsResource(self)
        self.roles = resources.RolesResource(self)
        self.groups = resources.GroupsResource(self)
        self.acls = resources.ACLsResource(self)
        self.users = resources.UsersResource(self)
        self.project_scores = resources.ProjectScoresResource(self)
        self.project_tags = resources.ProjectTagsResource(self)
        self.span_iframes = resources.SpanIframesResource(self)
        self.functions = resources.FunctionsResource(self)
        self.views = resources.ViewsResource(self)
        self.organizations = resources.OrganizationsResource(self)
        self.api_keys = resources.APIKeysResource(self)
        self.ai_secrets = resources.AISecretsResource(self)
        self.env_vars = resources.EnvVarsResource(self)
        self.evals = resources.EvalsResource(self)
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
    projects: resources.AsyncProjectsResource
    experiments: resources.AsyncExperimentsResource
    datasets: resources.AsyncDatasetsResource
    prompts: resources.AsyncPromptsResource
    roles: resources.AsyncRolesResource
    groups: resources.AsyncGroupsResource
    acls: resources.AsyncACLsResource
    users: resources.AsyncUsersResource
    project_scores: resources.AsyncProjectScoresResource
    project_tags: resources.AsyncProjectTagsResource
    span_iframes: resources.AsyncSpanIframesResource
    functions: resources.AsyncFunctionsResource
    views: resources.AsyncViewsResource
    organizations: resources.AsyncOrganizationsResource
    api_keys: resources.AsyncAPIKeysResource
    ai_secrets: resources.AsyncAISecretsResource
    env_vars: resources.AsyncEnvVarsResource
    evals: resources.AsyncEvalsResource
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
        self.projects = resources.AsyncProjectsResource(self)
        self.experiments = resources.AsyncExperimentsResource(self)
        self.datasets = resources.AsyncDatasetsResource(self)
        self.prompts = resources.AsyncPromptsResource(self)
        self.roles = resources.AsyncRolesResource(self)
        self.groups = resources.AsyncGroupsResource(self)
        self.acls = resources.AsyncACLsResource(self)
        self.users = resources.AsyncUsersResource(self)
        self.project_scores = resources.AsyncProjectScoresResource(self)
        self.project_tags = resources.AsyncProjectTagsResource(self)
        self.span_iframes = resources.AsyncSpanIframesResource(self)
        self.functions = resources.AsyncFunctionsResource(self)
        self.views = resources.AsyncViewsResource(self)
        self.organizations = resources.AsyncOrganizationsResource(self)
        self.api_keys = resources.AsyncAPIKeysResource(self)
        self.ai_secrets = resources.AsyncAISecretsResource(self)
        self.env_vars = resources.AsyncEnvVarsResource(self)
        self.evals = resources.AsyncEvalsResource(self)
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
        self.projects = resources.ProjectsResourceWithRawResponse(client.projects)
        self.experiments = resources.ExperimentsResourceWithRawResponse(client.experiments)
        self.datasets = resources.DatasetsResourceWithRawResponse(client.datasets)
        self.prompts = resources.PromptsResourceWithRawResponse(client.prompts)
        self.roles = resources.RolesResourceWithRawResponse(client.roles)
        self.groups = resources.GroupsResourceWithRawResponse(client.groups)
        self.acls = resources.ACLsResourceWithRawResponse(client.acls)
        self.users = resources.UsersResourceWithRawResponse(client.users)
        self.project_scores = resources.ProjectScoresResourceWithRawResponse(client.project_scores)
        self.project_tags = resources.ProjectTagsResourceWithRawResponse(client.project_tags)
        self.span_iframes = resources.SpanIframesResourceWithRawResponse(client.span_iframes)
        self.functions = resources.FunctionsResourceWithRawResponse(client.functions)
        self.views = resources.ViewsResourceWithRawResponse(client.views)
        self.organizations = resources.OrganizationsResourceWithRawResponse(client.organizations)
        self.api_keys = resources.APIKeysResourceWithRawResponse(client.api_keys)
        self.ai_secrets = resources.AISecretsResourceWithRawResponse(client.ai_secrets)
        self.env_vars = resources.EnvVarsResourceWithRawResponse(client.env_vars)
        self.evals = resources.EvalsResourceWithRawResponse(client.evals)


class AsyncBraintrustWithRawResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = resources.AsyncTopLevelResourceWithRawResponse(client.top_level)
        self.projects = resources.AsyncProjectsResourceWithRawResponse(client.projects)
        self.experiments = resources.AsyncExperimentsResourceWithRawResponse(client.experiments)
        self.datasets = resources.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.prompts = resources.AsyncPromptsResourceWithRawResponse(client.prompts)
        self.roles = resources.AsyncRolesResourceWithRawResponse(client.roles)
        self.groups = resources.AsyncGroupsResourceWithRawResponse(client.groups)
        self.acls = resources.AsyncACLsResourceWithRawResponse(client.acls)
        self.users = resources.AsyncUsersResourceWithRawResponse(client.users)
        self.project_scores = resources.AsyncProjectScoresResourceWithRawResponse(client.project_scores)
        self.project_tags = resources.AsyncProjectTagsResourceWithRawResponse(client.project_tags)
        self.span_iframes = resources.AsyncSpanIframesResourceWithRawResponse(client.span_iframes)
        self.functions = resources.AsyncFunctionsResourceWithRawResponse(client.functions)
        self.views = resources.AsyncViewsResourceWithRawResponse(client.views)
        self.organizations = resources.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.api_keys = resources.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.ai_secrets = resources.AsyncAISecretsResourceWithRawResponse(client.ai_secrets)
        self.env_vars = resources.AsyncEnvVarsResourceWithRawResponse(client.env_vars)
        self.evals = resources.AsyncEvalsResourceWithRawResponse(client.evals)


class BraintrustWithStreamedResponse:
    def __init__(self, client: Braintrust) -> None:
        self.top_level = resources.TopLevelResourceWithStreamingResponse(client.top_level)
        self.projects = resources.ProjectsResourceWithStreamingResponse(client.projects)
        self.experiments = resources.ExperimentsResourceWithStreamingResponse(client.experiments)
        self.datasets = resources.DatasetsResourceWithStreamingResponse(client.datasets)
        self.prompts = resources.PromptsResourceWithStreamingResponse(client.prompts)
        self.roles = resources.RolesResourceWithStreamingResponse(client.roles)
        self.groups = resources.GroupsResourceWithStreamingResponse(client.groups)
        self.acls = resources.ACLsResourceWithStreamingResponse(client.acls)
        self.users = resources.UsersResourceWithStreamingResponse(client.users)
        self.project_scores = resources.ProjectScoresResourceWithStreamingResponse(client.project_scores)
        self.project_tags = resources.ProjectTagsResourceWithStreamingResponse(client.project_tags)
        self.span_iframes = resources.SpanIframesResourceWithStreamingResponse(client.span_iframes)
        self.functions = resources.FunctionsResourceWithStreamingResponse(client.functions)
        self.views = resources.ViewsResourceWithStreamingResponse(client.views)
        self.organizations = resources.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.api_keys = resources.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.ai_secrets = resources.AISecretsResourceWithStreamingResponse(client.ai_secrets)
        self.env_vars = resources.EnvVarsResourceWithStreamingResponse(client.env_vars)
        self.evals = resources.EvalsResourceWithStreamingResponse(client.evals)


class AsyncBraintrustWithStreamedResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = resources.AsyncTopLevelResourceWithStreamingResponse(client.top_level)
        self.projects = resources.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.experiments = resources.AsyncExperimentsResourceWithStreamingResponse(client.experiments)
        self.datasets = resources.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.prompts = resources.AsyncPromptsResourceWithStreamingResponse(client.prompts)
        self.roles = resources.AsyncRolesResourceWithStreamingResponse(client.roles)
        self.groups = resources.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.acls = resources.AsyncACLsResourceWithStreamingResponse(client.acls)
        self.users = resources.AsyncUsersResourceWithStreamingResponse(client.users)
        self.project_scores = resources.AsyncProjectScoresResourceWithStreamingResponse(client.project_scores)
        self.project_tags = resources.AsyncProjectTagsResourceWithStreamingResponse(client.project_tags)
        self.span_iframes = resources.AsyncSpanIframesResourceWithStreamingResponse(client.span_iframes)
        self.functions = resources.AsyncFunctionsResourceWithStreamingResponse(client.functions)
        self.views = resources.AsyncViewsResourceWithStreamingResponse(client.views)
        self.organizations = resources.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.api_keys = resources.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.ai_secrets = resources.AsyncAISecretsResourceWithStreamingResponse(client.ai_secrets)
        self.env_vars = resources.AsyncEnvVarsResourceWithStreamingResponse(client.env_vars)
        self.evals = resources.AsyncEvalsResourceWithStreamingResponse(client.evals)


Client = Braintrust

AsyncClient = AsyncBraintrust
