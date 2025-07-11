# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.devices import OverrideCodeGetResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverrideCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            override_code = client.zero_trust.devices.override_codes.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            )

        assert_matches_type(SyncSinglePage[object], override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.zero_trust.devices.override_codes.with_raw_response.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = response.parse()
        assert_matches_type(SyncSinglePage[object], override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.zero_trust.devices.override_codes.with_streaming_response.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                override_code = response.parse()
                assert_matches_type(SyncSinglePage[object], override_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                client.zero_trust.devices.override_codes.with_raw_response.list(
                    device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
                client.zero_trust.devices.override_codes.with_raw_response.list(
                    device_id="",
                    account_id="699d98642c564d2e855e9661899b7252",
                )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        override_code = client.zero_trust.devices.override_codes.get(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.override_codes.with_raw_response.get(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = response.parse()
        assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.override_codes.with_streaming_response.get(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override_code = response.parse()
            assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.override_codes.with_raw_response.get(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            client.zero_trust.devices.override_codes.with_raw_response.get(
                registration_id="",
                account_id="account_id",
            )


class TestAsyncOverrideCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            override_code = await async_client.zero_trust.devices.override_codes.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            )

        assert_matches_type(AsyncSinglePage[object], override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.zero_trust.devices.override_codes.with_raw_response.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = await response.parse()
        assert_matches_type(AsyncSinglePage[object], override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.zero_trust.devices.override_codes.with_streaming_response.list(
                device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                override_code = await response.parse()
                assert_matches_type(AsyncSinglePage[object], override_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                await async_client.zero_trust.devices.override_codes.with_raw_response.list(
                    device_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_id` but received ''"):
                await async_client.zero_trust.devices.override_codes.with_raw_response.list(
                    device_id="",
                    account_id="699d98642c564d2e855e9661899b7252",
                )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        override_code = await async_client.zero_trust.devices.override_codes.get(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.override_codes.with_raw_response.get(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override_code = await response.parse()
        assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.override_codes.with_streaming_response.get(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override_code = await response.parse()
            assert_matches_type(OverrideCodeGetResponse, override_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.override_codes.with_raw_response.get(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            await async_client.zero_trust.devices.override_codes.with_raw_response.get(
                registration_id="",
                account_id="account_id",
            )
