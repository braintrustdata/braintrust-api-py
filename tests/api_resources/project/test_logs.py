# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from braintrust import Braintrust, AsyncBraintrust
from tests.utils import assert_matches_type
from braintrust.types.project import (
    LogFetchResponse,
    LogInsertResponse,
    LogFetchPostResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: Braintrust) -> None:
        log = client.project.logs.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert log is None

    @parametrize
    def test_raw_response_feedback(self, client: Braintrust) -> None:
        response = client.project.logs.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert log is None

    @parametrize
    def test_streaming_response_feedback(self, client: Braintrust) -> None:
        with client.project.logs.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_feedback(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.logs.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    def test_method_fetch(self, client: Braintrust) -> None:
        log = client.project.logs.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    def test_method_fetch_with_all_params(self, client: Braintrust) -> None:
        log = client.project.logs.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Braintrust) -> None:
        response = client.project.logs.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Braintrust) -> None:
        with client.project.logs.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogFetchResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.logs.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_fetch_post(self, client: Braintrust) -> None:
        log = client.project.logs.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    def test_method_fetch_post_with_all_params(self, client: Braintrust) -> None:
        log = client.project.logs.fetch_post(
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
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    def test_raw_response_fetch_post(self, client: Braintrust) -> None:
        response = client.project.logs.with_raw_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_fetch_post(self, client: Braintrust) -> None:
        with client.project.logs.with_streaming_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogFetchPostResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch_post(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.logs.with_raw_response.fetch_post(
                "",
            )

    @parametrize
    def test_method_insert(self, client: Braintrust) -> None:
        log = client.project.logs.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(LogInsertResponse, log, path=["response"])

    @parametrize
    def test_raw_response_insert(self, client: Braintrust) -> None:
        response = client.project.logs.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogInsertResponse, log, path=["response"])

    @parametrize
    def test_streaming_response_insert(self, client: Braintrust) -> None:
        with client.project.logs.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogInsertResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_insert(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.project.logs.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )
        assert log is None

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project.logs.with_raw_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert log is None

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project.logs.with_streaming_response.feedback(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert log is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_feedback(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.logs.with_raw_response.feedback(
                "",
                feedback=[{"id": "string"}, {"id": "string"}, {"id": "string"}],
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    async def test_method_fetch_with_all_params(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            max_root_span_id="string",
            max_xact_id=0,
            version=0,
        )
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project.logs.with_raw_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogFetchResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project.logs.with_streaming_response.fetch(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogFetchResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.logs.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_fetch_post(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    async def test_method_fetch_post_with_all_params(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.fetch_post(
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
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project.logs.with_raw_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogFetchPostResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_fetch_post(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project.logs.with_streaming_response.fetch_post(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogFetchPostResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch_post(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.logs.with_raw_response.fetch_post(
                "",
            )

    @parametrize
    async def test_method_insert(self, async_client: AsyncBraintrust) -> None:
        log = await async_client.project.logs.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )
        assert_matches_type(LogInsertResponse, log, path=["response"])

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.project.logs.with_raw_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogInsertResponse, log, path=["response"])

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncBraintrust) -> None:
        async with async_client.project.logs.with_streaming_response.insert(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            events=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogInsertResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_insert(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.project.logs.with_raw_response.insert(
                "",
                events=[{}, {}, {}],
            )
