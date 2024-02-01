# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from braintrust import Braintrust, AsyncBraintrust
from tests.utils import assert_matches_type
from braintrust.types import (
    Experiment,
    ExperimentListResponse,
    ExperimentFetchResponse,
    ExperimentInsertResponse,
    ExperimentFetchPostResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        experiment = client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
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
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        experiment = client.experiment.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.retrieve(
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
            client.experiment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        experiment = client.experiment.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiment.update(
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
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        experiment = client.experiment.list()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiment.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="string",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentListResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        experiment = client.experiment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.delete(
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
            client.experiment.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_feedback(self, client: Braintrust) -> None:
        experiment = client.experiment.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert experiment is None

    @parametrize
    def test_raw_response_feedback(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert experiment is None

    @parametrize
    def test_streaming_response_feedback(self, client: Braintrust) -> None:
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
    def test_path_params_feedback(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    def test_method_fetch(self, client: Braintrust) -> None:
        experiment = client.experiment.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiment.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_post(self, client: Braintrust) -> None:
        experiment = client.experiment.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    def test_method_fetch_post_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiment.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters=[
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
            ],
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_fetch_post(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_fetch_post(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_post(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.fetch_post(
                "",
            )

    @parametrize
    def test_method_insert(self, client: Braintrust) -> None:
        experiment = client.experiment.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: Braintrust) -> None:
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
    def test_path_params_insert(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            client.experiment.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        experiment = client.experiment.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        experiment = client.experiment.replace(
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
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.experiment.with_raw_response.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.experiment.with_streaming_response.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExperiment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
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
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.retrieve(
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
            await async_client.experiment.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.update(
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
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.list()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_name="string",
            limit=0,
            org_name="string",
            project_name="string",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentListResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentListResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.delete(
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
            await async_client.experiment.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert experiment is None

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert experiment is None

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrust) -> None:
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
    async def test_path_params_feedback(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentFetchResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_post(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    async def test_method_fetch_post_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters=[
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
                {
                    "type": "path_lookup",
                    "path": ["string", "string", "string"],
                    "value": {},
                },
            ],
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(ExperimentFetchPostResponse, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_post(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.fetch_post(
                "",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(ExperimentInsertResponse, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrust) -> None:
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
    async def test_path_params_insert(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `experiment_id` but received ''"):
            await async_client.experiment.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        experiment = await async_client.experiment.replace(
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
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.experiment.with_raw_response.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(Experiment, experiment, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.experiment.with_streaming_response.replace(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(Experiment, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True
