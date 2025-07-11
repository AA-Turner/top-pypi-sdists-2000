import os
from typing import Dict

# 3p
import rediscluster
import wrapt

# project
from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.redis.patch import instrumented_execute_command
from ddtrace.contrib.internal.redis.patch import instrumented_pipeline
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.ext import db
from ddtrace.ext import redis as redisx
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.schema import schematize_cache_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.formats import CMD_MAX_LEN
from ddtrace.internal.utils.formats import asbool
from ddtrace.internal.utils.formats import stringify_cache_args
from ddtrace.internal.utils.wrappers import unwrap
from ddtrace.trace import Pin


# DEV: In `2.0.0` `__version__` is a string and `VERSION` is a tuple,
#      but in `1.x.x` `__version__` is a tuple and `VERSION` does not exist
REDISCLUSTER_VERSION = getattr(rediscluster, "VERSION", rediscluster.__version__)

config._add(
    "rediscluster",
    dict(
        _default_service=schematize_service_name("rediscluster"),
        cmd_max_length=int(os.getenv("DD_REDISCLUSTER_CMD_MAX_LENGTH", CMD_MAX_LEN)),
        resource_only_command=asbool(os.getenv("DD_REDIS_RESOURCE_ONLY_COMMAND", True)),
    ),
)


def get_version():
    # type: () -> str
    return getattr(rediscluster, "__version__", "")


def _supported_versions() -> Dict[str, str]:
    return {"rediscluster": ">=2.0"}


def patch():
    """Patch the instrumented methods"""
    if getattr(rediscluster, "_datadog_patch", False):
        return
    rediscluster._datadog_patch = True

    _w = wrapt.wrap_function_wrapper
    if REDISCLUSTER_VERSION >= (2, 0, 0):
        _w("rediscluster", "client.RedisCluster.execute_command", instrumented_execute_command(config.rediscluster))
        _w("rediscluster", "client.RedisCluster.pipeline", instrumented_pipeline)
        _w("rediscluster", "pipeline.ClusterPipeline.execute", traced_execute_pipeline)
        Pin().onto(rediscluster.RedisCluster)
    else:
        _w("rediscluster", "StrictRedisCluster.execute_command", instrumented_execute_command(config.rediscluster))
        _w("rediscluster", "StrictRedisCluster.pipeline", instrumented_pipeline)
        _w("rediscluster", "StrictClusterPipeline.execute", traced_execute_pipeline)
        Pin().onto(rediscluster.StrictRedisCluster)


def unpatch():
    if getattr(rediscluster, "_datadog_patch", False):
        rediscluster._datadog_patch = False

        if REDISCLUSTER_VERSION >= (2, 0, 0):
            unwrap(rediscluster.client.RedisCluster, "execute_command")
            unwrap(rediscluster.client.RedisCluster, "pipeline")
            unwrap(rediscluster.pipeline.ClusterPipeline, "execute")
        else:
            unwrap(rediscluster.StrictRedisCluster, "execute_command")
            unwrap(rediscluster.StrictRedisCluster, "pipeline")
            unwrap(rediscluster.StrictClusterPipeline, "execute")


#
# tracing functions
#


def traced_execute_pipeline(func, instance, args, kwargs):
    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return func(*args, **kwargs)

    cmds = [
        stringify_cache_args(c.args, cmd_max_len=config.rediscluster.cmd_max_length) for c in instance.command_stack
    ]
    resource = "\n".join(cmds)
    tracer = pin.tracer
    with tracer.trace(
        schematize_cache_operation(redisx.CMD, cache_provider=redisx.APP),
        resource=resource,
        service=trace_utils.ext_service(pin, config.rediscluster, "rediscluster"),
        span_type=SpanTypes.REDIS,
    ) as s:
        s.set_tag_str(SPAN_KIND, SpanKind.CLIENT)
        s.set_tag_str(COMPONENT, config.rediscluster.integration_name)
        s.set_tag_str(db.SYSTEM, redisx.APP)
        s.set_tag(_SPAN_MEASURED_KEY)
        s.set_tag_str(redisx.RAWCMD, resource)
        s.set_metric(redisx.PIPELINE_LEN, len(instance.command_stack))

        return func(*args, **kwargs)
