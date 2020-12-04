from typing import TypeVar, Callable

T = TypeVar("T")


def vardef(define_var: Callable[[], T]) -> T:
    """
    Decorator to turn a callable into a variable definition.

    Calls the decorated function and returns its result, effectively overwriting
    the function's name with it's return value.

    It is expected that the callable have no mandatory arguments to be specified
    since it will be called without any.

    Usage::

      >>> from vardef import vardef
      >>>
      >>> @vardef
      ... def foo() -> int:
      ...     return 0
    """
    return define_var()
