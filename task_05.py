"""
>>> print(my_sum_1(1, 2))
6
>>> print(my_sum_2(3, 4))
21
"""

# Your code here

def decorator(num):
    def inner(func):
        def wrapper(*args):
            result = func(*args)
            return result * num
        return wrapper
    return inner


@decorator(2)
def my_sum_1(*args):
    return sum(args)


@decorator(3)
def my_sum_2(*args):
    return sum(args)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
