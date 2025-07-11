# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit.connectors import SnapshotGetResponse, SnapshotListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        snapshot = client.magic_transit.connectors.snapshots.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        snapshot = client.magic_transit.connectors.snapshots.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.snapshots.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.snapshots.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.snapshots.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
                from_=0,
                to=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.snapshots.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                from_=0,
                to=0,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        snapshot = client.magic_transit.connectors.snapshots.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        )
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.connectors.snapshots.with_raw_response.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.connectors.snapshots.with_streaming_response.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.connectors.snapshots.with_raw_response.get(
                snapshot_t=0,
                account_id="",
                connector_id="connector_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.magic_transit.connectors.snapshots.with_raw_response.get(
                snapshot_t=0,
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                connector_id="",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        snapshot = await async_client.magic_transit.connectors.snapshots.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        snapshot = await async_client.magic_transit.connectors.snapshots.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.snapshots.with_raw_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.snapshots.with_streaming_response.list(
            connector_id="connector_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_=0,
            to=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.with_raw_response.list(
                connector_id="connector_id",
                account_id="",
                from_=0,
                to=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.with_raw_response.list(
                connector_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                from_=0,
                to=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        snapshot = await async_client.magic_transit.connectors.snapshots.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        )
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.connectors.snapshots.with_raw_response.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.connectors.snapshots.with_streaming_response.get(
            snapshot_t=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            connector_id="connector_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotGetResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.with_raw_response.get(
                snapshot_t=0,
                account_id="",
                connector_id="connector_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.magic_transit.connectors.snapshots.with_raw_response.get(
                snapshot_t=0,
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                connector_id="",
            )
