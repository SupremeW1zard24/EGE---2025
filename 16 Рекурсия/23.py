def f(n):
    k = 0
    k += 1  # было print("*")
    if n >= 1:
        k += 1  # было print("*")
        k += f(n - 1)  # f(n - 1)
        k += f(n - 3)  # f(n - 3)
        k += 1  # было print("*")

        # Либо вместо этих 4 строк
        # k += 1 + f(n - 1 + f(n - 3) + 1

    return k


print(f(40))
