from itertools import product

k = 0
for x in product(range(12), repeat=6):
    if x[0] > 0 and x.count(11) == 1 and sum(d % 2 for d in x) == 3:
        k += 1
print(k)
