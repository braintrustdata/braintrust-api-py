# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.types import (
    EnvVarListResponse,
)
from braintrust_api.types.shared import EnvVar

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvVars:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        env_var = client.env_vars.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        env_var = client.env_vars.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        env_var = client.env_vars.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            client.env_vars.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        env_var = client.env_vars.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        env_var = client.env_vars.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            client.env_vars.with_raw_response.update(
                env_var_id="",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        env_var = client.env_vars.list()
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        env_var = client.env_vars.list(
            env_var_name="env_var_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVarListResponse, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        env_var = client.env_vars.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            client.env_vars.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        env_var = client.env_vars.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        env_var = client.env_vars.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.env_vars.with_raw_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.env_vars.with_streaming_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvVars:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            await async_client.env_vars.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.update(
            env_var_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            await async_client.env_vars.with_raw_response.update(
                env_var_id="",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.list()
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.list(
            env_var_name="env_var_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVarListResponse, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVarListResponse, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `env_var_id` but received ''"):
            await async_client.env_vars.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        env_var = await async_client.env_vars.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            value="value",
        )
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.env_vars.with_raw_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        env_var = await response.parse()
        assert_matches_type(EnvVar, env_var, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.env_vars.with_streaming_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            env_var = await response.parse()
            assert_matches_type(EnvVar, env_var, path=["response"])

        assert cast(Any, response.is_closed) is True
