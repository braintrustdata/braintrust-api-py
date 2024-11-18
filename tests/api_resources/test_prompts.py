# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.pagination import SyncListObjects, AsyncListObjects
from braintrust_api.types.shared import Prompt

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        prompt = client.prompts.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        prompt = client.prompts.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
            description="description",
            function_type="llm",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        prompt = client.prompts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        prompt = client.prompts.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        prompt = client.prompts.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            slug="slug",
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.update(
                prompt_id="",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        prompt = client.prompts.list()
        assert_matches_type(SyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        prompt = client.prompts.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            prompt_name="prompt_name",
            slug="slug",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(SyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(SyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(SyncListObjects[Prompt], prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        prompt = client.prompts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        prompt = client.prompts.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        prompt = client.prompts.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
            description="description",
            function_type="llm",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:
        response = client.prompts.with_raw_response.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.prompts.with_streaming_response.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
            description="description",
            function_type="llm",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.create(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            slug="slug",
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.update(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.update(
                prompt_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.list()
        assert_matches_type(AsyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            prompt_name="prompt_name",
            slug="slug",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(AsyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(AsyncListObjects[Prompt], prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(AsyncListObjects[Prompt], prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
            await async_client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        prompt = await async_client.prompts.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
            description="description",
            function_type="llm",
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {"type": "json_object"},
                        "stop": ["string"],
                        "temperature": 0,
                        "tool_choice": "auto",
                        "top_p": 0,
                        "use_cache": True,
                    },
                    "position": "position",
                },
                "origin": {
                    "project_id": "project_id",
                    "prompt_id": "prompt_id",
                    "prompt_version": "prompt_version",
                },
                "parser": {
                    "choice_scores": {"foo": 0},
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
                "tool_functions": [
                    {
                        "id": "id",
                        "type": "function",
                    }
                ],
            },
            tags=["string"],
        )
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.prompts.with_raw_response.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Prompt, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.prompts.with_streaming_response.replace(
            name="x",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Prompt, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True
