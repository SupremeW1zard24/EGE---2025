def f(a, b, m):
    if a + b <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a - 3, b, m - 1),
        f(a, b - 3, m - 1),
        f(a // 2 + a % 2, b, m - 1),
        f(a, b // 2 + b % 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


# 19
print(max(s for s in range(23, 1000) if f(50, s, 2)))  # Заменить all --> any / 94

# 20
print([s for s in range(23, 1000) if f(50, s, 3) > f(50, s, 1)])  # 50 100

# 21
print([s for s in range(23, 1000) if f(50, s, 4) > f(50, s, 2)])  # 103
