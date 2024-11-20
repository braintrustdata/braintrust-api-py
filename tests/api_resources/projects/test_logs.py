# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.types.shared import InsertEventsResponse, FeedbackResponseSchema, FetchProjectLogsEventsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: Braintrust) -> None:
        log = client.projects.logs.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, log, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Braintrust) -> None:
        response = client.projects.logs.with_raw_response.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(FeedbackResponseSchema, log, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Braintrust) -> None:
        with client.projects.logs.with_streaming_response.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(FeedbackResponseSchema, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.logs.with_raw_response.feedback(
                project_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    def test_method_fetch(self, client: Braintrust) -> None:
        log = client.projects.logs.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: Braintrust) -> None:
        log = client.projects.logs.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Braintrust) -> None:
        response = client.projects.logs.with_raw_response.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Braintrust) -> None:
        with client.projects.logs.with_streaming_response.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.logs.with_raw_response.fetch(
                project_id="",
            )

    @parametrize
    def test_method_fetch_post(self, client: Braintrust) -> None:
        log = client.projects.logs.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_method_fetch_post_with_all_params(self, client: Braintrust) -> None:
        log = client.projects.logs.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_raw_response_fetch_post(self, client: Braintrust) -> None:
        response = client.projects.logs.with_raw_response.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_fetch_post(self, client: Braintrust) -> None:
        with client.projects.logs.with_streaming_response.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_post(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.logs.with_raw_response.fetch_post(
                project_id="",
            )

    @parametrize
    def test_method_insert(self, client: Braintrust) -> None:
        log = client.projects.logs.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, log, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: Braintrust) -> None:
        response = client.projects.logs.with_raw_response.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(InsertEventsResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: Braintrust) -> None:
        with client.projects.logs.with_streaming_response.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(InsertEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.logs.with_raw_response.insert(
                project_id="",
                events=[{}],
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )
        assert_matches_type(FeedbackResponseSchema, log, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.projects.logs.with_raw_response.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(FeedbackResponseSchema, log, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrust) -> None:
        async with async_client.projects.logs.with_streaming_response.feedback(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(FeedbackResponseSchema, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.logs.with_raw_response.feedback(
                project_id="",
                feedback=[{"id": "id"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.projects.logs.with_raw_response.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrust) -> None:
        async with async_client.projects.logs.with_streaming_response.fetch(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.logs.with_raw_response.fetch(
                project_id="",
            )

    @parametrize
    async def test_method_fetch_post(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_method_fetch_post_with_all_params(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="cursor",
            limit=0,
            max_root_span_id="max_root_span_id",
            max_xact_id="max_xact_id",
            version="version",
        )
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.projects.logs.with_raw_response.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        async with async_client.projects.logs.with_streaming_response.fetch_post(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(FetchProjectLogsEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_post(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.logs.with_raw_response.fetch_post(
                project_id="",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.projects.logs.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )
        assert_matches_type(InsertEventsResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.projects.logs.with_raw_response.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(InsertEventsResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrust) -> None:
        async with async_client.projects.logs.with_streaming_response.insert(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(InsertEventsResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.logs.with_raw_response.insert(
                project_id="",
                events=[{}],
            )
