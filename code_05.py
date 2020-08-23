register = {}


def decorator(name):
    def inner_decorator(func):
        register[name] = func
        return func
    return inner_decorator


def default():
    print('Route not found')


@decorator('first func')
def func_1():
    print('Call func_1')


@decorator('second func')
def func_2():
    print('Call func_2')


register.get('first func', default)()
register.get('second func', default)()
register.get('not exists func', default)()
