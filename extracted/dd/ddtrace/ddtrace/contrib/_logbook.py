r"""
Datadog APM traces can be integrated with the logs produced by ```logbook`` by:

1. Having ``ddtrace`` patch the ``logbook`` module. This will configure a
patcher which appends trace related values to the log.

2. Ensuring the logger has a format which emits new values from the log record

3. For log correlation between APM and logs, the easiest format is via JSON
so that no further configuration needs to be done in the Datadog UI assuming
that the Datadog trace values are at the top level of the JSON

Enabling
--------

Patch ``logbook``
~~~~~~~~~~~~~~~~~~~

Logbook support is auto-enabled when :ref:`ddtrace-run<ddtracerun>` and a structured logging format  (ex: JSON) is used.
To disable this integration, set the environment variable ``DD_LOGS_INJECTION=false``.

Or use :func:`patch()<ddtrace.patch>` to manually enable the integration::

    from ddtrace import patch
    patch(logbook=True)

Proper Formatting
~~~~~~~~~~~~~~~~~

The trace values are patched to every log at the top level of the record. In order to correlate
logs, it is highly recommended to use JSON logs which can be achieved by using a handler with
a proper formatting::

    handler = FileHandler('output.log', format_string='{{\"message\": "{record.message}",'
                                                          '\"dd.trace_id\": "{record.extra[dd.trace_id]}",'
                                                          '\"dd.span_id\": "{record.extra[dd.span_id]}",'
                                                          '\"dd.env\": "{record.extra[dd.env]}",'
                                                          '\"dd.service\": "{record.extra[dd.service]}",'
                                                          '\"dd.version\": "{record.extra[dd.version]}"}}')
    handler.push_application()

Note that the ``extra`` field does not have a ``dd`` object but rather only a ``dd.trace_id``, ``dd.span_id``, etc.
To access the trace values inside extra, please use the ``[]`` operator.

This will create a handler for the application that formats the logs in a way that is JSON with all the
Datadog trace values in a JSON format that can be automatically parsed by the Datadog backend.

For more information, please see the attached guide for the Datadog Logging Product:
https://docs.datadoghq.com/logs/log_collection/python/
"""
