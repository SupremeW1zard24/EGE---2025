def f(a, m):
    if a <= 18: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 3, m - 1), f(a - 5, m - 1), f(a // 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print(min(s for s in range(18, 1000) if f(s, 2)))  # 36
print([s for s in range(18, 1000) if f(s, 3) > f(s, 1)])  # 39 77
print([s for s in range(18, 1000) if f(s, 3) > f(s, 2)])  # 80
