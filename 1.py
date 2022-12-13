def trc1(g):
    def f(num):
        return g
    return f


@trc1
def sqr(x):
    return x * x


@trc1
def sum_sqr(n):
    total = 0
    for i in range(n + 1):
        total += i * i
    return total


print(sqr(3))
print(sum_sqr(3))
