# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_hello_world(self, client: Braintrust) -> None:
        top_level = client.top_level.hello_world()
        assert_matches_type(str, top_level, path=["response"])

    @parametrize
    def test_raw_response_hello_world(self, client: Braintrust) -> None:
        response = client.top_level.with_raw_response.hello_world()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(str, top_level, path=["response"])

    @parametrize
    def test_streaming_response_hello_world(self, client: Braintrust) -> None:
        with client.top_level.with_streaming_response.hello_world() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(str, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_hello_world(self, async_client: AsyncBraintrust) -> None:
        top_level = await async_client.top_level.hello_world()
        assert_matches_type(str, top_level, path=["response"])

    @parametrize
    async def test_raw_response_hello_world(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.top_level.with_raw_response.hello_world()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(str, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_hello_world(self, async_client: AsyncBraintrust) -> None:
        async with async_client.top_level.with_streaming_response.hello_world() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(str, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True
