import collections.abc
import synchronicity.combined_types
import test.type_stub_helpers.e2e_example_impl
import typing
import typing_extensions

class BlockingFoo:

    singleton: BlockingFoo

    def __init__(self, arg: str):
        ...

    class __getarg_spec(typing_extensions.Protocol):
        def __call__(self, /) -> str:
            ...

        async def aio(self, /) -> str:
            ...

    getarg: __getarg_spec

    class __gen_spec(typing_extensions.Protocol):
        def __call__(self, /) -> typing.Generator[int, None, None]:
            ...

        def aio(self, /) -> typing.AsyncGenerator[int, None]:
            ...

    gen: __gen_spec

    @staticmethod
    def some_static(arg: str) -> float:
        ...

    @classmethod
    def clone(cls, foo: BlockingFoo) -> BlockingFoo:
        ...

    class __slow_clone_spec(typing_extensions.Protocol):
        def __call__(self, /, foo: BlockingFoo) -> BlockingFoo:
            ...

        async def aio(self, /, foo: BlockingFoo) -> BlockingFoo:
            ...

    slow_clone: typing.ClassVar[__slow_clone_spec]


_T_Blocking = typing.TypeVar("_T_Blocking", bound="BlockingFoo")

class __listify_spec(typing_extensions.Protocol):
    def __call__(self, /, t: _T_Blocking) -> typing.List[_T_Blocking]:
        ...

    async def aio(self, /, t: _T_Blocking) -> typing.List[_T_Blocking]:
        ...

listify: __listify_spec


@typing.overload
def overloaded(arg: str) -> float:
    ...

@typing.overload
def overloaded(arg: int) -> int:
    ...


class __returns_foo_spec(typing_extensions.Protocol):
    def __call__(self, /) -> BlockingFoo:
        ...

    async def aio(self, /) -> BlockingFoo:
        ...

returns_foo: __returns_foo_spec


class __wrapped_make_context_spec(typing_extensions.Protocol):
    def __call__(self, /, a: float) -> synchronicity.combined_types.AsyncAndBlockingContextManager[str]:
        ...

    def aio(self, /, a: float) -> typing.AsyncContextManager[str]:
        ...

wrapped_make_context: __wrapped_make_context_spec


P = typing_extensions.ParamSpec("P")

R = typing.TypeVar("R")

P_INNER = typing_extensions.ParamSpec("P_INNER")

R_INNER = typing.TypeVar("R_INNER", covariant=True)

class CallableWrapper(typing.Generic[P, R]):
    """Abstract base class for generic types.

    On Python 3.12 and newer, generic classes implicitly inherit from
    Generic when they declare a parameter list after the class's name::

        class Mapping[KT, VT]:
            def __getitem__(self, key: KT) -> VT:
                ...
            # Etc.

    On older versions of Python, however, generic classes have to
    explicitly inherit from Generic.

    After a class has been declared to be generic, it can then be used as
    follows::

        def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
            try:
                return mapping[key]
            except KeyError:
                return default
    """
    def __init__(self, /, *args, **kwargs):
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    class __func_spec(typing_extensions.Protocol[P_INNER, R_INNER]):
        def __call__(self, /, *args: P_INNER.args, **kwargs: P_INNER.kwargs) -> R_INNER:
            ...

        async def aio(self, /, *args: P_INNER.args, **kwargs: P_INNER.kwargs) -> R_INNER:
            ...

    func: __func_spec[P, R]


def wrap_callable(c: collections.abc.Callable[P, R]) -> CallableWrapper[P, R]:
    ...


class SomeGeneric(typing.Generic[test.type_stub_helpers.e2e_example_impl.T2]):
    """Abstract base class for generic types.

    On Python 3.12 and newer, generic classes implicitly inherit from
    Generic when they declare a parameter list after the class's name::

        class Mapping[KT, VT]:
            def __getitem__(self, key: KT) -> VT:
                ...
            # Etc.

    On older versions of Python, however, generic classes have to
    explicitly inherit from Generic.

    After a class has been declared to be generic, it can then be used as
    follows::

        def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
            try:
                return mapping[key]
            except KeyError:
                return default
    """
    def __init__(self, /, *args, **kwargs):
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    class __custom_constructor_int_spec(typing_extensions.Protocol):
        def __call__(self, /) -> SomeGeneric[int]:
            ...

        async def aio(self, /) -> SomeGeneric[int]:
            ...

    custom_constructor_int: typing.ClassVar[__custom_constructor_int_spec]

    class __custom_constructor_str_spec(typing_extensions.Protocol):
        def __call__(self, /) -> SomeGeneric[str]:
            ...

        async def aio(self, /) -> SomeGeneric[str]:
            ...

    custom_constructor_str: typing.ClassVar[__custom_constructor_str_spec]


some_instance: typing.Optional[BlockingFoo]