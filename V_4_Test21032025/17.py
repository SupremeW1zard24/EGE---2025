a = [int(x) for x in open("17.txt")]
p = []
m = max(a)
for i in range(len(a) - 1):
    if m % 10 == (i + i + 3) % 10:
        p.append(abs((i + i + 3) - (a[i] + a[i + 1])))
print(len(p), min(p))