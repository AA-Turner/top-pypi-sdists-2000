from contextlib import contextmanager
import os
import sys
from unittest import mock

import pytest

from ddtrace.appsec._iast._iast_request_context import get_iast_reporter
from ddtrace.appsec._iast._patch_modules import _testing_unpatch_iast
from ddtrace.appsec._iast.constants import VULN_INSECURE_HASHING_TYPE
from ddtrace.appsec._iast.taint_sinks._base import VulnerabilityBase
from tests.appsec.iast.conftest import iast_context
from tests.appsec.iast.fixtures.taint_sinks.weak_algorithms import hashlib_new
from tests.appsec.iast.fixtures.taint_sinks.weak_algorithms import parametrized_weak_hash
from tests.appsec.iast.iast_utils import get_line_and_hash


WEAK_ALGOS_FIXTURES_PATH = "tests/appsec/iast/fixtures/taint_sinks/weak_algorithms.py"
WEAK_HASH_FIXTURES_PATH = "tests/appsec/iast/taint_sinks/test_weak_hash.py"


@pytest.fixture
def iast_context_md5_and_sha1_configured():
    yield from iast_context(dict(DD_IAST_ENABLED="true", DD_IAST_WEAK_HASH_ALGORITHMS="MD5, SHA1"))


@pytest.fixture
def iast_context_only_md4():
    yield from iast_context(dict(DD_IAST_ENABLED="true", DD_IAST_WEAK_HASH_ALGORITHMS="MD4"))


@pytest.fixture
def iast_context_only_md5():
    yield from iast_context(dict(DD_IAST_ENABLED="true", DD_IAST_WEAK_HASH_ALGORITHMS="MD5"))


@pytest.fixture
def iast_context_only_sha1():
    yield from iast_context(dict(DD_IAST_ENABLED="true", DD_IAST_WEAK_HASH_ALGORITHMS="SHA1"))


@pytest.fixture
def iast_context_contextmanager_deduplication_enabled():
    def iast_aux(deduplication_enabled=True, time_lapse=3600.0):
        from ddtrace.appsec._deduplications import deduplication

        try:
            old_value = deduplication._time_lapse
            deduplication._time_lapse = time_lapse
            yield from iast_context(dict(DD_IAST_ENABLED="true"), deduplication=deduplication_enabled)
        finally:
            deduplication._time_lapse = old_value

    try:
        # Yield a context manager allowing to create several spans to test deduplication
        yield contextmanager(iast_aux)
    finally:
        # Reset the cache to avoid side effects in other tests
        VulnerabilityBase._prepare_report._reset_cache()


@pytest.mark.parametrize(
    "hash_func,method",
    [
        ("md5", "hexdigest"),
        ("md5", "digest"),
        ("sha1", "digest"),
        ("sha1", "hexdigest"),
    ],
)
def test_weak_hash_hashlib(iast_context_defaults, hash_func, method):
    parametrized_weak_hash(hash_func, method)

    line, hash_value = get_line_and_hash(
        "parametrized_weak_hash", VULN_INSECURE_HASHING_TYPE, filename=WEAK_ALGOS_FIXTURES_PATH
    )

    span_report = get_iast_reporter()
    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_ALGOS_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].location.line == line
    assert list(span_report.vulnerabilities)[0].evidence.value == hash_func
    assert list(span_report.vulnerabilities)[0].hash == hash_value


@pytest.mark.parametrize(
    "hash_func,method,fake_line",
    [
        ("md5", "hexdigest", 0),
        ("md5", "hexdigest", -100),
        ("md5", "hexdigest", -1),
    ],
)
def test_ensure_line_reported_is_minus_one_for_edge_cases(iast_context_defaults, hash_func, method, fake_line):
    absolute_path = os.path.abspath(WEAK_ALGOS_FIXTURES_PATH)
    with mock.patch(
        "ddtrace.appsec._iast.taint_sinks._base.get_info_frame",
        return_value=(absolute_path, fake_line, "", ""),
    ):
        parametrized_weak_hash(hash_func, method)

    _, hash_value = get_line_and_hash(
        "parametrized_weak_hash", VULN_INSECURE_HASHING_TYPE, filename=WEAK_ALGOS_FIXTURES_PATH, fixed_line=-1
    )

    span_report = get_iast_reporter()
    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_ALGOS_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].location.line == -1
    assert list(span_report.vulnerabilities)[0].evidence.value == hash_func
    assert list(span_report.vulnerabilities)[0].hash == hash_value


@pytest.mark.parametrize("hash_func", ["md5", "sha1"])
def test_weak_hash_hashlib_no_digest(iast_context_md5_and_sha1_configured, hash_func):
    import hashlib

    m = getattr(hashlib, hash_func)()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")

    span_report = get_iast_reporter()
    assert span_report is None


@pytest.mark.parametrize("hash_func,method", [("sha256", "digest"), ("sha256", "hexdigest")])
def test_weak_hash_secure_hash(iast_context_md5_and_sha1_configured, hash_func, method):
    import hashlib

    m = getattr(hashlib, hash_func)()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    getattr(m, method)()
    span_report = get_iast_reporter()
    assert span_report is None


def test_weak_hash_new(iast_context_defaults):
    hashlib_new()
    span_report = get_iast_reporter()

    line, hash_value = get_line_and_hash("hashlib_new", VULN_INSECURE_HASHING_TYPE, filename=WEAK_ALGOS_FIXTURES_PATH)
    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_ALGOS_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].location.line == line
    assert list(span_report.vulnerabilities)[0].evidence.value == "md5"
    assert list(span_report.vulnerabilities)[0].hash == hash_value


def test_weak_hash_md5_builtin_py3_unpatched(iast_context_md5_and_sha1_configured):
    _testing_unpatch_iast()
    import _md5

    m = _md5.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert span_report is None


def test_weak_hash_md5_builtin_py3_md5_and_sha1_configured(iast_context_defaults):
    import _md5

    m = _md5.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_HASH_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].evidence.value == "md5"


def test_weak_hash_md5_builtin_py3_only_md4_configured(iast_context_only_md4):
    import _md5

    m = _md5.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert span_report is None


def test_weak_hash_md5_builtin_py3_only_md5_configured(iast_context_only_md5):
    import _md5

    m = _md5.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_HASH_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].evidence.value == "md5"


def test_weak_hash_md5_builtin_py3_only_sha1_configured(iast_context_only_sha1):
    import _md5

    m = _md5.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert span_report is None


def test_weak_hash_pycryptodome_hashes_md5(iast_context_defaults):
    from Crypto.Hash import MD5

    m = MD5.new()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()
    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_HASH_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].evidence.value == "md5"


def test_weak_hash_pycryptodome_hashes_sha1_defaults(iast_context_defaults):
    from Crypto.Hash import SHA1

    m = SHA1.new()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_HASH_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].evidence.value == "sha1"


def test_weak_hash_pycryptodome_hashes_sha1_only_md5_configured(iast_context_only_md5):
    from Crypto.Hash import SHA1

    m = SHA1.new()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert span_report is None


def test_weak_hash_pycryptodome_hashes_sha1_only_sha1_configured(iast_context_only_sha1):
    from Crypto.Hash import SHA1

    m = SHA1.new()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    m.digest()
    span_report = get_iast_reporter()

    assert list(span_report.vulnerabilities)[0].type == VULN_INSECURE_HASHING_TYPE
    assert list(span_report.vulnerabilities)[0].location.path == WEAK_HASH_FIXTURES_PATH
    assert list(span_report.vulnerabilities)[0].evidence.value == "sha1"


def test_weak_check_repeated(iast_context_defaults):
    import hashlib

    m = hashlib.new("md5")
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    num_vulnerabilities = 10
    for _ in range(0, num_vulnerabilities):
        m.digest()

    span_report = get_iast_reporter()

    assert len(span_report.vulnerabilities) == 1


@pytest.mark.skipif(sys.version_info > (3, 10, 0), reason="hmac has a weak hash vulnerability until Python 3.10")
def test_weak_hash_check_hmac(iast_context_defaults):
    import hashlib
    import hmac

    mac = hmac.new(b"test", digestmod=hashlib.md5)
    mac.digest()
    span_report = get_iast_reporter()
    assert len(span_report.vulnerabilities) == 1


def test_weak_check_hmac_secure(iast_context_defaults):
    import hashlib
    import hmac

    mac = hmac.new(b"test", digestmod=hashlib.sha256)
    mac.digest()
    span_report = get_iast_reporter()
    assert span_report is None


@pytest.mark.parametrize("deduplication_enabled", (False, True))
def test_weak_hash_deduplication_expired_cache(
    iast_context_contextmanager_deduplication_enabled, deduplication_enabled
):
    """
    Test deduplication enabled/disabled over several spans
    Test expired/non expired cache with different time_lapse
    """
    import hashlib
    import time

    time_lapse = 0.01
    for i in range(3):
        with iast_context_contextmanager_deduplication_enabled(deduplication_enabled, time_lapse):
            time.sleep(0.5)
            m = hashlib.new("md5")
            m.update(b"Nobody inspects" * i)
            m.digest()

            span_report = get_iast_reporter()
            assert span_report is not None, f"Failed at iteration {i}. span_report {span_report}"
            assert len(span_report.vulnerabilities) == 1, f"Failed at iteration {i}"


@pytest.mark.parametrize("deduplication_enabled", (False, True))
def test_weak_hash_deduplication_cache(iast_context_contextmanager_deduplication_enabled, deduplication_enabled):
    """
    Test deduplication enabled/disabled over several spans
    Test expired/non expired cache with different time_lapse
    """
    import hashlib
    import time

    time_lapse = 3600.0
    for i in range(10):
        with iast_context_contextmanager_deduplication_enabled(deduplication_enabled, time_lapse):
            time.sleep(0.2)
            m = hashlib.new("md5")
            m.update(b"Nobody inspects" * i)
            m.digest()

            span_report = get_iast_reporter()
            if i > 0 and deduplication_enabled:
                assert span_report is None, f"Failed at iteration {i}"
            else:
                assert span_report is not None, f"Failed at iteration {i}. span_report {span_report}"
                assert len(span_report.vulnerabilities) == 1, f"Failed at iteration {i}"
