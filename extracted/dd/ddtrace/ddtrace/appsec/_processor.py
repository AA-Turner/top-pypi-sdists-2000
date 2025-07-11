import dataclasses
import errno
import json
from json.decoder import JSONDecodeError
import os
import os.path
from typing import TYPE_CHECKING
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Union


if TYPE_CHECKING:
    import ddtrace.appsec._ddwaf as ddwaf


from ddtrace._trace.processor import SpanProcessor
from ddtrace._trace.span import Span
from ddtrace.appsec import _asm_request_context
from ddtrace.appsec._constants import APPSEC
from ddtrace.appsec._constants import DEFAULT
from ddtrace.appsec._constants import EXPLOIT_PREVENTION
from ddtrace.appsec._constants import SPAN_DATA_NAMES
from ddtrace.appsec._constants import STACK_TRACE
from ddtrace.appsec._constants import WAF_ACTIONS
from ddtrace.appsec._constants import WAF_DATA_NAMES
from ddtrace.appsec._exploit_prevention.stack_traces import report_stack
from ddtrace.appsec._trace_utils import _asm_manual_keep
from ddtrace.appsec._utils import Binding_error
from ddtrace.appsec._utils import DDWaf_result
from ddtrace.constants import _ORIGIN_KEY
from ddtrace.constants import _RUNTIME_FAMILY
from ddtrace.internal._unpatched import unpatched_open as open  # noqa: A004
from ddtrace.internal.logger import get_logger
from ddtrace.internal.rate_limiter import RateLimiter
from ddtrace.internal.remoteconfig import PayloadType
from ddtrace.settings.asm import config as asm_config


log = get_logger(__name__)


def _transform_headers(data: Union[Dict[str, str], List[Tuple[str, str]]]) -> Dict[str, Union[str, List[str]]]:
    normalized: Dict[str, Union[str, List[str]]] = {}
    headers = data if isinstance(data, list) else data.items()
    for header, value in headers:
        header = header.lower()
        if header in ("cookie", "set-cookie"):
            continue
        if header in normalized:  # if a header with the same lowercase name already exists, let's make it an array
            existing = normalized[header]
            if isinstance(existing, list):
                existing.append(value)
            else:
                normalized[header] = [existing, value]
        else:
            normalized[header] = value
    return normalized


def get_rules() -> str:
    return asm_config._asm_static_rule_file or DEFAULT.RULES


def _get_rate_limiter() -> RateLimiter:
    return RateLimiter(int(os.getenv("DD_APPSEC_TRACE_RATE_LIMIT", DEFAULT.TRACE_RATE_LIMIT)))


@dataclasses.dataclass(eq=False)
class AppSecSpanProcessor(SpanProcessor):
    rule_filename: str = dataclasses.field(default_factory=get_rules)
    obfuscation_parameter_key_regexp: bytes = dataclasses.field(init=False)
    obfuscation_parameter_value_regexp: bytes = dataclasses.field(init=False)
    _addresses_to_keep: Set[str] = dataclasses.field(default_factory=set)
    _rate_limiter: RateLimiter = dataclasses.field(default_factory=_get_rate_limiter)

    @property
    def enabled(self):
        return self._ddwaf is not None

    def __post_init__(self) -> None:
        from ddtrace.appsec._listeners import load_appsec

        load_appsec()
        self.obfuscation_parameter_key_regexp = asm_config._asm_obfuscation_parameter_key_regexp.encode()
        self.obfuscation_parameter_value_regexp = asm_config._asm_obfuscation_parameter_value_regexp.encode()
        self._rules: Optional[Dict[str, Any]] = None
        try:
            with open(self.rule_filename, "r") as f:
                self._rules = json.load(f)
        except EnvironmentError as err:
            if err.errno == errno.ENOENT:
                log.error(
                    "[DDAS-0001-03] ASM could not read the rule file %s. Reason: file does not exist",
                    self.rule_filename,
                )
            else:
                # TODO: try to log reasons
                log.error("[DDAS-0001-03] ASM could not read the rule file %s.", self.rule_filename)
            raise
        except JSONDecodeError:
            log.error(
                "[DDAS-0001-03] ASM could not read the rule file %s. Reason: invalid JSON file", self.rule_filename
            )
            raise
        except Exception:
            # TODO: try to log reasons
            log.error("[DDAS-0001-03] ASM could not read the rule file %s.", self.rule_filename)
            raise

    def delayed_init(self) -> None:
        try:
            if self._rules is not None and not hasattr(self, "_ddwaf"):
                from ddtrace.appsec._ddwaf import DDWaf  # noqa: E402
                import ddtrace.appsec._metrics as metrics  # noqa: E402

                self.metrics = metrics
                self._ddwaf = DDWaf(
                    self._rules, self.obfuscation_parameter_key_regexp, self.obfuscation_parameter_value_regexp, metrics
                )
                self.metrics._set_waf_init_metric(self._ddwaf.info, self._ddwaf.initialized)
        except Exception:
            # Partial of DDAS-0005-00
            log.warning("[DDAS-0005-00] WAF initialization failed", exc_info=True)

        self._update_required()

    def _update_required(self):
        self._addresses_to_keep.clear()
        for address in self._ddwaf.required_data:
            self._addresses_to_keep.add(address)
        # we always need the request headers
        self._addresses_to_keep.add(WAF_DATA_NAMES.REQUEST_HEADERS_NO_COOKIES)
        # we always need the response headers
        self._addresses_to_keep.add(WAF_DATA_NAMES.RESPONSE_HEADERS_NO_COOKIES)

    def _update_rules(
        self, removals: Sequence[Tuple[str, str]], updates: Sequence[Tuple[str, str, PayloadType]]
    ) -> bool:
        if not hasattr(self, "_ddwaf"):
            self.delayed_init()
        result = False
        if asm_config._asm_static_rule_file is not None:
            return result
        result = self._ddwaf.update_rules(removals, updates)
        self.metrics._set_waf_updates_metric(self._ddwaf.info, result)
        self._update_required()
        return result

    @property
    def rasp_lfi_enabled(self) -> bool:
        return WAF_DATA_NAMES.LFI_ADDRESS in self._addresses_to_keep

    @property
    def rasp_shi_enabled(self) -> bool:
        return WAF_DATA_NAMES.SHI_ADDRESS in self._addresses_to_keep

    @property
    def rasp_cmdi_enabled(self) -> bool:
        return WAF_DATA_NAMES.CMDI_ADDRESS in self._addresses_to_keep

    @property
    def rasp_ssrf_enabled(self) -> bool:
        return WAF_DATA_NAMES.SSRF_ADDRESS in self._addresses_to_keep

    @property
    def rasp_sqli_enabled(self) -> bool:
        return WAF_DATA_NAMES.SQLI_ADDRESS in self._addresses_to_keep

    def on_span_start(self, span: Span) -> None:
        from ddtrace.contrib.internal import trace_utils

        if not hasattr(self, "_ddwaf"):
            self.delayed_init()

        if span.span_type not in asm_config._asm_processed_span_types:
            return

        ctx = self._ddwaf._at_request_start()
        _asm_request_context.start_context(span, ctx.rc_products if ctx is not None else "")
        peer_ip = _asm_request_context.get_ip()
        headers = _asm_request_context.get_headers()
        headers_case_sensitive = _asm_request_context.get_headers_case_sensitive()
        root_span = span._local_root or span

        root_span.set_metric(APPSEC.ENABLED, 1.0)
        root_span.set_tag_str(_RUNTIME_FAMILY, "python")

        def waf_callable(custom_data=None, **kwargs):
            return self._waf_action(root_span, ctx, custom_data, **kwargs)

        _asm_request_context.set_waf_callback(waf_callable)
        _asm_request_context.add_context_callback(self.metrics._set_waf_request_metrics)
        if headers is not None:
            _asm_request_context.set_waf_address(SPAN_DATA_NAMES.REQUEST_HEADERS_NO_COOKIES, headers)
            _asm_request_context.set_waf_address(
                SPAN_DATA_NAMES.REQUEST_HEADERS_NO_COOKIES_CASE, headers_case_sensitive
            )
            if not peer_ip:
                return

            ip = trace_utils._get_request_header_client_ip(headers, peer_ip, headers_case_sensitive)
            # Save the IP and headers in the context so the retrieval can be skipped later
            _asm_request_context.set_waf_address(SPAN_DATA_NAMES.REQUEST_HTTP_IP, ip)
            if ip and self._is_needed(WAF_DATA_NAMES.REQUEST_HTTP_IP):
                log.debug("[DDAS-001-00] Executing ASM WAF for checking IP block")
                _asm_request_context.call_waf_callback({"REQUEST_HTTP_IP": None})

    def _waf_action(
        self,
        span: Span,
        ctx: "ddwaf.ddwaf_types.ddwaf_context_capsule",
        custom_data: Optional[Dict[str, Any]] = None,
        crop_trace: Optional[str] = None,
        rule_type: Optional[str] = None,
        force_sent: bool = False,
    ) -> Optional[DDWaf_result]:
        """
        Call the `WAF` with the given parameters. If `custom_data_names` is specified as
        a list of `(WAF_NAME, WAF_STR)` tuples specifying what values of the `WAF_DATA_NAMES`
        constant class will be checked. Else, it will check all the possible values
        from `WAF_DATA_NAMES`.

        If `custom_data_values` is specified, it must be a dictionary where the key is the
        `WAF_DATA_NAMES` key and the value the custom value. If not used, the values will
        be retrieved from the `core`. This can be used when you don't want to store
        the value in the `core` before checking the `WAF`.
        """
        if _asm_request_context.get_blocked():
            # We still must run the waf if we need to extract schemas for API SECURITY
            if not custom_data or not custom_data.get("PROCESSOR_SETTINGS", {}).get("extract-schema", False):
                return None

        data = {}
        ephemeral_data = {}
        iter_data = [(key, WAF_DATA_NAMES[key]) for key in custom_data] if custom_data is not None else WAF_DATA_NAMES
        data_already_sent = _asm_request_context.get_data_sent()
        if data_already_sent is None:
            data_already_sent = set()

        # persistent addresses must be sent if api security is used
        force_keys = custom_data.get("PROCESSOR_SETTINGS", {}).get("extract-schema", False) if custom_data else False

        for key, waf_name in iter_data:
            if key in data_already_sent and not force_sent:
                continue
            # ensure ephemeral addresses are sent, event when value is None
            if waf_name not in WAF_DATA_NAMES.PERSISTENT_ADDRESSES and custom_data:
                if key in custom_data:
                    ephemeral_data[waf_name] = custom_data[key]

            elif self._is_needed(waf_name) or force_keys:
                value = None
                if custom_data is not None and custom_data.get(key) is not None:
                    value = custom_data.get(key)
                elif key in SPAN_DATA_NAMES:
                    value = _asm_request_context.get_value("waf_addresses", SPAN_DATA_NAMES[key])
                # if value is a callable, it's a lazy value for api security that should not be sent now
                if value is not None and not hasattr(value, "__call__"):
                    data[waf_name] = _transform_headers(value) if key.endswith("HEADERS_NO_COOKIES") else value
                    if waf_name in WAF_DATA_NAMES.PERSISTENT_ADDRESSES:
                        data_already_sent.add(key)
                    log.debug("[action] WAF got value %s", SPAN_DATA_NAMES.get(key, key))

        # small optimization to avoid running the waf if there is no data to check
        if not data and not ephemeral_data:
            return None

        try:
            waf_results = self._ddwaf.run(
                ctx, data, ephemeral_data=ephemeral_data or None, timeout_ms=asm_config._waf_timeout
            )
        except Exception:
            log.debug("appsec::processor::waf::run", exc_info=True)
            waf_results = Binding_error

        _asm_request_context.set_waf_info(lambda: self._ddwaf.info)
        root_span = span._local_root or span
        if waf_results.return_code < 0:
            error_tag = APPSEC.RASP_ERROR if rule_type else APPSEC.WAF_ERROR
            previous = root_span.get_tag(error_tag)
            if previous is None:
                root_span.set_tag_str(error_tag, str(waf_results.return_code))
            else:
                try:
                    int_previous = int(previous)
                except ValueError:
                    int_previous = -128
                root_span.set_tag_str(error_tag, str(max(int_previous, waf_results.return_code)))

        blocked = {}
        for action, parameters in waf_results.actions.items():
            if action == WAF_ACTIONS.BLOCK_ACTION:
                blocked = parameters
            elif action == WAF_ACTIONS.REDIRECT_ACTION:
                blocked = parameters
                blocked[WAF_ACTIONS.TYPE] = "none"
            elif action == WAF_ACTIONS.STACK_ACTION:
                stack_trace_id = parameters["stack_id"]
                report_stack("exploit detected", span, crop_trace, stack_id=stack_trace_id, namespace=STACK_TRACE.RASP)
                for rule in waf_results.data:
                    rule[EXPLOIT_PREVENTION.STACK_TRACE_ID] = stack_trace_id

        # Trace tagging
        for key, value in waf_results.meta_tags.items():
            root_span.set_tag_str(key, value)
        for key, value in waf_results.metrics.items():
            root_span.set_metric(key, value)

        if waf_results.data:
            log.debug("[DDAS-011-00] ASM In-App WAF returned: %s. Timeout %s", waf_results.data, waf_results.timeout)

        if blocked:
            _asm_request_context.set_blocked(blocked)

        allowed = True
        if waf_results.keep:
            allowed = self._rate_limiter.is_allowed()

        _asm_request_context.set_waf_telemetry_results(
            self._ddwaf.info.version,
            bool(blocked),
            waf_results,
            rule_type,
            not allowed,
        )

        if waf_results.data:
            _asm_request_context.store_waf_results_data(waf_results.data)
            if blocked:
                span.set_tag(APPSEC.BLOCKED, "true")

            # Partial DDAS-011-00
            span.set_tag_str(APPSEC.EVENT, "true")

            remote_ip = _asm_request_context.get_waf_address(SPAN_DATA_NAMES.REQUEST_HTTP_IP)
            if remote_ip:
                # Note that if the ip collection is disabled by the env var
                # DD_TRACE_CLIENT_IP_HEADER_DISABLED actor.ip won't be sent
                span.set_tag_str("actor.ip", remote_ip)

            # Right now, we overwrite any value that could be already there. We need to reconsider when ASM/AppSec's
            # specs are updated.
            if span.get_tag(_ORIGIN_KEY) is None:
                span.set_tag_str(_ORIGIN_KEY, APPSEC.ORIGIN_VALUE)

        if waf_results.keep and allowed:
            _asm_manual_keep(span)

        return waf_results

    def _is_needed(self, address: str) -> bool:
        return address in self._addresses_to_keep

    def on_span_finish(self, span: Span) -> None:
        if span.span_type in asm_config._asm_processed_span_types:
            _asm_request_context.call_waf_callback_no_instrumentation()
            self._ddwaf._at_request_end()
            _asm_request_context.end_context(span)
