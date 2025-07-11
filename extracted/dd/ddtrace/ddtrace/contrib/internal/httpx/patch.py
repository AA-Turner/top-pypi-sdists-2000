import os
from typing import Dict

import httpx
from wrapt import BoundFunctionWrapper
from wrapt import wrap_function_wrapper as _w

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib.internal.trace_utils import distributed_tracing_enabled
from ddtrace.contrib.internal.trace_utils import ext_service
from ddtrace.contrib.internal.trace_utils import set_http_meta
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.internal.compat import ensure_binary
from ddtrace.internal.compat import ensure_text
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.schema import schematize_url_operation
from ddtrace.internal.schema.span_attribute_schema import SpanDirection
from ddtrace.internal.utils import get_argument_value
from ddtrace.internal.utils.formats import asbool
from ddtrace.internal.utils.version import parse_version
from ddtrace.internal.utils.wrappers import unwrap as _u
from ddtrace.propagation.http import HTTPPropagator
from ddtrace.trace import Pin


HTTPX_VERSION = parse_version(httpx.__version__)


def get_version():
    # type: () -> str
    return getattr(httpx, "__version__", "")


config._add(
    "httpx",
    {
        "distributed_tracing": asbool(os.getenv("DD_HTTPX_DISTRIBUTED_TRACING", default=True)),
        "split_by_domain": asbool(os.getenv("DD_HTTPX_SPLIT_BY_DOMAIN", default=False)),
        "default_http_tag_query_string": config._http_client_tag_query_string,
    },
)


def _supported_versions() -> Dict[str, str]:
    return {"httpx": ">=0.17"}


def _url_to_str(url):
    # type: (httpx.URL) -> str
    """
    Helper to convert the httpx.URL parts from bytes to a str
    """
    # httpx==0.13.0 added URL.raw, removed in httpx==0.23.1. Otherwise, must construct manually
    if HTTPX_VERSION < (0, 13, 0):
        # Manually construct the same way httpx==0.13 does it:
        # https://github.com/encode/httpx/blob/2c2c6a71a9ff520d237f8283a586df2753f01f5e/httpx/_models.py#L161
        scheme = url.scheme.encode("ascii")
        host = url.host.encode("ascii")
        port = url.port
        raw_path = url.full_path.encode("ascii")
    elif HTTPX_VERSION < (0, 23, 1):
        scheme, host, port, raw_path = url.raw
    else:
        scheme = url.raw_scheme
        host = url.raw_host
        port = url.port
        raw_path = url.raw_path
    url = scheme + b"://" + host
    if port is not None:
        url += b":" + ensure_binary(str(port))
    url += raw_path
    return ensure_text(url)


def _get_service_name(pin, request):
    # type: (Pin, httpx.Request) -> typing.Text
    if config.httpx.split_by_domain:
        if hasattr(request.url, "netloc"):
            return ensure_text(request.url.netloc, errors="backslashreplace")
        else:
            service = ensure_binary(request.url.host)
            if request.url.port:
                service += b":" + ensure_binary(str(request.url.port))
            return ensure_text(service, errors="backslashreplace")
    return ext_service(pin, config.httpx)


def _init_span(span, request):
    # type: (Span, httpx.Request) -> None
    span.set_tag(_SPAN_MEASURED_KEY)

    if distributed_tracing_enabled(config.httpx):
        HTTPPropagator.inject(span.context, request.headers)


def _set_span_meta(span, request, response):
    # type: (Span, httpx.Request, httpx.Response) -> None
    set_http_meta(
        span,
        config.httpx,
        method=request.method,
        url=_url_to_str(request.url),
        target_host=request.url.host,
        status_code=response.status_code if response else None,
        query=request.url.query,
        request_headers=request.headers,
        response_headers=response.headers if response else None,
    )


async def _wrapped_async_send(
    wrapped: BoundFunctionWrapper,
    instance,  # type: httpx.AsyncClient
    args,  # type: typing.Tuple[httpx.Request]
    kwargs,  # type: typing.Dict[typing.Str, typing.Any]
):
    # type: (...) -> typing.Coroutine[None, None, httpx.Response]
    req = get_argument_value(args, kwargs, 0, "request")

    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return await wrapped(*args, **kwargs)

    operation_name = schematize_url_operation("http.request", protocol="http", direction=SpanDirection.OUTBOUND)
    with pin.tracer.trace(operation_name, service=_get_service_name(pin, req), span_type=SpanTypes.HTTP) as span:
        span.set_tag_str(COMPONENT, config.httpx.integration_name)

        # set span.kind to the operation type being performed
        span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

        _init_span(span, req)
        resp = None
        try:
            resp = await wrapped(*args, **kwargs)
            return resp
        finally:
            _set_span_meta(span, req, resp)


def _wrapped_sync_send(
    wrapped: BoundFunctionWrapper,
    instance,  # type: httpx.AsyncClient
    args,  # type: typing.Tuple[httpx.Request]
    kwargs,  # type: typing.Dict[typing.Str, typing.Any]
):
    # type: (...) -> httpx.Response
    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return wrapped(*args, **kwargs)

    req = get_argument_value(args, kwargs, 0, "request")

    operation_name = schematize_url_operation("http.request", protocol="http", direction=SpanDirection.OUTBOUND)
    with pin.tracer.trace(operation_name, service=_get_service_name(pin, req), span_type=SpanTypes.HTTP) as span:
        span.set_tag_str(COMPONENT, config.httpx.integration_name)

        # set span.kind to the operation type being performed
        span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

        _init_span(span, req)
        resp = None
        try:
            resp = wrapped(*args, **kwargs)
            return resp
        finally:
            _set_span_meta(span, req, resp)


def patch():
    # type: () -> None
    if getattr(httpx, "_datadog_patch", False):
        return

    httpx._datadog_patch = True

    pin = Pin()

    if HTTPX_VERSION >= (0, 11):
        # httpx==0.11 created synchronous Client class separate from AsyncClient
        _w(httpx.Client, "send", _wrapped_sync_send)
        _w(httpx.AsyncClient, "send", _wrapped_async_send)
        pin.onto(httpx.AsyncClient)
    else:
        # httpx==0.9 Client class was asynchronous, httpx==0.10 made Client synonymous with AsyncClient
        _w(httpx.Client, "send", _wrapped_async_send)

    pin.onto(httpx.Client)


def unpatch():
    # type: () -> None
    if not getattr(httpx, "_datadog_patch", False):
        return

    httpx._datadog_patch = False

    if HTTPX_VERSION >= (0, 11):
        # See above patching code for when this patching occurred
        _u(httpx.AsyncClient, "send")

    _u(httpx.Client, "send")
