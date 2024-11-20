# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import (
    Dataset,
    InsertEventsResponse,
    FeedbackResponseSchema,
    SummarizeDatasetResponse,
    FetchDatasetEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        dataset = client.datasets.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        dataset = client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        dataset = client.datasets.list()
        assert_matches_type(SyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.list(
            dataset_name="dataset_name",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncListObjects[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        dataset = client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_feedback(self, client: Braintrust) -> None:
        dataset = client.datasets.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.feedback(
                dataset_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    def test_method_fetch(self, client: Braintrust) -> None:
        dataset = client.datasets.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.fetch(
                dataset_id="",
            )

    @parametrize
    def test_method_fetch_post(self, client: Braintrust) -> None:
        dataset = client.datasets.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_method_fetch_post_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_fetch_post(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_fetch_post(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_post(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.fetch_post(
                dataset_id="",
            )

    @parametrize
    def test_method_insert(self, client: Braintrust) -> None:
        dataset = client.datasets.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(InsertEventsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(InsertEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.insert(
                dataset_id="",
                events=[{}],
            )

    @parametrize
    def test_method_summarize(self, client: Braintrust) -> None:
        dataset = client.datasets.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Braintrust) -> None:
        dataset = client.datasets.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summarize_data=True,
        )
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Braintrust) -> None:
        response = client.datasets.with_raw_response.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Braintrust) -> None:
        with client.datasets.with_streaming_response.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summarize(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.summarize(
                dataset_id="",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(AsyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.list(
            dataset_name="dataset_name",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncListObjects[Dataset], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncListObjects[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.feedback(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(FeedbackResponseSchema, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.feedback(
                dataset_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.fetch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.fetch(
                dataset_id="",
            )

    @parametrize
    async def test_method_fetch_post(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_method_fetch_post_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.fetch_post(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(FetchDatasetEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_post(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.fetch_post(
                dataset_id="",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(InsertEventsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.insert(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(InsertEventsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.insert(
                dataset_id="",
                events=[{}],
            )

    @parametrize
    async def test_method_summarize(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncBraintrust) -> None:
        dataset = await async_client.datasets.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summarize_data=True,
        )
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.datasets.with_raw_response.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncBraintrust) -> None:
        async with async_client.datasets.with_streaming_response.summarize(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(SummarizeDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.summarize(
                dataset_id="",
            )
