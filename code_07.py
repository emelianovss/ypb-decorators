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
    print(my_sum(1, 2))
    print(my_sum(1, 2))
    print(my_diff(1, 2))
    print(my_diff(1, 2))
