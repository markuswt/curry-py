# curry-py

Simple currying for python functions.

```python
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
```

Curry tries to evaluate the function with as few arguments as possible, so try to apply `*args` and `**kwargs` together with required arguments.

Curry also works as a decorator.

```python
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
```
