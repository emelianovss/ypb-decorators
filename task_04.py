"""
>>> print(my_sum(1, 2))
Cache call 0
Call my_sum
3
>>> print(my_sum(1, 2))
Cache call 1
3
>>> print(my_sum(1, 2))
Cache call 2
3
>>> print(my_diff(1, 2))
Cache call 0
Call my_diff
-1
>>> print(my_diff(2, 2))
Cache call 0
Call my_diff
0
"""


# Change code here
def cache(func):
    _cache = {}
    def inner(*args):
        result = _cache.get(args)
        if result is not None:
            return result
        else:
            result = func(*args)
            _cache[args] = result
            return result
    return inner


@cache
def my_sum(a, b):
    print('Call my_sum')
    return a + b


@cache
def my_diff(a, b):
    print('Call my_diff')
    return a - b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
