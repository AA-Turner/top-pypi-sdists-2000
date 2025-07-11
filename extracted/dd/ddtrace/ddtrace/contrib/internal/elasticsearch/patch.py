from importlib import import_module
from typing import Dict
from urllib import parse

from wrapt import wrap_function_wrapper as _w

from ddtrace import config
from ddtrace._trace import _limits
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib.internal.elasticsearch.quantize import quantize
from ddtrace.contrib.internal.trace_utils import ext_service
from ddtrace.contrib.internal.trace_utils import extract_netloc_and_query_info_from_url
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.ext import elasticsearch as metadata
from ddtrace.ext import http
from ddtrace.ext import net
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.wrappers import unwrap as _u
from ddtrace.trace import Pin


try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as get_package_version
except ImportError:
    from importlib_metadata import PackageNotFoundError
    from importlib_metadata import version as get_package_version


log = get_logger(__name__)

config._add(
    "elasticsearch",
    {
        "_default_service": schematize_service_name("elasticsearch"),
    },
)

ES_MODULE_VERSIONS = {}
ES_PACKAGE_TO_MODULE_NAME = {
    "elasticsearch": "elasticsearch",
    "elasticsearch1": "elasticsearch1",
    "elasticsearch2": "elasticsearch2",
    "elasticsearch5": "elasticsearch5",
    "elasticsearch6": "elasticsearch6",
    "elasticsearch7": "elasticsearch7",
    # Starting with version 8, the default transport which is what we
    # actually patch is found in the separate elastic_transport package
    "elastic-transport": "elastic_transport",
    "opensearch-py": "opensearchpy",
}


def _es_modules():
    for module_name in ES_PACKAGE_TO_MODULE_NAME.values():
        try:
            module = import_module(module_name)
            ES_MODULE_VERSIONS[module_name] = getattr(module, "__versionstr__", "")
            yield module
        except ImportError:
            pass


def get_version_tuple(elasticsearch):
    return getattr(elasticsearch, "__version__", "")


def get_version():
    # type: () -> str
    return ""


def _supported_versions() -> Dict[str, str]:
    return {"elasticsearch": ">=1.10"}


def get_versions():
    # type: () -> Dict[str, str]
    if not ES_MODULE_VERSIONS:
        for es_module in ES_PACKAGE_TO_MODULE_NAME.keys():
            try:
                ES_MODULE_VERSIONS[es_module] = get_package_version(es_module)
            except PackageNotFoundError:
                pass
    return ES_MODULE_VERSIONS


def _get_transport_module(elasticsearch):
    try:
        # elasticsearch7/opensearch async
        return elasticsearch._async.transport
    except AttributeError:
        try:
            # elasticsearch<8/opensearch sync
            return elasticsearch.transport
        except AttributeError:
            # elastic_transport (elasticsearch8)
            return elasticsearch


# NB: We are patching the default elasticsearch transport module
def patch():
    for elasticsearch in _es_modules():
        _patch(_get_transport_module(elasticsearch))


def _patch(transport):
    if getattr(transport, "_datadog_patch", False):
        return
    if hasattr(transport, "Transport"):
        transport._datadog_patch = True
        _w(transport.Transport, "perform_request", _get_perform_request(transport))
        Pin().onto(transport.Transport)
    if hasattr(transport, "AsyncTransport"):
        transport._datadog_patch = True
        _w(transport.AsyncTransport, "perform_request", _get_perform_request_async(transport))
        Pin().onto(transport.AsyncTransport)


def unpatch():
    for elasticsearch in _es_modules():
        _unpatch(_get_transport_module(elasticsearch))


def _unpatch(transport):
    if not getattr(transport, "_datadog_patch", False):
        return
    for classname in ("Transport", "AsyncTransport"):
        try:
            cls = getattr(transport, classname)
        except AttributeError:
            continue
        transport._datadog_patch = False
        _u(cls, "perform_request")


def _get_perform_request_coro(transport):
    def _perform_request(func, instance, args, kwargs):
        pin = Pin.get_from(instance)
        if not pin or not pin.enabled():
            yield func(*args, **kwargs)
            return

        with pin.tracer.trace(
            "elasticsearch.query", service=ext_service(pin, config.elasticsearch), span_type=SpanTypes.ELASTICSEARCH
        ) as span:
            if pin.tags:
                span.set_tags(pin.tags)

            span.set_tag_str(COMPONENT, config.elasticsearch.integration_name)

            # set span.kind to the type of request being performed
            span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

            span.set_tag(_SPAN_MEASURED_KEY)

            method, target = args
            params = kwargs.get("params")
            body = kwargs.get("body")

            # elastic_transport gets target url with query params already appended
            parsed = parse.urlparse(target)
            url = parsed.path
            if params:
                encoded_params = parse.urlencode(params)
            else:
                encoded_params = parsed.query

            span.set_tag_str(metadata.METHOD, method)
            span.set_tag_str(metadata.URL, url)
            span.set_tag_str(metadata.PARAMS, encoded_params)
            try:
                # elasticsearch<8
                connections = instance.connection_pool.connections
            except AttributeError:
                # elastic_transport
                connections = instance.node_pool.all()
            for connection in connections:
                hostname, _ = extract_netloc_and_query_info_from_url(connection.host)
                if hostname:
                    span.set_tag_str(net.TARGET_HOST, hostname)
                    span.set_tag_str(net.SERVER_ADDRESS, hostname)
                    break

            if config.elasticsearch.trace_query_string:
                span.set_tag_str(http.QUERY_STRING, encoded_params)

            if method in ["GET", "POST"]:
                try:
                    # elasticsearch<8
                    ser_body = instance.serializer.dumps(body)
                except AttributeError:
                    # elastic_transport
                    ser_body = instance.serializers.dumps(body)
                # Elasticsearch request bodies can be very large resulting in traces being too large
                # to send.
                # When this occurs, drop the value.
                # Ideally the body should be truncated, however we cannot truncate as the obfuscation
                # logic for the body lives in the agent and truncating would make the body undecodable.
                if len(ser_body) <= _limits.MAX_SPAN_META_VALUE_LEN:
                    span.set_tag_str(metadata.BODY, ser_body)
                else:
                    span.set_tag_str(
                        metadata.BODY,
                        "<body size %s exceeds limit of %s>" % (len(ser_body), _limits.MAX_SPAN_META_VALUE_LEN),
                    )
            status = None

            span = quantize(span)

            try:
                result = yield func(*args, **kwargs)
            except transport.TransportError as e:
                span.set_tag(http.STATUS_CODE, getattr(e, "status_code", 500))
                span.error = 1
                raise

            try:
                # Optional metadata extraction with soft fail.
                if isinstance(result, tuple):
                    try:
                        # elastic_transport returns a named tuple
                        meta, data = result.meta, result.body
                        status = meta.status
                    except AttributeError:
                        # elasticsearch<2.4; it returns both the status and the body
                        status, data = result
                else:
                    # elasticsearch>=2.4,<8; internal change for ``Transport.perform_request``
                    # that just returns the body
                    data = result

                took = data.get("took")
                if took:
                    span.set_metric(metadata.TOOK, int(took))
            except Exception:
                log.debug("Unexpected exception", exc_info=True)

            if status:
                span.set_tag(http.STATUS_CODE, status)

            return

    return _perform_request


def _get_perform_request(transport):
    _perform_request_coro = _get_perform_request_coro(transport)

    def _perform_request(func, instance, args, kwargs):
        coro = _perform_request_coro(func, instance, args, kwargs)
        result = next(coro)
        try:
            coro.send(result)
        except StopIteration:
            pass
        return result

    return _perform_request


def _get_perform_request_async(transport):
    _perform_request_coro = _get_perform_request_coro(transport)

    async def _perform_request(func, instance, args, kwargs):
        coro = _perform_request_coro(func, instance, args, kwargs)
        result = await next(coro)
        try:
            coro.send(result)
        except StopIteration:
            pass
        return result

    return _perform_request
