# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import AISecret

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAISecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.create(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.create(
            name="name",
            metadata={"foo": "bar"},
            org_name="org_name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            client.ai_secrets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            name="name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            client.ai_secrets.with_raw_response.update(
                ai_secret_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.list()
        assert_matches_type(SyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.list(
            ai_secret_name="ai_secret_name",
            ai_secret_type="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(SyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(SyncListObjects[AISecret], ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            client.ai_secrets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_find_and_delete(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.find_and_delete(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_method_find_and_delete_with_all_params(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.find_and_delete(
            name="name",
            org_name="org_name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_find_and_delete(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.find_and_delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_find_and_delete(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.find_and_delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.replace(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        ai_secret = client.ai_secrets.replace(
            name="name",
            metadata={"foo": "bar"},
            org_name="org_name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.ai_secrets.with_raw_response.replace(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.ai_secrets.with_streaming_response.replace(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAISecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.create(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.create(
            name="name",
            metadata={"foo": "bar"},
            org_name="org_name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            await async_client.ai_secrets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            name="name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.update(
            ai_secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            await async_client.ai_secrets.with_raw_response.update(
                ai_secret_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.list()
        assert_matches_type(AsyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.list(
            ai_secret_name="ai_secret_name",
            ai_secret_type="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AsyncListObjects[AISecret], ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AsyncListObjects[AISecret], ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ai_secret_id` but received ''"):
            await async_client.ai_secrets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_find_and_delete(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.find_and_delete(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_method_find_and_delete_with_all_params(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.find_and_delete(
            name="name",
            org_name="org_name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_find_and_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.find_and_delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_find_and_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.find_and_delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.replace(
            name="name",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        ai_secret = await async_client.ai_secrets.replace(
            name="name",
            metadata={"foo": "bar"},
            org_name="org_name",
            secret="secret",
            type="type",
        )
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.ai_secrets.with_raw_response.replace(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_secret = await response.parse()
        assert_matches_type(AISecret, ai_secret, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.ai_secrets.with_streaming_response.replace(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_secret = await response.parse()
            assert_matches_type(AISecret, ai_secret, path=["response"])

        assert cast(Any, response.is_closed) is True
