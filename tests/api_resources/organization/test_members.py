# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from braintrust_api import Braintrust, AsyncBraintrust

from braintrust_api.types.organization import MemberUpdateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from braintrust_api import Braintrust, AsyncBraintrust
from tests.utils import assert_matches_type
from braintrust_api.types.organization import member_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        member = client.organization.members.update()
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        member = client.organization.members.update(
            invite_users={
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "emails": ["string", "string", "string"],
                "send_invite_emails": True,
                "group_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "group_names": ["string", "string", "string"],
                "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "group_name": "group_name",
            },
            org_id="org_id",
            org_name="org_name",
            remove_users={
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "emails": ["string", "string", "string"],
            },
        )
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:

        response = client.organization.members.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        member = response.parse()
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.organization.members.with_streaming_response.update() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            member = response.parse()
            assert_matches_type(MemberUpdateResponse, member, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        member = await async_client.organization.members.update()
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        member = await async_client.organization.members.update(
            invite_users={
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "emails": ["string", "string", "string"],
                "send_invite_emails": True,
                "group_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "group_names": ["string", "string", "string"],
                "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "group_name": "group_name",
            },
            org_id="org_id",
            org_name="org_name",
            remove_users={
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "emails": ["string", "string", "string"],
            },
        )
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:

        response = await async_client.organization.members.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        member = await response.parse()
        assert_matches_type(MemberUpdateResponse, member, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organization.members.with_streaming_response.update() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            member = await response.parse()
            assert_matches_type(MemberUpdateResponse, member, path=['response'])

        assert cast(Any, response.is_closed) is True