import functools
import sys
from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from urllib import parse

import wrapt

from ddtrace import config
from ddtrace._trace._inferred_proxy import create_inferred_proxy_span_if_headers_exist
from ddtrace._trace._span_pointer import _SpanPointerDescription
from ddtrace._trace.utils import extract_DD_context_from_messages
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import ERROR_MSG
from ddtrace.constants import ERROR_STACK
from ddtrace.constants import ERROR_TYPE
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.botocore.constants import BOTOCORE_STEPFUNCTIONS_INPUT_KEY
from ddtrace.contrib.internal.trace_utils import _set_url_tag
from ddtrace.ext import SpanKind
from ddtrace.ext import azure_servicebus as azure_servicebusx
from ddtrace.ext import db
from ddtrace.ext import http
from ddtrace.internal import core
from ddtrace.internal.compat import maybe_stringify
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.constants import FLASK_ENDPOINT
from ddtrace.internal.constants import FLASK_URL_RULE
from ddtrace.internal.constants import FLASK_VIEW_ARGS
from ddtrace.internal.constants import MESSAGING_DESTINATION_NAME
from ddtrace.internal.constants import MESSAGING_MESSAGE_ID
from ddtrace.internal.constants import MESSAGING_OPERATION
from ddtrace.internal.constants import MESSAGING_SYSTEM
from ddtrace.internal.constants import NETWORK_DESTINATION_NAME
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema.span_attribute_schema import SpanDirection
from ddtrace.propagation.http import HTTPPropagator


if TYPE_CHECKING:
    from ddtrace._trace.span import Span


log = get_logger(__name__)


class _TracedIterable(wrapt.ObjectProxy):
    def __init__(self, wrapped, span, parent_span, wrapped_is_iterator=False):
        self._self_wrapped_is_iterator = wrapped_is_iterator
        if self._self_wrapped_is_iterator:
            super(_TracedIterable, self).__init__(wrapped)
            self._wrapped_iterator = iter(wrapped)
        else:
            super(_TracedIterable, self).__init__(iter(wrapped))
        self._self_span = span
        self._self_parent_span = parent_span
        self._self_span_finished = False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self._self_wrapped_is_iterator:
                return next(self._wrapped_iterator)
            else:
                return next(self.__wrapped__)
        except StopIteration:
            self._finish_spans()
            raise
        except Exception:
            self._self_span.set_exc_info(*sys.exc_info())
            self._finish_spans()
            raise

    # PY2 Support
    next = __next__

    def close(self):
        if getattr(self.__wrapped__, "close", None):
            self.__wrapped__.close()
        self._finish_spans()

    def _finish_spans(self):
        if not self._self_span_finished:
            self._self_span.finish()
            self._self_parent_span.finish()
            self._self_span_finished = True

    def __getattribute__(self, name):
        if name == "__len__":
            # __len__ is defined by the parent class, wrapt.ObjectProxy.
            # However this attribute should not be defined for iterables.
            # By definition, iterables should not support len(...).
            raise AttributeError("__len__ is not supported")
        return super(_TracedIterable, self).__getattribute__(name)


def _get_parameters_for_new_span_directly_from_context(ctx: core.ExecutionContext) -> Dict[str, str]:
    span_kwargs = {}
    for parameter_name in {"span_type", "resource", "service", "child_of", "activate"}:
        parameter_value = ctx.get_local_item(parameter_name)
        if parameter_value:
            span_kwargs[parameter_name] = parameter_value
    return span_kwargs


def _start_span(ctx: core.ExecutionContext, call_trace: bool = True, **kwargs) -> "Span":
    activate_distributed_headers = ctx.get_local_item("activate_distributed_headers")
    span_kwargs = _get_parameters_for_new_span_directly_from_context(ctx)
    call_trace = ctx.get_item("call_trace", call_trace)
    tracer = ctx.get_item("tracer") or (ctx.get_item("middleware") or ctx["pin"]).tracer
    integration_config = ctx.get_item("integration_config")
    if integration_config and activate_distributed_headers:
        trace_utils.activate_distributed_headers(
            tracer,
            int_config=integration_config,
            request_headers=ctx["distributed_headers"],
            override=ctx.get_item("distributed_headers_config_override"),
        )
    distributed_context = ctx.get_item("distributed_context")
    if distributed_context and not call_trace:
        span_kwargs["child_of"] = distributed_context

    if config._inferred_proxy_services_enabled:
        # dispatch event for checking headers and possibly making an inferred proxy span
        core.dispatch("inferred_proxy.start", (ctx, tracer, span_kwargs, call_trace, integration_config))
        # re-get span_kwargs in case an inferred span was created and we have a new span_kwargs.child_of field
        span_kwargs = ctx.get_item("span_kwargs", span_kwargs)

    span_kwargs.update(kwargs)
    span = (tracer.trace if call_trace else tracer.start_span)(ctx["span_name"], **span_kwargs)

    for tk, tv in ctx.get_item("tags", dict()).items():
        span.set_tag_str(tk, tv)

    ctx.span = span

    if config._inferred_proxy_services_enabled:
        # dispatch event for inferred proxy finish
        core.dispatch("inferred_proxy.finish", (ctx,))

    return span


def _set_web_frameworks_tags(ctx, span, int_config):
    span.set_tag_str(COMPONENT, int_config.integration_name)
    span.set_tag_str(SPAN_KIND, SpanKind.SERVER)
    span.set_tag(_SPAN_MEASURED_KEY)


def _on_web_framework_start_request(ctx, int_config):
    request_span = ctx.get_item("req_span")
    _set_web_frameworks_tags(ctx, request_span, int_config)


def _on_web_framework_finish_request(
    span, int_config, method, url, status_code, query, req_headers, res_headers, route, finish, **kwargs
):
    trace_utils.set_http_meta(
        span=span,
        integration_config=int_config,
        method=method,
        url=url,
        status_code=status_code,
        query=query,
        request_headers=req_headers,
        response_headers=res_headers,
        route=route,
        **kwargs,
    )
    _set_inferred_proxy_tags(span, status_code)

    if finish:
        span.finish()


def _set_inferred_proxy_tags(span, status_code):
    if span._parent and span._parent.name == "aws.apigateway":
        inferred_span = span._parent
        status_code = status_code if status_code else span.get_tag("http.status_code")
        if status_code:
            inferred_span.set_tag("http.status_code", status_code)
        if span.error == 1:
            inferred_span.error = span.error
            if ERROR_MSG in span._meta.keys():
                inferred_span.set_tag(ERROR_MSG, span.get_tag(ERROR_MSG))
            if ERROR_TYPE in span._meta.keys():
                inferred_span.set_tag(ERROR_TYPE, span.get_tag(ERROR_TYPE))
            if ERROR_STACK in span._meta.keys():
                inferred_span.set_tag(ERROR_STACK, span.get_tag(ERROR_STACK))


def _on_inferred_proxy_start(ctx, tracer, span_kwargs, call_trace, integration_config):
    # Skip creating another inferred span if one has already been created for this request
    if ctx.get_item("inferred_proxy_span"):
        return

    # some integrations like Flask / WSGI store headers from environ in 'distributed_headers'
    # and normalized headers in 'headers'
    headers = ctx.get_item("headers", ctx.get_item("distributed_headers", None))

    # Inferred Proxy Spans
    if integration_config and headers is not None:
        create_inferred_proxy_span_if_headers_exist(
            ctx,
            headers=headers,
            child_of=tracer.current_trace_context(),
            tracer=tracer,
        )
        inferred_proxy_span = ctx.get_item("inferred_proxy_span")

        # use the inferred proxy span as the new parent span
        if inferred_proxy_span and not call_trace:
            span_kwargs["child_of"] = inferred_proxy_span
            ctx.set_item("span_kwargs", span_kwargs)


def _on_inferred_proxy_finish(ctx):
    if not config._inferred_proxy_services_enabled:
        return

    inferred_proxy_span = ctx.get_item("inferred_proxy_span")
    inferred_proxy_finish_callback = ctx.get_item("inferred_proxy_finish_callback")

    # add callback to finish inferred proxy span when this span finishes
    if (
        inferred_proxy_span
        and inferred_proxy_finish_callback
        and ctx.span
        and ctx.span.parent_id == inferred_proxy_span.span_id
    ):
        ctx.span._on_finish_callbacks.append(inferred_proxy_finish_callback)


def _on_traced_request_context_started_flask(ctx):
    current_span = ctx["pin"].tracer.current_span()
    if not ctx["pin"].enabled or not current_span:
        return

    ctx.span = current_span
    flask_config = ctx["flask_config"]
    _set_flask_request_tags(ctx["flask_request"], current_span, flask_config)
    request_span = _start_span(ctx)
    request_span._ignore_exception(ctx.get_item("ignored_exception_type"))


def _maybe_start_http_response_span(ctx: core.ExecutionContext) -> None:
    request_span = ctx["request_span"]
    middleware = ctx["middleware"]
    status_code, status_msg = ctx["status"].split(" ", 1)
    trace_utils.set_http_meta(
        request_span, middleware._config, status_code=status_code, response_headers=ctx["environ"]
    )
    if ctx.get_item("start_span", False):
        request_span.set_tag_str(http.STATUS_MSG, status_msg)
        _start_span(
            ctx,
            call_trace=False,
            child_of=ctx["parent_call"],
            activate=True,
        )


def _on_request_prepare(ctx, start_response):
    middleware = ctx.get_item("middleware")
    req_span = ctx.get_item("req_span")
    req_span.set_tag_str(COMPONENT, middleware._config.integration_name)
    # set span.kind to the type of operation being performed
    req_span.set_tag_str(SPAN_KIND, SpanKind.SERVER)
    if hasattr(middleware, "_request_call_modifier"):
        modifier = middleware._request_call_modifier
        args = [ctx]
    else:
        modifier = middleware._request_span_modifier
        args = [req_span, ctx.get_item("environ")]
    modifier(*args)
    app_span = middleware.tracer.trace(
        middleware._application_call_name
        if hasattr(middleware, "_application_call_name")
        else middleware._application_span_name
    )

    app_span.set_tag_str(COMPONENT, middleware._config.integration_name)
    ctx.set_item("app_span", app_span)

    if hasattr(middleware, "_wrapped_start_response"):
        wrapped = middleware._wrapped_start_response
        args = [start_response, ctx]
    else:
        wrapped = middleware._traced_start_response
        args = [start_response, req_span, app_span]
    intercept_start_response = functools.partial(wrapped, *args)
    ctx.set_item("intercept_start_response", intercept_start_response)


def _on_app_success(ctx, closing_iterable):
    app_span = ctx.get_item("app_span")
    middleware = ctx.get_item("middleware")
    modifier = (
        middleware._application_call_modifier
        if hasattr(middleware, "_application_call_modifier")
        else middleware._application_span_modifier
    )
    modifier(app_span, ctx.get_item("environ"), closing_iterable)
    app_span.finish()


def _on_app_exception(ctx):
    req_span = ctx.get_item("req_span")
    app_span = ctx.get_item("app_span")
    req_span.set_exc_info(*sys.exc_info())
    app_span.set_exc_info(*sys.exc_info())
    app_span.finish()
    req_span.finish()


def _on_request_complete(ctx, closing_iterable, app_is_iterator):
    middleware = ctx.get_item("middleware")
    req_span = ctx.get_item("req_span")
    # start flask.response span. This span will be finished after iter(result) is closed.
    # start_span(child_of=...) is used to ensure correct parenting.
    resp_span = middleware.tracer.start_span(
        (
            middleware._response_call_name
            if hasattr(middleware, "_response_call_name")
            else middleware._response_span_name
        ),
        child_of=req_span,
        activate=True,
    )

    resp_span.set_tag_str(COMPONENT, middleware._config.integration_name)

    modifier = (
        middleware._response_call_modifier
        if hasattr(middleware, "_response_call_modifier")
        else middleware._response_span_modifier
    )
    modifier(resp_span, closing_iterable)

    return _TracedIterable(closing_iterable, resp_span, req_span, wrapped_is_iterator=app_is_iterator)


def _on_response_prepared(resp_span, response):
    if hasattr(response, "__class__"):
        resp_class = getattr(response.__class__, "__name__", None)
        if resp_class:
            resp_span.set_tag_str("result_class", resp_class)


def _on_request_prepared(middleware, req_span, url, request_headers, environ):
    method = environ.get("REQUEST_METHOD")
    query_string = environ.get("QUERY_STRING")
    trace_utils.set_http_meta(
        req_span, middleware._config, method=method, url=url, query=query_string, request_headers=request_headers
    )
    if middleware.span_modifier:
        middleware.span_modifier(req_span, environ)


def _set_flask_request_tags(request, span, flask_config):
    try:
        span.set_tag_str(COMPONENT, flask_config.integration_name)

        if span.name.split(".")[-1] == "request":
            span.set_tag_str(SPAN_KIND, SpanKind.SERVER)

        # DEV: This name will include the blueprint name as well (e.g. `bp.index`)
        if not span.get_tag(FLASK_ENDPOINT) and request.endpoint:
            span.resource = " ".join((request.method, request.endpoint))
            span.set_tag_str(FLASK_ENDPOINT, request.endpoint)

        if not span.get_tag(FLASK_URL_RULE) and request.url_rule and request.url_rule.rule:
            span.resource = " ".join((request.method, request.url_rule.rule))
            span.set_tag_str(FLASK_URL_RULE, request.url_rule.rule)

        if not span.get_tag(FLASK_VIEW_ARGS) and request.view_args and flask_config.get("collect_view_args"):
            for k, v in request.view_args.items():
                # DEV: Do not use `set_tag_str` here since view args can be string/int/float/path/uuid/etc
                #      https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations
                span.set_tag(".".join((FLASK_VIEW_ARGS, k)), v)
            trace_utils.set_http_meta(span, flask_config, request_path_params=request.view_args)
    except Exception:
        log.debug('failed to set tags for "flask.request" span', exc_info=True)


def _on_start_response_pre(request, ctx, flask_config, status_code, headers):
    span = ctx.get_item("req_span")
    code, _, _ = status_code.partition(" ")
    # If values are accessible, set the resource as `<method> <path>` and add other request tags
    _set_flask_request_tags(request, span, flask_config)
    # Override root span resource name to be `<method> 404` for 404 requests
    # DEV: We do this because we want to make it easier to see all unknown requests together
    #      Also, we do this to reduce the cardinality on unknown urls
    # DEV: If we have an endpoint or url rule tag, then we don't need to do this,
    #      we still want `GET /product/<int:product_id>` grouped together,
    #      even if it is a 404
    if not span.get_tag(FLASK_ENDPOINT) and not span.get_tag(FLASK_URL_RULE):
        span.resource = " ".join((request.method, code))

    response_cookies = _cookies_from_response_headers(headers)
    _on_web_framework_finish_request(
        span=span,
        int_config=flask_config,
        method=request.method,
        url=None,
        status_code=code,
        query=None,
        req_headers=None,
        res_headers=headers,
        route=span.get_tag(FLASK_URL_RULE),
        finish=False,
        response_cookies=response_cookies,
    )


def _cookies_from_response_headers(response_headers):
    cookies = {}
    for header_tuple in response_headers:
        if header_tuple[0] == "Set-Cookie":
            cookie_tokens = header_tuple[1].split("=", 1)
            cookies[cookie_tokens[0]] = cookie_tokens[1]

    return cookies


def _on_flask_render(template, flask_config):
    span = core.get_span()
    if not span:
        return
    name = maybe_stringify(getattr(template, "name", None) or flask_config.get("template_default_name"))
    if name is not None:
        span.resource = name
        span.set_tag_str("flask.template_name", name)


def _on_request_span_modifier(
    ctx, flask_config, request, environ, _HAS_JSON_MIXIN, flask_version, flask_version_str, exception_type
):
    span = ctx.get_item("req_span")
    # Default resource is method and path:
    #   GET /
    #   POST /save
    # We will override this below in `traced_dispatch_request` when we have a `
    # RequestContext` and possibly a url rule
    span.resource = " ".join((request.method, request.path))

    span.set_tag(_SPAN_MEASURED_KEY)

    span.set_tag_str(flask_version, flask_version_str)


def _on_request_span_modifier_post(ctx, flask_config, request, req_body):
    span = ctx.get_item("req_span")
    try:
        raw_uri = ctx.get_item("wsgi.construct_url")(ctx.get_item("environ"))
    except Exception:
        raw_uri = request.url
    trace_utils.set_http_meta(
        span,
        flask_config,
        method=request.method,
        url=request.base_url,
        raw_uri=raw_uri,
        query=request.query_string,
        parsed_query=request.args,
        request_headers=request.headers,
        request_cookies=request.cookies,
        request_body=req_body,
        peer_ip=request.remote_addr,
    )


def _on_traced_get_response_pre(_, ctx: core.ExecutionContext, request, before_request_tags):
    before_request_tags(ctx["pin"], ctx.span, request)
    ctx.span._metrics[_SPAN_MEASURED_KEY] = 1


def _on_web_request_final_tags(span):
    # Necessary to add remaining http status codes and
    # errors relevant to the aws api gateway spans on close
    if span and span.span_type == "web":
        _set_inferred_proxy_tags(span, None)


def _on_django_finalize_response_pre(ctx, after_request_tags, request, response):
    # DEV: Always set these tags, this is where `span.resource` is set
    span = ctx.span
    after_request_tags(ctx["pin"], span, request, response)

    trace_utils.set_http_meta(span, ctx["integration_config"], route=span.get_tag("http.route"))
    _set_inferred_proxy_tags(span, None)


def _on_django_start_response(
    ctx, request, extract_body: Callable, remake_body: Callable, query: str, uri: str, path: Optional[Dict[str, str]]
):
    parsed_query = request.GET
    body = extract_body(request)
    remake_body(request)

    trace_utils.set_http_meta(
        ctx.span,
        ctx["integration_config"],
        method=request.method,
        query=query,
        raw_uri=uri,
        request_path_params=path,
        parsed_query=parsed_query,
        request_body=body,
        request_cookies=request.COOKIES,
    )


def _on_django_cache(ctx: core.ExecutionContext, rowcount: int):
    ctx.span.set_metric(db.ROWCOUNT, rowcount)


def _on_django_func_wrapped(_unused1, _unused2, _unused3, ctx, ignored_excs):
    if ignored_excs:
        for exc in ignored_excs:
            ctx.span._ignore_exception(exc)


def _on_django_process_exception(ctx: core.ExecutionContext, should_set_traceback: bool):
    if should_set_traceback:
        ctx.span.set_traceback()


def _on_django_block_request(ctx: core.ExecutionContext, metadata: Dict[str, str], django_config, url: str, query: str):
    for tk, tv in metadata.items():
        ctx.span.set_tag_str(tk, tv)
    _set_url_tag(django_config, ctx.span, url, query)


def _on_django_after_request_headers_post(
    request_headers,
    response_headers,
    span: "Span",
    django_config,
    request,
    url,
    raw_uri,
    status,
    response_cookies,
):
    trace_utils.set_http_meta(
        span,
        django_config,
        method=request.method,
        url=url,
        raw_uri=raw_uri,
        status_code=status,
        query=request.META.get("QUERY_STRING", None),
        parsed_query=request.GET,
        request_headers=request_headers,
        response_headers=response_headers,
        request_cookies=request.COOKIES,
        request_path_params=request.resolver_match.kwargs if request.resolver_match is not None else None,
        peer_ip=core.get_item("http.request.remote_ip"),
        headers_are_case_sensitive=bool(core.get_item("http.request.headers_case_sensitive")),
        response_cookies=response_cookies,
    )


def _on_botocore_patched_api_call_started(ctx):
    from ddtrace._trace.utils_botocore.span_tags import set_botocore_patched_api_call_span_tags

    span = ctx.span
    set_botocore_patched_api_call_span_tags(
        span,
        ctx.get_item("instance"),
        ctx.get_item("args"),
        ctx.get_item("params"),
        ctx.get_item("endpoint_name"),
        ctx.get_item("operation"),
    )

    # we need this since we may have ran the wrapped operation before starting the span
    # we need to ensure the span start time is correct
    start_ns = ctx.get_item("start_ns")
    if start_ns is not None and ctx.get_item("func_run"):
        span.start_ns = start_ns


def _on_botocore_patched_api_call_exception(ctx, response, exception_type, is_error_code_fn):
    from ddtrace._trace.utils_botocore.span_tags import set_botocore_response_metadata_tags

    span = ctx.span
    # `ClientError.response` contains the result, so we can still grab response metadata
    set_botocore_response_metadata_tags(span, response, is_error_code_fn=is_error_code_fn)

    # If we have a status code, and the status code is not an error,
    #   then ignore the exception being raised
    status_code = span.get_tag(http.STATUS_CODE)
    if status_code and not is_error_code_fn(int(status_code)):
        span._ignore_exception(exception_type)


def _on_botocore_patched_api_call_success(ctx, response):
    from ddtrace._trace.utils_botocore.span_tags import set_botocore_response_metadata_tags

    span = ctx.span

    set_botocore_response_metadata_tags(span, response)

    if config.botocore.add_span_pointers:
        from ddtrace._trace.utils_botocore.span_pointers import extract_span_pointers_from_successful_botocore_response

        for span_pointer_description in extract_span_pointers_from_successful_botocore_response(
            dynamodb_primary_key_names_for_tables=config.botocore.dynamodb_primary_key_names_for_tables,
            endpoint_name=ctx.get_item("endpoint_name"),
            operation_name=ctx.get_item("operation"),
            request_parameters=ctx.get_item("params"),
            response=response,
        ):
            _set_span_pointer(span, span_pointer_description)


def _on_botocore_trace_context_injection_prepared(
    ctx, cloud_service, schematization_function, injection_function, trace_operation
):
    endpoint_name = ctx.get_item("endpoint_name")
    if cloud_service is not None:
        span = ctx.span
        inject_kwargs = dict(endpoint_service=endpoint_name) if cloud_service == "sns" else dict()
        schematize_kwargs = dict(cloud_provider="aws", cloud_service=cloud_service)
        if endpoint_name != "lambda":
            schematize_kwargs["direction"] = SpanDirection.OUTBOUND
        try:
            injection_function(ctx, **inject_kwargs)
            span.name = schematization_function(trace_operation, **schematize_kwargs)
        except Exception:
            log.warning("Unable to inject trace context", exc_info=True)


def _on_botocore_kinesis_update_record(ctx, stream, data_obj: Dict, record, inject_trace_context):
    if inject_trace_context:
        if "_datadog" not in data_obj:
            data_obj["_datadog"] = {}
        HTTPPropagator.inject(ctx.span.context, data_obj["_datadog"])


def _on_botocore_update_messages(ctx, span, _, trace_data, __, message=None):
    context = span.context if span else ctx.span.context
    HTTPPropagator.inject(context, trace_data)


def _on_botocore_patched_stepfunctions_update_input(ctx, span, _, trace_data, __):
    context = span.context if span else ctx.span.context
    HTTPPropagator.inject(context, trace_data["_datadog"])
    ctx.set_item(BOTOCORE_STEPFUNCTIONS_INPUT_KEY, trace_data)


def _on_botocore_patched_bedrock_api_call_started(ctx, request_params):
    span = ctx.span
    integration = ctx["bedrock_integration"]
    integration._tag_proxy_request(ctx)

    span.set_tag_str("bedrock.request.model_provider", ctx["model_provider"])
    span.set_tag_str("bedrock.request.model", ctx["model_name"])
    for k, v in request_params.items():
        if k == "prompt":
            if integration.is_pc_sampled_span(span):
                v = integration.trunc(str(v))
        span.set_tag_str("bedrock.request.{}".format(k), str(v))
        if k == "n":
            ctx.set_item("num_generations", str(v))


def _on_botocore_patched_bedrock_api_call_exception(ctx, exc_info):
    span = ctx.span
    span.set_exc_info(*exc_info)
    model_name = ctx["model_name"]
    integration = ctx["bedrock_integration"]
    if "embed" not in model_name:
        integration.llmobs_set_tags(span, args=[ctx], kwargs={})
    span.finish()


def _on_botocore_patched_bedrock_api_call_success(ctx, reqid, latency, input_token_count, output_token_count):
    span = ctx.span
    span.set_tag_str("bedrock.response.id", reqid)
    span.set_tag_str("bedrock.response.duration", latency)
    if input_token_count:
        span.set_metric("bedrock.response.usage.prompt_tokens", int(input_token_count))
    if output_token_count:
        span.set_metric("bedrock.response.usage.completion_tokens", int(output_token_count))


def _propagate_context(ctx, headers):
    distributed_tracing_enabled = ctx["integration_config"].distributed_tracing_enabled
    span = ctx.span
    if distributed_tracing_enabled and span:
        HTTPPropagator.inject(span.context, headers)


def _after_job_execution(ctx, job_failed, span_tags):
    """sets job.status and job.origin span tags after job is performed"""
    # get_status() returns None when ttl=0
    span = ctx.span
    if span:
        if job_failed:
            span.error = 1
        for k in span_tags.keys():
            span.set_tag_str(k, span_tags[k])


def _on_end_of_traced_method_in_fork(ctx):
    """Force flush to agent since the process `os.exit()`s
    immediately after this method returns
    """
    ctx["pin"].tracer.flush()


def _on_botocore_bedrock_process_response_converse(
    ctx: core.ExecutionContext,
    result: List[Dict[str, Any]],
):
    ctx["bedrock_integration"].llmobs_set_tags(
        ctx.span,
        args=[ctx],
        kwargs={},
        response=result,
    )
    ctx.span.finish()


def _on_botocore_bedrock_process_response(
    ctx: core.ExecutionContext,
    formatted_response: Dict[str, Any],
    metadata: Dict[str, Any],
    body: Dict[str, List[Dict]],
    should_set_choice_ids: bool,
) -> None:
    text = formatted_response["text"]
    span = ctx.span
    model_name = ctx["model_name"]
    if should_set_choice_ids:
        for i in range(len(text)):
            span.set_tag_str("bedrock.response.choices.{}.id".format(i), str(body["generations"][i]["id"]))
    integration = ctx["bedrock_integration"]
    if metadata is not None:
        for k, v in metadata.items():
            if k in ["usage.completion_tokens", "usage.prompt_tokens"] and v:
                span.set_metric("bedrock.response.{}".format(k), int(v))
            else:
                span.set_tag_str("bedrock.{}".format(k), str(v))
    if "embed" in model_name:
        span.set_metric("bedrock.response.embedding_length", len(formatted_response["text"][0]))
        span.finish()
        return
    for i in range(len(formatted_response["text"])):
        if integration.is_pc_sampled_span(span):
            span.set_tag_str(
                "bedrock.response.choices.{}.text".format(i),
                integration.trunc(str(formatted_response["text"][i])),
            )
        span.set_tag_str(
            "bedrock.response.choices.{}.finish_reason".format(i), str(formatted_response["finish_reason"][i])
        )
    integration.llmobs_set_tags(span, args=[ctx], kwargs={}, response=formatted_response)
    span.finish()


def _on_botocore_sqs_recvmessage_post(
    ctx: core.ExecutionContext, _, result: Dict, propagate: bool, message_parser: Callable
) -> None:
    if result is not None and "Messages" in result and len(result["Messages"]) >= 1:
        ctx.set_item("message_received", True)
        if propagate:
            ctx.set_safe("distributed_context", extract_DD_context_from_messages(result["Messages"], message_parser))


def _on_botocore_kinesis_getrecords_post(
    ctx: core.ExecutionContext,
    _,
    __,
    ___,
    ____,
    result,
    propagate: bool,
    message_parser: Callable,
):
    if result is not None and "Records" in result and len(result["Records"]) >= 1:
        ctx.set_item("message_received", True)
        if propagate:
            ctx.set_item("distributed_context", extract_DD_context_from_messages(result["Records"], message_parser))


def _on_redis_command_post(ctx: core.ExecutionContext, rowcount):
    if rowcount is not None:
        ctx.span.set_metric(db.ROWCOUNT, rowcount)


def _on_valkey_command_post(ctx: core.ExecutionContext, rowcount):
    if rowcount is not None:
        ctx.span.set_metric(db.ROWCOUNT, rowcount)


def _on_test_visibility_enable(config) -> None:
    from ddtrace.internal.ci_visibility import CIVisibility

    CIVisibility.enable(config=config)


def _on_test_visibility_disable() -> None:
    from ddtrace.internal.ci_visibility import CIVisibility

    CIVisibility.disable()


def _on_test_visibility_is_enabled() -> bool:
    from ddtrace.internal.ci_visibility import CIVisibility

    return CIVisibility.enabled


def _set_span_pointer(span: "Span", span_pointer_description: _SpanPointerDescription) -> None:
    span._add_span_pointer(
        pointer_kind=span_pointer_description.pointer_kind,
        pointer_direction=span_pointer_description.pointer_direction,
        pointer_hash=span_pointer_description.pointer_hash,
        extra_attributes=span_pointer_description.extra_attributes,
    )


def _set_azure_function_tags(span, azure_functions_config, function_name, trigger, span_kind):
    span.set_tag_str(COMPONENT, azure_functions_config.integration_name)
    span.set_tag_str(SPAN_KIND, span_kind)
    span.set_tag_str("aas.function.name", function_name)  # codespell:ignore
    span.set_tag_str("aas.function.trigger", trigger)  # codespell:ignore


def _on_azure_functions_request_span_modifier(ctx, azure_functions_config, req):
    span = ctx.span
    parsed_url = parse.urlparse(req.url)
    path = parsed_url.path
    span.resource = f"{req.method} {path}"
    trace_utils.set_http_meta(
        span,
        azure_functions_config,
        method=req.method,
        url=req.url,
        request_headers=req.headers,
        request_body=req.get_body(),
        route=path,
    )


def _on_azure_functions_start_response(ctx, azure_functions_config, res, function_name, trigger):
    span = ctx.span
    _set_azure_function_tags(span, azure_functions_config, function_name, trigger, SpanKind.SERVER)
    trace_utils.set_http_meta(
        span,
        azure_functions_config,
        status_code=res.status_code if res else None,
        response_headers=res.headers if res else None,
    )


def _on_azure_functions_trigger_span_modifier(ctx, azure_functions_config, function_name, trigger, span_kind):
    span = ctx.span
    _set_azure_function_tags(span, azure_functions_config, function_name, trigger, span_kind)


def _on_azure_functions_service_bus_trigger_span_modifier(
    ctx, azure_functions_config, function_name, trigger, span_kind, entity_name, message_id
):
    span = ctx.span
    _set_azure_function_tags(span, azure_functions_config, function_name, trigger, span_kind)
    span.set_tag_str(MESSAGING_DESTINATION_NAME, entity_name)
    span.set_tag_str(MESSAGING_MESSAGE_ID, message_id)
    span.set_tag_str(MESSAGING_OPERATION, "receive")
    span.set_tag_str(MESSAGING_SYSTEM, azure_servicebusx.SERVICE)


def _on_azure_servicebus_send_message_modifier(ctx, azure_servicebus_config, entity_name, fully_qualified_namespace):
    span = ctx.span
    span.set_tag_str(COMPONENT, azure_servicebus_config.integration_name)
    span.set_tag_str(MESSAGING_DESTINATION_NAME, entity_name)
    span.set_tag_str(MESSAGING_OPERATION, "send")
    span.set_tag_str(MESSAGING_SYSTEM, azure_servicebusx.SERVICE)
    span.set_tag_str(NETWORK_DESTINATION_NAME, fully_qualified_namespace)
    span.set_tag_str(SPAN_KIND, SpanKind.PRODUCER)


def listen():
    core.on("wsgi.request.prepare", _on_request_prepare)
    core.on("wsgi.request.prepared", _on_request_prepared)
    core.on("wsgi.app.success", _on_app_success)
    core.on("wsgi.app.exception", _on_app_exception)
    core.on("wsgi.request.complete", _on_request_complete, "traced_iterable")
    core.on("wsgi.response.prepared", _on_response_prepared)
    core.on("flask.start_response.pre", _on_start_response_pre)
    core.on("flask.request_call_modifier", _on_request_span_modifier)
    core.on("flask.request_call_modifier.post", _on_request_span_modifier_post)
    core.on("flask.render", _on_flask_render)
    core.on("context.started.wsgi.response", _maybe_start_http_response_span)
    core.on("context.started.flask._patched_request", _on_traced_request_context_started_flask)
    core.on("django.traced_get_response.pre", _on_traced_get_response_pre)
    core.on("django.finalize_response.pre", _on_django_finalize_response_pre)
    core.on("django.start_response", _on_django_start_response)
    core.on("django.cache", _on_django_cache)
    core.on("django.func.wrapped", _on_django_func_wrapped)
    core.on("django.process_exception", _on_django_process_exception)
    core.on("django.block_request_callback", _on_django_block_request)
    core.on("django.after_request_headers.post", _on_django_after_request_headers_post)
    core.on("botocore.patched_api_call.exception", _on_botocore_patched_api_call_exception)
    core.on("botocore.patched_api_call.success", _on_botocore_patched_api_call_success)
    core.on("botocore.patched_kinesis_api_call.success", _on_botocore_patched_api_call_success)
    core.on("botocore.patched_kinesis_api_call.exception", _on_botocore_patched_api_call_exception)
    core.on("botocore.prep_context_injection.post", _on_botocore_trace_context_injection_prepared)
    core.on("botocore.patched_api_call.started", _on_botocore_patched_api_call_started)
    core.on("botocore.patched_kinesis_api_call.started", _on_botocore_patched_api_call_started)
    core.on("botocore.patched_kinesis_api_call.exception", _on_botocore_patched_api_call_exception)
    core.on("botocore.patched_kinesis_api_call.success", _on_botocore_patched_api_call_success)
    core.on("botocore.kinesis.update_record", _on_botocore_kinesis_update_record)
    core.on("botocore.patched_sqs_api_call.started", _on_botocore_patched_api_call_started)
    core.on("botocore.patched_sqs_api_call.exception", _on_botocore_patched_api_call_exception)
    core.on("botocore.patched_sqs_api_call.success", _on_botocore_patched_api_call_success)
    core.on("botocore.sqs_sns.update_messages", _on_botocore_update_messages)
    core.on("botocore.patched_stepfunctions_api_call.started", _on_botocore_patched_api_call_started)
    core.on("botocore.patched_stepfunctions_api_call.exception", _on_botocore_patched_api_call_exception)
    core.on("botocore.stepfunctions.update_input", _on_botocore_patched_stepfunctions_update_input)
    core.on("botocore.eventbridge.update_messages", _on_botocore_update_messages)
    core.on("botocore.client_context.update_messages", _on_botocore_update_messages)
    core.on("botocore.patched_bedrock_api_call.started", _on_botocore_patched_bedrock_api_call_started)
    core.on("botocore.patched_bedrock_api_call.exception", _on_botocore_patched_bedrock_api_call_exception)
    core.on("botocore.patched_bedrock_api_call.success", _on_botocore_patched_bedrock_api_call_success)
    core.on("botocore.bedrock.process_response", _on_botocore_bedrock_process_response)
    core.on("botocore.bedrock.process_response_converse", _on_botocore_bedrock_process_response_converse)
    core.on("botocore.sqs.ReceiveMessage.post", _on_botocore_sqs_recvmessage_post)
    core.on("botocore.kinesis.GetRecords.post", _on_botocore_kinesis_getrecords_post)
    core.on("redis.async_command.post", _on_redis_command_post)
    core.on("redis.command.post", _on_redis_command_post)
    core.on("valkey.async_command.post", _on_valkey_command_post)
    core.on("valkey.command.post", _on_valkey_command_post)
    core.on("azure.functions.request_call_modifier", _on_azure_functions_request_span_modifier)
    core.on("azure.functions.start_response", _on_azure_functions_start_response)
    core.on("azure.functions.trigger_call_modifier", _on_azure_functions_trigger_span_modifier)
    core.on("azure.functions.service_bus_trigger_modifier", _on_azure_functions_service_bus_trigger_span_modifier)
    core.on("azure.servicebus.send_message_modifier", _on_azure_servicebus_send_message_modifier)

    # web frameworks general handlers
    core.on("web.request.start", _on_web_framework_start_request)
    core.on("web.request.finish", _on_web_framework_finish_request)
    core.on("web.request.final_tags", _on_web_request_final_tags)

    # inferred proxy handlers
    core.on("inferred_proxy.start", _on_inferred_proxy_start)
    core.on("inferred_proxy.finish", _on_inferred_proxy_finish)

    core.on("test_visibility.enable", _on_test_visibility_enable)
    core.on("test_visibility.disable", _on_test_visibility_disable)
    core.on("test_visibility.is_enabled", _on_test_visibility_is_enabled, "is_enabled")
    core.on("rq.worker.perform_job", _after_job_execution)
    core.on("rq.worker.after.perform.job", _on_end_of_traced_method_in_fork)
    core.on("rq.queue.enqueue_job", _propagate_context)

    for context_name in (
        # web frameworks
        "aiohttp.request",
        "bottle.request",
        "cherrypy.request",
        "falcon.request",
        "molten.request",
        "pyramid.request",
        "sanic.request",
        "tornado.request",
        "flask.call",
        "flask.jsonify",
        "flask.render_template",
        "asgi.__call__",
        "wsgi.__call__",
        "django.traced_get_response",
        "django.cache",
        "django.template.render",
        "django.process_exception",
        "django.func.wrapped",
        # non web frameworks
        "botocore.instrumented_api_call",
        "botocore.instrumented_lib_function",
        "botocore.patched_kinesis_api_call",
        "botocore.patched_sqs_api_call",
        "botocore.patched_stepfunctions_api_call",
        "botocore.patched_bedrock_api_call",
        "redis.command",
        "valkey.command",
        "rq.queue.enqueue_job",
        "rq.traced_queue_fetch_job",
        "rq.worker.perform_job",
        "rq.job.perform",
        "rq.job.fetch_many",
        "azure.functions.patched_route_request",
        "azure.functions.patched_service_bus",
        "azure.functions.patched_timer",
        "azure.servicebus.patched_producer",
    ):
        core.on(f"context.started.start_span.{context_name}", _start_span)


listen()
