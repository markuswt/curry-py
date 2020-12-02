"Simple currying for python functions"

import typing
import functools

T = typing.TypeVar("T")
T_func = typing.Callable[..., T]


def curry(func: T_func,
          *args: list,
          _first: bool = True,
          **kwargs: dict) -> typing.Union[T_func, T]:
    """
    curry python functions

    >>> foo = lambda a, b, m: (a+b) * m
    >>> curry(foo)(2)()(3)(10)
    50
    >>> curry(foo)(2)(3, 10)
    50
    >>> curry(foo)(2, m=10)(3)
    50
    >>> curry(foo, 2, 3, 10)()
    50
    >>> curry(print, "baz")(42)
    baz 42
    >>> curry(lambda: print(42))()
    42

    curry tries to apply the function with as minimal arguments as possible,
    so try to supply *args and **kwargs together with required arguments

    curry also works as a decorator

    >>> @curry
    ... def bar(a, b, m):
    ...     return (a+b) * m
    >>> bar(2)()(3)(10)
    50
    >>> bar(2)(3, 10)
    50
    >>> bar(2, m=10)(3)
    50
    >>> bar(2, 3, 10)
    50
    """
    
    if not _first:
        # test if given arguments suffice
        try:
            return func(*args, **kwargs)
        except TypeError as error:
            # don't raise error if too few arguments supplied
            if not "expected at least" in error.args[0] \
                and not "required positional argument" in error.args[0]:
                raise error
    
    # apply given arguments
    return functools.partial(curry, func, *args, _first=False, **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
