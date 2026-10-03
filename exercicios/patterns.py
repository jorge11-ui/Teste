def f(x):
    return 2 * x + 1

def g(x):
    return x ** 2

def comportamento(g, f):
    return lambda x: g(f(x))

h = comportamento(g, f)
print(h(3))
