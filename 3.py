def deep_rvrs(tup):
    return tuple(deep_rvrs(x) if isinstance(x, tuple) else x
                 for x in reversed(tup))


a = (11, 12, 13, 14)
print(deep_rvrs(a))

tpl = (11, (12, (13, 113), 14), 15)
print(deep_rvrs(tpl))
