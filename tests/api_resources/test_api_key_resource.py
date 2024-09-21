# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from braintrust_api import Braintrust, AsyncBraintrust

from braintrust_api.types.shared import CreateAPIKeyOutput, APIKey

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
from braintrust_api.types import api_key_resource_create_params
from braintrust_api.types import api_key_resource_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestAPIKeyResource:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.create(
            name="name",
        )
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.create(
            name="name",
            org_name="org_name",
        )
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:

        response = client.api_key_resource.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = response.parse()
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.api_key_resource.with_streaming_response.create(
            name="name",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = response.parse()
            assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:

        response = client.api_key_resource.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = response.parse()
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.api_key_resource.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = response.parse()
            assert_matches_type(APIKey, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
          client.api_key_resource.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.list()
        assert_matches_type(SyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.list(
            api_key_name="api_key_name",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:

        response = client.api_key_resource.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = response.parse()
        assert_matches_type(SyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.api_key_resource.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = response.parse()
            assert_matches_type(SyncListObjects[APIKey], api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        api_key_resource = client.api_key_resource.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:

        response = client.api_key_resource.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = response.parse()
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.api_key_resource.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = response.parse()
            assert_matches_type(APIKey, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
          client.api_key_resource.with_raw_response.delete(
              "",
          )
class TestAsyncAPIKeyResource:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.create(
            name="name",
        )
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.create(
            name="name",
            org_name="org_name",
        )
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.api_key_resource.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = await response.parse()
        assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.api_key_resource.with_streaming_response.create(
            name="name",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = await response.parse()
            assert_matches_type(CreateAPIKeyOutput, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.api_key_resource.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = await response.parse()
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.api_key_resource.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = await response.parse()
            assert_matches_type(APIKey, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
          await async_client.api_key_resource.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.list()
        assert_matches_type(AsyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.list(
            api_key_name="api_key_name",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.api_key_resource.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = await response.parse()
        assert_matches_type(AsyncListObjects[APIKey], api_key_resource, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.api_key_resource.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = await response.parse()
            assert_matches_type(AsyncListObjects[APIKey], api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        api_key_resource = await async_client.api_key_resource.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.api_key_resource.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        api_key_resource = await response.parse()
        assert_matches_type(APIKey, api_key_resource, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.api_key_resource.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            api_key_resource = await response.parse()
            assert_matches_type(APIKey, api_key_resource, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_id` but received ''"):
          await async_client.api_key_resource.with_raw_response.delete(
              "",
          )