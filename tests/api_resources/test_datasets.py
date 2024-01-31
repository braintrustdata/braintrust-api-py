# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_sdk_kotlin import BraintrustSdkKotlin, AsyncBraintrustSdkKotlin
from braintrust_sdk_kotlin.types import (
    Dataset,
    DatasetListResponse,
    DatasetFetchResponse,
    DatasetInsertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.create(
            name="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.create(
            name="string",
            description="string",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            description="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update(
                "",
                name="string",
            )

    @parametrize
    def test_method_list(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.list(
            dataset_name="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_feedback(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert dataset is None

    @parametrize
    def test_raw_response_feedback(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_feedback(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    def test_method_fetch(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_insert(self, client: BraintrustSdkKotlin) -> None:
        dataset = client.datasets.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: BraintrustSdkKotlin) -> None:
        response = client.datasets.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: BraintrustSdkKotlin) -> None:
        with client.datasets.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.create(
            name="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.create(
            name="string",
            description="string",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            description="string",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update(
                "",
                name="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.list(
            dataset_name="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetFetchResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        dataset = await async_client.datasets.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.datasets.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.datasets.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetInsertResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )
