from ddtrace import config
from ddtrace.internal import core
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.logger import get_logger
from ddtrace.internal.utils import ArgumentError
from ddtrace.internal.utils import get_argument_value

from ..constants import _SPAN_MEASURED_KEY
from ..constants import SPAN_KIND
from ..ext import SpanKind
from ..ext import SpanTypes
from ..trace import Pin
from .dbapi import TracedConnection
from .dbapi import TracedCursor
from .internal.trace_utils import ext_service
from .internal.trace_utils import iswrapped


log = get_logger(__name__)


def get_version():
    # type: () -> str
    return ""


class TracedAsyncCursor(TracedCursor):
    async def __aenter__(self):
        # previous versions of the dbapi didn't support context managers. let's
        # reference the func that would be called to ensure that error
        # messages will be the same.
        await self.__wrapped__.__aenter__()

        return self

    def __aiter__(self):
        return self.__wrapped__.__aiter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # previous versions of the dbapi didn't support context managers. let's
        # reference the func that would be called to ensure that error
        # messages will be the same.
        return await self.__wrapped__.__aexit__(exc_type, exc_val, exc_tb)

    async def _trace_method(self, method, name, resource, extra_tags, dbm_propagator, *args, **kwargs):
        """
        Internal function to trace the call to the underlying cursor method
        :param method: The callable to be wrapped
        :param name: The name of the resulting span.
        :param resource: The sql query. Sql queries are obfuscated on the agent side.
        :param extra_tags: A dict of tags to store into the span's meta
        :param dbm_propagator: _DBM_Propagator, prepends dbm comments to sql statements
        :param args: The args that will be passed as positional args to the wrapped method
        :param kwargs: The args that will be passed as kwargs to the wrapped method
        :return: The result of the wrapped method invocation
        """
        pin = Pin.get_from(self)
        if not pin or not pin.enabled():
            return await method(*args, **kwargs)
        measured = name == self._self_datadog_name

        with pin.tracer.trace(
            name, service=ext_service(pin, self._self_config), resource=resource, span_type=SpanTypes.SQL
        ) as s:
            if measured:
                s.set_tag(_SPAN_MEASURED_KEY)
            # No reason to tag the query since it is set as the resource by the agent. See:
            # https://github.com/DataDog/datadog-trace-agent/blob/bda1ebbf170dd8c5879be993bdd4dbae70d10fda/obfuscate/sql.go#L232
            s.set_tags(pin.tags)
            s.set_tags(extra_tags)

            s.set_tag_str(COMPONENT, self._self_config.integration_name)

            # set span.kind to the type of request being performed
            s.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

            # Security and IAST validations
            core.dispatch("db_query_check", (args, kwargs, self._self_config.integration_name, method))

            # dispatch DBM
            if dbm_propagator:
                # this check is necessary to prevent fetch methods from trying to add dbm propagation
                result = core.dispatch_with_results(
                    f"{self._self_config.integration_name}.execute", (self._self_config, s, args, kwargs)
                ).result
                if result:
                    s, args, kwargs = result.value

            try:
                return await method(*args, **kwargs)
            finally:
                # Try to fetch custom properties that were passed by the specific Database implementation
                self._set_post_execute_tags(s)

    async def executemany(self, query, *args, **kwargs):
        """Wraps the cursor.executemany method"""
        self._self_last_execute_operation = query
        # Always return the result as-is
        # DEV: Some libraries return `None`, others `int`, and others the cursor objects
        #      These differences should be overridden at the integration specific layer (e.g. in `sqlite3/patch.py`)
        # FIXME[matt] properly handle kwargs here. arg names can be different
        # with different libs.
        return await self._trace_method(
            self.__wrapped__.executemany,
            self._self_datadog_name,
            query,
            {"sql.executemany": "true"},
            self._self_dbm_propagator,
            query,
            *args,
            **kwargs,
        )

    async def execute(self, query, *args, **kwargs):
        """Wraps the cursor.execute method"""
        self._self_last_execute_operation = query

        # Always return the result as-is
        # DEV: Some libraries return `None`, others `int`, and others the cursor objects
        #      These differences should be overridden at the integration specific layer (e.g. in `sqlite3/patch.py`)
        return await self._trace_method(
            self.__wrapped__.execute,
            self._self_datadog_name,
            query,
            {},
            self._self_dbm_propagator,
            query,
            *args,
            **kwargs,
        )


class FetchTracedAsyncCursor(TracedAsyncCursor):
    """FetchTracedAsyncCursor for psycopg"""

    async def fetchone(self, *args, **kwargs):
        """Wraps the cursor.fetchone method"""
        span_name = "{}.{}".format(self._self_datadog_name, "fetchone")
        return await self._trace_method(
            self.__wrapped__.fetchone, span_name, self._self_last_execute_operation, {}, None, *args, **kwargs
        )

    async def fetchall(self, *args, **kwargs):
        """Wraps the cursor.fetchall method"""
        span_name = "{}.{}".format(self._self_datadog_name, "fetchall")
        return await self._trace_method(
            self.__wrapped__.fetchall, span_name, self._self_last_execute_operation, {}, None, *args, **kwargs
        )

    async def fetchmany(self, *args, **kwargs):
        """Wraps the cursor.fetchmany method"""
        span_name = "{}.{}".format(self._self_datadog_name, "fetchmany")
        # We want to trace the information about how many rows were requested. Note that this number may be larger
        # the number of rows actually returned if less then requested are available from the query.
        size_tag_key = "db.fetch.size"

        try:
            extra_tags = {size_tag_key: get_argument_value(args, kwargs, 0, "size")}
        except ArgumentError:
            default_array_size = getattr(self.__wrapped__, "arraysize", None)
            extra_tags = {size_tag_key: default_array_size} if default_array_size else {}

        return await self._trace_method(
            self.__wrapped__.fetchmany, span_name, self._self_last_execute_operation, extra_tags, None, *args, **kwargs
        )


class TracedAsyncConnection(TracedConnection):
    def __init__(self, conn, pin=None, cfg=config.dbapi2, cursor_cls=None):
        if not cursor_cls:
            # Do not trace `fetch*` methods by default
            cursor_cls = FetchTracedAsyncCursor if cfg.trace_fetch_methods else TracedAsyncCursor
        super(TracedAsyncConnection, self).__init__(conn, pin, cfg, cursor_cls)

    async def __aenter__(self):
        """Context management is not defined by the dbapi spec.

        This means unfortunately that the database clients each define their own
        implementations.

        The ones we know about are:

        - mysqlclient<2.0 which returns a cursor instance. >=2.0 returns a
          connection instance.
        - psycopg returns a connection.
        - pyodbc returns a connection.
        - pymysql doesn't implement it.
        - sqlite3 returns the connection.
        """
        r = await self.__wrapped__.__aenter__()

        if hasattr(r, "cursor"):
            # r is Connection-like.
            if r is self.__wrapped__:
                # Return the reference to this proxy object. Returning r would
                # return the untraced reference.
                return self
            else:
                # r is a different connection object.
                # This should not happen in practice but play it safe so that
                # the original functionality is maintained.
                log.warning(
                    "Unexpected object type returned from __wrapped__.__aenter__()."
                    "Expected a wrapped instance, but received a different object."
                )
                return r
        elif hasattr(r, "execute"):
            # r is Cursor-like.
            if iswrapped(r):
                return r
            else:
                pin = Pin.get_from(self)
                if not pin:
                    return r
                return self._self_cursor_cls(r, pin, self._self_config)
        else:
            # Otherwise r is some other object, so maintain the functionality
            # of the original.
            log.warning(
                "Unexpected object type returned from __wrapped__.__aenter__()."
                "Expected a wrapped instance, but received a different object."
            )
            return r

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # previous versions of the dbapi didn't support context managers. let's
        # reference the func that would be called to ensure that errors
        # messages will be the same.
        return await self.__wrapped__.__aexit__(exc_type, exc_val, exc_tb)

    async def _trace_method(self, method, name, extra_tags, *args, **kwargs):
        pin = Pin.get_from(self)
        if not pin or not pin.enabled():
            return await method(*args, **kwargs)

        with pin.tracer.trace(name, service=ext_service(pin, self._self_config)) as s:
            s.set_tag_str(COMPONENT, self._self_config.integration_name)

            # set span.kind to the type of request being performed
            s.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

            s.set_tags(pin.tags)
            s.set_tags(extra_tags)

            return await method(*args, **kwargs)

    async def commit(self, *args, **kwargs):
        span_name = "{}.{}".format(self._self_datadog_name, "commit")
        return await self._trace_method(self.__wrapped__.commit, span_name, {}, *args, **kwargs)

    async def rollback(self, *args, **kwargs):
        span_name = "{}.{}".format(self._self_datadog_name, "rollback")
        return await self._trace_method(self.__wrapped__.rollback, span_name, {}, *args, **kwargs)
