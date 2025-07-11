import os
from pathlib import Path
import re
import typing as t

from _pytest.runner import runtestprotocol
import pytest

from ddtrace import DDTraceDeprecationWarning
from ddtrace import config as dd_config
from ddtrace.contrib.internal.coverage.constants import PCT_COVERED_KEY
from ddtrace.contrib.internal.coverage.data import _coverage_data
from ddtrace.contrib.internal.coverage.patch import patch as patch_coverage
from ddtrace.contrib.internal.coverage.patch import run_coverage_report
from ddtrace.contrib.internal.coverage.utils import _is_coverage_invoked_by_coverage_run
from ddtrace.contrib.internal.coverage.utils import _is_coverage_patched
from ddtrace.contrib.internal.pytest._benchmark_utils import _set_benchmark_data_from_item
from ddtrace.contrib.internal.pytest._plugin_v1 import _is_pytest_cov_enabled
from ddtrace.contrib.internal.pytest._report_links import print_test_report_links
from ddtrace.contrib.internal.pytest._types import _pytest_report_teststatus_return_type
from ddtrace.contrib.internal.pytest._types import pytest_CallInfo
from ddtrace.contrib.internal.pytest._types import pytest_Config
from ddtrace.contrib.internal.pytest._types import pytest_TestReport
from ddtrace.contrib.internal.pytest._utils import PYTEST_STATUS
from ddtrace.contrib.internal.pytest._utils import TestPhase
from ddtrace.contrib.internal.pytest._utils import _get_module_path_from_item
from ddtrace.contrib.internal.pytest._utils import _get_names_from_item
from ddtrace.contrib.internal.pytest._utils import _get_session_command
from ddtrace.contrib.internal.pytest._utils import _get_source_file_info
from ddtrace.contrib.internal.pytest._utils import _get_test_id_from_item
from ddtrace.contrib.internal.pytest._utils import _get_test_parameters_json
from ddtrace.contrib.internal.pytest._utils import _is_enabled_early
from ddtrace.contrib.internal.pytest._utils import _is_test_unskippable
from ddtrace.contrib.internal.pytest._utils import _pytest_marked_to_skip
from ddtrace.contrib.internal.pytest._utils import _pytest_version_supports_atr
from ddtrace.contrib.internal.pytest._utils import _pytest_version_supports_attempt_to_fix
from ddtrace.contrib.internal.pytest._utils import _pytest_version_supports_efd
from ddtrace.contrib.internal.pytest._utils import _pytest_version_supports_itr
from ddtrace.contrib.internal.pytest._utils import _pytest_version_supports_retries
from ddtrace.contrib.internal.pytest._utils import _TestOutcome
from ddtrace.contrib.internal.pytest._utils import excinfo_by_report
from ddtrace.contrib.internal.pytest._utils import reports_by_item
from ddtrace.contrib.internal.pytest.constants import FRAMEWORK
from ddtrace.contrib.internal.pytest.constants import USER_PROPERTY_QUARANTINED
from ddtrace.contrib.internal.pytest.constants import XFAIL_REASON
from ddtrace.contrib.internal.pytest.plugin import is_enabled
from ddtrace.contrib.internal.unittest.patch import unpatch as unpatch_unittest
from ddtrace.ext import test
from ddtrace.ext.test_visibility import ITR_SKIPPING_LEVEL
from ddtrace.ext.test_visibility.api import TestExcInfo
from ddtrace.ext.test_visibility.api import TestStatus
from ddtrace.ext.test_visibility.api import disable_test_visibility
from ddtrace.ext.test_visibility.api import enable_test_visibility
from ddtrace.ext.test_visibility.api import is_test_visibility_enabled
from ddtrace.internal.ci_visibility.constants import SKIPPED_BY_ITR_REASON
from ddtrace.internal.ci_visibility.telemetry.coverage import COVERAGE_LIBRARY
from ddtrace.internal.ci_visibility.telemetry.coverage import record_code_coverage_empty
from ddtrace.internal.ci_visibility.telemetry.coverage import record_code_coverage_finished
from ddtrace.internal.ci_visibility.telemetry.coverage import record_code_coverage_started
from ddtrace.internal.ci_visibility.utils import take_over_logger_stream_handler
from ddtrace.internal.coverage.code import ModuleCodeCollector
from ddtrace.internal.coverage.installer import install as install_coverage
from ddtrace.internal.logger import get_logger
from ddtrace.internal.test_visibility._library_capabilities import LibraryCapabilities
from ddtrace.internal.test_visibility.api import InternalTest
from ddtrace.internal.test_visibility.api import InternalTestModule
from ddtrace.internal.test_visibility.api import InternalTestSession
from ddtrace.internal.test_visibility.api import InternalTestSuite
from ddtrace.internal.test_visibility.coverage_lines import CoverageLines
from ddtrace.internal.utils.formats import asbool
from ddtrace.settings.asm import config as asm_config
from ddtrace.vendor.debtcollector import deprecate


if _pytest_version_supports_retries():
    from ddtrace.contrib.internal.pytest._retry_utils import get_retry_num

if _pytest_version_supports_efd():
    from ddtrace.contrib.internal.pytest._efd_utils import efd_get_failed_reports
    from ddtrace.contrib.internal.pytest._efd_utils import efd_get_teststatus
    from ddtrace.contrib.internal.pytest._efd_utils import efd_handle_retries
    from ddtrace.contrib.internal.pytest._efd_utils import efd_pytest_terminal_summary_post_yield

if _pytest_version_supports_atr():
    from ddtrace.contrib.internal.pytest._atr_utils import atr_get_failed_reports
    from ddtrace.contrib.internal.pytest._atr_utils import atr_get_teststatus
    from ddtrace.contrib.internal.pytest._atr_utils import atr_handle_retries
    from ddtrace.contrib.internal.pytest._atr_utils import atr_pytest_terminal_summary_post_yield
    from ddtrace.contrib.internal.pytest._atr_utils import quarantine_atr_get_teststatus
    from ddtrace.contrib.internal.pytest._atr_utils import quarantine_pytest_terminal_summary_post_yield

if _pytest_version_supports_attempt_to_fix():
    from ddtrace.contrib.internal.pytest._attempt_to_fix import attempt_to_fix_get_teststatus
    from ddtrace.contrib.internal.pytest._attempt_to_fix import attempt_to_fix_handle_retries
    from ddtrace.contrib.internal.pytest._attempt_to_fix import attempt_to_fix_pytest_terminal_summary_post_yield

log = get_logger(__name__)


_NODEID_REGEX = re.compile("^((?P<module>.*)/(?P<suite>[^/]*?))::(?P<name>.*?)$")
OUTCOME_QUARANTINED = "quarantined"
DISABLED_BY_TEST_MANAGEMENT_REASON = "Flaky test is disabled by Datadog"
INCOMPATIBLE_PLUGINS = ("flaky", "rerunfailures")

skip_pytest_runtest_protocol = False


class XdistHooks:
    @pytest.hookimpl
    def pytest_configure_node(self, node):
        main_session_span = InternalTestSession.get_span()
        if main_session_span:
            root_span = main_session_span.span_id
        else:
            root_span = 0

        node.workerinput["root_span"] = root_span

    @pytest.hookimpl
    def pytest_testnodedown(self, node, error):
        if hasattr(node, "workeroutput") and "itr_skipped_count" in node.workeroutput:
            if not hasattr(pytest, "global_worker_itr_results"):
                pytest.global_worker_itr_results = 0
            pytest.global_worker_itr_results += node.workeroutput["itr_skipped_count"]


def _handle_itr_should_skip(item, test_id) -> bool:
    """Checks whether a test should be skipped

    This function has the side effect of marking the test as skipped immediately if it should be skipped.
    """
    if not InternalTestSession.is_test_skipping_enabled():
        return False

    suite_id = test_id.parent_id

    item_is_unskippable = InternalTestSuite.is_itr_unskippable(suite_id) or InternalTest.is_attempt_to_fix(test_id)

    if InternalTestSuite.is_itr_skippable(suite_id):
        if item_is_unskippable:
            # Marking the test as forced run also applies to its hierarchy
            InternalTest.mark_itr_forced_run(test_id)
            return False

        InternalTest.mark_itr_skipped(test_id)
        # Marking the test as skipped by ITR so that it appears in pytest's output
        item.add_marker(pytest.mark.skip(reason=SKIPPED_BY_ITR_REASON))  # TODO don't rely on internal for reason

        # If we're in a worker process, count the skipped test
        if hasattr(item.config, "workeroutput"):
            if "itr_skipped_count" not in item.config.workeroutput:
                item.config.workeroutput["itr_skipped_count"] = 0
            item.config.workeroutput["itr_skipped_count"] += 1

        return True

    return False


def _handle_test_management(item, test_id):
    """Add a user property to identify quarantined tests, and mark them for skipping if quarantine is enabled in
    skipping mode.
    """
    is_quarantined = InternalTest.is_quarantined_test(test_id)
    is_disabled = InternalTest.is_disabled_test(test_id)
    is_attempt_to_fix = InternalTest.is_attempt_to_fix(test_id)

    if is_quarantined and asbool(os.getenv("_DD_TEST_SKIP_QUARANTINED_TESTS")):
        # For internal use: treat quarantined tests as disabled.
        is_disabled = True

    if is_disabled and not is_attempt_to_fix:
        # A test that is both disabled and quarantined should be skipped just like a regular disabled test.
        # It should still have both disabled and quarantined event tags, though.
        item.add_marker(pytest.mark.skip(reason=DISABLED_BY_TEST_MANAGEMENT_REASON))
    elif is_quarantined or (is_disabled and is_attempt_to_fix):
        # We add this information to user_properties to have it available in pytest_runtest_makereport().
        item.user_properties += [USER_PROPERTY_QUARANTINED]


def _start_collecting_coverage() -> ModuleCodeCollector.CollectInContext:
    coverage_collector = ModuleCodeCollector.CollectInContext()
    # TODO: don't depend on internal for telemetry
    record_code_coverage_started(COVERAGE_LIBRARY.COVERAGEPY, FRAMEWORK)

    coverage_collector.__enter__()

    return coverage_collector


def _handle_collected_coverage(test_id, coverage_collector) -> None:
    # TODO: clean up internal coverage API usage
    test_covered_lines = coverage_collector.get_covered_lines()
    coverage_collector.__exit__()

    record_code_coverage_finished(COVERAGE_LIBRARY.COVERAGEPY, FRAMEWORK)

    if not test_covered_lines:
        log.debug("No covered lines found for test %s", test_id)
        record_code_coverage_empty()
        return

    coverage_data: t.Dict[Path, CoverageLines] = {}

    for path_str, covered_lines in test_covered_lines.items():
        coverage_data[Path(path_str).absolute()] = covered_lines

    InternalTestSuite.add_coverage_data(test_id.parent_id, coverage_data)


def _handle_coverage_dependencies(suite_id) -> None:
    coverage_data = InternalTestSuite.get_coverage_data(suite_id)
    coverage_paths = coverage_data.keys()
    import_coverage = ModuleCodeCollector.get_import_coverage_for_paths(coverage_paths)
    InternalTestSuite.add_coverage_data(suite_id, import_coverage)


def _disable_ci_visibility():
    try:
        disable_test_visibility()
    except Exception:  # noqa: E722
        log.debug("encountered error during disable_ci_visibility", exc_info=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_load_initial_conftests(early_config, parser, args):
    """Perform early initialization of the Test Optimization plugin.

    This has to happen early enough that `sys.stderr` has not been redirected by pytest, so that logging is configured
    properly. Setting the hook with `tryfirst=True` and `hookwrapper=True` achieves that.
    """
    _pytest_load_initial_conftests_pre_yield(early_config, parser, args)
    yield


def _pytest_load_initial_conftests_pre_yield(early_config, parser, args):
    """Performs the bare-minimum to determine whether or ModuleCodeCollector should be enabled

    ModuleCodeCollector has a tangible impact on the time it takes to load modules, so it should only be installed if
    coverage collection is requested by the backend.
    """
    if not _is_enabled_early(early_config, args):
        return

    try:
        take_over_logger_stream_handler()
        if not asbool(os.getenv("_DD_PYTEST_FREEZEGUN_SKIP_PATCH")):
            from ddtrace._monkey import patch

            # Freezegun is proactively patched to avoid it interfering with internal timing
            patch(freezegun=True)
        dd_config.test_visibility.itr_skipping_level = ITR_SKIPPING_LEVEL.SUITE
        enable_test_visibility(config=dd_config.pytest)
        if InternalTestSession.should_collect_coverage():
            workspace_path = InternalTestSession.get_workspace_path()
            if workspace_path is None:
                workspace_path = Path.cwd().absolute()
            log.warning("Installing ModuleCodeCollector with include_paths=%s", [workspace_path])
            install_coverage(include_paths=[workspace_path], collect_import_time_coverage=True)
    except Exception:  # noqa: E722
        log.warning("encountered error during configure, disabling Datadog CI Visibility", exc_info=True)
        _disable_ci_visibility()


def pytest_configure(config: pytest_Config) -> None:
    global skip_pytest_runtest_protocol

    if os.getenv("DD_PYTEST_USE_NEW_PLUGIN_BETA"):
        # Logging the warning at this point ensures it shows up in output regardless of the use of the -s flag.
        deprecate(
            "the DD_PYTEST_USE_NEW_PLUGIN_BETA environment variable is deprecated",
            message="the new pytest plugin is now the default version. No additional configurations are required.",
            removal_version="3.0.0",
            category=DDTraceDeprecationWarning,
        )

    try:
        if is_enabled(config):
            unpatch_unittest()
            enable_test_visibility(config=dd_config.pytest)
            if _is_pytest_cov_enabled(config):
                patch_coverage()

            skip_pytest_runtest_protocol = False

            for plugin in INCOMPATIBLE_PLUGINS:
                if config.pluginmanager.hasplugin(plugin):
                    log.warning(
                        "The pytest `%s` plugin is in use; Test Optimization advanced features will be disabled. "
                        "You can run `pytest` with `-p no:%s` to disable the plugin and enable Test Optimization "
                        "features.",
                        plugin,
                        plugin,
                    )
                    skip_pytest_runtest_protocol = True

            # pytest-bdd plugin support
            if config.pluginmanager.hasplugin("pytest-bdd"):
                from ddtrace.contrib.internal.pytest._pytest_bdd_subplugin import _PytestBddSubPlugin

                config.pluginmanager.register(_PytestBddSubPlugin(), "_datadog-pytest-bdd")

            if config.pluginmanager.hasplugin("xdist"):
                config.pluginmanager.register(XdistHooks())

                if not hasattr(config, "workerinput") and os.environ.get("PYTEST_XDIST_WORKER") is None:
                    # Main process
                    pytest.global_worker_itr_results = 0
        else:
            # If the pytest ddtrace plugin is not enabled, we should disable CI Visibility, as it was enabled during
            # pytest_load_initial_conftests
            _disable_ci_visibility()
    except Exception:  # noqa: E722
        log.warning("encountered error during configure, disabling Datadog CI Visibility", exc_info=True)
        _disable_ci_visibility()


def pytest_unconfigure(config: pytest_Config) -> None:
    if not is_test_visibility_enabled():
        return

    _disable_ci_visibility()


def pytest_sessionstart(session: pytest.Session) -> None:
    if not is_test_visibility_enabled():
        return

    log.debug("CI Visibility enabled - starting test session")

    try:
        command = _get_session_command(session)

        library_capabilities = LibraryCapabilities(
            early_flake_detection="1" if _pytest_version_supports_efd() else None,
            auto_test_retries="1" if _pytest_version_supports_atr() else None,
            test_impact_analysis="1" if _pytest_version_supports_itr() else None,
            test_management_quarantine="1",
            test_management_disable="1",
            test_management_attempt_to_fix="4" if _pytest_version_supports_attempt_to_fix() else None,
        )

        InternalTestSession.discover(
            test_command=command,
            test_framework=FRAMEWORK,
            test_framework_version=pytest.__version__,
            session_operation_name="pytest.test_session",
            module_operation_name="pytest.test_module",
            suite_operation_name="pytest.test_suite",
            test_operation_name=dd_config.pytest.operation_name,
            reject_duplicates=False,
        )

        InternalTestSession.set_library_capabilities(library_capabilities)

        extracted_context = None
        distributed_children = False
        if hasattr(session.config, "workerinput"):
            from ddtrace._trace.context import Context
            from ddtrace.constants import USER_KEEP

            received_root_span = session.config.workerinput.get("root_span", "MISSING_SPAN")
            try:
                root_span = int(received_root_span)
                extracted_context = Context(
                    trace_id=1,
                    span_id=root_span,  # This span_id here becomes context.span_id for the parent context
                    sampling_priority=USER_KEEP,
                )
            except ValueError:
                log.debug(
                    "pytest_sessionstart: Could not convert root_span %s to int",
                    received_root_span,
                )
        elif hasattr(pytest, "global_worker_itr_results"):
            distributed_children = True

        InternalTestSession.start(distributed_children, extracted_context)

        if InternalTestSession.efd_enabled() and not _pytest_version_supports_efd():
            log.warning("Early Flake Detection disabled: pytest version is not supported")

    except Exception:  # noqa: E722
        log.debug("encountered error during session start, disabling Datadog CI Visibility", exc_info=True)
        _disable_ci_visibility()


def _pytest_collection_finish(session) -> None:
    """Discover modules, suites, and tests that have been selected by pytest

    NOTE: Using pytest_collection_finish instead of pytest_collection_modifyitems allows us to capture only the
    tests that pytest has selection for run (eg: with the use of -k as an argument).
    """
    for item in session.items:
        test_id = _get_test_id_from_item(item)
        suite_id = test_id.parent_id
        module_id = suite_id.parent_id

        # TODO: don't rediscover modules and suites if already discovered
        InternalTestModule.discover(module_id, _get_module_path_from_item(item))
        InternalTestSuite.discover(suite_id)

        item_path = Path(item.path if hasattr(item, "path") else item.fspath).absolute()
        workspace_path = InternalTestSession.get_workspace_path()
        if workspace_path:
            try:
                repo_relative_path = item_path.relative_to(workspace_path)
            except ValueError:
                repo_relative_path = item_path
        else:
            repo_relative_path = item_path

        item_codeowners = InternalTestSession.get_path_codeowners(repo_relative_path) if repo_relative_path else None

        source_file_info = _get_source_file_info(item, item_path)

        InternalTest.discover(test_id, codeowners=item_codeowners, source_file_info=source_file_info)

        markers = [marker.kwargs for marker in item.iter_markers(name="dd_tags")]
        for tags in markers:
            InternalTest.set_tags(test_id, tags)

        # Pytest markers do not allow us to determine if the test or the suite was marked as unskippable, but any
        # test marked unskippable in a suite makes the entire suite unskippable (since we are in suite skipping
        # mode)
        if InternalTestSession.is_test_skipping_enabled() and _is_test_unskippable(item):
            InternalTest.mark_itr_unskippable(test_id)
            InternalTestSuite.mark_itr_unskippable(suite_id)

    # NOTE: EFD enablement status is already specified during service enablement
    if InternalTestSession.efd_enabled() and InternalTestSession.efd_is_faulty_session():
        log.warning("Early Flake Detection disabled: too many new tests detected")


def pytest_collection_finish(session) -> None:
    if not is_test_visibility_enabled():
        return

    try:
        return _pytest_collection_finish(session)
    except Exception:  # noqa: E722
        log.debug("encountered error during collection finish, disabling Datadog CI Visibility", exc_info=True)
        _disable_ci_visibility()


def _pytest_runtest_protocol_pre_yield(item) -> t.Optional[ModuleCodeCollector.CollectInContext]:
    test_id = _get_test_id_from_item(item)
    suite_id = test_id.parent_id
    module_id = suite_id.parent_id

    # TODO: don't re-start modules if already started
    InternalTestModule.start(module_id)
    InternalTestSuite.start(suite_id)

    # DEV: pytest's fixtures resolution may change parameters between collection finish and test run
    parameters = _get_test_parameters_json(item)
    if parameters is not None:
        InternalTest.set_parameters(test_id, parameters)

    InternalTest.start(test_id)

    _handle_test_management(item, test_id)
    _handle_itr_should_skip(item, test_id)

    item_will_skip = _pytest_marked_to_skip(item) or InternalTest.was_itr_skipped(test_id)

    collect_test_coverage = InternalTestSession.should_collect_coverage() and not item_will_skip

    if collect_test_coverage:
        return _start_collecting_coverage()

    return None


def _pytest_runtest_protocol_post_yield(item, nextitem, coverage_collector):
    test_id = _get_test_id_from_item(item)
    suite_id = test_id.parent_id
    module_id = suite_id.parent_id

    if not InternalTest.is_finished(test_id):
        log.debug("Test %s was not finished normally during pytest_runtest_protocol, finishing it now", test_id)
        reports_dict = reports_by_item.get(item)
        if reports_dict:
            test_outcome = _process_reports_dict(item, reports_dict)
            InternalTest.finish(test_id, test_outcome.status, test_outcome.skip_reason, test_outcome.exc_info)
        else:
            log.debug("Test %s has no entry in reports_by_item", test_id)
            InternalTest.finish(test_id)

    if coverage_collector is not None:
        _handle_collected_coverage(test_id, coverage_collector)

    # We rely on the CI Visibility service to prevent finishing items that have been discovered and have unfinished
    # children, but as an optimization:
    # - we know we don't need to finish the suite if the next item is in the same suite
    # - we know we don't need to finish the module if the next item is in the same module
    # - we trust that the next item is in the same module if it is in the same suite
    next_test_id = _get_test_id_from_item(nextitem) if nextitem else None
    if next_test_id is None or next_test_id.parent_id != suite_id:
        if InternalTestSuite.is_itr_skippable(suite_id) and not InternalTestSuite.was_itr_forced_run(suite_id):
            InternalTestSuite.mark_itr_skipped(suite_id)
        else:
            _handle_coverage_dependencies(suite_id)
        InternalTestSuite.finish(suite_id)
        if nextitem is None or (next_test_id is not None and next_test_id.parent_id.parent_id != module_id):
            InternalTestModule.finish(module_id)


@pytest.hookimpl(tryfirst=True, hookwrapper=True, specname="pytest_runtest_protocol")
def pytest_runtest_protocol_wrapper(item, nextitem) -> None:
    if not is_test_visibility_enabled():
        yield
        return

    try:
        coverage_collector = _pytest_runtest_protocol_pre_yield(item)
    except Exception:  # noqa: E722
        log.debug("encountered error during pre-test", exc_info=True)

    yield

    try:
        _pytest_runtest_protocol_post_yield(item, nextitem, coverage_collector)
    except Exception:  # noqa: E722
        log.debug("encountered error during post-test", exc_info=True)


@pytest.hookimpl(specname="pytest_runtest_protocol")
def pytest_runtest_protocol(item, nextitem) -> t.Optional[bool]:
    if not is_test_visibility_enabled():
        return None

    if skip_pytest_runtest_protocol:
        # Retry-based features such as Early Flake Detection, Auto Test Retries, and Attempt-to-Fix do not work properly
        # with external retry plugins such as `flaky` and `pytest-rerunfailures`. If those plugins are in use, we let
        # their `pytest_runtest_protocol` run and report their results to the backend, and do not run our advanced
        # features.
        return None

    try:
        _pytest_run_one_test(item, nextitem)
        return True  # Do not run pytest's internal `pytest_runtest_protocol`.

    except Exception:  # noqa: E722
        log.warning("Encountered internal error while running test, disabling Datadog CI Visibility", exc_info=True)
        _disable_ci_visibility()
        return None


def _pytest_run_one_test(item, nextitem):
    item.ihook.pytest_runtest_logstart(nodeid=item.nodeid, location=item.location)
    reports = runtestprotocol(item, nextitem=nextitem, log=False)
    reports_dict = {report.when: report for report in reports}
    test_outcome = _process_reports_dict(item, reports_dict)

    test_id = _get_test_id_from_item(item)
    is_quarantined = InternalTest.is_quarantined_test(test_id)
    is_disabled = InternalTest.is_disabled_test(test_id)
    is_attempt_to_fix = InternalTest.is_attempt_to_fix(test_id)
    setup_or_teardown_failed = False

    if not InternalTest.is_finished(test_id):
        InternalTest.finish(test_id, test_outcome.status, test_outcome.skip_reason, test_outcome.exc_info)

    for report in reports:
        if report.failed and report.when in (TestPhase.SETUP, TestPhase.TEARDOWN):
            setup_or_teardown_failed = True

        if report.when == TestPhase.CALL or "failed" in report.outcome:
            if is_quarantined or is_disabled:
                # Ensure test doesn't count as failed for pytest's exit status logic
                # (see <https://github.com/pytest-dev/pytest/blob/8.3.x/src/_pytest/main.py#L654>).
                report.outcome = OUTCOME_QUARANTINED

        if report.failed or report.skipped:
            InternalTest.stash_set(test_id, "failure_longrepr", report.longrepr)

    retry_handler = None

    if setup_or_teardown_failed:
        # ATR and EFD retry tests only if their teardown succeeded to ensure the best chance the retry will succeed.
        log.debug("Test %s failed during setup or teardown, skipping retries", test_id)
    elif is_attempt_to_fix and _pytest_version_supports_attempt_to_fix():
        retry_handler = attempt_to_fix_handle_retries
    elif InternalTestSession.efd_enabled() and InternalTest.efd_should_retry(test_id):
        retry_handler = efd_handle_retries
    elif InternalTestSession.atr_is_enabled() and InternalTest.atr_should_retry(test_id):
        retry_handler = atr_handle_retries

    if retry_handler:
        # Retry handler is responsible for logging the test reports.
        retry_handler(
            test_id=test_id,
            item=item,
            test_reports=reports_dict,
            test_outcome=test_outcome,
            is_quarantined=is_quarantined,
        )
    else:
        # If no retry handler, we log the reports ourselves.
        for report in reports:
            item.ihook.pytest_runtest_logreport(report=report)

    item.ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)


def _process_reports_dict(item, reports) -> _TestOutcome:
    final_outcome = None

    for when in (TestPhase.SETUP, TestPhase.CALL, TestPhase.TEARDOWN):
        report = reports.get(when)
        if not report:
            continue

        outcome = _process_result(item, report)
        if final_outcome is None or final_outcome.status is None:
            final_outcome = outcome
            if final_outcome.status is not None:
                return final_outcome

    return final_outcome


def _process_result(item, result) -> _TestOutcome:
    test_id = _get_test_id_from_item(item)

    report_excinfo = excinfo_by_report.get(result)
    has_exception = report_excinfo is not None

    # In cases where a test was marked as XFAIL, the reason is only available during when call.when == "call", so we
    # add it as a tag immediately:
    if getattr(result, "wasxfail", None):
        InternalTest.set_tag(test_id, XFAIL_REASON, result.wasxfail)
    elif "xfail" in getattr(result, "keywords", []) and getattr(result, "longrepr", None):
        InternalTest.set_tag(test_id, XFAIL_REASON, result.longrepr)

    # Only capture result if:
    # - there is an exception
    # - the test failed
    # - the test passed with xfail
    # - we are tearing down the test
    # DEV NOTE: some skip scenarios (eg: skipif) have an exception during setup
    if result.when != TestPhase.TEARDOWN and not (has_exception or result.failed):
        return _TestOutcome()

    xfail = hasattr(result, "wasxfail") or "xfail" in result.keywords
    xfail_reason_tag = InternalTest.get_tag(test_id, XFAIL_REASON) if xfail else None
    has_skip_keyword = any(x in result.keywords for x in ["skip", "skipif", "skipped"])

    # If run with --runxfail flag, tests behave as if they were not marked with xfail,
    # that's why no XFAIL_REASON or test.RESULT tags will be added.
    if result.skipped:
        if InternalTest.was_itr_skipped(test_id):
            # Items that were skipped by ITR already have their status and reason set
            return _TestOutcome()

        if xfail and not has_skip_keyword:
            # XFail tests that fail are recorded skipped by pytest, should be passed instead
            if not item.config.option.runxfail:
                InternalTest.set_tag(test_id, test.RESULT, test.Status.XFAIL.value)
                if xfail_reason_tag is None:
                    InternalTest.set_tag(test_id, XFAIL_REASON, getattr(result, "wasxfail", "XFail"))
                return _TestOutcome(TestStatus.PASS)

        return _TestOutcome(TestStatus.SKIP, report_excinfo.value if report_excinfo else None)

    if result.passed:
        if xfail and not has_skip_keyword and not item.config.option.runxfail:
            # XPass (strict=False) are recorded passed by pytest
            if xfail_reason_tag is None:
                InternalTest.set_tag(test_id, XFAIL_REASON, "XFail")
            InternalTest.set_tag(test_id, test.RESULT, test.Status.XPASS.value)

        return _TestOutcome(TestStatus.PASS)

    if xfail and not has_skip_keyword and not item.config.option.runxfail:
        # XPass (strict=True) are recorded failed by pytest, longrepr contains reason
        if xfail_reason_tag is None:
            InternalTest.set_tag(test_id, XFAIL_REASON, getattr(result, "longrepr", "XFail"))
        InternalTest.set_tag(test_id, test.RESULT, test.Status.XPASS.value)
        return _TestOutcome(TestStatus.FAIL)

    # NOTE: for ATR and EFD purposes, we need to know if the test failed during setup or teardown.
    if result.when == TestPhase.SETUP and result.failed:
        InternalTest.stash_set(test_id, "setup_failed", True)
    elif result.when == TestPhase.TEARDOWN and result.failed:
        InternalTest.stash_set(test_id, "teardown_failed", True)

    exc_info = TestExcInfo(report_excinfo.type, report_excinfo.value, report_excinfo.tb) if report_excinfo else None

    return _TestOutcome(status=TestStatus.FAIL, exc_info=exc_info)


def _pytest_runtest_makereport(item: pytest.Item, call: pytest_CallInfo, outcome: pytest_TestReport) -> None:
    original_result = outcome.get_result()

    # When ATR or EFD retries are active, we do not want makereport to generate results
    if _pytest_version_supports_retries() and get_retry_num(original_result) is not None:
        return

    if call.when != TestPhase.TEARDOWN:
        return

    # Support for pytest-benchmark plugin
    if item.config.pluginmanager.hasplugin("benchmark"):
        _set_benchmark_data_from_item(item)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest_CallInfo) -> None:
    """Store outcome for tracing."""
    outcome: pytest_TestReport
    outcome = yield

    # DEV: Make excinfo available for later use, when we don't have the `call` object anymore.
    # We cannot stash it directly into the report because pytest-xdist fails to serialize the report if we do that.
    excinfo_by_report[outcome.get_result()] = call.excinfo
    reports_by_item.setdefault(item, {})[call.when] = outcome.get_result()

    if not is_test_visibility_enabled():
        return

    try:
        return _pytest_runtest_makereport(item, call, outcome)
    except Exception:  # noqa: E722
        log.debug("encountered error during makereport", exc_info=True)


def _pytest_terminal_summary_pre_yield(terminalreporter) -> int:
    # Before yield gives us a chance to show failure reports (with the stack trace of the failing test), but they have
    # to be in terminalreporter.stats["failed"] to be shown. That, however, would make them count towards the final
    # summary, so we add them temporarily, then restore terminalreporter.stats["failed"] to its original size after the
    # yield.
    failed_reports_initial_size = len(terminalreporter.stats.get(PYTEST_STATUS.FAILED, []))

    if _pytest_version_supports_efd() and InternalTestSession.efd_enabled():
        for failed_report in efd_get_failed_reports(terminalreporter):
            failed_report.outcome = PYTEST_STATUS.FAILED
            terminalreporter.stats.setdefault("failed", []).append(failed_report)

    if _pytest_version_supports_atr() and InternalTestSession.atr_is_enabled():
        for failed_report in atr_get_failed_reports(terminalreporter):
            failed_report.outcome = PYTEST_STATUS.FAILED
            terminalreporter.stats.setdefault("failed", []).append(failed_report)

    return failed_reports_initial_size


def _pytest_terminal_summary_post_yield(terminalreporter, failed_reports_initial_size: t.Optional[int] = None):
    # After yield gives us a chance to:
    # - print our flaky test status summary
    # - modify the total counts

    # Restore terminalreporter.stats["failed"] to its original size so the final summary remains correct
    if failed_reports_initial_size is None:
        log.debug("Could not get initial failed report size, not restoring failed reports")
    elif failed_reports_initial_size == 0:
        terminalreporter.stats.pop("failed", None)
    else:
        terminalreporter.stats[PYTEST_STATUS.FAILED] = terminalreporter.stats[PYTEST_STATUS.FAILED][
            :failed_reports_initial_size
        ]

    # IMPORTANT: terminal summary functions mutate terminalreporter.stats
    if _pytest_version_supports_efd() and InternalTestSession.efd_enabled():
        efd_pytest_terminal_summary_post_yield(terminalreporter)

    if _pytest_version_supports_atr() and InternalTestSession.atr_is_enabled():
        atr_pytest_terminal_summary_post_yield(terminalreporter)

    quarantine_pytest_terminal_summary_post_yield(terminalreporter)
    attempt_to_fix_pytest_terminal_summary_post_yield(terminalreporter)

    print_test_report_links(terminalreporter)
    return


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Report flaky or failed tests"""
    try:
        if asm_config._iast_enabled:
            from ddtrace.appsec._iast._pytest_plugin import print_iast_report

            print_iast_report(terminalreporter)
    except Exception:  # noqa: E722
        log.debug("Encountered error during code security summary", exc_info=True)

    if not is_test_visibility_enabled():
        yield
        return

    failed_reports_initial_size = None
    try:
        failed_reports_initial_size = _pytest_terminal_summary_pre_yield(terminalreporter)
    except Exception:  # noqa: E722
        log.debug("Encountered error during terminal summary pre-yield", exc_info=True)

    yield

    try:
        _pytest_terminal_summary_post_yield(terminalreporter, failed_reports_initial_size)
    except Exception:  # noqa: E722
        log.debug("Encountered error during terminal summary post-yield", exc_info=True)

    return


def _pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    if not is_test_visibility_enabled():
        return

    invoked_by_coverage_run_status = _is_coverage_invoked_by_coverage_run()
    pytest_cov_status = _is_pytest_cov_enabled(session.config)
    if _is_coverage_patched() and (pytest_cov_status or invoked_by_coverage_run_status):
        if invoked_by_coverage_run_status and not pytest_cov_status:
            run_coverage_report()

        lines_pct_value = _coverage_data.get(PCT_COVERED_KEY, None)
        if not isinstance(lines_pct_value, float):
            log.warning("Tried to add total covered percentage to session span but the format was unexpected")
        else:
            InternalTestSession.set_covered_lines_pct(lines_pct_value)

    if ModuleCodeCollector.is_installed():
        ModuleCodeCollector.uninstall()

    # Count ITR skipped tests from workers if we're in the main process
    if hasattr(pytest, "global_worker_itr_results"):
        skipped_count = pytest.global_worker_itr_results
        if skipped_count > 0:
            # Update the session's internal _itr_skipped_count so that when _set_itr_tags() is called
            # during session finishing, it will use the correct worker-aggregated count
            InternalTestSession.set_itr_skipped_count(skipped_count)

    InternalTestSession.finish(
        force_finish_children=True,
        override_status=TestStatus.FAIL if session.exitstatus == pytest.ExitCode.TESTS_FAILED else None,
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    yield

    if not is_test_visibility_enabled():
        return

    try:
        _pytest_sessionfinish(session, exitstatus)
    except Exception:  # noqa: E722
        log.debug("encountered error during session finish", exc_info=True)


def pytest_report_teststatus(
    report: pytest_TestReport,
) -> _pytest_report_teststatus_return_type:
    if not is_test_visibility_enabled():
        return

    if _pytest_version_supports_attempt_to_fix():
        test_status = attempt_to_fix_get_teststatus(report)
        if test_status:
            return test_status

    if _pytest_version_supports_atr() and InternalTestSession.atr_is_enabled():
        test_status = atr_get_teststatus(report) or quarantine_atr_get_teststatus(report)
        if test_status is not None:
            return test_status

    if _pytest_version_supports_efd() and InternalTestSession.efd_enabled():
        test_status = efd_get_teststatus(report)
        if test_status is not None:
            return test_status

    user_properties = getattr(report, "user_properties", [])
    is_quarantined = USER_PROPERTY_QUARANTINED in user_properties
    if is_quarantined:
        if report.when == TestPhase.TEARDOWN:
            return (OUTCOME_QUARANTINED, "q", ("QUARANTINED", {"blue": True}))
        else:
            # Don't show anything for setup and call of quarantined tests, regardless of
            # whether there were errors or not.
            return ("", "", "")


@pytest.hookimpl(trylast=True)
def pytest_ddtrace_get_item_module_name(item):
    names = _get_names_from_item(item)
    return names.module


@pytest.hookimpl(trylast=True)
def pytest_ddtrace_get_item_suite_name(item):
    """
    Extract suite name from a `pytest.Item` instance.
    If the module path doesn't exist, the suite path will be reported in full.
    """
    names = _get_names_from_item(item)
    return names.suite


@pytest.hookimpl(trylast=True)
def pytest_ddtrace_get_item_test_name(item):
    """Extract name from item, prepending class if desired"""
    names = _get_names_from_item(item)
    return names.test
