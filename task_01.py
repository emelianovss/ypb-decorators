"""
>>> @decorator
... def increment(arg: int):
...    return arg + 1
...
Function name "increment" was decorated
>>> value = increment(10)
>>> value
11
"""

# Yor code here


if __name__ == "__main__":
    import doctest
    doctest.testmod()
