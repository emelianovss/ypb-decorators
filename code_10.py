from functools import wraps
from functools import singledispatch
from contextlib import contextmanager


def decorator(func):
    def wrapper(*args):
        return func(*args)
    return wrapper


@decorator
def func_1(*args):
    """
    Func 1 doc
    """
    return args

print(func_1.__name__)
print(func_1.__doc__)


def decorator_2(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper


@decorator_2
def func_2(*args):
    """
    Func 2 doc
    """
    return args


print(func_2.__name__)
print(func_2.__doc__)
print(func_2.__wrapped__)


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

fun('some')
fun(10)
fun([1, 2], verbose=True)


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print('X was getted')
        return self._x

    @x.setter
    def x(self, value):
        print('X was setted')
        self._x = value

    @x.deleter
    def x(self):
        print('X was deleted')
        del self._x

c = C()
print(c.x)
c.x = 10
print(c.x)
del c.x



@contextmanager
def managed_resource(resource):
    try:
        print('Resource was getted')
        yield resource
    finally:
        print('Resource was closed')


with managed_resource(10) as r:
    print(f'Resorce: {r}')
