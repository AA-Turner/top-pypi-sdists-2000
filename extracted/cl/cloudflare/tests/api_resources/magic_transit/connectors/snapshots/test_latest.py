# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit.connectors.snapshots import LatestListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLatest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        latest = client.magic_transit.connectors.snapshots.latest.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LatestListResponse, latest, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        latest = response.parse()
        assert_matches_type(LatestListResponse, latest, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.snapshots.latest.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            latest = response.parse()
            assert_matches_type(LatestListResponse, latest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLatest:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        latest = await async_client.magic_transit.connectors.snapshots.latest.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LatestListResponse, latest, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        latest = await response.parse()
        assert_matches_type(LatestListResponse, latest, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.snapshots.latest.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            latest = await response.parse()
            assert_matches_type(LatestListResponse, latest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.latest.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
