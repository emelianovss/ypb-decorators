def counter():
    count = [0]
    def inner(*args):
        count[0] += 1
        return print('sum:', sum(args), ', count:', count[0])
    return inner

c_1 = counter()
c_1(1, 2)
c_1(3, 4)
print()

c_2 = counter()
c_2(1, 2)
c_2(3, 4)
print()

c_1(5, 6)

count