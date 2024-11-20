# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import (
    Experiment,
    InsertEventsResponse,
    FeedbackResponseSchema,
    SummarizeExperimentResponse,
    FetchExperimentEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        experiment = client.experiments.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="dataset_version",
            description="description",
            ensure_new=True,
            metadata={"foo": "bar"},
            name="x",
            public=True,
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
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        experiment = client.experiments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        experiment = client.experiments.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="dataset_version",
            description="description",
            metadata={"foo": "bar"},
            name="name",
            public=True,
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
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.update(
                experiment_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        experiment = client.experiments.list()
        assert_matches_type(SyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="experiment_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(SyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(SyncListObjects[Experiment], experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        experiment = client.experiments.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_feedback(self, client: Braintrust) -> None:
        experiment = client.experiments.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.feedback(
                experiment_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    def test_method_fetch(self, client: Braintrust) -> None:
        experiment = client.experiments.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.fetch(
                experiment_id="",
            )

    @parametrize
    def test_method_fetch_post(self, client: Braintrust) -> None:
        experiment = client.experiments.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_method_fetch_post_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_fetch_post(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_fetch_post(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_post(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.fetch_post(
                experiment_id="",
            )

    @parametrize
    def test_method_insert(self, client: Braintrust) -> None:
        experiment = client.experiments.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(InsertEventsResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(InsertEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.insert(
                experiment_id="",
                events=[{}],
            )

    @parametrize
    def test_method_summarize(self, client: Braintrust) -> None:
        experiment = client.experiments.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    def test_method_summarize_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiments.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summarize_scores=True,
        )
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_summarize(self, client: Braintrust) -> None:
        response = client.experiments.with_raw_response.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_summarize(self, client: Braintrust) -> None:
        with client.experiments.with_streaming_response.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summarize(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiments.with_raw_response.summarize(
                experiment_id="",
            )


class TestAsyncExperiments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="dataset_version",
            description="description",
            ensure_new=True,
            metadata={"foo": "bar"},
            name="x",
            public=True,
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
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            base_exp_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_version="dataset_version",
            description="description",
            metadata={"foo": "bar"},
            name="name",
            public=True,
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
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.update(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.update(
                experiment_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.list()
        assert_matches_type(AsyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="experiment_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(AsyncListObjects[Experiment], experiment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(AsyncListObjects[Experiment], experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.feedback(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(FeedbackResponseSchema, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.feedback(
                experiment_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.fetch(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.fetch(
                experiment_id="",
            )

    @parametrize
    async def test_method_fetch_post(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_method_fetch_post_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.fetch_post(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(FetchExperimentEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_post(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.fetch_post(
                experiment_id="",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(InsertEventsResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.insert(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(InsertEventsResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.insert(
                experiment_id="",
                events=[{}],
            )

    @parametrize
    async def test_method_summarize(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiments.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summarize_scores=True,
        )
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiments.with_raw_response.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiments.with_streaming_response.summarize(
            experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(SummarizeExperimentResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiments.with_raw_response.summarize(
                experiment_id="",
            )
