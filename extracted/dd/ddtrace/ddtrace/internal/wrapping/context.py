from abc import ABC
from contextvars import ContextVar
from inspect import iscoroutinefunction
from inspect import isgeneratorfunction
import sys
from types import FrameType
from types import FunctionType
from types import TracebackType
import typing as t


try:
    from typing import Protocol  # noqa:F401
except ImportError:
    from typing_extensions import Protocol  # type: ignore[assignment]

import bytecode
from bytecode import Bytecode

from ddtrace.internal.assembly import Assembly
from ddtrace.internal.utils.inspection import link_function_to_code


T = t.TypeVar("T")

# This module implements utilities for wrapping a function with a context
# manager. The rough idea is to re-write the function's bytecode to look like
# this:
#
#   def foo():
#       with wrapping_context:
#           # Original function code
#
# Because we also want to capture the return value, our context manager extends
# the Python one by implementing a __return__ method that will be called with
# the return value of the function. Contrary to ordinary context managers,
# though, the __exit__ method is only called if the function raises an
# exception.
#
# Because CPython 3.11 introduced zero-cost exceptions, we cannot nest try
# blocks in the function's bytecode. In this case, we call the context manager
# methods directly at the right places, and set up the appropriate exception
# handling code. For older versions of Python we rely on the with statement to
# perform entry and exit operations. Calls to __return__ are explicit in all
# cases.
#
# Some advantages of wrapping a function this way are:
# - Access to the local variables on entry and on return/exit via the frame
#   object.
# - No intermediate function calls that pollute the call stack.
# - No need to call the wrapped function manually.
#
# The actual bytecode wrapping is performed once on a target function via a
# universal wrapping context. Multiple context wrapping of a function is allowed
# and it is virtually implemented on top of the concrete universal wrapping
# context. This makes multiple wrapping/unwrapping easy, as it translates to a
# single bytecode wrapping/unwrapping operation.
#
# Context wrappers should be implemented as subclasses of the WrappingContext
# class. The __priority__ attribute can be used to control the order in which
# multiple context wrappers are entered and exited. The __enter__ and __exit__
# methods should be implemented to perform the necessary operations. The
# __exit__ method is called if the wrapped function raises an exception. The
# frame of the wrapped function can be accessed via the __frame__ property. The
# __return__ method can be implemented to capture the return value of the
# wrapped function. If implemented, its return value will be used as the wrapped
# function return value. The wrapped function can be accessed via the
# __wrapped__ attribute. Context-specific values can be stored and retrieved
# with the set and get methods.

CONTEXT_HEAD = Assembly()
CONTEXT_RETURN = Assembly()
CONTEXT_FOOT = Assembly()

if sys.version_info >= (3, 14):
    raise NotImplementedError("Python >= 3.14 is not supported yet")
elif sys.version_info >= (3, 13):
    CONTEXT_HEAD.parse(
        r"""
            load_const                  {context_enter}
            push_null
            call                        0
            pop_top
        """
    )
    CONTEXT_RETURN.parse(
        r"""
            push_null
            load_const                  {context_return}
            swap                        3
            call                        1
        """
    )

    CONTEXT_RETURN_CONST = Assembly()
    CONTEXT_RETURN_CONST.parse(
        r"""
            load_const                  {context_return}
            push_null
            load_const                  {value}
            call                        1
        """
    )

    CONTEXT_FOOT.parse(
        r"""
        try                             @_except lasti
            push_exc_info
            load_const                  {context_exit}
            push_null
            call                        0
            pop_top
            reraise                     2
        tried

        _except:
            copy                        3
            pop_except
            reraise                     1
        """
    )

elif sys.version_info >= (3, 12):
    CONTEXT_HEAD.parse(
        r"""
            push_null
            load_const                  {context_enter}
            call                        0
            pop_top
        """
    )

    CONTEXT_RETURN.parse(
        r"""
            load_const                  {context_return}
            push_null
            swap                        3
            call                        1
        """
    )

    CONTEXT_RETURN_CONST = Assembly()
    CONTEXT_RETURN_CONST.parse(
        r"""
            push_null
            load_const                  {context_return}
            load_const                  {value}
            call                        1
        """
    )

    CONTEXT_FOOT.parse(
        r"""
        try                             @_except lasti
            push_exc_info
            push_null
            load_const                  {context_exit}
            call                        0
            pop_top
            reraise                     2
        tried

        _except:
            copy                        3
            pop_except
            reraise                     1
        """
    )


elif sys.version_info >= (3, 11):
    CONTEXT_HEAD.parse(
        r"""
            push_null
            load_const                  {context_enter}
            precall                     0
            call                        0
            pop_top
        """
    )

    CONTEXT_RETURN.parse(
        r"""
            load_const                  {context_return}
            push_null
            swap                        3
            precall                     1
            call                        1
        """
    )

    CONTEXT_EXC_HEAD = Assembly()
    CONTEXT_EXC_HEAD.parse(
        r"""
            push_null
            load_const                  {context_exit}
            precall                     0
            call                        0
            pop_top
        """
    )

    CONTEXT_FOOT.parse(
        r"""
        try                             @_except lasti
            push_exc_info
            push_null
            load_const                  {context_exit}
            precall                     0
            call                        0
            pop_top
            reraise                     2
        tried

        _except:
            copy                        3
            pop_except
            reraise                     1
        """
    )

elif sys.version_info >= (3, 10):
    CONTEXT_HEAD.parse(
        r"""
            load_const                  {context}
            setup_with                  @_except
            pop_top
        _except:
        """
    )

    CONTEXT_RETURN.parse(
        r"""
            pop_block
            load_const                  {context}
            load_method                 $__return__
            rot_three
            rot_three
            call_method                 1
            rot_two
            pop_top
        """
    )

    CONTEXT_FOOT.parse(
        r"""
            with_except_start
            pop_top
            reraise                     1
        """
    )

elif sys.version_info >= (3, 9):
    CONTEXT_HEAD.parse(
        r"""
            load_const                  {context}
            setup_with                  @_except
            pop_top
        _except:
        """
    )

    CONTEXT_RETURN.parse(
        r"""
            pop_block
            load_const                  {context}
            load_method                 $__return__
            rot_three
            rot_three
            call_method                 1
            rot_two
            pop_top
        """
    )

    CONTEXT_FOOT.parse(
        r"""
            with_except_start
            pop_top
            reraise
        """
    )


elif sys.version_info >= (3, 8):
    CONTEXT_HEAD.parse(
        r"""
            load_const                  {context}
            setup_with                  @_except
            pop_top
        _except:
        """
    )

    CONTEXT_RETURN.parse(
        r"""
            load_const                  {context}
            load_method                 $__return__
            rot_three
            rot_three
            call_method                 1
        """
    )

    CONTEXT_FOOT.parse(
        r"""
            with_cleanup_start
            with_cleanup_finish
            end_finally
            load_const                  None
            return_value
        """
    )


# This is abstract and should not be used directly
class BaseWrappingContext(ABC):
    __priority__: int = 0

    def __init__(self, f: FunctionType):
        self.__wrapped__ = f
        self._storage_stack: ContextVar[list[dict]] = ContextVar(f"{type(self).__name__}__storage_stack", default=[])

    def __enter__(self) -> "BaseWrappingContext":
        self._storage_stack.get().append({})
        return self

    def _pop_storage(self) -> t.Dict[str, t.Any]:
        return self._storage_stack.get().pop()

    def __return__(self, value: T) -> T:
        self._pop_storage()
        return value

    def __exit__(
        self,
        exc_type: t.Optional[t.Type[BaseException]],
        exc_val: t.Optional[BaseException],
        exc_tb: t.Optional[TracebackType],
    ) -> None:
        self._pop_storage()

    def get(self, key: str) -> t.Any:
        return self._storage_stack.get()[-1][key]

    def set(self, key: str, value: T) -> T:
        self._storage_stack.get()[-1][key] = value
        return value

    @classmethod
    def wrapped(cls, f: FunctionType) -> "BaseWrappingContext":
        if cls.is_wrapped(f):
            context = cls.extract(f)
            assert isinstance(context, cls)  # nosec
        else:
            context = cls(f)
            context.wrap()
        return context

    @classmethod
    def is_wrapped(cls, _f: FunctionType) -> bool:
        raise NotImplementedError

    @classmethod
    def extract(cls, _f: FunctionType) -> "BaseWrappingContext":
        raise NotImplementedError

    def wrap(self) -> None:
        raise NotImplementedError

    def unwrap(self) -> None:
        raise NotImplementedError


# This is the public interface exported by this module
class WrappingContext(BaseWrappingContext):
    @property
    def __frame__(self) -> FrameType:
        try:
            return _UniversalWrappingContext.extract(self.__wrapped__).get("__frame__")
        except ValueError:
            raise AttributeError("Wrapping context not entered")

    def get_local(self, name: str) -> t.Any:
        return self.__frame__.f_locals[name]

    @classmethod
    def is_wrapped(cls, f: FunctionType) -> bool:
        try:
            return bool(cls.extract(f))
        except ValueError:
            return False

    @classmethod
    def extract(cls, f: FunctionType) -> "WrappingContext":
        if _UniversalWrappingContext.is_wrapped(f):
            try:
                return _UniversalWrappingContext.extract(f).registered(cls)
            except KeyError:
                pass
        msg = f"Function is not wrapped with {cls}"
        raise ValueError(msg)

    def wrap(self) -> None:
        t.cast(_UniversalWrappingContext, _UniversalWrappingContext.wrapped(self.__wrapped__)).register(self)

    def unwrap(self) -> None:
        f = self.__wrapped__

        if _UniversalWrappingContext.is_wrapped(f):
            _UniversalWrappingContext.extract(f).unregister(self)


class ContextWrappedFunction(Protocol):
    """A wrapped function."""

    __dd_context_wrapped__ = None  # type: t.Optional[_UniversalWrappingContext]

    def __call__(self, *args, **kwargs):
        pass


# This class provides an interface between single bytecode wrapping and multiple
# logical context wrapping
class _UniversalWrappingContext(BaseWrappingContext):
    def __init__(self, f: FunctionType) -> None:
        super().__init__(f)

        self._contexts: t.List[WrappingContext] = []

    def register(self, context: WrappingContext) -> None:
        _type = type(context)
        if any(isinstance(c, _type) for c in self._contexts):
            raise ValueError("Context already registered")

        self._contexts.append(context)
        self._contexts.sort(key=lambda c: c.__priority__)

    def unregister(self, context: WrappingContext) -> None:
        try:
            self._contexts.remove(context)
        except ValueError:
            raise ValueError("Context not registered")

        if not self._contexts:
            self.unwrap()

    def is_registered(self, context: WrappingContext) -> bool:
        return type(context) in self._contexts

    def registered(self, context_type: t.Type[WrappingContext]) -> WrappingContext:
        for context in self._contexts:
            if isinstance(context, context_type):
                return context
        raise KeyError(f"Context {context_type} not registered")

    def __enter__(self) -> "_UniversalWrappingContext":
        super().__enter__()

        # Make the frame object available to the contexts
        self.set("__frame__", sys._getframe(1))

        for context in self._contexts:
            context.__enter__()

        return self

    def _exit(self) -> None:
        self.__exit__(*sys.exc_info())

    def __exit__(self, *exc) -> None:
        if exc == (None, None, None):
            return

        for context in self._contexts[::-1]:
            context.__exit__(*exc)

        super().__exit__(*exc)

    def __return__(self, value: T) -> T:
        for context in self._contexts[::-1]:
            context.__return__(value)

        return super().__return__(value)

    @classmethod
    def is_wrapped(cls, f: FunctionType) -> bool:
        return hasattr(f, "__dd_context_wrapped__")

    @classmethod
    def extract(cls, f: FunctionType) -> "_UniversalWrappingContext":
        if not cls.is_wrapped(f):
            raise ValueError("Function is not wrapped")
        return t.cast(_UniversalWrappingContext, t.cast(ContextWrappedFunction, f).__dd_context_wrapped__)

    if sys.version_info >= (3, 11):

        def wrap(self) -> None:
            f = self.__wrapped__

            if self.is_wrapped(f):
                raise ValueError("Function already wrapped")

            bc = Bytecode.from_code(f.__code__)

            # Prefix every return
            i = 0
            while i < len(bc):
                instr = bc[i]
                try:
                    if instr.name == "RETURN_VALUE":
                        return_code = CONTEXT_RETURN.bind({"context_return": self.__return__}, lineno=instr.lineno)
                    elif sys.version_info >= (3, 12) and instr.name == "RETURN_CONST":  # Python 3.12+
                        return_code = CONTEXT_RETURN_CONST.bind(
                            {"context_return": self.__return__, "value": instr.arg}, lineno=instr.lineno
                        )
                    else:
                        return_code = []

                    bc[i:i] = return_code
                    i += len(return_code)
                except AttributeError:
                    # Not an instruction
                    pass
                i += 1

            # Search for the RESUME instruction
            for i, instr in enumerate(bc, 1):
                try:
                    if instr.name == "RESUME":
                        break
                except AttributeError:
                    # Not an instruction
                    pass
            else:
                i = 0

            bc[i:i] = CONTEXT_HEAD.bind({"context_enter": self.__enter__}, lineno=f.__code__.co_firstlineno)

            # Wrap every line outside a try block
            except_label = bytecode.Label()
            first_try_begin = last_try_begin = bytecode.TryBegin(except_label, push_lasti=True)

            i = 0
            while i < len(bc):
                instr = bc[i]
                if isinstance(instr, bytecode.TryBegin) and last_try_begin is not None:
                    bc.insert(i, bytecode.TryEnd(last_try_begin))
                    last_try_begin = None
                    i += 1
                elif isinstance(instr, bytecode.TryEnd):
                    j = i + 1
                    while j < len(bc) and not isinstance(bc[j], bytecode.TryBegin):
                        if isinstance(bc[j], bytecode.Instr):
                            last_try_begin = bytecode.TryBegin(except_label, push_lasti=True)
                            bc.insert(i + 1, last_try_begin)
                            break
                        j += 1
                    i += 1
                i += 1

            bc.insert(0, first_try_begin)

            bc.append(bytecode.TryEnd(last_try_begin))
            bc.append(except_label)
            bc.extend(CONTEXT_FOOT.bind({"context_exit": self._exit}))

            # Mark the function as wrapped by a wrapping context
            t.cast(ContextWrappedFunction, f).__dd_context_wrapped__ = self

            # Replace the function code with the wrapped code. We also link
            # the function to its original code object so that we can retrieve
            # it later if required.
            link_function_to_code(f.__code__, f)
            f.__code__ = bc.to_code()

        def unwrap(self) -> None:
            f = self.__wrapped__

            if not self.is_wrapped(f):
                return

            wrapped = t.cast(ContextWrappedFunction, f)

            bc = Bytecode.from_code(f.__code__)

            # Remove the exception handling code
            bc[-len(CONTEXT_FOOT) :] = []
            bc.pop()
            bc.pop()

            except_label = bc.pop(0).target

            # Remove the try blocks
            i = 0
            while i < len(bc):
                instr = bc[i]
                if isinstance(instr, bytecode.TryBegin) and instr.target is except_label:
                    bc.pop(i)
                elif isinstance(instr, bytecode.TryEnd) and instr.entry.target is except_label:
                    bc.pop(i)
                else:
                    i += 1

            # Remove the head of the try block
            wc = wrapped.__dd_context_wrapped__
            for i, instr in enumerate(bc):
                try:
                    if instr.name == "LOAD_CONST" and instr.arg is wc:
                        break
                except AttributeError:
                    # Not an instruction
                    pass

            # Search for the RESUME instruction
            for i, instr in enumerate(bc, 1):
                try:
                    if instr.name == "RESUME":
                        break
                except AttributeError:
                    # Not an instruction
                    pass
            else:
                i = 0

            bc[i : i + len(CONTEXT_HEAD)] = []

            # Un-prefix every return
            i = 0
            while i < len(bc):
                instr = bc[i]
                try:
                    if instr.name == "RETURN_VALUE":
                        return_code = CONTEXT_RETURN
                    elif sys.version_info >= (3, 12) and instr.name == "RETURN_CONST":  # Python 3.12+
                        return_code = CONTEXT_RETURN_CONST
                    else:
                        return_code = None

                    if return_code is not None:
                        bc[i - len(return_code) : i] = []
                        i -= len(return_code)
                except AttributeError:
                    # Not an instruction
                    pass
                i += 1

            # Recreate the code object
            f.__code__ = bc.to_code()

            # Remove the wrapping context marker
            del wrapped.__dd_context_wrapped__

    else:

        def wrap(self) -> None:
            f = self.__wrapped__

            if self.is_wrapped(f):
                raise ValueError("Function already wrapped")

            bc = Bytecode.from_code(f.__code__)

            # Prefix every return
            i = 0
            while i < len(bc):
                instr = bc[i]
                try:
                    if instr.name == "RETURN_VALUE":
                        return_code = CONTEXT_RETURN.bind({"context": self}, lineno=instr.lineno)
                    else:
                        return_code = []

                    bc[i:i] = return_code
                    i += len(return_code)
                except AttributeError:
                    # Not an instruction
                    pass
                i += 1

            # Search for the GEN_START instruction, which needs to stay on top.
            i = 0
            if sys.version_info >= (3, 10) and (iscoroutinefunction(f) or isgeneratorfunction(f)):
                for i, instr in enumerate(bc, 1):
                    try:
                        if instr.name == "GEN_START":
                            break
                    except AttributeError:
                        # Not an instruction
                        pass

            *bc[i:i], except_label = CONTEXT_HEAD.bind({"context": self}, lineno=f.__code__.co_firstlineno)

            bc.append(except_label)
            bc.extend(CONTEXT_FOOT.bind())

            # Mark the function as wrapped by a wrapping context
            t.cast(ContextWrappedFunction, f).__dd_context_wrapped__ = self

            # Replace the function code with the wrapped code. We also link
            # the function to its original code object so that we can retrieve
            # it later if required.
            link_function_to_code(f.__code__, f)
            f.__code__ = bc.to_code()

        def unwrap(self) -> None:
            f = self.__wrapped__

            if not self.is_wrapped(f):
                return

            wrapped = t.cast(ContextWrappedFunction, f)

            bc = Bytecode.from_code(f.__code__)

            # Remove the exception handling code
            bc[-len(CONTEXT_FOOT) :] = []
            bc.pop()

            # Remove the head of the try block
            wc = wrapped.__dd_context_wrapped__
            for i, instr in enumerate(bc):
                try:
                    if instr.name == "LOAD_CONST" and instr.arg is wc:
                        break
                except AttributeError:
                    # Not an instruction
                    pass

            bc[i : i + len(CONTEXT_HEAD) - 1] = []

            # Remove all the return handlers
            i = 0
            while i < len(bc):
                instr = bc[i]
                try:
                    if instr.name == "RETURN_VALUE":
                        bc[i - len(CONTEXT_RETURN) : i] = []
                        i -= len(CONTEXT_RETURN)
                except AttributeError:
                    # Not an instruction
                    pass
                i += 1

            # Recreate the code object
            f.__code__ = bc.to_code()

            # Remove the wrapping context marker
            del wrapped.__dd_context_wrapped__
