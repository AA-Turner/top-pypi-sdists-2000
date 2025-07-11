import inspect
from typing import Text

from ddtrace.appsec._constants import IAST
from ddtrace.appsec._constants import IAST_SPAN_TAGS
from ddtrace.appsec._iast._logs import iast_error
from ddtrace.appsec._iast._metrics import _set_metric_iast_executed_sink
from ddtrace.appsec._iast._metrics import _set_metric_iast_instrumented_sink
from ddtrace.appsec._iast._patch_modules import WrapFunctonsForIAST
from ddtrace.appsec._iast._span_metrics import increment_iast_span_metric
from ddtrace.appsec._iast._taint_tracking import VulnerabilityType
from ddtrace.appsec._iast.constants import VULN_CODE_INJECTION
from ddtrace.appsec._iast.taint_sinks._base import VulnerabilityBase
from ddtrace.appsec._iast.taint_sinks.utils import patch_once
from ddtrace.internal.logger import get_logger
from ddtrace.settings.asm import config as asm_config


log = get_logger(__name__)


def get_version() -> Text:
    return ""


@patch_once
def patch():
    iast_funcs = WrapFunctonsForIAST()

    iast_funcs.wrap_function("builtins", "eval", _iast_coi)

    # TODO: wrap exec functions is very dangerous because it needs and modifies locals and globals from the original
    #  function
    # iast_funcs.wrap_function("builtins", "exec", _iast_coi)

    iast_funcs.patch()

    _set_metric_iast_instrumented_sink(VULN_CODE_INJECTION)


class CodeInjection(VulnerabilityBase):
    vulnerability_type = VULN_CODE_INJECTION
    secure_mark = VulnerabilityType.CODE_INJECTION


def _iast_coi(wrapped, instance, args, kwargs):
    if len(args) >= 1:
        _iast_report_code_injection(args[0])

    caller_frame = None
    if len(args) > 1:
        func_globals = args[1]
    elif kwargs.get("globals"):
        func_globals = kwargs.get("globals")
    else:
        frames = inspect.currentframe()
        caller_frame = frames.f_back
        func_globals = caller_frame.f_globals

    if len(args) > 2:
        func_locals = args[2]
    elif kwargs.get("locals"):
        func_locals = kwargs.get("locals")
    else:
        if caller_frame is None:
            frames = inspect.currentframe()
            caller_frame = frames.f_back
        func_locals = caller_frame.f_locals

    return wrapped(args[0], func_globals, func_locals)


def _iast_report_code_injection(code_string: Text):
    reported = False
    try:
        if asm_config.is_iast_request_enabled:
            if code_string and isinstance(code_string, IAST.TEXT_TYPES) and CodeInjection.has_quota():
                if CodeInjection.is_tainted_pyobject(code_string):
                    CodeInjection.report(evidence_value=code_string)

            # Reports Span Metrics
            increment_iast_span_metric(IAST_SPAN_TAGS.TELEMETRY_EXECUTED_SINK, CodeInjection.vulnerability_type)
            # Report Telemetry Metrics
            _set_metric_iast_executed_sink(CodeInjection.vulnerability_type)
    except Exception as e:
        iast_error(f"propagation::sink_point::Error in _iast_report_code_injection. {e}")
    return reported
