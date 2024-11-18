# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.types.shared import SummarizeExperimentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        eval = client.evals.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        )
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        eval = client.evals.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[
                {
                    "function_id": "function_id",
                    "version": "version",
                }
            ],
            task={
                "function_id": "function_id",
                "version": "version",
            },
            base_experiment_id="base_experiment_id",
            base_experiment_name="base_experiment_name",
            experiment_name="experiment_name",
            git_metadata_settings={
                "collect": "all",
                "fields": ["commit"],
            },
            is_public=True,
            max_concurrency=0,
            metadata={"foo": "bar"},
            repo_info={
                "author_email": "author_email",
                "author_name": "author_name",
                "branch": "branch",
                "commit": "commit",
                "commit_message": "commit_message",
                "commit_time": "commit_time",
                "dirty": True,
                "git_diff": "git_diff",
                "tag": "tag",
            },
            stream=True,
            api_timeout=0,
            trial_count=0,
        )
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.evals.with_raw_response.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = response.parse()
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.evals.with_streaming_response.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = response.parse()
            assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        eval = await async_client.evals.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        )
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        eval = await async_client.evals.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[
                {
                    "function_id": "function_id",
                    "version": "version",
                }
            ],
            task={
                "function_id": "function_id",
                "version": "version",
            },
            base_experiment_id="base_experiment_id",
            base_experiment_name="base_experiment_name",
            experiment_name="experiment_name",
            git_metadata_settings={
                "collect": "all",
                "fields": ["commit"],
            },
            is_public=True,
            max_concurrency=0,
            metadata={"foo": "bar"},
            repo_info={
                "author_email": "author_email",
                "author_name": "author_name",
                "branch": "branch",
                "commit": "commit",
                "commit_message": "commit_message",
                "commit_time": "commit_time",
                "dirty": True,
                "git_diff": "git_diff",
                "tag": "tag",
            },
            stream=True,
            api_timeout=0,
            trial_count=0,
        )
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.evals.with_raw_response.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eval = await response.parse()
        assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.evals.with_streaming_response.create(
            data={"dataset_id": "dataset_id"},
            project_id="project_id",
            scores=[{"function_id": "function_id"}],
            task={"function_id": "function_id"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eval = await response.parse()
            assert_matches_type(SummarizeExperimentResponse, eval, path=["response"])

        assert cast(Any, response.is_closed) is True
