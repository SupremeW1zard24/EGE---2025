def cc3(x):
    s = ""
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s


for x in range(100):
    k = cc3(x) + str(x % 3)
    k = int(k, 3)

    if k >= 100:
        print(x, k)
