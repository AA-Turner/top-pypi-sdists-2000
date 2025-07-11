import os
import typing as t

from ddtrace.internal.forksafe import has_forked
from ddtrace.internal.logger import get_logger
from ddtrace.internal.products import manager as product_manager
from ddtrace.internal.remoteconfig import Payload
from ddtrace.internal.remoteconfig._connectors import PublisherSubscriberConnector
from ddtrace.internal.remoteconfig._publishers import RemoteConfigPublisher
from ddtrace.internal.remoteconfig._pubsub import PubSub
from ddtrace.internal.remoteconfig._subscribers import RemoteConfigSubscriber
from ddtrace.internal.remoteconfig.worker import remoteconfig_poller
from ddtrace.internal.runtime import get_ancestor_runtime_id
from ddtrace.internal.symbol_db.symbols import SymbolDatabaseUploader


DI_PRODUCT_KEY = "dynamic-instrumentation"

log = get_logger(__name__)


def _rc_callback(data: t.List[Payload], test_tracer=None):
    if get_ancestor_runtime_id() is not None and has_forked():
        log.debug("[PID %d] SymDB: Disabling Symbol DB in forked process", os.getpid())
        # We assume that forking is being used for spawning child worker
        # processes. Therefore, we avoid uploading the same symbols from each
        # child process. We restrict the enablement of Symbol DB to just the
        # parent process and the first fork child.
        remoteconfig_poller.unregister("LIVE_DEBUGGING_SYMBOL_DB")

        if SymbolDatabaseUploader.is_installed():
            SymbolDatabaseUploader.uninstall()

        return

    for payload in data:
        if payload.metadata is None:
            continue

        config = payload.content
        if not isinstance(config, dict):
            continue

        upload_symbols = config.get("upload_symbols")
        if upload_symbols is None:
            continue

        if upload_symbols:
            log.debug("[PID %d] SymDB: Symbol DB RCM enablement signal received", os.getpid())
            if not SymbolDatabaseUploader.is_installed():
                try:
                    SymbolDatabaseUploader.install(shallow=not product_manager.is_enabled(DI_PRODUCT_KEY))
                    log.debug("[PID %d] SymDB: Symbol DB uploader installed", os.getpid())
                except Exception:
                    log.error("[PID %d] SymDB: Failed to install Symbol DB uploader", os.getpid(), exc_info=True)
                    remoteconfig_poller.unregister("LIVE_DEBUGGING_SYMBOL_DB")
            else:
                SymbolDatabaseUploader.update()
        else:
            log.debug("[PID %d] SymDB: Symbol DB RCM shutdown signal received", os.getpid())
            if SymbolDatabaseUploader.is_installed():
                try:
                    SymbolDatabaseUploader.uninstall()
                    log.debug("[PID %d] SymDB: Symbol DB uploader uninstalled", os.getpid())
                except Exception:
                    log.error("[PID %d] SymDB: Failed to uninstall Symbol DB uploader", os.getpid(), exc_info=True)
                    remoteconfig_poller.unregister("LIVE_DEBUGGING_SYMBOL_DB")
        break


class SymbolDatabaseAdapter(PubSub):
    __publisher_class__ = RemoteConfigPublisher
    __subscriber_class__ = RemoteConfigSubscriber
    __shared_data__ = PublisherSubscriberConnector()

    def __init__(self):
        self._publisher = self.__publisher_class__(self.__shared_data__)
        self._subscriber = self.__subscriber_class__(self.__shared_data__, _rc_callback, "LIVE_DEBUGGING_SYMBOL_DB")
