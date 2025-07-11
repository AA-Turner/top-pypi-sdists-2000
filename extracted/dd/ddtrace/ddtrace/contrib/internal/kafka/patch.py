import os
import sys
from time import time_ns
from typing import Dict

import confluent_kafka

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.ext import kafka as kafkax
from ddtrace.internal import core
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.constants import MESSAGING_DESTINATION_NAME
from ddtrace.internal.constants import MESSAGING_SYSTEM
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema import schematize_messaging_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.schema.span_attribute_schema import SpanDirection
from ddtrace.internal.utils import ArgumentError
from ddtrace.internal.utils import get_argument_value
from ddtrace.internal.utils import set_argument_value
from ddtrace.internal.utils.formats import asbool
from ddtrace.internal.utils.version import parse_version
from ddtrace.propagation.http import HTTPPropagator as Propagator
from ddtrace.trace import Pin


_Producer = confluent_kafka.Producer
_Consumer = confluent_kafka.Consumer
_SerializingProducer = confluent_kafka.SerializingProducer if hasattr(confluent_kafka, "SerializingProducer") else None
_DeserializingConsumer = (
    confluent_kafka.DeserializingConsumer if hasattr(confluent_kafka, "DeserializingConsumer") else None
)


log = get_logger(__name__)


config._add(
    "kafka",
    dict(
        _default_service=schematize_service_name("kafka"),
        distributed_tracing_enabled=asbool(os.getenv("DD_KAFKA_PROPAGATION_ENABLED", default=False)),
        trace_empty_poll_enabled=asbool(os.getenv("DD_KAFKA_EMPTY_POLL_ENABLED", default=True)),
    ),
)


def get_version():
    # type: () -> str
    return getattr(confluent_kafka, "__version__", "")


def _supported_versions() -> Dict[str, str]:
    return {"confluent_kafka": ">=1.9.2"}


KAFKA_VERSION_TUPLE = parse_version(get_version())


_SerializationContext = confluent_kafka.serialization.SerializationContext if KAFKA_VERSION_TUPLE >= (1, 4, 0) else None
_MessageField = confluent_kafka.serialization.MessageField if KAFKA_VERSION_TUPLE >= (1, 4, 0) else None


class TracedProducerMixin:
    def __init__(self, config=None, *args, **kwargs):
        if not config:
            config = kwargs
        super(TracedProducerMixin, self).__init__(config, *args, **kwargs)
        self._dd_bootstrap_servers = (
            config.get("bootstrap.servers")
            if config.get("bootstrap.servers") is not None
            else config.get("metadata.broker.list")
        )

    # in older versions of confluent_kafka, bool(Producer()) evaluates to False,
    # which makes the Pin functionality ignore it.
    def __bool__(self):
        return True

    __nonzero__ = __bool__


class TracedConsumerMixin:
    def __init__(self, config=None, *args, **kwargs):
        if not config:
            config = kwargs
        super(TracedConsumerMixin, self).__init__(config, *args, **kwargs)
        self._group_id = config.get("group.id", "")
        self._auto_commit = asbool(config.get("enable.auto.commit", True))


class TracedConsumer(TracedConsumerMixin, confluent_kafka.Consumer):
    pass


class TracedProducer(TracedProducerMixin, confluent_kafka.Producer):
    pass


class TracedDeserializingConsumer(TracedConsumerMixin, confluent_kafka.DeserializingConsumer):
    pass


class TracedSerializingProducer(TracedProducerMixin, confluent_kafka.SerializingProducer):
    pass


def patch():
    if getattr(confluent_kafka, "_datadog_patch", False):
        return
    confluent_kafka._datadog_patch = True

    confluent_kafka.Producer = TracedProducer
    confluent_kafka.Consumer = TracedConsumer
    if _SerializingProducer is not None:
        confluent_kafka.SerializingProducer = TracedSerializingProducer
    if _DeserializingConsumer is not None:
        confluent_kafka.DeserializingConsumer = TracedDeserializingConsumer

    for producer in (TracedProducer, TracedSerializingProducer):
        trace_utils.wrap(producer, "produce", traced_produce)
    for consumer in (TracedConsumer, TracedDeserializingConsumer):
        trace_utils.wrap(consumer, "poll", traced_poll_or_consume)
        trace_utils.wrap(consumer, "commit", traced_commit)

    # Consume is not implemented in deserializing consumers
    trace_utils.wrap(TracedConsumer, "consume", traced_poll_or_consume)
    Pin().onto(confluent_kafka.Producer)
    Pin().onto(confluent_kafka.Consumer)
    Pin().onto(confluent_kafka.SerializingProducer)
    Pin().onto(confluent_kafka.DeserializingConsumer)


def unpatch():
    if getattr(confluent_kafka, "_datadog_patch", False):
        confluent_kafka._datadog_patch = False

    for producer in (TracedProducer, TracedSerializingProducer):
        if trace_utils.iswrapped(producer.produce):
            trace_utils.unwrap(producer, "produce")
    for consumer in (TracedConsumer, TracedDeserializingConsumer):
        if trace_utils.iswrapped(consumer.poll):
            trace_utils.unwrap(consumer, "poll")
        if trace_utils.iswrapped(consumer.commit):
            trace_utils.unwrap(consumer, "commit")

    # Consume is not implemented in deserializing consumers
    if trace_utils.iswrapped(TracedConsumer.consume):
        trace_utils.unwrap(TracedConsumer, "consume")

    confluent_kafka.Producer = _Producer
    confluent_kafka.Consumer = _Consumer
    if _SerializingProducer is not None:
        confluent_kafka.SerializingProducer = _SerializingProducer
    if _DeserializingConsumer is not None:
        confluent_kafka.DeserializingConsumer = _DeserializingConsumer


def traced_produce(func, instance, args, kwargs):
    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return func(*args, **kwargs)

    topic = get_argument_value(args, kwargs, 0, "topic") or ""
    core.set_item("kafka_topic", topic)
    try:
        value = get_argument_value(args, kwargs, 1, "value")
    except ArgumentError:
        value = None
    message_key = kwargs.get("key", "") or ""
    partition = kwargs.get("partition", -1)
    headers = get_argument_value(args, kwargs, 6, "headers", optional=True) or {}
    with pin.tracer.trace(
        schematize_messaging_operation(kafkax.PRODUCE, provider="kafka", direction=SpanDirection.OUTBOUND),
        service=trace_utils.ext_service(pin, config.kafka),
        span_type=SpanTypes.WORKER,
    ) as span:
        cluster_id = _get_cluster_id(instance, topic)
        core.set_item("kafka_cluster_id", cluster_id)
        if cluster_id:
            span.set_tag_str(kafkax.CLUSTER_ID, cluster_id)

        core.dispatch("kafka.produce.start", (instance, args, kwargs, isinstance(instance, _SerializingProducer), span))

        span.set_tag_str(MESSAGING_SYSTEM, kafkax.SERVICE)
        span.set_tag_str(COMPONENT, config.kafka.integration_name)
        span.set_tag_str(SPAN_KIND, SpanKind.PRODUCER)
        span.set_tag_str(kafkax.TOPIC, topic)
        if topic:
            # Should fall back to broker id if topic is not provided but it is not readily available here
            span.set_tag_str(MESSAGING_DESTINATION_NAME, topic)

        if _SerializingProducer is not None and isinstance(instance, _SerializingProducer):
            serialized_key = serialize_key(instance, topic, message_key, headers)
            if serialized_key is not None:
                span.set_tag_str(kafkax.MESSAGE_KEY, serialized_key)
        else:
            span.set_tag_str(kafkax.MESSAGE_KEY, message_key)

        span.set_tag(kafkax.PARTITION, partition)
        span.set_tag_str(kafkax.TOMBSTONE, str(value is None))
        span.set_tag(_SPAN_MEASURED_KEY)
        if instance._dd_bootstrap_servers is not None:
            span.set_tag_str(kafkax.HOST_LIST, instance._dd_bootstrap_servers)

        # inject headers with Datadog tags if trace propagation is enabled
        if config.kafka.distributed_tracing_enabled:
            # inject headers with Datadog tags:
            headers = get_argument_value(args, kwargs, 6, "headers", True) or {}
            Propagator.inject(span.context, headers)
            args, kwargs = set_argument_value(args, kwargs, 6, "headers", headers, override_unset=True)
        return func(*args, **kwargs)


def traced_poll_or_consume(func, instance, args, kwargs):
    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return func(*args, **kwargs)

    # we must get start time now since execute before starting a span in order to get distributed context
    # if it exists
    start_ns = time_ns()
    err = None
    result = None
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        err = e
        raise err
    finally:
        if isinstance(result, confluent_kafka.Message):
            # poll returns a single message
            _instrument_message([result], pin, start_ns, instance, err)
        elif isinstance(result, list):
            # consume returns a list of messages,
            _instrument_message(result, pin, start_ns, instance, err)
        elif config.kafka.trace_empty_poll_enabled:
            _instrument_message([None], pin, start_ns, instance, err)

    return result


def _instrument_message(messages, pin, start_ns, instance, err):
    ctx = None
    # First message is used to extract context and enrich datadog spans
    # This approach aligns with the opentelemetry confluent kafka semantics
    first_message = messages[0] if len(messages) else None
    if first_message is not None and config.kafka.distributed_tracing_enabled and first_message.headers():
        ctx = Propagator.extract(dict(first_message.headers()))
    with pin.tracer.start_span(
        name=schematize_messaging_operation(kafkax.CONSUME, provider="kafka", direction=SpanDirection.PROCESSING),
        service=trace_utils.ext_service(pin, config.kafka),
        span_type=SpanTypes.WORKER,
        child_of=ctx if ctx is not None and ctx.trace_id is not None else pin.tracer.context_provider.active(),
        activate=True,
    ) as span:
        # reset span start time to before function call
        span.start_ns = start_ns
        cluster_id = None

        for message in messages:
            if message is not None and first_message is not None:
                cluster_id = _get_cluster_id(instance, str(first_message.topic()))
                core.set_item("kafka_cluster_id", cluster_id)
                core.set_item("kafka_topic", str(first_message.topic()))
                core.dispatch("kafka.consume.start", (instance, first_message, span))

        span.set_tag_str(MESSAGING_SYSTEM, kafkax.SERVICE)
        span.set_tag_str(COMPONENT, config.kafka.integration_name)
        span.set_tag_str(SPAN_KIND, SpanKind.CONSUMER)
        if cluster_id:
            span.set_tag_str(kafkax.CLUSTER_ID, cluster_id)
        span.set_tag_str(kafkax.RECEIVED_MESSAGE, str(first_message is not None))
        span.set_tag_str(kafkax.GROUP_ID, instance._group_id)
        if first_message is not None:
            message_key = first_message.key() or ""
            message_offset = first_message.offset() or -1
            topic = str(first_message.topic())
            span.set_tag_str(kafkax.TOPIC, topic)
            span.set_tag_str(MESSAGING_DESTINATION_NAME, topic)

            # If this is a deserializing consumer, do not set the key as a tag since we
            # do not have the serialization function
            if (
                (_DeserializingConsumer is not None and not isinstance(instance, _DeserializingConsumer))
                or isinstance(message_key, str)
                or isinstance(message_key, bytes)
            ):
                span.set_tag_str(kafkax.MESSAGE_KEY, message_key)
            span.set_tag(kafkax.PARTITION, first_message.partition())
            is_tombstone = False
            try:
                is_tombstone = len(first_message) == 0
            except TypeError:  # https://github.com/confluentinc/confluent-kafka-python/issues/1192
                pass
            span.set_tag_str(kafkax.TOMBSTONE, str(is_tombstone))
            span.set_tag(kafkax.MESSAGE_OFFSET, message_offset)
        span.set_tag(_SPAN_MEASURED_KEY)

        if err is not None:
            span.set_exc_info(*sys.exc_info())


def traced_commit(func, instance, args, kwargs):
    pin = Pin.get_from(instance)
    if not pin or not pin.enabled():
        return func(*args, **kwargs)

    core.dispatch("kafka.commit.start", (instance, args, kwargs))
    return func(*args, **kwargs)


def serialize_key(instance, topic, key, headers):
    if _SerializationContext is not None and _MessageField is not None:
        ctx = _SerializationContext(topic, _MessageField.KEY, headers)
        if hasattr(instance, "_key_serializer") and instance._key_serializer is not None:
            try:
                key = instance._key_serializer(key, ctx)
                return key
            except Exception:
                log.debug("Failed to set Kafka Consumer key tag: %s", str(key))
                return None
        else:
            log.warning("Failed to set Kafka Consumer key tag, no method available to serialize key: %s", str(key))
            return None


def _get_cluster_id(instance, topic):
    if instance and getattr(instance, "_dd_cluster_id", None):
        return instance._dd_cluster_id

    if getattr(instance, "list_topics", None) is None:
        return None

    cluster_metadata = instance.list_topics(topic=topic)
    if cluster_metadata and getattr(cluster_metadata, "cluster_id", None):
        instance._dd_cluster_id = cluster_metadata.cluster_id
        return cluster_metadata.cluster_id
    return None
