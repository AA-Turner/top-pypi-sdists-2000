from collections import deque
from dis import findlinestarts
from functools import lru_cache
from functools import partial
from functools import singledispatch
from pathlib import Path
from types import CodeType
from types import FunctionType
from typing import Iterator
from typing import List
from typing import MutableMapping
from typing import Set
from typing import cast

from ddtrace.internal.safety import _isinstance


@singledispatch
def linenos(_) -> Set[int]:
    raise NotImplementedError()


@linenos.register
def _(code: CodeType) -> Set[int]:
    """Get the line numbers of a function."""
    return {ln for _, ln in findlinestarts(code) if ln is not None} - {code.co_firstlineno}


@linenos.register
def _(f: FunctionType) -> Set[int]:
    return linenos(f.__code__)


def undecorated(f: FunctionType, name: str, path: Path) -> FunctionType:
    # Find the original function object from a decorated function. We use the
    # expected function name to guide the search and pick the correct function.
    # The recursion is needed in case of multiple decorators. We make it BFS
    # to find the function as soon as possible.

    def match(g):
        return g.__code__.co_name == name and Path(g.__code__.co_filename).resolve() == path

    if _isinstance(f, FunctionType) and match(f):
        return f

    seen_functions = {f}
    q = deque([f])  # FIFO: use popleft and append

    while q:
        g = q.popleft()

        # Look for a wrapped function. These attributes are generally used by
        # the decorators provided by the standard library (e.g. partial)
        for attr in ("__wrapped__", "func"):
            try:
                wrapped = object.__getattribute__(g, attr)
                if _isinstance(wrapped, FunctionType) and wrapped not in seen_functions:
                    if match(wrapped):
                        return wrapped
                    q.append(wrapped)
                    seen_functions.add(wrapped)
            except AttributeError:
                pass

        # A partial object is a common decorator. The function can either be the
        # curried function, or it can appear as one of the arguments (e.g. the
        # implementation of the wraps decorator).
        if _isinstance(g, partial):
            p = cast(partial, g)
            if match(p.func):
                return cast(FunctionType, p.func)
            for arg in p.args:
                if _isinstance(arg, FunctionType) and arg not in seen_functions:
                    if match(arg):
                        return arg
                    q.append(arg)
                    seen_functions.add(arg)
            for arg in p.keywords.values():
                if _isinstance(arg, FunctionType) and arg not in seen_functions:
                    if match(arg):
                        return arg
                    q.append(arg)
                    seen_functions.add(arg)

        # Look for a closure (function decoration)
        if _isinstance(g, FunctionType):
            for c in (_.cell_contents for _ in (g.__closure__ or []) if _isinstance(_.cell_contents, FunctionType)):
                if c not in seen_functions:
                    if match(c):
                        return c
                    q.append(c)
                    seen_functions.add(c)

        # Look for a function attribute (method decoration)
        # DEV: We don't recurse over arbitrary objects. We stop at the first
        # depth level.
        try:
            for v in object.__getattribute__(g, "__dict__").values():
                if _isinstance(v, FunctionType) and v not in seen_functions and match(v):
                    return v
        except AttributeError:
            # Maybe we have slots
            try:
                for v in (object.__getattribute__(g, _) for _ in object.__getattribute__(g, "__slots__")):
                    if _isinstance(v, FunctionType) and v not in seen_functions and match(v):
                        return v
            except AttributeError:
                pass

        # Last resort
        try:
            for v in (object.__getattribute__(g, a) for a in object.__dir__(g)):
                if _isinstance(v, FunctionType) and v not in seen_functions and match(v):
                    return v
        except AttributeError:
            pass

    return f


def collect_code_objects(code: CodeType) -> Iterator[CodeType]:
    q = deque([code])
    while q:
        c = q.popleft()
        for new_code in (_ for _ in c.co_consts if isinstance(_, CodeType)):
            yield new_code
            q.append(new_code)


_CODE_TO_ORIGINAL_FUNCTION_MAPPING: MutableMapping[CodeType, FunctionType] = dict()


def link_function_to_code(code: CodeType, function: FunctionType) -> None:
    """
    Link a function to a code object. This is used to speed up the search for
    the original function from a code object.
    """
    global _CODE_TO_ORIGINAL_FUNCTION_MAPPING

    _CODE_TO_ORIGINAL_FUNCTION_MAPPING[code] = function


@lru_cache(maxsize=(1 << 14))  # 16k entries
def _functions_for_code_gc(code: CodeType) -> List[FunctionType]:
    import gc

    return [_ for _ in gc.get_referrers(code) if isinstance(_, FunctionType) and _.__code__ is code]


def functions_for_code(code: CodeType) -> List[FunctionType]:
    global _CODE_TO_ORIGINAL_FUNCTION_MAPPING

    try:
        # Try to get the function from the original code-to-function mapping
        return [_CODE_TO_ORIGINAL_FUNCTION_MAPPING[code]]
    except KeyError:
        # If the code is not in the mapping, we fall back to the garbage
        # collector
        return _functions_for_code_gc(code)


def clear():
    """Clear the inspection state.

    This should be called when modules are reloaded to ensure that the mappings
    stay relevant.
    """
    global _CODE_TO_ORIGINAL_FUNCTION_MAPPING

    _functions_for_code_gc.cache_clear()
    _CODE_TO_ORIGINAL_FUNCTION_MAPPING.clear()
