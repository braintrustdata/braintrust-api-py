# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from braintrust import Braintrust, AsyncBraintrust
from tests.utils import assert_matches_type
from braintrust.types import ACL
from braintrust.pagination import SyncListObjects, AsyncListObjects

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Braintrust) -> None:
        acl = client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Braintrust) -> None:
        acl = client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Braintrust) -> None:
        acl = client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Braintrust) -> None:
        acl = client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Braintrust) -> None:
        acl = client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Braintrust) -> None:
        acl = client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Braintrust) -> None:
        acl = client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Braintrust) -> None:
        acl = client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Braintrust) -> None:
        acl = client.acl.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.acl.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Braintrust) -> None:
        acl = client.acl.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(SyncListObjects[ACL], acl, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Braintrust) -> None:
        acl = client.acl.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncListObjects[ACL], acl, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(SyncListObjects[ACL], acl, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(SyncListObjects[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Braintrust) -> None:
        acl = client.acl.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Braintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            client.acl.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_replace_overload_1(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_1(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_1(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_1(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_overload_2(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_2(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_2(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_2(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_overload_3(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_3(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_3(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_3(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace_overload_4(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_method_replace_with_all_params_overload_4(self, client: Braintrust) -> None:
        acl = client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_raw_response_replace_overload_4(self, client: Braintrust) -> None:
        response = client.acl.with_raw_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    def test_streaming_response_replace_overload_4(self, client: Braintrust) -> None:
        with client.acl.with_streaming_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncACL:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.create(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.create(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.acl.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )
        assert_matches_type(AsyncListObjects[ACL], acl, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncListObjects[ACL], acl, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(AsyncListObjects[ACL], acl, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.list(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(AsyncListObjects[ACL], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBraintrust) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `acl_id` but received ''"):
            await async_client.acl.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_replace_overload_1(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_1(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_1(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_1(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_overload_2(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_2(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_2(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_2(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.replace(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_overload_3(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_3(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_3(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_3(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            permission="create",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace_overload_4(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params_overload_4(self, async_client: AsyncBraintrust) -> None:
        acl = await async_client.acl.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            restrict_object_type="organization",
        )
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_raw_response_replace_overload_4(self, async_client: AsyncBraintrust) -> None:
        response = await async_client.acl.with_raw_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACL, acl, path=["response"])

    @parametrize
    async def test_streaming_response_replace_overload_4(self, async_client: AsyncBraintrust) -> None:
        async with async_client.acl.with_streaming_response.replace(
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="organization",
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACL, acl, path=["response"])

        assert cast(Any, response.is_closed) is True
