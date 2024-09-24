# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import Organization

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        organization = client.organizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.organizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.organizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        organization = client.organizations.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        organization = client.organizations.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            api_url="api_url",
            is_universal_api=True,
            name="name",
            proxy_url="proxy_url",
            realtime_url="realtime_url",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.organizations.with_raw_response.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.organizations.with_streaming_response.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.update(
                organization_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        organization = client.organizations.list()
        assert_matches_type(SyncListObjects[Organization], organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        organization = client.organizations.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[Organization], organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncListObjects[Organization], organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncListObjects[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        organization = client.organizations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.organizations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.organizations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.delete(
                "",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.organizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            api_url="api_url",
            is_universal_api=True,
            name="name",
            proxy_url="proxy_url",
            realtime_url="realtime_url",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.organizations.with_raw_response.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organizations.with_streaming_response.update(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.update(
                organization_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(AsyncListObjects[Organization], organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[Organization], organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncListObjects[Organization], organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncListObjects[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        organization = await async_client.organizations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.organizations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Organization, organization, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organizations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Organization, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.delete(
                "",
            )
