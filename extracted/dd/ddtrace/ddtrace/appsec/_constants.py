# this module must not load any other unsafe appsec module directly

from _io import BytesIO
from _io import StringIO
import os
from re import Match
from typing import Any
from typing import Iterator
from typing import Literal  # noqa:F401
from typing import Tuple

from ddtrace.internal.constants import HTTP_REQUEST_BLOCKED
from ddtrace.internal.constants import REQUEST_PATH_PARAMS
from ddtrace.internal.constants import RESPONSE_HEADERS
from ddtrace.internal.constants import STATUS_403_TYPE_AUTO


class Constant_Class(type):
    """
    metaclass for Constant Classes
    - You can access constants with APPSEC.ENV or APPSEC["ENV"]
    - Direct assignment will fail: APPSEC.ENV = "something" raise TypeError, like other immutable types
    - Constant Classes can be iterated:
        for constant_name, constant_value in APPSEC: ...
    """

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise TypeError("Constant class does not support item assignment: %s.%s" % (self.__name__, __name))

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        def aux():
            for t in self.__dict__.items():
                if not t[0].startswith("_"):
                    yield t

        return aux()

    def get(self, k: str, default: Any = None) -> Any:
        return self.__dict__.get(k, default)

    def __contains__(self, k: str) -> bool:
        return k in self.__dict__

    def __getitem__(self, k: str) -> Any:
        return self.__dict__[k]


class APPSEC(metaclass=Constant_Class):
    """Specific constants for AppSec"""

    ENV: Literal["DD_APPSEC_ENABLED"] = "DD_APPSEC_ENABLED"
    APM_TRACING_ENV: Literal["DD_APM_TRACING_ENABLED"] = "DD_APM_TRACING_ENABLED"
    RULE_FILE: Literal["DD_APPSEC_RULES"] = "DD_APPSEC_RULES"
    ENABLED: Literal["_dd.appsec.enabled"] = "_dd.appsec.enabled"
    JSON: Literal["_dd.appsec.json"] = "_dd.appsec.json"
    STRUCT: Literal["appsec"] = "appsec"
    EVENT_RULE_VERSION: Literal["_dd.appsec.event_rules.version"] = "_dd.appsec.event_rules.version"
    EVENT_RULE_ERRORS: Literal["_dd.appsec.event_rules.errors"] = "_dd.appsec.event_rules.errors"
    EVENT_RULE_LOADED: Literal["_dd.appsec.event_rules.loaded"] = "_dd.appsec.event_rules.loaded"
    EVENT_RULE_ERROR_COUNT: Literal["_dd.appsec.event_rules.error_count"] = "_dd.appsec.event_rules.error_count"
    WAF_DURATION: Literal["_dd.appsec.waf.duration"] = "_dd.appsec.waf.duration"
    WAF_DURATION_EXT: Literal["_dd.appsec.waf.duration_ext"] = "_dd.appsec.waf.duration_ext"
    WAF_TIMEOUTS: Literal["_dd.appsec.waf.timeouts"] = "_dd.appsec.waf.timeouts"
    WAF_VERSION: Literal["_dd.appsec.waf.version"] = "_dd.appsec.waf.version"
    RASP_DURATION: Literal["_dd.appsec.rasp.duration"] = "_dd.appsec.rasp.duration"
    RASP_DURATION_EXT: Literal["_dd.appsec.rasp.duration_ext"] = "_dd.appsec.rasp.duration_ext"
    RASP_RULE_EVAL: Literal["_dd.appsec.rasp.rule.eval"] = "_dd.appsec.rasp.rule.eval"
    RASP_TIMEOUTS: Literal["_dd.appsec.rasp.timeout"] = "_dd.appsec.rasp.timeout"
    RC_PRODUCTS: Literal["_dd.appsec.rc_products"] = "_dd.appsec.rc_products"
    TRUNCATION_STRING_LENGTH: Literal["_dd.appsec.truncated.string_length"] = "_dd.appsec.truncated.string_length"
    TRUNCATION_CONTAINER_SIZE: Literal["_dd.appsec.truncated.container_size"] = "_dd.appsec.truncated.container_size"
    TRUNCATION_CONTAINER_DEPTH: Literal["_dd.appsec.truncated.container_depth"] = "_dd.appsec.truncated.container_depth"
    ORIGIN_VALUE: Literal["appsec"] = "appsec"
    CUSTOM_EVENT_PREFIX: Literal["appsec.events"] = "appsec.events"
    USER_LOGIN_EVENT_PREFIX: Literal["_dd.appsec.events.users.login"] = "_dd.appsec.events.users.login"
    USER_LOGIN_EVENT_PREFIX_PUBLIC: Literal["appsec.events.users.login"] = "appsec.events.users.login"
    USER_LOGIN_USERID: Literal["_dd.appsec.usr.id"] = "_dd.appsec.usr.id"
    USER_LOGIN_USERNAME: Literal["_dd.appsec.usr.login"] = "_dd.appsec.usr.login"
    USER_LOGIN_EVENT_SUCCESS_TRACK: Literal[
        "appsec.events.users.login.success.track"
    ] = "appsec.events.users.login.success.track"
    USER_LOGIN_EVENT_FAILURE_TRACK: Literal[
        "appsec.events.users.login.failure.track"
    ] = "appsec.events.users.login.failure.track"
    USER_SIGNUP_EVENT: Literal["appsec.events.users.signup.track"] = "appsec.events.users.signup.track"
    USER_SIGNUP_EVENT_USERNAME: Literal["appsec.events.users.signup.usr.login"] = "appsec.events.users.signup.usr.login"
    USER_SIGNUP_EVENT_USERID: Literal["appsec.events.users.signup.usr.id"] = "appsec.events.users.signup.usr.id"
    USER_SIGNUP_EVENT_MODE: Literal[
        "_dd.appsec.events.users.signup.auto.mode"
    ] = "_dd.appsec.events.users.signup.auto.mode"
    AUTO_LOGIN_EVENTS_SUCCESS_MODE: Literal[
        "_dd.appsec.events.users.login.success.auto.mode"
    ] = "_dd.appsec.events.users.login.success.auto.mode"
    AUTO_LOGIN_EVENTS_FAILURE_MODE: Literal[
        "_dd.appsec.events.users.login.failure.auto.mode"
    ] = "_dd.appsec.events.users.login.failure.auto.mode"
    AUTO_LOGIN_EVENTS_COLLECTION_MODE: Literal["_dd.appsec.user.collection_mode"] = "_dd.appsec.user.collection_mode"
    BLOCKED: Literal["appsec.blocked"] = "appsec.blocked"
    EVENT: Literal["appsec.event"] = "appsec.event"
    AUTO_USER_INSTRUMENTATION_MODE: Literal[
        "DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE"
    ] = "DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE"
    AUTO_USER_INSTRUMENTATION_MODE_ENABLED: Literal[
        "DD_APPSEC_AUTOMATED_USER_EVENTS_TRACKING_ENABLED"
    ] = "DD_APPSEC_AUTOMATED_USER_EVENTS_TRACKING_ENABLED"
    USER_MODEL_LOGIN_FIELD: Literal["DD_USER_MODEL_LOGIN_FIELD"] = "DD_USER_MODEL_LOGIN_FIELD"
    USER_MODEL_EMAIL_FIELD: Literal["DD_USER_MODEL_EMAIL_FIELD"] = "DD_USER_MODEL_EMAIL_FIELD"
    USER_MODEL_NAME_FIELD: Literal["DD_USER_MODEL_NAME_FIELD"] = "DD_USER_MODEL_NAME_FIELD"
    PROPAGATION_HEADER: Literal["_dd.p.ts"] = "_dd.p.ts"
    OBFUSCATION_PARAMETER_KEY_REGEXP: Literal[
        "DD_APPSEC_OBFUSCATION_PARAMETER_KEY_REGEXP"
    ] = "DD_APPSEC_OBFUSCATION_PARAMETER_KEY_REGEXP"
    OBFUSCATION_PARAMETER_VALUE_REGEXP: Literal[
        "DD_APPSEC_OBFUSCATION_PARAMETER_VALUE_REGEXP"
    ] = "DD_APPSEC_OBFUSCATION_PARAMETER_VALUE_REGEXP"
    RC_CLIENT_ID: Literal["_dd.rc.client_id"] = "_dd.rc.client_id"
    WAF_ERROR: Literal["_dd.appsec.waf.error"] = "_dd.appsec.waf.error"
    RASP_ERROR: Literal["_dd.appsec.rasp.error"] = "_dd.appsec.rasp.error"
    ERROR_TYPE: Literal["_dd.appsec.error.type"] = "_dd.appsec.error.type"
    ERROR_MESSAGE: Literal["_dd.appsec.error.message"] = "_dd.appsec.error.message"


TELEMETRY_OFF_NAME = "OFF"
TELEMETRY_DEBUG_NAME = "DEBUG"
TELEMETRY_MANDATORY_NAME = "MANDATORY"
TELEMETRY_INFORMATION_NAME = "INFORMATION"

TELEMETRY_DEBUG_VERBOSITY = 10
TELEMETRY_INFORMATION_VERBOSITY = 20
TELEMETRY_MANDATORY_VERBOSITY = 30
TELEMETRY_OFF_VERBOSITY = 40


class IAST(metaclass=Constant_Class):
    """Specific constants for IAST"""

    ENV: Literal["DD_IAST_ENABLED"] = "DD_IAST_ENABLED"
    ENV_DEBUG: Literal["DD_IAST_DEBUG"] = "DD_IAST_DEBUG"
    ENV_PROPAGATION_DEBUG: Literal["DD_IAST_PROPAGATION_DEBUG"] = "DD_IAST_PROPAGATION_DEBUG"
    ENV_REQUEST_SAMPLING: Literal["DD_IAST_REQUEST_SAMPLING"] = "DD_IAST_REQUEST_SAMPLING"
    DD_IAST_VULNERABILITIES_PER_REQUEST: Literal[
        "DD_IAST_VULNERABILITIES_PER_REQUEST"
    ] = "DD_IAST_VULNERABILITIES_PER_REQUEST"
    DD_IAST_MAX_CONCURRENT_REQUESTS: Literal["DD_IAST_MAX_CONCURRENT_REQUESTS"] = "DD_IAST_MAX_CONCURRENT_REQUESTS"
    ENV_TELEMETRY_REPORT_LVL: Literal["DD_IAST_TELEMETRY_VERBOSITY"] = "DD_IAST_TELEMETRY_VERBOSITY"
    LAZY_TAINT: Literal["_DD_IAST_LAZY_TAINT"] = "_DD_IAST_LAZY_TAINT"
    JSON: Literal["_dd.iast.json"] = "_dd.iast.json"
    ENABLED: Literal["_dd.iast.enabled"] = "_dd.iast.enabled"
    PATCH_MODULES: Literal["_DD_IAST_PATCH_MODULES"] = "_DD_IAST_PATCH_MODULES"
    ENV_NO_DIR_PATCH: Literal["_DD_IAST_NO_DIR_PATCH"] = "_DD_IAST_NO_DIR_PATCH"
    DENY_MODULES: Literal["_DD_IAST_DENY_MODULES"] = "_DD_IAST_DENY_MODULES"
    SEP_MODULES: Literal[","] = ","
    PATCH_ADDED_SYMBOL_PREFIX: Literal["_ddtrace_"] = "_ddtrace_"
    REDACTION_ENABLED: Literal["DD_IAST_REDACTION_ENABLED"] = "DD_IAST_REDACTION_ENABLED"
    REDACTION_NAME_PATTERN: Literal["DD_IAST_REDACTION_NAME_PATTERN"] = "DD_IAST_REDACTION_NAME_PATTERN"
    REDACTION_VALUE_PATTERN: Literal["DD_IAST_REDACTION_VALUE_PATTERN"] = "DD_IAST_REDACTION_VALUE_PATTERN"
    REDACTION_VALUE_NUMERAL: Literal["DD_IAST_REDACTION_VALUE_NUMERAL"] = "DD_IAST_REDACTION_VALUE_NUMERAL"
    STACK_TRACE_ENABLED: Literal["DD_IAST_STACK_TRACE_ENABLED"] = "DD_IAST_STACK_TRACE_ENABLED"

    METRICS_REPORT_LVLS = (
        (TELEMETRY_DEBUG_VERBOSITY, TELEMETRY_DEBUG_NAME),
        (TELEMETRY_INFORMATION_VERBOSITY, TELEMETRY_INFORMATION_NAME),
        (TELEMETRY_MANDATORY_VERBOSITY, TELEMETRY_MANDATORY_NAME),
        (TELEMETRY_OFF_VERBOSITY, TELEMETRY_OFF_NAME),
    )

    TEXT_TYPES = (str, bytes, bytearray)
    TAINTEABLE_TYPES = (str, bytes, bytearray, Match, BytesIO, StringIO)
    REQUEST_CONTEXT_KEY: Literal["_iast_env"] = "_iast_env"


class IAST_SPAN_TAGS(metaclass=Constant_Class):
    """Specific constants for IAST span tags"""

    TELEMETRY_REQUEST_TAINTED: Literal["_dd.iast.telemetry.request.tainted"] = "_dd.iast.telemetry.request.tainted"
    TELEMETRY_EXECUTED_SINK: Literal["_dd.iast.telemetry.executed.sink"] = "_dd.iast.telemetry.executed.sink"
    TELEMETRY_EXECUTED_SOURCE: Literal["_dd.iast.telemetry.executed.source"] = "_dd.iast.telemetry.executed.source"


class WAF_DATA_NAMES(metaclass=Constant_Class):
    """string names used by the waf library for requesting data from requests"""

    # PERSISTENT ADDRESSES
    REQUEST_BODY: Literal["server.request.body"] = "server.request.body"
    REQUEST_QUERY: Literal["server.request.query"] = "server.request.query"
    REQUEST_HEADERS_NO_COOKIES: Literal["server.request.headers.no_cookies"] = "server.request.headers.no_cookies"
    REQUEST_URI_RAW: Literal["server.request.uri.raw"] = "server.request.uri.raw"
    REQUEST_METHOD: Literal["server.request.method"] = "server.request.method"
    REQUEST_PATH_PARAMS: Literal["server.request.path_params"] = "server.request.path_params"
    REQUEST_COOKIES: Literal["server.request.cookies"] = "server.request.cookies"
    REQUEST_HTTP_IP: Literal["http.client_ip"] = "http.client_ip"
    REQUEST_USER_ID: Literal["usr.id"] = "usr.id"
    REQUEST_USERNAME: Literal["usr.login"] = "usr.login"
    REQUEST_SESSION_ID: Literal["usr.session_id"] = "usr.session_id"
    RESPONSE_STATUS: Literal["server.response.status"] = "server.response.status"
    RESPONSE_HEADERS_NO_COOKIES: Literal["server.response.headers.no_cookies"] = "server.response.headers.no_cookies"
    RESPONSE_BODY: Literal["server.response.body"] = "server.response.body"
    PERSISTENT_ADDRESSES = frozenset(
        (
            REQUEST_BODY,
            REQUEST_QUERY,
            REQUEST_HEADERS_NO_COOKIES,
            REQUEST_URI_RAW,
            REQUEST_METHOD,
            REQUEST_PATH_PARAMS,
            REQUEST_COOKIES,
            REQUEST_HTTP_IP,
            REQUEST_USER_ID,
            REQUEST_USERNAME,
            REQUEST_SESSION_ID,
            RESPONSE_STATUS,
            RESPONSE_HEADERS_NO_COOKIES,
            RESPONSE_BODY,
        )
    )

    # EPHEMERAL ADDRESSES
    PROCESSOR_SETTINGS: Literal["waf.context.processor"] = "waf.context.processor"
    CMDI_ADDRESS: Literal["server.sys.exec.cmd"] = "server.sys.exec.cmd"
    SHI_ADDRESS: Literal["server.sys.shell.cmd"] = "server.sys.shell.cmd"
    LFI_ADDRESS: Literal["server.io.fs.file"] = "server.io.fs.file"
    SSRF_ADDRESS: Literal["server.io.net.url"] = "server.io.net.url"
    SQLI_ADDRESS: Literal["server.db.statement"] = "server.db.statement"
    SQLI_SYSTEM_ADDRESS: Literal["server.db.system"] = "server.db.system"
    LOGIN_FAILURE: Literal["server.business_logic.users.login.failure"] = "server.business_logic.users.login.failure"
    LOGIN_SUCCESS: Literal["server.business_logic.users.login.success"] = "server.business_logic.users.login.success"


class SPAN_DATA_NAMES(metaclass=Constant_Class):
    """string names used by the library for tagging data from requests in context or span"""

    REQUEST_BODY: Literal["http.request.body"] = "http.request.body"
    REQUEST_QUERY: Literal["http.request.query"] = "http.request.query"
    REQUEST_HEADERS_NO_COOKIES: Literal["http.request.headers"] = "http.request.headers"
    REQUEST_HEADERS_NO_COOKIES_CASE: Literal[
        "http.request.headers_case_sensitive"
    ] = "http.request.headers_case_sensitive"
    REQUEST_URI_RAW: Literal["http.request.uri"] = "http.request.uri"
    REQUEST_ROUTE: Literal["http.request.route"] = "http.request.route"
    REQUEST_METHOD: Literal["http.request.method"] = "http.request.method"
    REQUEST_PATH_PARAMS = REQUEST_PATH_PARAMS
    REQUEST_COOKIES: Literal["http.request.cookies"] = "http.request.cookies"
    REQUEST_HTTP_IP: Literal["http.request.remote_ip"] = "http.request.remote_ip"
    REQUEST_USER_ID: Literal["usr.id"] = "usr.id"
    RESPONSE_STATUS: Literal["http.response.status"] = "http.response.status"
    RESPONSE_HEADERS_NO_COOKIES = RESPONSE_HEADERS
    RESPONSE_BODY: Literal["http.response.body"] = "http.response.body"
    GRPC_SERVER_REQUEST_MESSAGE: Literal["grpc.server.request.message"] = "grpc.server.request.message"
    GRPC_SERVER_RESPONSE_MESSAGE: Literal["grpc.server.response.message"] = "grpc.server.response.message"
    GRPC_SERVER_REQUEST_METADATA: Literal["grpc.server.request.metadata"] = "grpc.server.request.metadata"
    GRPC_SERVER_METHOD: Literal["grpc.server.method"] = "grpc.server.method"


class API_SECURITY(metaclass=Constant_Class):
    """constants related to API Security"""

    ENABLED: Literal["_dd.appsec.api_security.enabled"] = "_dd.appsec.api_security.enabled"
    ENV_VAR_ENABLED: Literal["DD_API_SECURITY_ENABLED"] = "DD_API_SECURITY_ENABLED"
    PARSE_RESPONSE_BODY: Literal["DD_API_SECURITY_PARSE_RESPONSE_BODY"] = "DD_API_SECURITY_PARSE_RESPONSE_BODY"
    REQUEST_HEADERS_NO_COOKIES: Literal["_dd.appsec.s.req.headers"] = "_dd.appsec.s.req.headers"
    REQUEST_COOKIES: Literal["_dd.appsec.s.req.cookies"] = "_dd.appsec.s.req.cookies"
    REQUEST_QUERY: Literal["_dd.appsec.s.req.query"] = "_dd.appsec.s.req.query"
    REQUEST_PATH_PARAMS: Literal["_dd.appsec.s.req.params"] = "_dd.appsec.s.req.params"
    REQUEST_BODY: Literal["_dd.appsec.s.req.body"] = "_dd.appsec.s.req.body"
    RESPONSE_HEADERS_NO_COOKIES: Literal["_dd.appsec.s.res.headers"] = "_dd.appsec.s.res.headers"
    RESPONSE_BODY: Literal["_dd.appsec.s.res.body"] = "_dd.appsec.s.res.body"
    SAMPLE_RATE: Literal["DD_API_SECURITY_REQUEST_SAMPLE_RATE"] = "DD_API_SECURITY_REQUEST_SAMPLE_RATE"
    SAMPLE_DELAY: Literal["DD_API_SECURITY_SAMPLE_DELAY"] = "DD_API_SECURITY_SAMPLE_DELAY"
    MAX_PAYLOAD_SIZE: Literal[0x1000000] = 0x1000000  # 16MB maximum size


class WAF_CONTEXT_NAMES(metaclass=Constant_Class):
    """string names used by the library for tagging data from requests in context"""

    RESULTS: Literal["http.request.waf.results"] = "http.request.waf.results"
    BLOCKED = HTTP_REQUEST_BLOCKED
    CALLBACK: Literal["http.request.waf.callback"] = "http.request.waf.callback"


class WAF_ACTIONS(metaclass=Constant_Class):
    """string identifier for actions returned by the waf"""

    BLOCK: Literal["block"] = "block"
    PARAMETERS: Literal["parameters"] = "parameters"
    TYPE: Literal["type"] = "type"
    ID: Literal["id"] = "id"
    DEFAULT_PARAMETERS = STATUS_403_TYPE_AUTO
    BLOCK_ACTION: Literal["block_request"] = "block_request"
    REDIRECT_ACTION: Literal["redirect_request"] = "redirect_request"
    STACK_ACTION: Literal["generate_stack"] = "generate_stack"
    DEFAULT_ACTIONS = {
        BLOCK: {
            ID: BLOCK,
            TYPE: BLOCK_ACTION,
            PARAMETERS: DEFAULT_PARAMETERS,
        }
    }


class PRODUCTS(metaclass=Constant_Class):
    """string identifier for remote config products"""

    ASM: Literal["ASM"] = "ASM"
    ASM_DATA: Literal["ASM_DATA"] = "ASM_DATA"
    ASM_DD: Literal["ASM_DD"] = "ASM_DD"
    ASM_FEATURES: Literal["ASM_FEATURES"] = "ASM_FEATURES"


class LOGIN_EVENTS_MODE(metaclass=Constant_Class):
    """
    string identifier for the mode of the user login events. Can be:
    DISABLED: automatic login events are disabled. Can still be enabled by Remote Config.
    ANONYMIZATION: automatic login events are enabled but will only store non-PII fields (id, pk uid...)
    EXTENDED: automatic login events are enabled and will store potentially PII fields (username,
    email, ...).
    SDK: manually issued login events using the SDK.
    """

    DISABLED: Literal["disabled"] = "disabled"
    IDENT: Literal["identification"] = "identification"
    ANON: Literal["anonymization"] = "anonymization"
    SDK: Literal["sdk"] = "sdk"
    AUTO: Literal["auto"] = "auto"


class DEFAULT(metaclass=Constant_Class):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    RULES = os.path.join(ROOT_DIR, "rules.json")
    TRACE_RATE_LIMIT = 100
    WAF_TIMEOUT = 5.0  # float (milliseconds)
    APPSEC_OBFUSCATION_PARAMETER_KEY_REGEXP = (
        r"(?i)pass|pw(?:or)?d|secret|(?:api|private|public|access)[_-]?key|token|consumer[_-]?"
        r"(?:id|key|secret)|sign(?:ed|ature)|bearer|authorization|jsessionid|phpsessid|asp\.net[_-]sessionid|sid|jwt"
    )
    APPSEC_OBFUSCATION_PARAMETER_VALUE_REGEXP = (
        r"(?i)(?:p(?:ass)?w(?:or)?d|pass(?:[_-]?phrase)?|secret(?:[_-]?key)?|(?:(?:api|private|public|access)[_-]?)"
        r"key(?:[_-]?id)?|(?:(?:auth|access|id|refresh)[_-]?)?token|consumer[_-]?(?:id|key|secret)|sign(?:ed|ature)?"
        r"|auth(?:entication|orization)?|jsessionid|phpsessid|asp\.net(?:[_-]|-)sessionid|sid|jwt)"
        r'(?:\s*=([^;&]+)|"\s*:\s*("[^"]+"|\d+))|bearer\s+([a-z0-9\._\-]+)|token\s*:\s*([a-z0-9]{13})|gh[opsu]_([0-9a-zA-Z]{36})'
        r"|ey[I-L][\w=-]+\.(ey[I-L][\w=-]+(?:\.[\w.+\/=-]+)?)|[\-]{5}BEGIN[a-z\s]+PRIVATE\sKEY[\-]{5}([^\-]+)[\-]"
        r"{5}END[a-z\s]+PRIVATE\sKEY|ssh-rsa\s*([a-z0-9\/\.+]{100,})"
    )


class EXPLOIT_PREVENTION(metaclass=Constant_Class):
    BLOCKING: Literal["exploit_prevention"] = "exploit_prevention"
    STACK_TRACE_ID: Literal["stack_id"] = "stack_id"
    EP_ENABLED: Literal["DD_APPSEC_RASP_ENABLED"] = "DD_APPSEC_RASP_ENABLED"
    STACK_TRACE_ENABLED: Literal["DD_APPSEC_STACK_TRACE_ENABLED"] = "DD_APPSEC_STACK_TRACE_ENABLED"
    MAX_STACK_TRACES: Literal["DD_APPSEC_MAX_STACK_TRACES"] = "DD_APPSEC_MAX_STACK_TRACES"
    MAX_STACK_TRACE_DEPTH: Literal["DD_APPSEC_MAX_STACK_TRACE_DEPTH"] = "DD_APPSEC_MAX_STACK_TRACE_DEPTH"
    STACK_TOP_PERCENT: Literal[
        "DD_APPSEC_MAX_STACK_TRACE_DEPTH_TOP_PERCENT"
    ] = "DD_APPSEC_MAX_STACK_TRACE_DEPTH_TOP_PERCENT"

    class TYPE(metaclass=Constant_Class):
        CMDI: Literal["command_injection"] = "command_injection"
        SHI: Literal["shell_injection"] = "shell_injection"
        LFI: Literal["lfi"] = "lfi"
        SSRF: Literal["ssrf"] = "ssrf"
        SQLI: Literal["sql_injection"] = "sql_injection"

    class ADDRESS(metaclass=Constant_Class):
        CMDI: Literal["CMDI_ADDRESS"] = "CMDI_ADDRESS"
        LFI: Literal["LFI_ADDRESS"] = "LFI_ADDRESS"
        SHI: Literal["SHI_ADDRESS"] = "SHI_ADDRESS"
        SSRF: Literal["SSRF_ADDRESS"] = "SSRF_ADDRESS"
        SQLI: Literal["SQLI_ADDRESS"] = "SQLI_ADDRESS"
        SQLI_TYPE: Literal["SQLI_SYSTEM_ADDRESS"] = "SQLI_SYSTEM_ADDRESS"


class FINGERPRINTING(metaclass=Constant_Class):
    PREFIX = "_dd.appsec.fp."
    ENDPOINT = PREFIX + "http.endpoint"
    HEADER = PREFIX + "http.header"
    NETWORK = PREFIX + "http.network"
    SESSION = PREFIX + "session"


class STACK_TRACE(metaclass=Constant_Class):
    RASP = "exploit"
    IAST = "vulnerability"
    TAG: Literal["_dd.stack"] = "_dd.stack"
