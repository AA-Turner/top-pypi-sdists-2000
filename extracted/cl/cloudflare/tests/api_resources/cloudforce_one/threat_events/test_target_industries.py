# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import TargetIndustryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTargetIndustries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        target_industry = client.cloudforce_one.threat_events.target_industries.list(
            account_id="account_id",
        )
        assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.target_industries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target_industry = response.parse()
        assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.target_industries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target_industry = response.parse()
            assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.target_industries.with_raw_response.list(
                account_id="",
            )


class TestAsyncTargetIndustries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        target_industry = await async_client.cloudforce_one.threat_events.target_industries.list(
            account_id="account_id",
        )
        assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.target_industries.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target_industry = await response.parse()
        assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.target_industries.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target_industry = await response.parse()
            assert_matches_type(TargetIndustryListResponse, target_industry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.target_industries.with_raw_response.list(
                account_id="",
            )
