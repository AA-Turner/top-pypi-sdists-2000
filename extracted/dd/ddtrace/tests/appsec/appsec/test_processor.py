import json
import logging
import os.path

import mock
import pytest

from ddtrace.appsec import _asm_request_context
from ddtrace.appsec import _metrics
from ddtrace.appsec._constants import APPSEC
from ddtrace.appsec._constants import DEFAULT
from ddtrace.appsec._constants import FINGERPRINTING
from ddtrace.appsec._constants import WAF_DATA_NAMES
from ddtrace.appsec._ddwaf import DDWaf
from ddtrace.appsec._processor import AppSecSpanProcessor
from ddtrace.appsec._processor import _transform_headers
from ddtrace.appsec._utils import get_triggers
from ddtrace.constants import USER_KEEP
from ddtrace.contrib.internal.trace_utils import set_http_meta
from ddtrace.ext import SpanTypes
from ddtrace.internal import core
import tests.appsec.rules as rules
from tests.appsec.utils import asm_context
from tests.appsec.utils import get_waf_addresses
from tests.appsec.utils import is_blocked
from tests.utils import override_env
from tests.utils import override_global_config
from tests.utils import snapshot


try:
    from json.decoder import JSONDecodeError
except ImportError:
    # handling python 2.X import error
    JSONDecodeError = ValueError  # type: ignore


APPSEC_JSON_TAG = f"meta.{APPSEC.JSON}"
config_asm = {"_asm_enabled": True}
config_good_rules = {"_asm_static_rule_file": rules.RULES_GOOD_PATH, "_asm_enabled": True}
config_bad_rules = {"_asm_static_rule_file": rules.RULES_BAD_PATH, "_asm_enabled": True, "_raise": True}


def test_transform_headers():
    transformed = _transform_headers(
        {
            "hello": "world",
            "Foo": "bar1",
            "foo": "bar2",
            "fOO": "bar3",
            "BAR": "baz",
            "COOKIE": "secret",
        },
    )
    assert set(transformed.keys()) == {"hello", "bar", "foo"}
    assert transformed["hello"] == "world"
    assert transformed["bar"] == "baz"
    assert set(transformed["foo"]) == {"bar1", "bar2", "bar3"}


def test_enable(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")

    assert span.get_metric("_dd.appsec.enabled") == 1.0


def test_enable_custom_rules():
    with override_global_config(dict(_asm_static_rule_file=rules.RULES_GOOD_PATH)):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled
    assert processor.rule_filename == rules.RULES_GOOD_PATH


def test_ddwaf_ctx(tracer):
    with asm_context(tracer=tracer, config=config_good_rules) as span:
        processor = AppSecSpanProcessor()
        processor.on_span_start(span)
        ctx = _asm_request_context._get_asm_context()
        assert ctx
        processor.on_span_finish(span)
        assert _asm_request_context._get_asm_context() is None


@pytest.mark.parametrize("rule, _exc", [(rules.RULES_MISSING_PATH, IOError), (rules.RULES_BAD_PATH, ValueError)])
def test_enable_bad_rules(rule, _exc, tracer):
    # by default enable must not crash but display errors in the logs
    with asm_context(tracer=tracer, config=config_bad_rules) as span:
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")


def test_retain_traces(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        print(">>> set HTTP meta", flush=True)
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")

    assert span.context.sampling_priority == USER_KEEP


def test_valid_json(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")

    assert get_triggers(span)


def test_header_attack(tracer):
    with asm_context(tracer=tracer, config=dict(retrieve_client_ip=True, _asm_enabled=True)) as span:
        set_http_meta(
            span,
            rules.Config(),
            request_headers={
                "User-Agent": "Arachni/v1",
                "user-agent": "aa",
                "x-forwarded-for": "8.8.8.8",
            },
        )

    assert get_triggers(span)
    assert span.get_tag("actor.ip") == "8.8.8.8"


def test_headers_collection(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(
            span,
            rules.Config(),
            raw_uri="http://example.com/.git",
            status_code="404",
            request_headers={
                "hello": "world",
                "accept": "something",
                "x-Forwarded-for": "127.0.0.1",
            },
            response_headers={
                "foo": "bar",
                "Content-Length": "500",
            },
        )

    assert span.get_tag("http.request.headers.hello") is None
    assert span.get_tag("http.request.headers.accept") == "something"
    assert span.get_tag("http.request.headers.x-forwarded-for") == "127.0.0.1"
    assert span.get_tag("http.response.headers.content-length") == "500"
    assert span.get_tag("http.response.headers.foo") is None


@snapshot(
    include_tracer=True,
    ignores=[
        "meta_struct",
        "metrics._dd.appsec.waf.duration",
        "metrics._dd.appsec.waf.duration_ext",
        APPSEC_JSON_TAG,
        "meta." + FINGERPRINTING.NETWORK,
        "meta." + FINGERPRINTING.HEADER,
        "meta." + FINGERPRINTING.ENDPOINT,
        "meta." + FINGERPRINTING.SESSION,
        "service",
        "meta._dd.rc.client_id",
        "meta._dd.appsec.rc_products",
    ],
)
def test_appsec_cookies_no_collection_snapshot(tracer):
    # We use tracer instead of tracer_appsec because snapshot is looking for tracer fixture and not understands
    # other fixtures
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(
            span,
            {},
            raw_uri="http://example.com/.git",
            status_code="404",
            request_cookies={"cookie1": "im the cookie1"},
        )

    assert get_triggers(span)


@snapshot(
    include_tracer=True,
    ignores=[
        "meta_struct",
        "metrics._dd.appsec.waf.duration",
        "metrics._dd.appsec.waf.duration_ext",
        APPSEC_JSON_TAG,
        "meta." + FINGERPRINTING.NETWORK,
        "meta." + FINGERPRINTING.HEADER,
        "meta." + FINGERPRINTING.ENDPOINT,
        "meta." + FINGERPRINTING.SESSION,
        "service",
        "meta._dd.rc.client_id",
        "meta._dd.appsec.rc_products",
    ],
)
def test_appsec_body_no_collection_snapshot(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(
            span,
            {},
            raw_uri="http://example.com/.git",
            status_code="404",
            request_body={"somekey": "somekey value"},
        )

    assert get_triggers(span)


def test_ip_block(tracer):
    with asm_context(tracer=tracer, ip_addr=rules._IP.BLOCKED, config=config_good_rules) as span:
        set_http_meta(
            span,
            rules.Config(),
        )
    assert get_triggers(span)
    assert get_waf_addresses("http.request.remote_ip") == rules._IP.BLOCKED
    assert is_blocked(span)


@pytest.mark.parametrize("ip", [rules._IP.MONITORED, rules._IP.BYPASS, rules._IP.DEFAULT])
def test_ip_not_block(tracer, ip):
    with asm_context(tracer=tracer, ip_addr=ip, config=config_good_rules) as span:
        set_http_meta(
            span,
            rules.Config(),
        )

    assert get_waf_addresses("http.request.remote_ip") == ip
    assert is_blocked(span) is False


def test_ip_update_rules_and_block(tracer):
    with asm_context(tracer=tracer, ip_addr=rules._IP.BLOCKED, config=config_asm) as span1:
        tracer._appsec_processor._update_rules(
            [],
            [
                (
                    "ASM",
                    "Datadog/1/ASM/data",
                    {
                        "rules_data": [
                            {
                                "data": [
                                    {"value": rules._IP.BLOCKED},
                                ],
                                "id": "blocked_ips",
                                "type": "ip_with_expiration",
                            },
                        ]
                    },
                )
            ],
        )
        with tracer.trace("test", span_type=SpanTypes.WEB) as span:
            set_http_meta(
                span,
                rules.Config(),
            )

    assert get_waf_addresses("http.request.remote_ip") == rules._IP.BLOCKED
    assert is_blocked(span1)
    assert (span._local_root or span).get_tag(APPSEC.RC_PRODUCTS) == "[ASM:1] u:1 r:2"


def test_ip_update_rules_expired_no_block(tracer):
    with asm_context(tracer=tracer, ip_addr=rules._IP.BLOCKED, config=config_asm):
        tracer._appsec_processor._update_rules(
            [],
            [
                (
                    "ASM",
                    "Datadog/1/ASM/data",
                    {
                        "rules_data": [
                            {
                                "data": [
                                    {"expiration": 1662804872, "value": rules._IP.BLOCKED},
                                ],
                                "id": "blocked_ips",
                                "type": "ip_with_expiration",
                            },
                        ]
                    },
                )
            ],
        )
        with tracer.trace("test", span_type=SpanTypes.WEB) as span:
            set_http_meta(
                span,
                rules.Config(),
            )

    assert get_waf_addresses("http.request.remote_ip") == rules._IP.BLOCKED
    assert is_blocked(span) is False
    assert (span._local_root or span).get_tag(APPSEC.RC_PRODUCTS) == "[ASM:1] u:1 r:2"


@snapshot(
    include_tracer=True,
    ignores=[
        "meta_struct",
        "metrics._dd.appsec.waf.duration",
        "metrics._dd.appsec.waf.duration_ext",
        APPSEC_JSON_TAG,
        "meta." + FINGERPRINTING.NETWORK,
        "meta." + FINGERPRINTING.HEADER,
        "meta." + FINGERPRINTING.ENDPOINT,
        "meta." + FINGERPRINTING.SESSION,
        "service",
        "meta._dd.base_service",
        "meta._dd.rc.client_id",
        "meta._dd.appsec.rc_products",
    ],
)
def test_appsec_span_tags_snapshot(tracer):
    with asm_context(tracer=tracer, config=config_asm, service="test") as span:
        span.set_tag("http.url", "http://example.com/.git")
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")

    assert get_triggers(span)


@snapshot(
    include_tracer=True,
    ignores=[
        "meta_struct",
        "metrics._dd.appsec.waf.duration",
        "metrics._dd.appsec.waf.duration_ext",
        APPSEC_JSON_TAG,
        "meta._dd.appsec.event_rules.errors",
        "service",
        "meta._dd.base_service",
        "meta._dd.rc.client_id",
        "meta._dd.appsec.rc_products",
    ],
)
def test_appsec_span_tags_snapshot_with_errors(tracer):
    config = dict(
        _asm_enabled=True,
        _asm_static_rule_file=os.path.join(rules.ROOT_DIR, "rules-with-2-errors.json"),
        _waf_timeout=50_000,
    )
    with asm_context(tracer=tracer, config=config, service="test") as span:
        span.set_tag("http.url", "http://example.com/.git")
        set_http_meta(span, {}, raw_uri="http://example.com/.git", status_code="404")

    assert get_triggers(span) is None


def test_appsec_span_rate_limit(tracer):
    with override_env(dict(DD_APPSEC_TRACE_RATE_LIMIT="1")):
        with asm_context(tracer=tracer, config=config_asm) as span1:
            set_http_meta(span1, {}, raw_uri="http://example.com/.git", status_code="404")

        with asm_context(tracer=tracer, config={}) as span2:
            set_http_meta(span2, {}, raw_uri="http://example.com/.git", status_code="404")
            span2.start_ns = span1.start_ns + 1

        with asm_context(tracer=tracer, config={}) as span3:
            set_http_meta(span3, {}, raw_uri="http://example.com/.git", status_code="404")
            span2.start_ns = span1.start_ns + 2

        assert get_triggers(span1)
        assert get_triggers(span2) is None
        assert get_triggers(span3) is None


def test_ddwaf_not_raises_exception():
    with open(DEFAULT.RULES) as rules:
        rules_json = json.loads(rules.read())
        DDWaf(
            rules_json,
            DEFAULT.APPSEC_OBFUSCATION_PARAMETER_KEY_REGEXP.encode("utf-8"),
            DEFAULT.APPSEC_OBFUSCATION_PARAMETER_VALUE_REGEXP.encode("utf-8"),
            _metrics,
        )


def test_obfuscation_parameter_key_empty():
    with override_global_config(dict(_asm_obfuscation_parameter_key_regexp="")):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_value_empty():
    with override_global_config(dict(_asm_obfuscation_parameter_value_regexp="")):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_key_and_value_empty():
    with override_global_config(
        dict(_asm_obfuscation_parameter_key_regexp="", _asm_obfuscation_parameter_value_regexp="")
    ):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_key_invalid_regex():
    with override_global_config(dict(_asm_obfuscation_parameter_key_regexp="(")):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_invalid_regex():
    with override_global_config(dict(_asm_obfuscation_parameter_value_regexp="(")):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_key_and_value_invalid_regex():
    with override_global_config(
        dict(_asm_obfuscation_parameter_key_regexp="(", _asm_obfuscation_parameter_value_regexp="(")
    ):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor.enabled


def test_obfuscation_parameter_value_unconfigured_not_matching(tracer):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(span, rules.Config(), raw_uri="http://example.com/.git?hello=goodbye", status_code="404")

    triggers = get_triggers(span)
    assert triggers
    values = [
        value.get("value")
        for rule in triggers
        for match in rule.get("rule_matches", [])
        for value in match.get("parameters", [])
    ]
    assert any("hello" in value for value in values)
    assert any("goodbye" in value for value in values)
    assert all("<Redacted>" not in value for value in values)


@pytest.mark.parametrize("key", ["password", "public_key", "jsessionid", "jwt"])
def test_obfuscation_parameter_value_unconfigured_matching(tracer, key):
    with asm_context(tracer=tracer, config=config_asm) as span:
        set_http_meta(span, rules.Config(), raw_uri=f"http://example.com/.git?{key}=goodbye", status_code="404")

    triggers = get_triggers(span)
    assert triggers
    values = [
        value.get("value")
        for rule in triggers
        for match in rule.get("rule_matches", [])
        for value in match.get("parameters", [])
    ]
    assert all("goodbye" not in value for value in values)
    assert any("<Redacted>" in value for value in values)


def test_obfuscation_parameter_value_configured_not_matching(tracer):
    config = dict(_asm_enabled=True, _asm_obfuscation_parameter_value_regexp="token")
    with asm_context(tracer=tracer, config=config) as span:
        set_http_meta(span, rules.Config(), raw_uri="http://example.com/.git?password=goodbye", status_code="404")

    triggers = get_triggers(span)
    assert triggers
    values = [
        value.get("value")
        for rule in triggers
        for match in rule.get("rule_matches", [])
        for value in match.get("parameters", [])
    ]
    assert any("password" in value for value in values)
    assert any("goodbye" in value for value in values)
    assert all("<Redacted>" not in value for value in values)


def test_obfuscation_parameter_value_configured_matching(tracer):
    config = dict(_asm_enabled=True, _asm_obfuscation_parameter_value_regexp="token")
    with asm_context(tracer=tracer, config=config) as span:
        set_http_meta(span, rules.Config(), raw_uri="http://example.com/.git?token=goodbye", status_code="404")

    triggers = get_triggers(span)
    assert triggers
    values = [
        value.get("value")
        for rule in triggers
        for match in rule.get("rule_matches", [])
        for value in match.get("parameters", [])
    ]
    assert all("token" not in value for value in values)
    assert all("goodbye" not in value for value in values)
    assert any("<Redacted>" in value for value in values)


def test_ddwaf_run():
    with open(rules.RULES_GOOD_PATH) as rule_set:
        rules_json = json.loads(rule_set.read())
        _ddwaf = DDWaf(rules_json, b"", b"", _metrics)
        data = {
            "server.request.query": {},
            "server.request.headers.no_cookies": {"user-agent": "werkzeug/2.1.2", "host": "localhost"},
            "server.request.cookies": {"attack": "1' or '1' = '1'"},
            "server.response.headers.no_cookies": {"content-type": "text/html; charset=utf-8", "content-length": "207"},
        }
        ctx = _ddwaf._at_request_start()
        res = _ddwaf.run(ctx, data, timeout_ms=DEFAULT.WAF_TIMEOUT)  # res is a serialized json
        assert res.data
        assert res.data[0]["rule"]["id"] == "crs-942-100"
        assert res.runtime > 0
        assert res.total_runtime > 0
        assert res.total_runtime > res.runtime
        assert res.timeout is False


def test_ddwaf_run_timeout():
    with open(rules.RULES_GOOD_PATH) as rule_set:
        rules_json = json.loads(rule_set.read())
        _ddwaf = DDWaf(rules_json, b"", b"", _metrics)
        data = {
            "server.request.path_params": {"param_{}".format(i): "value_{}".format(i) for i in range(100)},
            "server.request.cookies": {"attack{}".format(i): "1' or '1' = '{}'".format(i) for i in range(100)},
        }
        ctx = _ddwaf._at_request_start()
        res = _ddwaf.run(ctx, data, timeout_ms=0.001)  # res is a serialized json
        assert res.runtime > 0
        assert res.total_runtime > 0
        assert res.total_runtime > res.runtime
        assert res.timeout is True


def test_ddwaf_info():
    with open(rules.RULES_GOOD_PATH) as rule_set:
        rules_json = json.loads(rule_set.read())
        _ddwaf = DDWaf(rules_json, b"", b"", _metrics)

        info = _ddwaf.info
        assert info.loaded == len(rules_json["rules"])
        assert info.failed == 0
        assert info.errors == ""
        assert info.version == "rules_good"


def test_ddwaf_info_with_2_errors():
    with open(os.path.join(rules.ROOT_DIR, "rules-with-2-errors.json")) as rule_set:
        rules_json = json.loads(rule_set.read())
        _ddwaf = DDWaf(rules_json, b"", b"", _metrics)

        info = _ddwaf.info
        assert info.loaded == 1
        assert info.failed == 2
        # Compare dict contents insensitive to ordering
        expected_dict = sorted(
            {"missing key 'conditions'": ["crs-913-110"], "missing key 'tags'": ["crs-942-100"]}.items()
        )
        assert sorted(json.loads(info.errors).items()) == expected_dict
        assert info.version == "5.5.5"


def test_ddwaf_info_with_3_errors():
    with open(os.path.join(rules.ROOT_DIR, "rules-with-3-errors.json")) as rule_set:
        rules_json = json.loads(rule_set.read())
        _ddwaf = DDWaf(rules_json, b"", b"", _metrics)

        info = _ddwaf.info
        assert info.loaded == 1
        assert info.failed == 2
        assert json.loads(info.errors) == {"missing key 'name'": ["crs-942-100", "crs-913-120"]}


def test_ddwaf_run_contained_typeerror(tracer, caplog):
    config = rules.Config()
    config.http_tag_query_string = True

    with caplog.at_level(logging.DEBUG), mock.patch(
        "ddtrace.appsec._ddwaf.waf.ddwaf_run", side_effect=TypeError("expected c_long instead of int")
    ):
        with asm_context(tracer=tracer, config=config_asm) as span:
            set_http_meta(
                span,
                config,
                method="PATCH",
                url="http://localhost/api/unstable/role_requests/dab1e9ae-9d99-11ed-bfdf-da7ad0900000?_authentication_token=2b0297348221f294de3a047e2ecf1235abb866b6",  # noqa: E501
                status_code="200",
                raw_uri="http://localhost/api/unstable/role_requests/dab1e9ae-9d99-11ed-bfdf-da7ad0900000?_authentication_token=2b0297348221f294de3a047e2ecf1235abb866b6",  # noqa: E501
                request_headers={
                    "host": "localhost",
                    "user-agent": "aa",
                    "content-length": "73",
                },
                response_headers={
                    "content-length": "501",
                    "x-ratelimit-remaining": "363",
                    "x-ratelimit-name": "role_api",
                    "x-ratelimit-limit": "500",
                    "x-ratelimit-period": "60",
                    "content-type": "application/json",
                    "x-ratelimit-reset": "16",
                },
                request_body={"_authentication_token": "2b0297348221f294de3a047e2ecf1235abb866b6"},
            )

    assert get_triggers(span) is None
    assert "TypeError: expected c_long instead of int" in caplog.text


def test_ddwaf_run_contained_oserror(tracer, caplog):
    config = rules.Config()
    config.http_tag_query_string = True

    with caplog.at_level(logging.DEBUG), mock.patch(
        "ddtrace.appsec._ddwaf.waf.ddwaf_run", side_effect=OSError("ddwaf run failed")
    ):
        with asm_context(tracer=tracer, config=config_asm) as span:
            set_http_meta(
                span,
                config,
                method="PATCH",
                url="http://localhost/api/unstable/role_requests/dab1e9ae-9d99-11ed-bfdf-da7ad0900000?_authentication_token=2b0297348221f294de3a047e2ecf1235abb866b6",  # noqa: E501
                status_code="200",
                raw_uri="http://localhost/api/unstable/role_requests/dab1e9ae-9d99-11ed-bfdf-da7ad0900000?_authentication_token=2b0297348221f294de3a047e2ecf1235abb866b6",  # noqa: E501
                request_headers={
                    "host": "localhost",
                    "user-agent": "aa",
                    "content-length": "73",
                },
                response_headers={
                    "content-length": "501",
                    "x-ratelimit-remaining": "363",
                    "x-ratelimit-name": "role_api",
                    "x-ratelimit-limit": "500",
                    "x-ratelimit-period": "60",
                    "content-type": "application/json",
                    "x-ratelimit-reset": "16",
                },
                request_body={"_authentication_token": "2b0297348221f294de3a047e2ecf1235abb866b6"},
            )

    assert get_triggers(span) is None
    assert "OSError: ddwaf run failed" in caplog.text


def test_asm_context_registration(tracer):
    from ddtrace.appsec._asm_request_context import _ASM_CONTEXT

    # For a web type span, a context manager is added, but then removed
    with asm_context(tracer=tracer, config=config_asm) as span:
        assert core.get_item(_ASM_CONTEXT) is not None
    assert core.get_item(_ASM_CONTEXT) is None

    # Regression test, if the span type changes after being created, we always removed
    with asm_context(tracer=tracer, config=config_asm) as span:
        span.span_type = SpanTypes.HTTP
        assert core.get_item(_ASM_CONTEXT) is not None
    assert core.get_item(_ASM_CONTEXT) is None


CUSTOM_RULE_METHOD = [
    (
        "ASM",
        "Datadog/3421/ASM/data",
        {
            "custom_rules": [
                {
                    "conditions": [
                        {
                            "operator": "match_regex",
                            "parameters": {
                                "inputs": [{"address": "server.request.method"}],
                                "options": {"case_sensitive": False},
                                "regex": "GET",
                            },
                        }
                    ],
                    "id": "32b243c7-26eb-4046-adf4-custom",
                    "name": "test required",
                    "tags": {"category": "attack_attempt", "custom": "1", "type": "custom"},
                    "transformers": [],
                },
                {
                    "conditions": [
                        {
                            "operator": "match_regex",
                            "parameters": {
                                "inputs": [{"address": "usr.login"}],
                                "options": {"case_sensitive": False},
                                "regex": "GET",
                            },
                        }
                    ],
                    "id": "32b243c7-26eb-4046-bbbb-custom",
                    "name": "test required",
                    "tags": {"category": "attack_attempt", "custom": "1", "type": "custom"},
                    "transformers": [],
                },
            ]
        },
    )
]


def test_required_addresses():
    with override_global_config(dict(_asm_static_rule_file=rules.RULES_GOOD_PATH)):
        processor = AppSecSpanProcessor()
        processor.delayed_init()

    assert processor._addresses_to_keep == {
        "grpc.server.request.message",
        "http.client_ip",
        "server.request.body",
        "server.request.cookies",
        "server.request.headers.no_cookies",
        "server.request.path_params",
        "server.request.query",
        "server.response.headers.no_cookies",
        "usr.id",
    }

    processor._update_rules([], CUSTOM_RULE_METHOD)

    assert processor._addresses_to_keep == {
        "grpc.server.request.message",
        "http.client_ip",
        "server.request.body",
        "server.request.cookies",
        "server.request.headers.no_cookies",
        "server.request.method",  # New required address
        "server.request.path_params",
        "server.request.query",
        "server.response.headers.no_cookies",
        "usr.id",
        "usr.login",
    }


@pytest.mark.parametrize(
    "persistent", [key for key, value in WAF_DATA_NAMES if value in WAF_DATA_NAMES.PERSISTENT_ADDRESSES]
)
@pytest.mark.parametrize("ephemeral", ["LFI_ADDRESS", "PROCESSOR_SETTINGS"])
@mock.patch("ddtrace.appsec._ddwaf.DDWaf.run")
def test_ephemeral_addresses(mock_run, persistent, ephemeral):
    from ddtrace.appsec._ddwaf.waf_stubs import DDWaf_result
    from ddtrace.appsec._utils import _observator
    from ddtrace.trace import tracer

    mock_run.return_value = DDWaf_result(0, [], {}, 0.0, 0.0, False, _observator(), {})

    with asm_context(tracer=tracer, config=config_asm, rc_payload=CUSTOM_RULE_METHOD) as span:
        processor = tracer._appsec_processor
        assert processor
        # first call must send all data to the waf
        processor._waf_action(span, None, {persistent: {"key_1": "value_1"}, ephemeral: {"key_2": "value_2"}})
        assert mock_run.call_args[0][1] == {WAF_DATA_NAMES[persistent]: {"key_1": "value_1"}}
        assert mock_run.call_args[1]["ephemeral_data"] == {WAF_DATA_NAMES[ephemeral]: {"key_2": "value_2"}}
        # second call must only send ephemeral data to the waf, not persistent data again
        processor._waf_action(span, None, {persistent: {"key_1": "value_1"}, ephemeral: {"key_2": "value_3"}})
        assert mock_run.call_args[0][1] == {}
        assert mock_run.call_args[1]["ephemeral_data"] == {
            WAF_DATA_NAMES[ephemeral]: {"key_2": "value_3"},
        }
    assert (span._local_root or span).get_tag(APPSEC.RC_PRODUCTS) == "[ASM:1] u:1 r:1"
