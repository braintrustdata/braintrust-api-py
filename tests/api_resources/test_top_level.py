# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_sdk_kotlin import BraintrustSdkKotlin, AsyncBraintrustSdkKotlin
from braintrust_sdk_kotlin.types import Dataset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_datasets(self, client: BraintrustSdkKotlin) -> None:
        top_level = client.top_level.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, top_level, path=["response"])

    @parametrize
    def test_raw_response_datasets(self, client: BraintrustSdkKotlin) -> None:
        response = client.top_level.with_raw_response.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(Dataset, top_level, path=["response"])

    @parametrize
    def test_streaming_response_datasets(self, client: BraintrustSdkKotlin) -> None:
        with client.top_level.with_streaming_response.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(Dataset, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_datasets(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.top_level.with_raw_response.datasets(
                "",
            )


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_datasets(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        top_level = await async_client.top_level.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, top_level, path=["response"])

    @parametrize
    async def test_raw_response_datasets(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.top_level.with_raw_response.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(Dataset, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_datasets(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.top_level.with_streaming_response.datasets(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(Dataset, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_datasets(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.top_level.with_raw_response.datasets(
                "",
            )
