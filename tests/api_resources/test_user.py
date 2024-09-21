# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from braintrust_api import Braintrust, AsyncBraintrust

from braintrust_api.types.shared import User

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
from braintrust_api.types import user_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        user = client.user.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:

        response = client.user.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = response.parse()
        assert_matches_type(User, user, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.user.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = response.parse()
            assert_matches_type(User, user, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
          client.user.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        user = client.user.list()
        assert_matches_type(SyncListObjects[User], user, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        user = client.user.list(
            email="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            family_name="string",
            given_name="string",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[User], user, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:

        response = client.user.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = response.parse()
        assert_matches_type(SyncListObjects[User], user, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.user.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = response.parse()
            assert_matches_type(SyncListObjects[User], user, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        user = await async_client.user.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(User, user, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.user.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = await response.parse()
        assert_matches_type(User, user, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.user.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = await response.parse()
            assert_matches_type(User, user, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
          await async_client.user.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        user = await async_client.user.list()
        assert_matches_type(AsyncListObjects[User], user, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        user = await async_client.user.list(
            email="string",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            family_name="string",
            given_name="string",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            org_name="org_name",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[User], user, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.user.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = await response.parse()
        assert_matches_type(AsyncListObjects[User], user, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.user.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = await response.parse()
            assert_matches_type(AsyncListObjects[User], user, path=['response'])

        assert cast(Any, response.is_closed) is True