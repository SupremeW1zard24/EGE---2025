for p in range(30, 37):
    for s in range(20, 35):
        if int("R4", p - 1) + int("B0", s + 2) + int("T3NK4", p) == 23593399:
            print(p * s)
