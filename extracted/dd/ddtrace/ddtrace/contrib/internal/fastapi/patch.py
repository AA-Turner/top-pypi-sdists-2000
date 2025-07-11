import os
from typing import Dict

import fastapi
import fastapi.routing
from wrapt import ObjectProxy
from wrapt import wrap_function_wrapper as _w

from ddtrace import config
from ddtrace.contrib.internal.asgi.middleware import TraceMiddleware
from ddtrace.contrib.internal.starlette.patch import _trace_background_tasks
from ddtrace.contrib.internal.starlette.patch import traced_handler
from ddtrace.contrib.internal.starlette.patch import traced_route_init
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.wrappers import unwrap as _u
from ddtrace.settings.asm import config as asm_config
from ddtrace.trace import Pin


log = get_logger(__name__)

config._add(
    "fastapi",
    dict(
        _default_service=schematize_service_name("fastapi"),
        request_span_name="fastapi.request",
        distributed_tracing=True,
        trace_query_string=None,  # Default to global config
        _trace_asgi_websocket=os.getenv("DD_ASGI_TRACE_WEBSOCKET", default=False),
    ),
)


def get_version():
    # type: () -> str
    return getattr(fastapi, "__version__", "")


def _supported_versions() -> Dict[str, str]:
    return {"fastapi": ">=0.64.0"}


def wrap_middleware_stack(wrapped, instance, args, kwargs):
    return TraceMiddleware(app=wrapped(*args, **kwargs), integration_config=config.fastapi)


async def traced_serialize_response(wrapped, instance, args, kwargs):
    """Wrapper for fastapi.routing.serialize_response function.

    This function is called on all non-Response objects to
    convert them to a serializable form.

    This is the wrapper which calls ``jsonable_encoder``.

    This function does not do the actual encoding from
    obj -> json string  (e.g. json.dumps()). That is handled
    by the Response.render function.

    DEV: We do not wrap ``jsonable_encoder`` because it calls
    itself recursively, so there is a chance the overhead
    added by creating spans will be higher than desired for
    the result.
    """
    pin = Pin.get_from(fastapi)
    if not pin or not pin.enabled():
        return await wrapped(*args, **kwargs)

    with pin.tracer.trace("fastapi.serialize_response"):
        return await wrapped(*args, **kwargs)


def patch():
    if getattr(fastapi, "_datadog_patch", False):
        return

    fastapi._datadog_patch = True
    Pin().onto(fastapi)
    _w("fastapi.applications", "FastAPI.build_middleware_stack", wrap_middleware_stack)
    _w("fastapi.routing", "serialize_response", traced_serialize_response)

    if not isinstance(fastapi.BackgroundTasks.add_task, ObjectProxy):
        _w("fastapi", "BackgroundTasks.add_task", _trace_background_tasks(fastapi))
    # We need to check that Starlette instrumentation hasn't already patched these
    if not isinstance(fastapi.routing.APIRoute.__init__, ObjectProxy):
        _w("fastapi.routing", "APIRoute.__init__", traced_route_init)

    if not isinstance(fastapi.routing.APIRoute.handle, ObjectProxy):
        _w("fastapi.routing", "APIRoute.handle", traced_handler)

    if not isinstance(fastapi.routing.Mount.handle, ObjectProxy):
        _w("starlette.routing", "Mount.handle", traced_handler)

    if asm_config._iast_enabled:
        from ddtrace.appsec._iast._handlers import _on_iast_fastapi_patch

        _on_iast_fastapi_patch()


def unpatch():
    if not getattr(fastapi, "_datadog_patch", False):
        return

    fastapi._datadog_patch = False

    _u(fastapi.applications.FastAPI, "build_middleware_stack")
    _u(fastapi.routing, "serialize_response")

    # We need to check that Starlette instrumentation hasn't already unpatched these
    if isinstance(fastapi.routing.APIRoute.handle, ObjectProxy):
        _u(fastapi.routing.APIRoute, "handle")

    if isinstance(fastapi.routing.Mount.handle, ObjectProxy):
        _u(fastapi.routing.Mount, "handle")

    if isinstance(fastapi.BackgroundTasks.add_task, ObjectProxy):
        _u(fastapi.BackgroundTasks, "add_task")
