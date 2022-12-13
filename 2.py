def verify_add(m, ls):
    values = {}
    for index, value in enumerate(ls):
        if m - value in values:
            return True
        else:
            values[value] = index
    return False


print(verify_add(100, [1, 2, 3, 4, 5]))
print(verify_add(7, [1, 2, 3, 4, 2]))
print(verify_add(10, [5, 5]))
print(verify_add(151, range(0, 200000, 3)))
print(verify_add(50004, range(0, 200000, 4)))
