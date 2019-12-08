"Simple currying for python functions"

import typing
import functools

T = typing.TypeVar("T")
T_func = typing.Callable[..., T]


def curry(func: T_func, *args: list,
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

    curry tries to apply the function with as few arguments as possible,
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
    
    # invoked on subsequent applications
    def _curry(func: T_func, *args: list,
               **kwargs: dict) -> typing.Union[T_func, T]:
        try:
            # test if given arguments suffice
            return func(*args, **kwargs)
        except TypeError as error:
            # don't raise error if too few arguments supplied
            msg = error.args[0]
            if not "missing" in msg and not "at least" in msg:
                raise error
        # apply given arguments
        return functools.partial(_curry, func, *args, **kwargs)
    
    # don't try to evaluate on first application/decoration
    return functools.partial(_curry, func, *args, **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
