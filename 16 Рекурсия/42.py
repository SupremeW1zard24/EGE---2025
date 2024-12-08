cache = {}


def f(n):
    if n not in cache:
        if n == 1: cache[n] = 1
        else: cache[n] = f(n - 1) + 3 * g(n - 1)

    return cache[n]


def g(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) - 2 * g(n - 1)


k = f(50)
print(sum(int(el) for el in str(k)))

# ------------------------   РЕШЕНИЕ С ИСПОЛЬЗОВАНИЕМ ВСТРОЕННОЙ БИБЛИОТЕКИ   ----------------------------

from functools import *


@lru_cache(None)
def f(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1: return 1
    if n > 1: return f(n - 1) - 2 * g(n - 1)


k = f(50)
print(sum(int(el) for el in str(k)))

