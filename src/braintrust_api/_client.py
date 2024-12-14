# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from .resources import (
    acls,
    evals,
    roles,
    users,
    views,
    groups,
    prompts,
    api_keys,
    datasets,
    env_vars,
    functions,
    top_level,
    ai_secrets,
    experiments,
    project_tags,
    span_iframes,
    project_scores,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.projects import projects
from .resources.organizations import organizations

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Braintrust",
    "AsyncBraintrust",
    "Client",
    "AsyncClient",
]


class Braintrust(SyncAPIClient):
    top_level: top_level.TopLevelResource
    projects: projects.ProjectsResource
    experiments: experiments.ExperimentsResource
    datasets: datasets.DatasetsResource
    prompts: prompts.PromptsResource
    roles: roles.RolesResource
    groups: groups.GroupsResource
    acls: acls.ACLsResource
    users: users.UsersResource
    project_scores: project_scores.ProjectScoresResource
    project_tags: project_tags.ProjectTagsResource
    span_iframes: span_iframes.SpanIframesResource
    functions: functions.FunctionsResource
    views: views.ViewsResource
    organizations: organizations.OrganizationsResource
    api_keys: api_keys.APIKeysResource
    ai_secrets: ai_secrets.AISecretsResource
    env_vars: env_vars.EnvVarsResource
    evals: evals.EvalsResource
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

        self.top_level = top_level.TopLevelResource(self)
        self.projects = projects.ProjectsResource(self)
        self.experiments = experiments.ExperimentsResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.prompts = prompts.PromptsResource(self)
        self.roles = roles.RolesResource(self)
        self.groups = groups.GroupsResource(self)
        self.acls = acls.ACLsResource(self)
        self.users = users.UsersResource(self)
        self.project_scores = project_scores.ProjectScoresResource(self)
        self.project_tags = project_tags.ProjectTagsResource(self)
        self.span_iframes = span_iframes.SpanIframesResource(self)
        self.functions = functions.FunctionsResource(self)
        self.views = views.ViewsResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.api_keys = api_keys.APIKeysResource(self)
        self.ai_secrets = ai_secrets.AISecretsResource(self)
        self.env_vars = env_vars.EnvVarsResource(self)
        self.evals = evals.EvalsResource(self)
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
    top_level: top_level.AsyncTopLevelResource
    projects: projects.AsyncProjectsResource
    experiments: experiments.AsyncExperimentsResource
    datasets: datasets.AsyncDatasetsResource
    prompts: prompts.AsyncPromptsResource
    roles: roles.AsyncRolesResource
    groups: groups.AsyncGroupsResource
    acls: acls.AsyncACLsResource
    users: users.AsyncUsersResource
    project_scores: project_scores.AsyncProjectScoresResource
    project_tags: project_tags.AsyncProjectTagsResource
    span_iframes: span_iframes.AsyncSpanIframesResource
    functions: functions.AsyncFunctionsResource
    views: views.AsyncViewsResource
    organizations: organizations.AsyncOrganizationsResource
    api_keys: api_keys.AsyncAPIKeysResource
    ai_secrets: ai_secrets.AsyncAISecretsResource
    env_vars: env_vars.AsyncEnvVarsResource
    evals: evals.AsyncEvalsResource
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

        self.top_level = top_level.AsyncTopLevelResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.experiments = experiments.AsyncExperimentsResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.prompts = prompts.AsyncPromptsResource(self)
        self.roles = roles.AsyncRolesResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.acls = acls.AsyncACLsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.project_scores = project_scores.AsyncProjectScoresResource(self)
        self.project_tags = project_tags.AsyncProjectTagsResource(self)
        self.span_iframes = span_iframes.AsyncSpanIframesResource(self)
        self.functions = functions.AsyncFunctionsResource(self)
        self.views = views.AsyncViewsResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.api_keys = api_keys.AsyncAPIKeysResource(self)
        self.ai_secrets = ai_secrets.AsyncAISecretsResource(self)
        self.env_vars = env_vars.AsyncEnvVarsResource(self)
        self.evals = evals.AsyncEvalsResource(self)
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
        self.top_level = top_level.TopLevelResourceWithRawResponse(client.top_level)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.experiments = experiments.ExperimentsResourceWithRawResponse(client.experiments)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.prompts = prompts.PromptsResourceWithRawResponse(client.prompts)
        self.roles = roles.RolesResourceWithRawResponse(client.roles)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)
        self.acls = acls.ACLsResourceWithRawResponse(client.acls)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.project_scores = project_scores.ProjectScoresResourceWithRawResponse(client.project_scores)
        self.project_tags = project_tags.ProjectTagsResourceWithRawResponse(client.project_tags)
        self.span_iframes = span_iframes.SpanIframesResourceWithRawResponse(client.span_iframes)
        self.functions = functions.FunctionsResourceWithRawResponse(client.functions)
        self.views = views.ViewsResourceWithRawResponse(client.views)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.api_keys = api_keys.APIKeysResourceWithRawResponse(client.api_keys)
        self.ai_secrets = ai_secrets.AISecretsResourceWithRawResponse(client.ai_secrets)
        self.env_vars = env_vars.EnvVarsResourceWithRawResponse(client.env_vars)
        self.evals = evals.EvalsResourceWithRawResponse(client.evals)


class AsyncBraintrustWithRawResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = top_level.AsyncTopLevelResourceWithRawResponse(client.top_level)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.experiments = experiments.AsyncExperimentsResourceWithRawResponse(client.experiments)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.prompts = prompts.AsyncPromptsResourceWithRawResponse(client.prompts)
        self.roles = roles.AsyncRolesResourceWithRawResponse(client.roles)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)
        self.acls = acls.AsyncACLsResourceWithRawResponse(client.acls)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.project_scores = project_scores.AsyncProjectScoresResourceWithRawResponse(client.project_scores)
        self.project_tags = project_tags.AsyncProjectTagsResourceWithRawResponse(client.project_tags)
        self.span_iframes = span_iframes.AsyncSpanIframesResourceWithRawResponse(client.span_iframes)
        self.functions = functions.AsyncFunctionsResourceWithRawResponse(client.functions)
        self.views = views.AsyncViewsResourceWithRawResponse(client.views)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithRawResponse(client.api_keys)
        self.ai_secrets = ai_secrets.AsyncAISecretsResourceWithRawResponse(client.ai_secrets)
        self.env_vars = env_vars.AsyncEnvVarsResourceWithRawResponse(client.env_vars)
        self.evals = evals.AsyncEvalsResourceWithRawResponse(client.evals)


class BraintrustWithStreamedResponse:
    def __init__(self, client: Braintrust) -> None:
        self.top_level = top_level.TopLevelResourceWithStreamingResponse(client.top_level)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.experiments = experiments.ExperimentsResourceWithStreamingResponse(client.experiments)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.prompts = prompts.PromptsResourceWithStreamingResponse(client.prompts)
        self.roles = roles.RolesResourceWithStreamingResponse(client.roles)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)
        self.acls = acls.ACLsResourceWithStreamingResponse(client.acls)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.project_scores = project_scores.ProjectScoresResourceWithStreamingResponse(client.project_scores)
        self.project_tags = project_tags.ProjectTagsResourceWithStreamingResponse(client.project_tags)
        self.span_iframes = span_iframes.SpanIframesResourceWithStreamingResponse(client.span_iframes)
        self.functions = functions.FunctionsResourceWithStreamingResponse(client.functions)
        self.views = views.ViewsResourceWithStreamingResponse(client.views)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.api_keys = api_keys.APIKeysResourceWithStreamingResponse(client.api_keys)
        self.ai_secrets = ai_secrets.AISecretsResourceWithStreamingResponse(client.ai_secrets)
        self.env_vars = env_vars.EnvVarsResourceWithStreamingResponse(client.env_vars)
        self.evals = evals.EvalsResourceWithStreamingResponse(client.evals)


class AsyncBraintrustWithStreamedResponse:
    def __init__(self, client: AsyncBraintrust) -> None:
        self.top_level = top_level.AsyncTopLevelResourceWithStreamingResponse(client.top_level)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.experiments = experiments.AsyncExperimentsResourceWithStreamingResponse(client.experiments)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.prompts = prompts.AsyncPromptsResourceWithStreamingResponse(client.prompts)
        self.roles = roles.AsyncRolesResourceWithStreamingResponse(client.roles)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)
        self.acls = acls.AsyncACLsResourceWithStreamingResponse(client.acls)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.project_scores = project_scores.AsyncProjectScoresResourceWithStreamingResponse(client.project_scores)
        self.project_tags = project_tags.AsyncProjectTagsResourceWithStreamingResponse(client.project_tags)
        self.span_iframes = span_iframes.AsyncSpanIframesResourceWithStreamingResponse(client.span_iframes)
        self.functions = functions.AsyncFunctionsResourceWithStreamingResponse(client.functions)
        self.views = views.AsyncViewsResourceWithStreamingResponse(client.views)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.api_keys = api_keys.AsyncAPIKeysResourceWithStreamingResponse(client.api_keys)
        self.ai_secrets = ai_secrets.AsyncAISecretsResourceWithStreamingResponse(client.ai_secrets)
        self.env_vars = env_vars.AsyncEnvVarsResourceWithStreamingResponse(client.env_vars)
        self.evals = evals.AsyncEvalsResourceWithStreamingResponse(client.evals)


Client = Braintrust

AsyncClient = AsyncBraintrust
