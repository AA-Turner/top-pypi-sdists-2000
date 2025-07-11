import os
from typing import Dict

import mariadb
import wrapt

from ddtrace import config
from ddtrace.contrib.dbapi import TracedConnection
from ddtrace.ext import db
from ddtrace.ext import net
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.formats import asbool
from ddtrace.internal.utils.wrappers import unwrap
from ddtrace.trace import Pin


config._add(
    "mariadb",
    dict(
        trace_fetch_methods=asbool(os.getenv("DD_MARIADB_TRACE_FETCH_METHODS", default=False)),
        _default_service=schematize_service_name("mariadb"),
        _dbapi_span_name_prefix="mariadb",
    ),
)


def get_version():
    # type: () -> str
    return getattr(mariadb, "__version__", "")


def _supported_versions() -> Dict[str, str]:
    return {"mariadb": ">=1.0.0"}


def patch():
    if getattr(mariadb, "_datadog_patch", False):
        return
    mariadb._datadog_patch = True
    wrapt.wrap_function_wrapper("mariadb", "connect", _connect)


def unpatch():
    if getattr(mariadb, "_datadog_patch", False):
        mariadb._datadog_patch = False
        unwrap(mariadb, "connect")


def _connect(func, instance, args, kwargs):
    conn = func(*args, **kwargs)
    tags = {
        net.TARGET_HOST: kwargs.get("host", "127.0.0.1"),
        net.TARGET_PORT: kwargs.get("port", 3306),
        net.SERVER_ADDRESS: kwargs.get("host", "127.0.0.1"),
        db.USER: kwargs.get("user", "test"),
        db.NAME: kwargs.get("database", "test"),
        db.SYSTEM: "mariadb",
    }

    pin = Pin(tags=tags)

    wrapped = TracedConnection(conn, pin=pin, cfg=config.mariadb)
    pin.onto(wrapped)
    return wrapped
