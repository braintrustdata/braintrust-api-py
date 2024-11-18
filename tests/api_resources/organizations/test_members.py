# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from braintrust_api import Braintrust, AsyncBraintrust
from braintrust_api.types.shared import PatchOrganizationMembersOutput

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Braintrust) -> None:
        member = client.organizations.members.update()
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Braintrust) -> None:
        member = client.organizations.members.update(
            invite_users={
                "emails": ["string"],
                "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "group_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "group_name": "group_name",
                "group_names": ["string"],
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "send_invite_emails": True,
            },
            org_id="org_id",
            org_name="org_name",
            remove_users={
                "emails": ["string"],
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
        )
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Braintrust) -> None:
        response = client.organizations.members.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Braintrust) -> None:
        with client.organizations.members.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncBraintrust) -> None:
        member = await async_client.organizations.members.update()
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBraintrust) -> None:
        member = await async_client.organizations.members.update(
            invite_users={
                "emails": ["string"],
                "group_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "group_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "group_name": "group_name",
                "group_names": ["string"],
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "send_invite_emails": True,
            },
            org_id="org_id",
            org_name="org_name",
            remove_users={
                "emails": ["string"],
                "ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
        )
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.organizations.members.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBraintrust) -> None:
        async with async_client.organizations.members.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(PatchOrganizationMembersOutput, member, path=["response"])

        assert cast(Any, response.is_closed) is True
