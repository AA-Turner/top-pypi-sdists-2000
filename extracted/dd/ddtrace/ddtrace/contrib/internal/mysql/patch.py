import os
from typing import Dict

import mysql.connector
import wrapt

from ddtrace import config
from ddtrace.contrib.dbapi import TracedConnection
from ddtrace.contrib.internal.trace_utils import _convert_to_string
from ddtrace.ext import db
from ddtrace.ext import net
from ddtrace.internal.schema import schematize_database_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.formats import asbool
from ddtrace.propagation._database_monitoring import _DBM_Propagator
from ddtrace.settings.asm import config as asm_config
from ddtrace.trace import Pin


config._add(
    "mysql",
    dict(
        _default_service=schematize_service_name("mysql"),
        _dbapi_span_name_prefix="mysql",
        _dbapi_span_operation_name=schematize_database_operation("mysql.query", database_provider="mysql"),
        trace_fetch_methods=asbool(os.getenv("DD_MYSQL_TRACE_FETCH_METHODS", default=False)),
        _dbm_propagator=_DBM_Propagator(0, "query"),
    ),
)


def get_version():
    # type: () -> str
    return mysql.connector.version.VERSION_TEXT


def _supported_versions() -> Dict[str, str]:
    return {"mysql": ">=8.0.5"}


CONN_ATTR_BY_TAG = {
    net.TARGET_HOST: "server_host",
    net.TARGET_PORT: "server_port",
    net.SERVER_ADDRESS: "server_host",
    db.USER: "user",
    db.NAME: "database",
}


def patch():
    wrapt.wrap_function_wrapper("mysql.connector", "connect", _connect)
    # `Connect` is an alias for `connect`, patch it too
    if hasattr(mysql.connector, "Connect"):
        mysql.connector.Connect = mysql.connector.connect

    if asm_config._iast_enabled:
        from ddtrace.appsec._iast._metrics import _set_metric_iast_instrumented_sink
        from ddtrace.appsec._iast.constants import VULN_SQL_INJECTION

        _set_metric_iast_instrumented_sink(VULN_SQL_INJECTION)
    mysql.connector._datadog_patch = True


def unpatch():
    if isinstance(mysql.connector.connect, wrapt.ObjectProxy):
        mysql.connector.connect = mysql.connector.connect.__wrapped__
        if hasattr(mysql.connector, "Connect"):
            mysql.connector.Connect = mysql.connector.connect
    mysql.connector._datadog_patch = False


def _connect(func, instance, args, kwargs):
    conn = func(*args, **kwargs)
    return patch_conn(conn)


def patch_conn(conn):
    tags = {
        t: _convert_to_string(getattr(conn, a, None)) for t, a in CONN_ATTR_BY_TAG.items() if getattr(conn, a, "") != ""
    }
    tags[db.SYSTEM] = "mysql"
    pin = Pin(tags=tags)

    # grab the metadata from the conn
    wrapped = TracedConnection(conn, pin=pin, cfg=config.mysql)
    pin.onto(wrapped)
    return wrapped
