register = {}


def decorator(func):
    register[func.__name__] = func
    return func

def default():
    print('Route not found')


@decorator
def func_1():
    print('Call func_1')


@decorator
def func_2():
    print('Call func_2')


register.get('func_1', default)()
register.get('func_2', default)()
register.get('func_3', default)()
