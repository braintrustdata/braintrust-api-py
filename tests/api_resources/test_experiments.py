# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_sdk_kotlin import BraintrustSdkKotlin, AsyncBraintrustSdkKotlin
from braintrust_sdk_kotlin.types import ExperimentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiments.list()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiments.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="string",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BraintrustSdkKotlin) -> None:
        with client.experiments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentListResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExperiments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiments.list()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiments.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="string",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentListResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True
