# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import ProjectScore

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjectScores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        project_score = client.project_scores.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        project_score = client.project_scores.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        project_score = client.project_scores.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            client.project_scores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        project_score = client.project_scores.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        project_score = client.project_scores.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
            name="name",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            client.project_scores.with_raw_response.update(
                project_score_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        project_score = client.project_scores.list()
        assert_matches_type(SyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        project_score = client.project_scores.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            project_score_name="project_score_name",
            score_type="slider",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(SyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(SyncListObjects[ProjectScore], project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        project_score = client.project_scores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            client.project_scores.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        project_score = client.project_scores.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        project_score = client.project_scores.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.project_scores.with_raw_response.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.project_scores.with_streaming_response.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjectScores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            await async_client.project_scores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
            name="name",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.update(
            project_score_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            await async_client.project_scores.with_raw_response.update(
                project_score_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.list()
        assert_matches_type(AsyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            project_score_name="project_score_name",
            score_type="slider",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(AsyncListObjects[ProjectScore], project_score, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(AsyncListObjects[ProjectScore], project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_score_id` but received ''"):
            await async_client.project_scores.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        project_score = await async_client.project_scores.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
            categories=[
                {
                    "name": "name",
                    "value": 0,
                }
            ],
            config={
                "destination": "expected",
                "multi_select": True,
                "online": {
                    "sampling_rate": 0,
                    "scorers": [
                        {
                            "id": "id",
                            "type": "function",
                        }
                    ],
                    "apply_to_root_span": True,
                    "apply_to_span_names": ["string"],
                },
            },
            description="description",
        )
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project_scores.with_raw_response.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project_score = await response.parse()
        assert_matches_type(ProjectScore, project_score, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project_scores.with_streaming_response.replace(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_type="slider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project_score = await response.parse()
            assert_matches_type(ProjectScore, project_score, path=["response"])

        assert cast(Any, response.is_closed) is True
