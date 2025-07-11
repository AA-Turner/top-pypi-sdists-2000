import os
import sqlite3
import sqlite3.dbapi2
from typing import Dict

import wrapt

from ddtrace import config
from ddtrace.contrib.dbapi import FetchTracedCursor
from ddtrace.contrib.dbapi import TracedConnection
from ddtrace.contrib.dbapi import TracedCursor
from ddtrace.ext import db
from ddtrace.internal.schema import schematize_database_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.formats import asbool
from ddtrace.settings.asm import config as asm_config
from ddtrace.trace import Pin


# Original connect method
_connect = sqlite3.connect

config._add(
    "sqlite",
    dict(
        _default_service=schematize_service_name("sqlite"),
        _dbapi_span_name_prefix="sqlite",
        _dbapi_span_operation_name=schematize_database_operation("sqlite.query", database_provider="sqlite"),
        trace_fetch_methods=asbool(os.getenv("DD_SQLITE_TRACE_FETCH_METHODS", default=False)),
    ),
)


def get_version():
    # type: () -> str
    return sqlite3.sqlite_version


def _supported_versions() -> Dict[str, str]:
    return {"sqlite3": "*"}


def patch():
    if getattr(sqlite3, "_datadog_patch", False):
        return
    sqlite3._datadog_patch = True
    wrapped = wrapt.FunctionWrapper(_connect, traced_connect)

    sqlite3.connect = wrapped
    sqlite3.dbapi2.connect = wrapped

    if asm_config._iast_enabled:
        from ddtrace.appsec._iast._metrics import _set_metric_iast_instrumented_sink
        from ddtrace.appsec._iast.constants import VULN_SQL_INJECTION

        _set_metric_iast_instrumented_sink(VULN_SQL_INJECTION)


def unpatch():
    if getattr(sqlite3, "_datadog_patch", False):
        sqlite3._datadog_patch = False
    sqlite3.connect = _connect
    sqlite3.dbapi2.connect = _connect


def traced_connect(func, _, args, kwargs):
    conn = func(*args, **kwargs)
    return patch_conn(conn)


def patch_conn(conn):
    wrapped = TracedSQLite(conn)
    Pin(tags={db.SYSTEM: "sqlite"}).onto(wrapped)
    return wrapped


class TracedSQLiteCursor(TracedCursor):
    def executemany(self, *args, **kwargs):
        # DEV: SQLite3 Cursor.execute always returns back the cursor instance
        super(TracedSQLiteCursor, self).executemany(*args, **kwargs)
        return self

    def execute(self, *args, **kwargs):
        # DEV: SQLite3 Cursor.execute always returns back the cursor instance
        super(TracedSQLiteCursor, self).execute(*args, **kwargs)
        return self


class TracedSQLiteFetchCursor(TracedSQLiteCursor, FetchTracedCursor):
    pass


class TracedSQLite(TracedConnection):
    def __init__(self, conn, pin=None, cursor_cls=None):
        if not cursor_cls:
            # Do not trace `fetch*` methods by default
            cursor_cls = TracedSQLiteFetchCursor if config.sqlite.trace_fetch_methods else TracedSQLiteCursor

            super(TracedSQLite, self).__init__(conn, pin=pin, cfg=config.sqlite, cursor_cls=cursor_cls)

    def execute(self, *args, **kwargs):
        # sqlite has a few extra sugar functions
        return self.cursor().execute(*args, **kwargs)

    def backup(self, target, *args, **kwargs):
        # sqlite3 checks the type of `target`, it cannot be a wrapped connection
        # https://github.com/python/cpython/blob/4652093e1b816b78e9a585d671a807ce66427417/Modules/_sqlite/connection.c#L1897-L1899
        if isinstance(target, TracedConnection):
            target = target.__wrapped__
        return self.__wrapped__.backup(target, *args, **kwargs)
