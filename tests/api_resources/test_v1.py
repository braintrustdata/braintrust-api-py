# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_sdk_kotlin import BraintrustSdkKotlin, AsyncBraintrustSdkKotlin

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_hello_world(self, client: BraintrustSdkKotlin) -> None:
        v1 = client.v1.hello_world()
        assert_matches_type(str, v1, path=["response"])

    @parametrize
    def test_raw_response_hello_world(self, client: BraintrustSdkKotlin) -> None:
        response = client.v1.with_raw_response.hello_world()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(str, v1, path=["response"])

    @parametrize
    def test_streaming_response_hello_world(self, client: BraintrustSdkKotlin) -> None:
        with client.v1.with_streaming_response.hello_world() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(str, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_hello_world(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        v1 = await async_client.v1.hello_world()
        assert_matches_type(str, v1, path=["response"])

    @parametrize
    async def test_raw_response_hello_world(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.v1.with_raw_response.hello_world()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(str, v1, path=["response"])

    @parametrize
    async def test_streaming_response_hello_world(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.v1.with_streaming_response.hello_world() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(str, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
