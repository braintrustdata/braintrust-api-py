# File generated from our OpenAPI spec by Stainless.

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
from ._exceptions import APIStatusError, BraintrustSdkKotlinError
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
    "BraintrustSdkKotlin",
    "AsyncBraintrustSdkKotlin",
    "Client",
    "AsyncClient",
]


class BraintrustSdkKotlin(SyncAPIClient):
    project: resources.ProjectResource
    project_logs: resources.ProjectLogs
    experiment: resources.ExperimentResource
    experiments: resources.Experiments
    datasets: resources.Datasets
    top_level: resources.TopLevel
    v1: resources.V1
    with_raw_response: BraintrustSdkKotlinWithRawResponse
    with_streaming_response: BraintrustSdkKotlinWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
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
        """Construct a new synchronous braintrust-sdk-kotlin client instance.

        This automatically infers the `api_key` argument from the `BRAINTRUST_SDK_KOTLIN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAINTRUST_SDK_KOTLIN_API_KEY")
        if api_key is None:
            raise BraintrustSdkKotlinError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BRAINTRUST_SDK_KOTLIN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BRAINTRUST_SDK_KOTLIN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.braintrustdata.com"

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

        self.project = resources.ProjectResource(self)
        self.project_logs = resources.ProjectLogs(self)
        self.experiment = resources.ExperimentResource(self)
        self.experiments = resources.Experiments(self)
        self.datasets = resources.Datasets(self)
        self.top_level = resources.TopLevel(self)
        self.v1 = resources.V1(self)
        self.with_raw_response = BraintrustSdkKotlinWithRawResponse(self)
        self.with_streaming_response = BraintrustSdkKotlinWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
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


class AsyncBraintrustSdkKotlin(AsyncAPIClient):
    project: resources.AsyncProjectResource
    project_logs: resources.AsyncProjectLogs
    experiment: resources.AsyncExperimentResource
    experiments: resources.AsyncExperiments
    datasets: resources.AsyncDatasets
    top_level: resources.AsyncTopLevel
    v1: resources.AsyncV1
    with_raw_response: AsyncBraintrustSdkKotlinWithRawResponse
    with_streaming_response: AsyncBraintrustSdkKotlinWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
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
        """Construct a new async braintrust-sdk-kotlin client instance.

        This automatically infers the `api_key` argument from the `BRAINTRUST_SDK_KOTLIN_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAINTRUST_SDK_KOTLIN_API_KEY")
        if api_key is None:
            raise BraintrustSdkKotlinError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BRAINTRUST_SDK_KOTLIN_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BRAINTRUST_SDK_KOTLIN_BASE_URL")
        if base_url is None:
            base_url = f"https://api.braintrustdata.com"

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

        self.project = resources.AsyncProjectResource(self)
        self.project_logs = resources.AsyncProjectLogs(self)
        self.experiment = resources.AsyncExperimentResource(self)
        self.experiments = resources.AsyncExperiments(self)
        self.datasets = resources.AsyncDatasets(self)
        self.top_level = resources.AsyncTopLevel(self)
        self.v1 = resources.AsyncV1(self)
        self.with_raw_response = AsyncBraintrustSdkKotlinWithRawResponse(self)
        self.with_streaming_response = AsyncBraintrustSdkKotlinWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
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


class BraintrustSdkKotlinWithRawResponse:
    def __init__(self, client: BraintrustSdkKotlin) -> None:
        self.project = resources.ProjectResourceWithRawResponse(client.project)
        self.project_logs = resources.ProjectLogsWithRawResponse(client.project_logs)
        self.experiment = resources.ExperimentResourceWithRawResponse(client.experiment)
        self.experiments = resources.ExperimentsWithRawResponse(client.experiments)
        self.datasets = resources.DatasetsWithRawResponse(client.datasets)
        self.top_level = resources.TopLevelWithRawResponse(client.top_level)
        self.v1 = resources.V1WithRawResponse(client.v1)


class AsyncBraintrustSdkKotlinWithRawResponse:
    def __init__(self, client: AsyncBraintrustSdkKotlin) -> None:
        self.project = resources.AsyncProjectResourceWithRawResponse(client.project)
        self.project_logs = resources.AsyncProjectLogsWithRawResponse(client.project_logs)
        self.experiment = resources.AsyncExperimentResourceWithRawResponse(client.experiment)
        self.experiments = resources.AsyncExperimentsWithRawResponse(client.experiments)
        self.datasets = resources.AsyncDatasetsWithRawResponse(client.datasets)
        self.top_level = resources.AsyncTopLevelWithRawResponse(client.top_level)
        self.v1 = resources.AsyncV1WithRawResponse(client.v1)


class BraintrustSdkKotlinWithStreamedResponse:
    def __init__(self, client: BraintrustSdkKotlin) -> None:
        self.project = resources.ProjectResourceWithStreamingResponse(client.project)
        self.project_logs = resources.ProjectLogsWithStreamingResponse(client.project_logs)
        self.experiment = resources.ExperimentResourceWithStreamingResponse(client.experiment)
        self.experiments = resources.ExperimentsWithStreamingResponse(client.experiments)
        self.datasets = resources.DatasetsWithStreamingResponse(client.datasets)
        self.top_level = resources.TopLevelWithStreamingResponse(client.top_level)
        self.v1 = resources.V1WithStreamingResponse(client.v1)


class AsyncBraintrustSdkKotlinWithStreamedResponse:
    def __init__(self, client: AsyncBraintrustSdkKotlin) -> None:
        self.project = resources.AsyncProjectResourceWithStreamingResponse(client.project)
        self.project_logs = resources.AsyncProjectLogsWithStreamingResponse(client.project_logs)
        self.experiment = resources.AsyncExperimentResourceWithStreamingResponse(client.experiment)
        self.experiments = resources.AsyncExperimentsWithStreamingResponse(client.experiments)
        self.datasets = resources.AsyncDatasetsWithStreamingResponse(client.datasets)
        self.top_level = resources.AsyncTopLevelWithStreamingResponse(client.top_level)
        self.v1 = resources.AsyncV1WithStreamingResponse(client.v1)


Client = BraintrustSdkKotlin

AsyncClient = AsyncBraintrustSdkKotlin
