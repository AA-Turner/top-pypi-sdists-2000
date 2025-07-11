#!/usr/bin/env python3
from collections import abc
from typing import Any
from typing import List
from typing import Optional
from typing import Union

from ddtrace.appsec._constants import IAST
from ddtrace.appsec._iast._taint_tracking._taint_objects import taint_pyobject
from ddtrace.appsec._iast._taint_tracking._taint_objects_base import is_pyobject_tainted
from ddtrace.internal.logger import get_logger
from ddtrace.settings.asm import config as asm_config


DBAPI_PREFIXES = ("django-",)

log = get_logger(__name__)


# Non Lazy Tainting


# don't use dataclass that can create circular import problems here
# @dataclasses.dataclass
class _DeepTaintCommand:
    def __init__(
        self,
        pre: bool,
        source_key: str,
        obj: Any,
        store_struct: Union[list, dict],
        key: Optional[List[str]] = None,
        struct: Optional[Union[list, dict]] = None,
        is_key: bool = False,
    ):
        self.pre = pre
        self.source_key = source_key
        self.obj = obj
        self.store_struct = store_struct
        self.key = key
        self.struct = struct
        self.is_key = is_key

    def store(self, value):
        if isinstance(self.store_struct, list):
            self.store_struct.append(value)
        elif isinstance(self.store_struct, dict):
            key = self.key[0] if self.key else None
            self.store_struct[key] = value
        else:
            raise ValueError(f"store_struct of type {type(self.store_struct)}")

    def post(self, struct):
        return self.__class__(False, self.source_key, self.obj, self.store_struct, self.key, struct)


def build_new_tainted_object_from_generic_object(initial_object, wanted_object):
    if initial_object.__class__ is wanted_object.__class__:
        return wanted_object
    #### custom tailor actions
    wanted_type = initial_object.__class__.__module__, initial_object.__class__.__name__
    if wanted_type == ("builtins", "tuple"):
        return tuple(wanted_object)
    # Django
    if wanted_type == ("django.http.request", "HttpHeaders"):
        res = initial_object.__class__({})
        res._store = {k.lower(): (k, v) for k, v in wanted_object.items()}
        return res
    if wanted_type == ("django.http.request", "QueryDict"):
        res = initial_object.__class__()
        for k, v in wanted_object.items():
            dict.__setitem__(res, k, v)
        return res
    # Flask 2+
    if wanted_type == ("werkzeug.datastructures.structures", "ImmutableMultiDict"):
        return initial_object.__class__(wanted_object)
    # Flask 1
    if wanted_type == ("werkzeug.datastructures", "ImmutableMultiDict"):
        return initial_object.__class__(wanted_object)

    # if the class is unknown, return the initial object
    # this may prevent interned string to be tainted but ensure
    # that normal behavior of the code is not changed.
    return initial_object


def taint_structure(main_obj, source_key, source_value, override_pyobject_tainted=False):
    """taint any structured object
    use a queue like mechanism to avoid recursion
    Best effort: mutate mutable structures and rebuild immutable ones if possible
    """
    if not main_obj:
        return main_obj

    main_res = []
    try:
        # fifo contains tuple (pre/post:bool, source key, object to taint,
        # key to use, struct to store result, struct to )
        stack = [_DeepTaintCommand(True, source_key, main_obj, main_res)]
        while stack:
            command = stack.pop()
            if command.pre:  # first processing of the object
                if not command.obj:
                    command.store(command.obj)
                elif isinstance(command.obj, IAST.TEXT_TYPES):
                    if override_pyobject_tainted or not is_pyobject_tainted(command.obj):
                        new_obj = taint_pyobject(
                            pyobject=command.obj,
                            source_name=command.source_key,
                            source_value=command.obj,
                            source_origin=source_key if command.is_key else source_value,
                        )
                        command.store(new_obj)
                    else:
                        command.store(command.obj)
                elif isinstance(command.obj, abc.Mapping):
                    res = {}
                    stack.append(command.post(res))
                    # use dict fundamental enumeration if possible to bypass any override of custom classes
                    iterable = dict.items(command.obj) if isinstance(command.obj, dict) else command.obj.items()
                    todo = []
                    for k, v in list(iterable):
                        key_store = []
                        todo.append(_DeepTaintCommand(True, str(k), k, key_store, is_key=True))
                        todo.append(_DeepTaintCommand(True, str(k), v, res, key_store))
                    stack.extend(reversed(todo))
                elif isinstance(command.obj, abc.Sequence):
                    res = []
                    stack.append(command.post(res))
                    todo = [_DeepTaintCommand(True, command.source_key, v, res) for v in command.obj]
                    stack.extend(reversed(todo))
                else:
                    command.store(command.obj)
            else:
                command.store(build_new_tainted_object_from_generic_object(command.obj, command.struct))
    except Exception:
        log.debug("taint_structure error", exc_info=True)
        pass
    finally:
        return main_res[0] if main_res else main_obj


# Lazy Tainting


def _is_tainted_struct(obj):
    return hasattr(obj, "_origins")


class LazyTaintList:
    """
    Encapsulate a list to lazily taint all content on any depth
    It will appear and act as the original list except for some additional private fields
    """

    def __init__(self, original_list, origins=(0, 0), override_pyobject_tainted=False, source_name="[]"):
        self._obj = original_list._obj if _is_tainted_struct(original_list) else original_list
        self._origins = origins
        self._origin_value = origins[1]
        self._override_pyobject_tainted = override_pyobject_tainted
        self._source_name = source_name

    def _taint(self, value):
        if value:
            if isinstance(value, IAST.TEXT_TYPES):
                if not is_pyobject_tainted(value) or self._override_pyobject_tainted:
                    try:
                        # TODO: migrate this part to shift ranges instead of creating a new one
                        value = taint_pyobject(
                            pyobject=value,
                            source_name=self._source_name,
                            source_value=value,
                            source_origin=self._origin_value,
                        )
                    except SystemError:
                        # TODO: Find the root cause for
                        # SystemError: NULL object passed to Py_BuildValue
                        log.debug("IAST SystemError while tainting value: %s", value, exc_info=True)
                    except Exception:
                        log.debug("IAST Unexpected exception while tainting value", exc_info=True)
            elif isinstance(value, abc.Mapping) and not _is_tainted_struct(value):
                value = LazyTaintDict(
                    value, origins=self._origins, override_pyobject_tainted=self._override_pyobject_tainted
                )
            elif isinstance(value, abc.Sequence) and not _is_tainted_struct(value):
                value = LazyTaintList(
                    value,
                    origins=self._origins,
                    override_pyobject_tainted=self._override_pyobject_tainted,
                    source_name=self._source_name,
                )
        return value

    def __add__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return LazyTaintList(
            self._obj + other,
            origins=self._origins,
            override_pyobject_tainted=self._override_pyobject_tainted,
            source_name=self._source_name,
        )

    @property  # type: ignore
    def __class__(self):
        return list

    def __contains__(self, item):
        return item in self._obj

    def __delitem__(self, key):
        del self._obj[key]

    def __eq__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj == other

    def __ge__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj >= other

    def __getitem__(self, key):
        return self._taint(self._obj[key])

    def __gt__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj > other

    def __iadd__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        self._obj += other

    def __imul__(self, other):
        self._obj *= other

    def __iter__(self):
        return (self[i] for i in range(len(self._obj)))

    def __le__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj <= other

    def __len__(self):
        return len(self._obj)

    def __lt__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj < other

    def __mul__(self, other):
        return LazyTaintList(
            self._obj * other,
            origins=self._origins,
            override_pyobject_tainted=self._override_pyobject_tainted,
            source_name=self._source_name,
        )

    def __ne__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj != other

    def __repr__(self):
        return repr(self._obj)

    def __reversed__(self):
        return (self[i] for i in reversed(range(len(self._obj))))

    def __setitem__(self, key, value):
        self._obj[key] = value

    def __str__(self):
        return str(self._obj)

    def append(self, item):
        self._obj.append(item)

    def clear(self):
        # TODO: stop tainting in this case
        self._obj.clear()

    def copy(self):
        return LazyTaintList(
            self._obj.copy(),
            origins=self._origins,
            override_pyobject_tainted=self._override_pyobject_tainted,
            source_name=self._source_name,
        )

    def count(self, *args):
        return self._obj.count(*args)

    def extend(self, *args):
        return self._obj.extend(*args)

    def index(self, *args):
        return self._obj.index(*args)

    def insert(self, *args):
        return self._obj.insert(*args)

    def pop(self, *args):
        return self._taint(self._obj.pop(*args))

    def remove(self, *args):
        return self._obj.remove(*args)

    def reverse(self, *args):
        return self._obj.reverse(*args)

    def sort(self, *args):
        return self._obj.sort(*args)

    # psycopg2 support
    def __conform__(self, proto):
        return self

    def getquoted(self) -> bytes:
        import psycopg2.extensions as ext

        value = ext.adapt(self._obj).getquoted()
        value = self._taint(value)
        return value


class LazyTaintDict:
    def __init__(self, original_dict, origins=(0, 0), override_pyobject_tainted=False):
        from ddtrace.appsec._iast._taint_tracking import OriginType

        self._obj = original_dict
        self._origins = origins
        self._origin_key = origins[0] if origins[0] else OriginType.PARAMETER_NAME
        self._origin_value = origins[1] if origins[1] else OriginType.PARAMETER
        self._override_pyobject_tainted = override_pyobject_tainted

    def _taint(self, value, key, origin=None):
        if origin is None:
            origin = self._origin_value
        if value:
            if isinstance(value, IAST.TEXT_TYPES):
                if not is_pyobject_tainted(value) or self._override_pyobject_tainted:
                    try:
                        # TODO: migrate this part to shift ranges instead of creating a new one
                        value = taint_pyobject(
                            pyobject=value,
                            source_name=key,
                            source_value=value,
                            source_origin=origin,
                        )
                    except Exception:
                        log.debug("IAST Unexpected exception while tainting value", exc_info=True)
            elif isinstance(value, abc.Mapping) and not _is_tainted_struct(value):
                value = LazyTaintDict(
                    value, origins=self._origins, override_pyobject_tainted=self._override_pyobject_tainted
                )
            elif isinstance(value, abc.Sequence) and not _is_tainted_struct(value):
                value = LazyTaintList(
                    value,
                    origins=self._origins,
                    override_pyobject_tainted=self._override_pyobject_tainted,
                    source_name=key,
                )
        return value

    @property  # type: ignore
    def __class__(self):
        return dict

    def __contains__(self, item):
        return item in self._obj

    def __delitem__(self, key):
        del self._obj[key]

    def __eq__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj == other

    def __ge__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj >= other

    def __getitem__(self, key):
        return self._taint(self._obj[key], key)

    def __gt__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj > other

    def __ior__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        self._obj |= other

    def __iter__(self):
        return iter(self.keys())

    def __le__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj <= other

    def __len__(self):
        return len(self._obj)

    def __lt__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj < other

    def __ne__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return self._obj != other

    def __or__(self, other):
        if _is_tainted_struct(other):
            other = other._obj
        return LazyTaintDict(
            self._obj | other,
            origins=self._origins,
            override_pyobject_tainted=self._override_pyobject_tainted,
        )

    def __repr__(self):
        return repr(self._obj)

    def __reversed__(self):
        return reversed(self.keys())

    def __setitem__(self, key, value):
        self._obj[key] = value

    def __str__(self):
        return str(self._obj)

    def clear(self):
        # TODO: stop tainting in this case
        self._obj.clear()

    def copy(self):
        return LazyTaintDict(
            self._obj.copy(),
            origins=self._origins,
            override_pyobject_tainted=self._override_pyobject_tainted,
        )

    @classmethod
    def fromkeys(cls, *args):
        return dict.fromkeys(*args)

    def get(self, key, default=None):
        observer = object()
        res = self._obj.get(key, observer)
        if res is observer:
            return default
        return self._taint(res, key)

    def items(self):
        for k in self.keys():
            yield (k, self[k])

    def keys(self):
        for k in self._obj.keys():
            yield self._taint(k, k, self._origin_key)

    def pop(self, *args):
        return self._taint(self._obj.pop(*args), "pop")

    def popitem(self):
        k, v = self._obj.popitem()
        return self._taint(k, k), self._taint(v, k)

    def remove(self, *args):
        return self._obj.remove(*args)

    def setdefault(self, *args):
        return self._taint(self._obj.setdefault(*args), args[0])

    def update(self, *args, **kargs):
        self._obj.update(*args, **kargs)

    def values(self):
        for _, v in self.items():
            yield v

    # Django Query Dict support
    def getlist(self, key, default=None):
        return self._taint(self._obj.getlist(key, default=default), key)

    def setlist(self, key, list_):
        self._obj.setlist(key, list_)

    def appendlist(self, key, item):
        self._obj.appendlist(key, item)

    def setlistdefault(self, key, default_list=None):
        return self._taint(self._obj.setlistdefault(key, default_list=default_list), key)

    def lists(self):
        return self._taint(self._obj.lists(), self._origin_value)

    def dict(self):
        return self

    def urlencode(self, safe=None):
        return self._taint(self._obj.urlencode(safe=safe), self._origin_value)


if asm_config._iast_lazy_taint:
    # redefining taint_structure to use lazy object if required

    def taint_structure(main_obj, origin_key, origin_value, override_pyobject_tainted=False):  # noqa: F811
        if isinstance(main_obj, abc.Mapping):
            return LazyTaintDict(main_obj, (origin_key, origin_value), override_pyobject_tainted)
        elif isinstance(main_obj, abc.Sequence):
            return LazyTaintList(main_obj, (origin_key, origin_value), override_pyobject_tainted)


def taint_dictionary(origin_key, origin_value, original_func, instance, args, kwargs):
    result = original_func(*args, **kwargs)

    return taint_structure(result, origin_key, origin_value, override_pyobject_tainted=True)
