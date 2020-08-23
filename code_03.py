def counter_local_no_change():
    count, text, arr, dct = 0, "text", [],  {}
    def inner():
        text = 'func_text'
        print(locals())
        return print(count)
    return inner

c_0 = counter_local_no_change()
print(c_0.__closure__)
c_0()
print()


def counter_local_with_change():
    count, text, arr, dct = 0, "text", [],  {}
    def inner():
        print(locals())
        count += 1
        return print(count)
    return inner

c_1 = counter_local_with_change()
print(c_1.__closure__)
try:
    c_1()
except UnboundLocalError as e:
    print(e)
print()


def counter_nonlocal():
    count, text, arr, dct = 0, "text", [],  {}
    def inner():
        nonlocal count, text
        print(locals())
        count += 1
        return print(count)
    return inner

c_2 = counter_nonlocal()
print(c_2.__closure__)
c_2()
c_2()
print()


def counter_list():
    count, text, arr, dct = 0, "text", [0],  {}
    def inner():
        print(locals())
        arr[0] += 1
        return print(arr[0])
    return inner


c_3 = counter_list()
print(c_3.__closure__)
c_3()
