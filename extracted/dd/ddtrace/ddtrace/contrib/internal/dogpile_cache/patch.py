try:
    import dogpile.cache as dogpile_cache
    import dogpile.lock as dogpile_lock
except AttributeError:
    from dogpile import cache as dogpile_cache
    from dogpile import lock as dogpile_lock

from typing import Dict

from wrapt import wrap_function_wrapper as _w

from ddtrace._trace.pin import _DD_PIN_NAME
from ddtrace._trace.pin import _DD_PIN_PROXY_NAME
from ddtrace.internal.schema import schematize_service_name
from ddtrace.trace import Pin

from .lock import _wrap_lock_ctor
from .region import _wrap_get_create
from .region import _wrap_get_create_multi


_get_or_create = dogpile_cache.region.CacheRegion.get_or_create
_get_or_create_multi = dogpile_cache.region.CacheRegion.get_or_create_multi
_lock_ctor = dogpile_lock.Lock.__init__


def get_version():
    # type: () -> str
    return getattr(dogpile_cache, "__version__", "")


def _supported_versions() -> Dict[str, str]:
    return {"dogpile.cache": "*"}


def patch():
    if getattr(dogpile_cache, "_datadog_patch", False):
        return
    dogpile_cache._datadog_patch = True

    _w("dogpile.cache.region", "CacheRegion.get_or_create", _wrap_get_create)
    _w("dogpile.cache.region", "CacheRegion.get_or_create_multi", _wrap_get_create_multi)
    _w("dogpile.lock", "Lock.__init__", _wrap_lock_ctor)

    Pin(service=schematize_service_name("dogpile.cache")).onto(dogpile_cache)


def unpatch():
    if not getattr(dogpile_cache, "_datadog_patch", False):
        return
    dogpile_cache._datadog_patch = False
    # This looks silly but the unwrap util doesn't support class instance methods, even
    # though wrapt does. This was causing the patches to stack on top of each other
    # during testing.
    dogpile_cache.region.CacheRegion.get_or_create = _get_or_create
    dogpile_cache.region.CacheRegion.get_or_create_multi = _get_or_create_multi
    dogpile_lock.Lock.__init__ = _lock_ctor
    setattr(dogpile_cache, _DD_PIN_NAME, None)
    setattr(dogpile_cache, _DD_PIN_PROXY_NAME, None)
