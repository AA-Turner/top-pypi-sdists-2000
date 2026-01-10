"""gRPC-based threads operations."""

from __future__ import annotations

import asyncio
from datetime import UTC
from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Literal
from uuid import UUID

if TYPE_CHECKING:
    from collections.abc import Sequence

import orjson
import structlog
from starlette.exceptions import HTTPException

from langgraph_api.grpc.client import get_shared_client
from langgraph_api.grpc.generated import checkpointer_pb2
from langgraph_api.grpc.generated import core_api_pb2 as pb
from langgraph_api.grpc.generated import enum_thread_status_pb2 as enum_thread_status
from langgraph_api.grpc.ops import (
    Authenticated,
    _map_sort_order,
    grpc_error_guard,
    map_if_exists,
)
from langgraph_api.serde import json_dumpb, json_dumpb_optional, json_loads
from langgraph_api.state import patch_interrupt

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from langgraph_api.schema import (
        MetadataInput,
        OnConflictBehavior,
        Thread,
        ThreadSelectField,
        ThreadStatus,
    )

logger = structlog.stdlib.get_logger(__name__)

THREAD_STATUS_TO_PB = {
    "idle": enum_thread_status.idle,
    "busy": enum_thread_status.busy,
    "interrupted": enum_thread_status.interrupted,
    "error": enum_thread_status.error,
}

THREAD_STATUS_FROM_PB = {v: k for k, v in THREAD_STATUS_TO_PB.items()}

THREAD_SORT_BY_MAP = {
    "unspecified": pb.ThreadsSortBy.THREADS_SORT_BY_UNSPECIFIED,  # for enum completeness, never sent
    "thread_id": pb.ThreadsSortBy.THREADS_SORT_BY_THREAD_ID,
    "created_at": pb.ThreadsSortBy.THREADS_SORT_BY_CREATED_AT,
    "updated_at": pb.ThreadsSortBy.THREADS_SORT_BY_UPDATED_AT,
    "status": pb.ThreadsSortBy.THREADS_SORT_BY_STATUS,
}

THREAD_TTL_STRATEGY_MAP = {
    "delete": pb.ThreadTTLStrategy.THREAD_TTL_STRATEGY_DELETE,
    "keep_latest": pb.ThreadTTLStrategy.THREAD_TTL_STRATEGY_KEEP_LATEST,
}


def _map_thread_status(
    status: ThreadStatus | None,
) -> enum_thread_status.ThreadStatus | None:
    if status is None:
        return None
    return THREAD_STATUS_TO_PB.get(status)


def _map_threads_sort_by(sort_by: str | None) -> pb.ThreadsSortBy:
    if not sort_by or sort_by.lower() == "unspecified":
        return pb.ThreadsSortBy.THREADS_SORT_BY_CREATED_AT
    return THREAD_SORT_BY_MAP.get(
        sort_by.lower(), pb.ThreadsSortBy.THREADS_SORT_BY_CREATED_AT
    )


def _map_thread_ttl(ttl: dict[str, Any] | None) -> pb.ThreadTTLConfig | None:
    if not ttl:
        return None

    config = pb.ThreadTTLConfig()
    strategy = ttl.get("strategy")
    if strategy:
        mapped_strategy = THREAD_TTL_STRATEGY_MAP.get(str(strategy).lower())
        if mapped_strategy is None:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=f"Invalid thread TTL strategy: {strategy}. Expected one of {list(THREAD_TTL_STRATEGY_MAP.keys())}",
            )
        config.strategy = mapped_strategy

    ttl_value = ttl.get("ttl", ttl.get("default_ttl"))
    if ttl_value is not None:
        config.default_ttl = float(ttl_value)

    sweep_interval = ttl.get("sweep_interval_minutes")
    if sweep_interval is not None:
        config.sweep_interval_minutes = int(sweep_interval)

    # Note: sweep_limit is a server-side configuration for the TTL sweep loop,
    # not a per-thread setting, so we don't send it via gRPC

    return config


def fragment_to_value(fragment: pb.Fragment | None) -> Any:
    if fragment is None or not fragment.value or fragment.value == b"{}":
        return None
    try:
        return json_loads(fragment.value)
    except orjson.JSONDecodeError:
        logger.warning("Failed to decode fragment", fragment=fragment.value)
        return None


def _proto_interrupts_to_dict(
    interrupts_map: dict[str, pb.Interrupts],
) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for key, interrupts in interrupts_map.items():
        entries: list[dict[str, Any]] = []
        for interrupt in interrupts.interrupts:
            entry: dict[str, Any] = {
                "id": interrupt.id or None,
                "value": json_loads(interrupt.value),
            }
            if interrupt.when:
                entry["when"] = interrupt.when
            if interrupt.resumable:
                entry["resumable"] = interrupt.resumable
            if interrupt.ns:
                entry["ns"] = list(interrupt.ns)
            entries.append(entry)
        out[key] = entries
    return out


def proto_to_thread(proto_thread: pb.Thread) -> Thread:
    """Convert protobuf Thread to API dictionary format."""
    thread_id = (
        UUID(proto_thread.thread_id.value)
        if proto_thread.HasField("thread_id")
        else None
    )
    if thread_id is None:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail="Thread response missing thread_id",
        )
    created_at = (
        proto_thread.created_at.ToDatetime(tzinfo=UTC)
        if proto_thread.HasField("created_at")
        else None
    )
    updated_at = (
        proto_thread.updated_at.ToDatetime(tzinfo=UTC)
        if proto_thread.HasField("updated_at")
        else None
    )
    status = THREAD_STATUS_FROM_PB.get(proto_thread.status, "idle")

    return {
        "thread_id": thread_id,
        "created_at": created_at,
        "updated_at": updated_at,
        # Unlike other fields, metadata should never be `None`.
        "metadata": fragment_to_value(proto_thread.metadata) or {},
        "config": fragment_to_value(proto_thread.config) or {},
        "error": fragment_to_value(proto_thread.error),
        "status": status,  # type: ignore[typeddict-item]
        "values": fragment_to_value(proto_thread.values),
        "interrupts": _proto_interrupts_to_dict(dict(proto_thread.interrupts)),
    }


def _filter_thread_fields(
    thread: Thread, select: list[ThreadSelectField] | None
) -> dict[str, Any]:
    if not select:
        return dict(thread)
    return {field: thread[field] for field in select if field in thread}


def _normalize_uuid(value: UUID | str) -> str:
    return str(value) if isinstance(value, UUID) else str(UUID(str(value)))


def _thread_status_checkpoint_to_proto(
    checkpoint: dict[str, Any] | None,
) -> pb.ThreadStatusCheckpoint | None:
    """Convert checkpoint dict to ThreadStatusCheckpoint proto."""
    if checkpoint is None:
        return None

    # Compute interrupts map from tasks (same logic as storage_postgres/ops.py)
    interrupts = {
        t["id"]: [patch_interrupt(i) for i in t["interrupts"]]
        for t in checkpoint.get("tasks", [])
        if t.get("interrupts")
    }

    return pb.ThreadStatusCheckpoint(
        values_json=json_dumpb(checkpoint.get("values", {})),
        next=list(checkpoint.get("next", [])),
        interrupts_json=json_dumpb(interrupts),
    )


def _json_contains(container: Any, subset: dict[str, Any]) -> bool:
    if not subset:
        return True
    if not isinstance(container, dict):
        return False
    for key, value in subset.items():
        if key not in container:
            return False
        candidate = container[key]
        if isinstance(value, dict):
            if not _json_contains(candidate, value):
                return False
        else:
            if candidate != value:
                return False
    return True


@grpc_error_guard
class Threads(Authenticated):
    """gRPC-based threads operations."""

    resource = "threads"

    @staticmethod
    async def search(
        conn,  # Not used in gRPC implementation
        *,
        ids: list[str] | list[UUID] | None = None,
        metadata: MetadataInput,
        values: MetadataInput,
        status: ThreadStatus | None,
        limit: int,
        offset: int,
        sort_by: str | None = None,
        sort_order: str | None = None,
        select: list[ThreadSelectField] | None = None,
        ctx: Any = None,
    ) -> tuple[AsyncIterator[Thread], int | None]:  # type: ignore[return-value]
        metadata = metadata or {}
        values = values or {}

        auth_filters = await Threads.handle_event(
            ctx,
            "search",
            {
                "metadata": metadata,
                "values": values,
                "status": status,
                "limit": limit,
                "offset": offset,
            },
        )

        if ids:
            normalized_ids = [_normalize_uuid(thread_id) for thread_id in ids]
            threads: list[Thread] = []
            client = await get_shared_client()
            for thread_id in normalized_ids:
                request = pb.GetThreadRequest(
                    thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
                    filters=auth_filters,
                )
                response = await client.threads.Get(request)
                thread = proto_to_thread(response)

                if status and thread["status"] != status:
                    continue
                if metadata and not _json_contains(thread["metadata"], metadata):
                    continue
                if values and not _json_contains(thread.get("values") or {}, values):
                    continue
                threads.append(thread)

            total = len(threads)
            paginated = threads[offset : offset + limit]
            cursor = offset + limit if total > offset + limit else None

            async def generate_results():
                for thread in paginated:
                    yield _filter_thread_fields(thread, select)

            return generate_results(), cursor

        request_kwargs: dict[str, Any] = {
            "filters": auth_filters,
            "metadata_json": json_dumpb_optional(metadata),
            "values_json": json_dumpb_optional(values),
            "limit": limit,
            "offset": offset,
            "sort_by": _map_threads_sort_by(sort_by),
            "sort_order": _map_sort_order(sort_order),
        }

        if status:
            mapped_status = _map_thread_status(status)
            if mapped_status is None:
                raise HTTPException(
                    status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                    detail=f"Invalid thread status: {status}",
                )
            request_kwargs["status"] = mapped_status

        if select:
            request_kwargs["select"] = select

        client = await get_shared_client()
        response = await client.threads.Search(
            pb.SearchThreadsRequest(**request_kwargs)
        )

        threads = [proto_to_thread(thread) for thread in response.threads]
        cursor = offset + limit if len(threads) == limit else None

        async def generate_results():
            for thread in threads:
                yield _filter_thread_fields(thread, select)

        return generate_results(), cursor

    @staticmethod
    async def count(
        conn,  # Not used
        *,
        metadata: MetadataInput,
        values: MetadataInput,
        status: ThreadStatus | None,
        ctx: Any = None,
    ) -> int:  # type: ignore[override]
        metadata = metadata or {}
        values = values or {}

        auth_filters = await Threads.handle_event(
            ctx,
            "search",
            {
                "metadata": metadata,
                "values": values,
                "status": status,
            },
        )

        request_kwargs: dict[str, Any] = {
            "filters": auth_filters,
            "metadata_json": json_dumpb_optional(metadata),
            "values_json": json_dumpb_optional(values),
        }
        if status:
            mapped_status = _map_thread_status(status)
            if mapped_status is None:
                raise HTTPException(
                    status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                    detail=f"Invalid thread status: {status}",
                )
            request_kwargs["status"] = mapped_status

        client = await get_shared_client()
        response = await client.threads.Count(pb.CountThreadsRequest(**request_kwargs))

        return int(response.count)

    @staticmethod
    async def get(
        conn,  # Not used
        thread_id: UUID | str,
        ctx: Any = None,
        include_ttl: bool = False,
    ) -> AsyncIterator[Thread]:  # type: ignore[return-value]
        """Get a thread by ID.

        Args:
            conn: Not used (required for interface compatibility)
            thread_id: Thread ID
            ctx: Auth context
            include_ttl: Not yet supported in gRPC - parameter ignored.
        """
        auth_filters = await Threads.handle_event(
            ctx, "read", {"thread_id": str(thread_id)}
        )

        request = pb.GetThreadRequest(
            thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
            filters=auth_filters,
        )
        client = await get_shared_client()
        response = await client.threads.Get(request)

        thread = proto_to_thread(response)

        async def generate_result():
            yield thread

        return generate_result()

    @staticmethod
    async def put(
        conn,  # Not used
        thread_id: UUID | str,
        *,
        metadata: MetadataInput,
        if_exists: OnConflictBehavior,
        ttl: dict[str, Any] | None = None,
        ctx: Any = None,
    ) -> AsyncIterator[Thread]:  # type: ignore[return-value]
        metadata = metadata or {}

        auth_filters = await Threads.handle_event(
            ctx,
            "create",
            {
                "thread_id": str(thread_id),
                "metadata": metadata,
                "if_exists": if_exists,
            },
        )

        request = pb.CreateThreadRequest(
            thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
            filters=auth_filters,
            if_exists=map_if_exists(if_exists),
            metadata_json=json_dumpb_optional(metadata),
        )
        ttl_config = _map_thread_ttl(ttl)
        if ttl_config is not None:
            request.ttl.CopyFrom(ttl_config)

        client = await get_shared_client()
        response = await client.threads.Create(request)
        thread = proto_to_thread(response)

        async def generate_result():
            yield thread

        return generate_result()

    @staticmethod
    async def patch(
        conn,  # Not used
        thread_id: UUID | str,
        *,
        metadata: MetadataInput,
        ttl: dict[str, Any] | None = None,
        ctx: Any = None,
    ) -> AsyncIterator[Thread]:  # type: ignore[return-value]
        metadata = metadata or {}

        auth_filters = await Threads.handle_event(
            ctx,
            "update",
            {
                "thread_id": str(thread_id),
                "metadata": metadata,
            },
        )

        request = pb.PatchThreadRequest(
            thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
            filters=auth_filters,
            metadata_json=json_dumpb_optional(metadata),
        )

        ttl_config = _map_thread_ttl(ttl)
        if ttl_config is not None:
            request.ttl.CopyFrom(ttl_config)

        client = await get_shared_client()
        response = await client.threads.Patch(request)

        thread = proto_to_thread(response)

        async def generate_result():
            yield thread

        return generate_result()

    @staticmethod
    async def delete(
        conn,  # Not used
        thread_id: UUID | str,
        ctx: Any = None,
    ) -> AsyncIterator[UUID]:  # type: ignore[return-value]
        auth_filters = await Threads.handle_event(
            ctx,
            "delete",
            {
                "thread_id": str(thread_id),
            },
        )

        request = pb.DeleteThreadRequest(
            thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
            filters=auth_filters,
        )

        client = await get_shared_client()
        response = await client.threads.Delete(request)

        deleted_id = UUID(response.value)

        async def generate_result():
            yield deleted_id

        return generate_result()

    @staticmethod
    async def prune(
        thread_ids: Sequence[str] | Sequence[UUID],
        strategy: Literal["delete", "keep_latest"] = "delete",
        batch_size: int = 100,
        ctx: Any = None,
    ) -> int:
        """Prune threads via gRPC.

        Args:
            thread_ids: List of thread IDs to prune
            strategy: "delete" to remove entirely, "keep_latest" to prune checkpoints
            batch_size: Batch size for operations
            ctx: Auth context for permission checks

        Returns:
            Number of threads successfully pruned
        """

        if not thread_ids:
            return 0

        str_ids = [str(tid) for tid in thread_ids]
        client = await get_shared_client()

        # Validate delete authorization for all threads before pruning.
        # Auth filters are based on user/action, so we only need to get them once.
        auth_filters = await Threads.handle_event(
            ctx,
            "delete",
            {"thread_ids": str_ids},
        )

        # Only validate access if auth filters are present
        if auth_filters:

            async def validate_thread_access(thread_id: str) -> None:
                request = pb.GetThreadRequest(
                    thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
                    filters=auth_filters,
                )
                await client.threads.Get(request)

            await asyncio.gather(*[validate_thread_access(tid) for tid in str_ids])

        if strategy == "delete":
            strategy_proto = checkpointer_pb2.PruneRequest.PruneStrategy.DELETE_ALL
        else:
            strategy_proto = checkpointer_pb2.PruneRequest.PruneStrategy.KEEP_LATEST
        stub = client.checkpointer

        processed = 0
        for i in range(0, len(str_ids), batch_size):
            batch = str_ids[i : i + batch_size]
            try:
                request = checkpointer_pb2.PruneRequest(
                    thread_ids=batch,
                    strategy=strategy_proto,
                )
                await stub.Prune(request)
                processed += len(batch)
            except Exception:
                await logger.aexception("Failed to prune thread. Skipping batch.")
                pass

        return processed

    @staticmethod
    async def copy(
        conn,  # Not used
        thread_id: UUID | str,
        ctx: Any = None,
    ) -> AsyncIterator[Thread]:  # type: ignore[return-value]
        auth_filters = await Threads.handle_event(
            ctx,
            "read",
            {
                "thread_id": str(thread_id),
            },
        )
        # Validate that the user also has create permissions
        # Filters will be the same as the read filters, so we can toss these
        await Threads.handle_event(
            ctx,
            "create",
            {
                "thread_id": str(thread_id),
            },
        )

        request = pb.CopyThreadRequest(
            thread_id=pb.UUID(value=_normalize_uuid(thread_id)),
            filters=auth_filters,
        )

        client = await get_shared_client()
        response = await client.threads.Copy(request)

        thread = proto_to_thread(response)

        async def generate_result():
            yield thread

        return generate_result()

    @staticmethod
    async def _set_status(
        conn,  # Not used in gRPC implementation
        thread_id: UUID | str,
        checkpoint: dict[str, Any] | None,
        exception: BaseException | dict[str, Any] | None,
        expected_status: ThreadStatus | Sequence[ThreadStatus] | None = None,
    ) -> None:
        """Set thread status.

        This is an internal method (no auth) used in `Threads.State`.

        Args:
            conn: Not used (required for interface compatibility)
            thread_id: Thread ID
            checkpoint: Checkpoint payload containing values, next, tasks, etc.
            exception: Exception to store on thread (BaseException or serialized dict)
            expected_status: Expected current status(es) for optimistic locking
        """
        request_kwargs: dict[str, Any] = {
            "thread_id": pb.UUID(value=_normalize_uuid(thread_id)),
        }

        # Map checkpoint to proto
        checkpoint_proto = _thread_status_checkpoint_to_proto(checkpoint)
        if checkpoint_proto is not None:
            request_kwargs["checkpoint"] = checkpoint_proto

        # Map exception to JSON bytes
        if exception is not None:
            if isinstance(exception, BaseException):
                exception_dict = {
                    "type": type(exception).__name__,
                    "message": str(exception),
                }
            else:
                exception_dict = exception
            request_kwargs["exception_json"] = json_dumpb(exception_dict)

        # Map expected_status to enum values
        if expected_status:
            if isinstance(expected_status, str):
                expected_status = [expected_status]
            status_enums = []
            for status in expected_status:
                mapped = THREAD_STATUS_TO_PB.get(status)
                if mapped is not None:
                    status_enums.append(mapped)
            if status_enums:
                request_kwargs["expected_status"] = status_enums

        client = await get_shared_client()
        await client.threads.SetStatus(pb.SetThreadStatusRequest(**request_kwargs))
