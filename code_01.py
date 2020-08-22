def decorator(func):
    print('Hello from decorator')
    return func


@decorator
def func_1():
    print('Call func_1')


def func_2():
    print('Call func_2')


func_1()
func_2 = decorator(func_2)
func_2()
