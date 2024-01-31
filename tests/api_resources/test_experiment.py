# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_sdk_kotlin import BraintrustSdkKotlin, AsyncBraintrustSdkKotlin
from braintrust_sdk_kotlin.types import (
    Experiment,
    ExperimentInsertResponse,
    ExperimentFetchEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_feedback(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert experiment is None

    @parametrize
    def test_raw_response_feedback(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert experiment is None

    @parametrize
    def test_streaming_response_feedback(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert experiment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    def test_method_fetch_events(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    def test_method_fetch_events_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_fetch_events(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_fetch_events(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_events(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.fetch_events(
                "",
            )

    @parametrize
    def test_method_insert(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )

    @parametrize
    def test_method_update_partial(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_update_partial_with_all_params(self, client: BraintrustSdkKotlin) -> None:
        experiment = client.experiment.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_update_partial(self, client: BraintrustSdkKotlin) -> None:
        response = client.experiment.with_raw_response.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_update_partial(self, client: BraintrustSdkKotlin) -> None:
        with client.experiment.with_streaming_response.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_partial(self, client: BraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.update_partial(
                "",
            )


class TestAsyncExperiment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.update(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert experiment is None

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert experiment is None

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert experiment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    async def test_method_fetch_events(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_method_fetch_events_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_fetch_events(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_events(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.fetch_events(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentFetchEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_events(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.fetch_events(
                "",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )

    @parametrize
    async def test_method_update_partial(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_update_partial_with_all_params(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        experiment = await async_client.experiment.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="string",
            description="string",
            metadata={"foo": {}},
            name="string",
            public=True,
            repo_info={
                "commit": "string",
                "branch": "string",
                "tag": "string",
                "dirty": True,
                "author_name": "string",
                "author_email": "string",
                "commit_message": "string",
                "commit_time": "string",
                "git_diff": "string",
            },
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_update_partial(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        response = await async_client.experiment.with_raw_response.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_update_partial(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        async with async_client.experiment.with_streaming_response.update_partial(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_partial(self, async_client: AsyncBraintrustSdkKotlin) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.update_partial(
                "",
            )
