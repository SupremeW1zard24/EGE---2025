from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10: return n - 1
    if n % 2 == 0: return 3 * n - 1 + f(n - 3)
    return 5 * n + 2 + f(n - 4)


for _ in range(10, 4000):
    f(_)

print(f(4445) - f(4444))
