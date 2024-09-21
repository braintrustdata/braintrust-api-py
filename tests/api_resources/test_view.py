# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from braintrust_api import Braintrust, AsyncBraintrust

from braintrust_api.types.shared import View

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
from braintrust_api.types import view_create_params
from braintrust_api.types import view_retrieve_params
from braintrust_api.types import view_update_params
from braintrust_api.types import view_list_params
from braintrust_api.types import view_delete_params
from braintrust_api.types import view_replace_params
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api.types import shared
from braintrust_api._utils import parse_datetime
from braintrust_api._utils import parse_datetime
from braintrust_api._utils import parse_datetime
from braintrust_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestView:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Braintrust) -> None:
        view = client.view.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: Braintrust) -> None:
        view = client.view.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        view = client.view.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          client.view.with_raw_response.retrieve(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        view = client.view.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        view = client.view.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            name="name",
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          client.view.with_raw_response.update(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        view = client.view.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(SyncListObjects[View], view, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        view = client.view.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_name="view_name",
            view_type="projects",
        )
        assert_matches_type(SyncListObjects[View], view, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(SyncListObjects[View], view, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(SyncListObjects[View], view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        view = client.view.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          client.view.with_raw_response.delete(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    def test_method_replace(self, client: Braintrust) -> None:
        view = client.view.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_method_replace_with_all_params(self, client: Braintrust) -> None:
        view = client.view.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_raw_response_replace(self, client: Braintrust) -> None:

        response = client.view.with_raw_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    def test_streaming_response_replace(self, client: Braintrust) -> None:
        with client.view.with_streaming_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncView:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.create(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.retrieve(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          await async_client.view.with_raw_response.retrieve(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            name="name",
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          await async_client.view.with_raw_response.update(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(AsyncListObjects[View], view, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_name="view_name",
            view_type="projects",
        )
        assert_matches_type(AsyncListObjects[View], view, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(AsyncListObjects[View], view, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(AsyncListObjects[View], view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
          await async_client.view.with_raw_response.delete(
              view_id="",
              object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              object_type="organization",
          )

    @parametrize
    async def test_method_replace(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncBraintrust) -> None:
        view = await async_client.view.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            options={
                "column_visibility": {
                    "foo": True
                },
                "column_order": ["string", "string", "string"],
                "column_sizing": {
                    "foo": 0
                },
            },
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_data={
                "search": {
                    "filter": [{}, {}, {}],
                    "tag": [{}, {}, {}],
                    "match": [{}, {}, {}],
                    "sort": [{}, {}, {}],
                }
            },
        )
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.view.with_raw_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        view = await response.parse()
        assert_matches_type(View, view, path=['response'])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncBraintrust) -> None:
        async with async_client.view.with_streaming_response.replace(
            name="name",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            view_type="projects",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            view = await response.parse()
            assert_matches_type(View, view, path=['response'])

        assert cast(Any, response.is_closed) is True