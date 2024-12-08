def f(n):
    sm = 0
    sm += (n + 1)
    if n > 1:
        sm += (n + 5)
        sm += f(n - 1)
        sm += f(n - 2)
    return sm


print(f(30))
