"""gRPC-based runs operations."""

from __future__ import annotations

from datetime import UTC
from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Literal
from uuid import UUID

import structlog
from google.protobuf.empty_pb2 import Empty  # type: ignore[import]
from grpc import StatusCode
from langgraph_sdk import Auth
from starlette.exceptions import HTTPException

from langgraph_api.grpc.client import get_shared_client
from langgraph_api.grpc.config_conversion import config_from_proto
from langgraph_api.grpc.generated import (
    core_api_pb2 as pb,
)
from langgraph_api.grpc.generated import (
    enum_cancel_run_action_pb2 as enum_cancel_run_action,
)
from langgraph_api.grpc.generated import (
    enum_multitask_strategy_pb2 as enum_multitask_strategy,
)
from langgraph_api.grpc.generated import (
    enum_run_status_pb2 as enum_run_status,
)
from langgraph_api.grpc.generated import (
    enum_stream_mode_pb2 as enum_stream_mode,
)
from langgraph_api.grpc.ops import (
    Authenticated,
    grpc_error_guard,
)
from langgraph_api.serde import json_loads_optional

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Sequence

    from langgraph_api.schema import (
        IfNotExists,
        MultitaskStrategy,
        QueueStats,
        Run,
        RunSelectField,
        RunStatus,
    )


RUN_STATUS_TO_PB = {
    "pending": enum_run_status.pending,
    "running": enum_run_status.running,
    "error": enum_run_status.error,
    "success": enum_run_status.success,
    "timeout": enum_run_status.timeout,
    "interrupted": enum_run_status.interrupted,
    # This is a pseudo-status that is not exposed to the user
    # but is used internally to indicate a rollback.
    # We should never return it from the API, as it should never be persisted.
    "rollback": enum_run_status.rollback,
}

RUN_STATUS_FROM_PB = {v: k for k, v in RUN_STATUS_TO_PB.items()}

CANCEL_STATUS_TO_PB = {
    "pending": pb.CancelRunStatus.CANCEL_RUN_STATUS_PENDING,
    "running": pb.CancelRunStatus.CANCEL_RUN_STATUS_RUNNING,
    "all": pb.CancelRunStatus.CANCEL_RUN_STATUS_ALL,
}


def _map_run_status(status: RunStatus | None) -> enum_run_status.RunStatus | None:
    """Map string status to protobuf enum."""
    return None if status is None else RUN_STATUS_TO_PB.get(status)


MULTITASK_STRATEGY_TO_PB = {
    "reject": enum_multitask_strategy.reject,
    "interrupt": enum_multitask_strategy.interrupt,
    "rollback": enum_multitask_strategy.rollback,
    "enqueue": enum_multitask_strategy.enqueue,
}

MULTITASK_STRATEGY_FROM_PB = {v: k for k, v in MULTITASK_STRATEGY_TO_PB.items()}

STREAM_MODE_TO_PB = {
    "unknown": enum_stream_mode.unknown,
    "values": enum_stream_mode.values,
    "updates": enum_stream_mode.updates,
    "checkpoints": enum_stream_mode.checkpoints,
    "tasks": enum_stream_mode.tasks,
    "debug": enum_stream_mode.debug,
    "messages": enum_stream_mode.messages,
    "custom": enum_stream_mode.custom,
    "events": enum_stream_mode.events,
    "messages-tuple": enum_stream_mode.messages_tuple,
}

STREAM_MODE_FROM_PB = {
    **{v: k for k, v in STREAM_MODE_TO_PB.items()},
    # This isn't actually a valid stream mode (it's just a placeholder
    # in the protobuf definition), so if we receive it from the gRPC
    # server for some reason, we should suppress it to avoid exposing it
    # to the user.
    enum_stream_mode.unknown: None,
}


logger = structlog.stdlib.get_logger(__name__)


class GrpcRetryableException(Exception):
    """Exception indicating a gRPC error that should trigger a run retry."""

    pass


GRPC_RETRIABLE_STATUS_CODES = (
    StatusCode.UNAVAILABLE,
    StatusCode.DEADLINE_EXCEEDED,
)


def _map_multitask_strategy(
    strategy: MultitaskStrategy | None,
) -> enum_multitask_strategy.MultitaskStrategy | None:
    """Map string multitask strategy to protobuf enum."""
    return None if strategy is None else MULTITASK_STRATEGY_TO_PB.get(strategy)


def _map_if_not_exists(
    if_not_exists: IfNotExists | None,
) -> pb.CreateRunBehavior | None:
    """Map if_not_exists string to protobuf enum."""
    if if_not_exists is None:
        return None
    return (
        pb.CreateRunBehavior.CREATE_THREAD_IF_THREAD_NOT_EXISTS
        if if_not_exists == "create"
        else pb.CreateRunBehavior.REJECT_RUN_IF_THREAD_NOT_EXISTS
    )


def proto_to_run(proto_run: pb.Run) -> Run:
    """Convert protobuf Run to dictionary format."""
    return {
        "run_id": UUID(proto_run.run_id.value)
        if proto_run.HasField("run_id")
        else None,
        "thread_id": UUID(proto_run.thread_id.value)
        if proto_run.HasField("thread_id")
        else None,
        "assistant_id": UUID(proto_run.assistant_id.value)
        if proto_run.HasField("assistant_id")
        else None,
        "created_at": proto_run.created_at.ToDatetime(tzinfo=UTC)
        if proto_run.HasField("created_at")
        else None,
        "updated_at": proto_run.updated_at.ToDatetime(tzinfo=UTC)
        if proto_run.HasField("updated_at")
        else None,
        "status": RUN_STATUS_FROM_PB.get(proto_run.status, "pending"),
        "metadata": json_loads_optional(proto_run.metadata.value)
        if proto_run.HasField("metadata")
        else {},
        "kwargs": _proto_kwargs_to_dict(proto_run.kwargs)
        if proto_run.HasField("kwargs")
        else {},
        "multitask_strategy": MULTITASK_STRATEGY_FROM_PB.get(
            proto_run.multitask_strategy
        ),
    }


def _proto_kwargs_to_dict(kwargs: pb.RunKwargs) -> dict:
    """Convert protobuf RunKwargs to dictionary format."""
    result: dict = {
        "input": json_loads_optional(kwargs.input_json)
        if kwargs.HasField("input_json")
        else None,
        "config": dict(config_from_proto(kwargs.config))
        if kwargs.HasField("config")
        else None,
        "context": json_loads_optional(kwargs.context_json)
        if kwargs.HasField("context_json")
        else None,
        "command": json_loads_optional(kwargs.command_json)
        if kwargs.HasField("command_json")
        else None,
        "stream_mode": [STREAM_MODE_FROM_PB.get(kwargs.stream_mode)]
        if kwargs.stream_mode
        else None,
        "interrupt_before": list(kwargs.interrupt_before.node_names.names)
        if kwargs.HasField("interrupt_before")
        else None,
        "interrupt_after": list(kwargs.interrupt_after.node_names.names)
        if kwargs.HasField("interrupt_after")
        else None,
        "webhook": kwargs.webhook if kwargs.HasField("webhook") else None,
        "feedback_keys": list(kwargs.feedback_keys) if kwargs.feedback_keys else None,
        "temporary": kwargs.temporary if kwargs.HasField("temporary") else False,
        "subgraphs": kwargs.subgraphs if kwargs.HasField("subgraphs") else False,
        "resumable": kwargs.resumable if kwargs.HasField("resumable") else False,
        "checkpoint_during": kwargs.checkpoint_during
        if kwargs.HasField("checkpoint_during")
        else True,
        "durability": kwargs.durability if kwargs.HasField("durability") else None,
    }
    return result


def _filter_run_fields(run: Run, select: list[RunSelectField] | None) -> dict[str, Any]:
    """Filter run fields based on select list.

    Returns the original run if no fields are provided."""
    if not select:
        return run
    return {field: run[field] for field in select if field in run}


@grpc_error_guard
class Runs(Authenticated):
    """gRPC-based runs operations."""

    # Auth for runs is applied at the thread level.
    resource = "threads"

    @staticmethod
    async def search(
        conn,  # Not used in gRPC implementation
        thread_id: UUID,
        *,
        limit: int = 10,
        offset: int = 0,
        status: RunStatus | None = None,
        select: list[RunSelectField] | None = None,
        ctx: Any = None,
    ) -> AsyncIterator[Run]:  # type: ignore[return-value]
        """List all runs by thread."""
        auth_filters = await Runs.handle_event(
            ctx,
            "search",
            Auth.types.ThreadsSearch(thread_id=thread_id, metadata={}),
        )

        request_kwargs: dict[str, Any] = {
            "filters": auth_filters,
            "thread_id": pb.UUID(value=str(thread_id)),
            "limit": limit,
            "offset": offset,
        }

        mapped_status = _map_run_status(status)
        if mapped_status is not None:
            request_kwargs["status"] = mapped_status

        if select:
            request_kwargs["select"] = select

        client = await get_shared_client()
        response = await client.runs.Search(pb.SearchRunsRequest(**request_kwargs))

        runs = [proto_to_run(run) for run in response.runs]

        async def generate_results():
            for run in runs:
                yield _filter_run_fields(run, select)

        return generate_results()

    @staticmethod
    async def get(
        conn,  # Not used in gRPC implementation
        run_id: UUID,
        *,
        thread_id: UUID,
        ctx: Any = None,
    ) -> AsyncIterator[Run]:  # type: ignore[return-value]
        """Get a run by ID."""
        auth_filters = await Runs.handle_event(
            ctx,
            "read",
            Auth.types.ThreadsRead(run_id=run_id, thread_id=thread_id),
        )

        request = pb.GetRunRequest(
            run_id=pb.UUID(value=str(run_id)),
            thread_id=pb.UUID(value=str(thread_id)),
            filters=auth_filters,
        )

        client = await get_shared_client()
        response = await client.runs.Get(request)

        run = proto_to_run(response)

        async def generate_result():
            yield run

        return generate_result()

    @staticmethod
    async def delete(
        conn,  # Not used in gRPC implementation
        run_id: UUID,
        *,
        thread_id: UUID,
        ctx: Any = None,
    ) -> AsyncIterator[UUID]:  # type: ignore[return-value]
        """Delete a run by ID."""
        auth_filters = await Runs.handle_event(
            ctx,
            "delete",
            Auth.types.ThreadsDelete(run_id=run_id, thread_id=thread_id),
        )

        request = pb.DeleteRunRequest(
            run_id=pb.UUID(value=str(run_id)),
            thread_id=pb.UUID(value=str(thread_id)),
            filters=auth_filters,
        )

        client = await get_shared_client()
        response = await client.runs.Delete(request)

        deleted_id = UUID(response.value)

        async def generate_result():
            yield deleted_id

        return generate_result()

    @staticmethod
    async def cancel(
        conn,  # Not used in gRPC implementation
        run_ids: Sequence[UUID] | None = None,
        *,
        action: Literal["interrupt", "rollback"] = "interrupt",
        thread_id: UUID | None = None,
        status: Literal["pending", "running", "all"] | None = None,
        ctx: Any = None,
    ) -> None:
        """Cancel runs.

        Must provide either:
        1) thread_id + run_ids, or
        2) a status (pending, running, all).
        """
        if status is not None:
            if thread_id is not None or run_ids is not None:
                raise HTTPException(
                    status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                    detail="Cannot specify 'thread_id' or 'run_ids' when using 'status'",
                )
        elif thread_id is None or run_ids is None:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail="Please provide a thread_id and run_ids, or a status to cancel",
            )

        auth_filters = await Runs.handle_event(
            ctx,
            "update",
            Auth.types.ThreadsUpdate(
                thread_id=thread_id,  # type: ignore
                action=action,
                metadata={"run_ids": run_ids, "status": status},
            ),
        )

        action_enum = (
            enum_cancel_run_action.rollback
            if action == "rollback"
            else enum_cancel_run_action.interrupt
        )

        request_kwargs: dict[str, Any] = {
            "filters": auth_filters,
            "action": action_enum,
        }

        if status is not None:
            request_kwargs["status"] = pb.CancelStatusTarget(
                status=CANCEL_STATUS_TO_PB[status]
            )
        else:
            request_kwargs["run_ids"] = pb.CancelRunIdsTarget(
                thread_id=pb.UUID(value=str(thread_id)),
                run_ids=[pb.UUID(value=str(rid)) for rid in run_ids],  # type: ignore
            )

        client = await get_shared_client()
        await client.runs.Cancel(pb.CancelRunRequest(**request_kwargs))

    @staticmethod
    async def stats(conn) -> QueueStats:  # type: ignore[return-value]
        """Get queue statistics (not exposed via API, no auth)."""
        client = await get_shared_client()
        response = await client.runs.Stats(Empty())

        return {
            "n_pending": response.n_pending,
            "n_running": response.n_running,
            "pending_runs_wait_time_max_secs": (
                response.pending_runs_wait_time_max_secs
                if response.HasField("pending_runs_wait_time_max_secs")
                else None
            ),
            "pending_runs_wait_time_med_secs": (
                response.pending_runs_wait_time_med_secs
                if response.HasField("pending_runs_wait_time_med_secs")
                else None
            ),
            "pending_unblocked_runs_wait_time_max_secs": (
                response.pending_unblocked_runs_wait_time_max_secs
                if response.HasField("pending_unblocked_runs_wait_time_max_secs")
                else None
            ),
        }

    @staticmethod
    async def sweep() -> list[UUID]:
        """Sweep runs that have been in running state for too long (not exposed via API, no auth)."""
        client = await get_shared_client()
        response = await client.runs.Sweep(Empty())

        return [UUID(uuid_pb.value) for uuid_pb in response.run_ids]

    class Stream(Authenticated):
        """Stream operations for runs."""

        resource = "threads"

        @staticmethod
        async def subscribe(
            run_id: UUID,
            thread_id: UUID | None = None,
        ):
            """Subscribe to the run stream, returning a stream handler.

            The stream handler must be passed to `join` to receive messages.
            """
            # TODO: Implement gRPC streaming subscription
            raise NotImplementedError("Stream.subscribe not yet implemented for gRPC")

        @staticmethod
        async def join(
            run_id: UUID,
            *,
            stream_channel,
            thread_id: UUID,
            ignore_404: bool = False,
            cancel_on_disconnect: bool = False,
            stream_mode=None,
            last_event_id: str | None = None,
            ctx: Any = None,
        ):
            """Stream the run output."""
            # TODO: Implement gRPC streaming join
            raise NotImplementedError("Stream.join not yet implemented for gRPC")

        @staticmethod
        async def check_run_stream_auth(
            run_id: UUID,
            thread_id: UUID,
            ctx: Any = None,
        ) -> None:
            """Check auth for streaming a run."""
            # TODO: Implement auth check for gRPC streaming
            raise NotImplementedError(
                "Stream.check_run_stream_auth not yet implemented for gRPC"
            )

        @staticmethod
        async def publish(
            run_id: UUID | str,
            event: str,
            message: bytes,
            *,
            thread_id: UUID | str | None = None,
            resumable: bool = False,
        ) -> None:
            """Publish a message to the run stream."""
            # TODO: Implement gRPC stream publishing
            raise NotImplementedError("Stream.publish not yet implemented for gRPC")
