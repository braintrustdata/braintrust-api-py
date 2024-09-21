# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from braintrust_api import Braintrust, AsyncBraintrust

from braintrust_api.types.shared import Function

from typing import Any, cast

from braintrust_api.pagination import SyncListObjects, AsyncListObjects

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from braintrust_api import Braintrust, AsyncBraintrust
from tests.utils import assert_matches_type
from braintrust_api.types import function_create_params
from braintrust_api.types import function_update_params
from braintrust_api.types import function_list_params
from braintrust_api.types import function_replace_params
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api.types import shared

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestFunction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        function = client.function.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        function = client.function.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            description="description",
            function_type="task",
            origin={
                "object_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "object_type": "organization",
                "internal": True,
            },
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        function = client.function.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          client.function.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        function = client.function.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        function = client.function.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            function_data={
                "type": "prompt"
            },
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
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          client.function.with_raw_response.update(
              function_id="",
          )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        function = client.function.list()
        assert_matches_type(SyncListObjects[Function], function, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        function = client.function.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            slug="slug",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(SyncListObjects[Function], function, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(SyncListObjects[Function], function, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(SyncListObjects[Function], function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        function = client.function.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          client.function.with_raw_response.delete(
              "",
          )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        function = client.function.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        function = client.function.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            description="description",
            function_type="task",
            origin={
                "object_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "object_type": "organization",
                "internal": True,
            },
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:

        response = client.function.with_raw_response.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.function.with_streaming_response.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncFunction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            description="description",
            function_type="task",
            origin={
                "object_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "object_type": "organization",
                "internal": True,
            },
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.create(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          await async_client.function.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            function_data={
                "type": "prompt"
            },
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
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.update(
            function_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          await async_client.function.with_raw_response.update(
              function_id="",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.list()
        assert_matches_type(AsyncListObjects[Function], function, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            function_name="function_name",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            slug="slug",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version="version",
        )
        assert_matches_type(AsyncListObjects[Function], function, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(AsyncListObjects[Function], function, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(AsyncListObjects[Function], function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
          await async_client.function.with_raw_response.delete(
              "",
          )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        function = await async_client.function.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            description="description",
            function_type="task",
            origin={
                "object_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "object_type": "organization",
                "internal": True,
            },
            prompt_data={
                "options": {
                    "model": "model",
                    "params": {
                        "frequency_penalty": 0,
                        "function_call": "auto",
                        "max_tokens": 0,
                        "n": 0,
                        "presence_penalty": 0,
                        "response_format": {
                            "type": "json_object"
                        },
                        "stop": ["string", "string", "string"],
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
                    "choice_scores": {
                        "foo": 0
                    },
                    "type": "llm_classifier",
                    "use_cot": True,
                },
                "prompt": {
                    "content": "content",
                    "type": "completion",
                },
            },
            tags=["string", "string", "string"],
        )
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.function.with_raw_response.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        function = await response.parse()
        assert_matches_type(Function, function, path=['response'])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.function.with_streaming_response.replace(
            function_data={
                "type": "prompt"
            },
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            function = await response.parse()
            assert_matches_type(Function, function, path=['response'])

        assert cast(Any, response.is_closed) is True